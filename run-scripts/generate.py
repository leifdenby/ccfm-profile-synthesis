"""
Generate a runscript for every forcing file in ../scm-forcing-files
"""


import os
import glob
import scipy.io
import netCDF4
from datetime import datetime, timedelta

PROJECT_ROOT = os.environ.get('PROJECT_ROOT')

if PROJECT_ROOT is None:
    raise Exception("Please set PROJECT_ROOT env variable")

forcing_files = glob.glob(os.path.join(PROJECT_ROOT, 'scm-forcing-files', '*.nc'))


with open('run_all.sh', 'w') as fh_runscript:

    fh_runscript.write('export LD_LIBRARY_PATH=/sw/wheezy-x64/mpilib/mvapich2-2.1a-static-gcc51/lib:$LD_LIBRARY_PATH\n')

    for file_fullpath in forcing_files:
        filename = os.path.basename(file_fullpath)

        scm_name = filename.replace('.nc', '')

        # scm_fh = scipy.io.netcdf_file(file_fullpath)
        scm_fh = netCDF4.Dataset(file_fullpath)

        start_datetime_str = str(int(scm_fh.variables['date'][0]))

        start_datetime = datetime.strptime(start_datetime_str, '%Y%m%d%H')
        duration = int(scm_fh.variables['time'][-1])
        assert scm_fh.variables['time'].units.lower().startswith('seconds')

        end_datetime = start_datetime + timedelta(seconds=duration)

        print "{name} ({start} -> {end})".format(name=scm_name, start=start_datetime, end=end_datetime)

        runscript_template_filename = os.path.join(os.path.dirname(__file__), 'base', 'mpi-workstation.job.template')

        runscript_template = open(runscript_template_filename).read()

        jobfile_filename = os.path.join('all', '%s.job' % scm_name)

        with open(jobfile_filename, 'w') as fh:
            out_template = runscript_template\
                           .replace('{{PROJECT_ROOT}}', PROJECT_ROOT)\
                           .replace('{{EXP_IDENTIFIER}}', scm_name)\
                           .replace('{{DT_START}}', start_datetime.strftime('%Y,%m,%d,%H,0,0'))\
                           .replace('{{DT_STOP}}', end_datetime.strftime('%Y,%m,%d,%H,0,0'))\
                           .replace('{{SCM_FORCING_FILENAME}}', file_fullpath)
            fh.write(out_template)

        fh_runscript.write('bash %s\n' % jobfile_filename)



