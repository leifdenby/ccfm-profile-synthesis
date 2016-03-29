#
#
# Run with `bash -i make.sh` so that `module load` works

module load gcc/5.1.0

# download ECHAM source from SVN
svn checkout https://svn.zmaw.de/svn/echam6/tags/echam-6.1.02p1 --username leif.denby

# to run this version on the MPI workstation the library paths needs modifying
cp files/config/mh-linux-x64 echam-6.1.02p1/config

cd echam-6.1.02p1


# mpi workstations zlib has moved...
patch < ../files/configure.patch

# update Makefile to make sure it includes the CCFM source files
./util/createMakefiles.pl


./configure --with-fortran=gcc


# on the MPI workstations the fortran and c part of the netcdf library have
# been split, this change has happened since ECHAM6.1 was released. The
# following line adds into the Makefile

sed -i 's/-I$(NETCDFROOT)\/include/-I$(NETCDFROOT)\/include  -I\/sw\/wheezy-x64\/netcdf-4.3.3.1-static-gccsys\/include /' Makefile
sed -i 's/-L$(NETCDFROOT)\/lib/-L$(NETCDFROOT)\/lib  -L\/sw\/wheezy-x64\/netcdf-4.3.3.1-static-gccsys\/lib /' Makefile

make -j8


echo "make done, add the mpi library to your ld_library_path:"
echo "export LD_LIBRARY_PATH=/sw/wheezy-x64/mpilib/mvapich2-2.1a-static-gcc51/lib:$LD_LIBRARY_PATH"
