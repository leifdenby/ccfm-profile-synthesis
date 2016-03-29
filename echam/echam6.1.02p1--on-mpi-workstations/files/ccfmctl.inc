! This file belongs to the Convective Cloud Field Model (CCFM) 
!
! *ccfmctl* namelist for the M7 aerosol model
!
! Author:
! -------
! Till M Wagner, University of Oxford,                                   03/2012
! Z. CAO,        Univeristy OF Cambridge,                                2015

! Purpose:
! --------
! This namelist contains the logical switches and parameters 
! to control the Convective Cloud Field Model 
! convection parameterisation.
!
!
NAMELIST /ccfmctl/    emic,     &  ! true  = ECHAM5 microphysics parametrisation 
                                   ! false = Kessler scheme
                      sfc_bbl,  &  ! cloud initialised by entraining parcel lifted from surface
                                   ! -  default = .true.        
                      sclevap,  &  ! evaporation below cloud base
                                   ! -  default = .true. 
                      lshear,    &  ! correction of v_z due to wind shear
                                   ! -  default  = .false.         
                      lmidcv,    &  ! correction of v_z due to wind shear
                      lccfm_diag, &  ! diagnostic ccfm mode
                                   ! - default = .false.
                      lentr,  &    ! vertical velocity and cloud radius dependent entrainment
                                   ! -  default  = .false.
                      lccfm5, &    ! ccfm5 
                                   !-  default  = .false.
                      ldry,  &     ! true for dry thermodynamics
                                   !-default =.false.
                      lgenlv,  &   ! dry thermodynamics
                                   !-default =.false.
                      lpseudo, &   ! pseudo adiabatic
                                   !-default =.false.
                      C_fa,    &   ! pseudo-adiabatic parameter
                      C_fb,    &   ! pseudo-adiabatic parameter
                      ks,      &   ! wind shear 
                      kw,      &   ! wind shear  
                      T_emic,  &   ! microphysics
                      qi_emic 
