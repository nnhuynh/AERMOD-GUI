from enum import Enum

class EVENTPER(Enum):
    EVENTPER = 0
    Evname_1 = 1
    Aveper_1 = 2
    Grpid_1 = 3
    Date_1 = 4
    Conc_1 = 5

    Evname_2 = 21
    Aveper_2 = 22
    Grpid_2 = 23
    Date_2 = 24
    Conc_2 = 25

    Evname_3 = 31
    Aveper_3 = 32
    Grpid_3 = 33
    Date_3 = 34
    Conc_3 = 35

class EVENTLOC(Enum):
    EVENTLOC = 0

    Evname_1 = 'Evname_1'
    Xr_1 = 1
    Yr_1 = 2
    Zelev_1 = 3
    Zhill_1 = 4
    Zflag_1 = 5
    Rng_1 = 6
    Dir_1 = 7

    Evname_2 = 'Evname_2'
    Xr_2 = 21
    Yr_2 = 22
    Zelev_2 = 23
    Zhill_2 = 24
    Zflag_2 = 25
    Rng_2 = 26
    Dir_2 = 27

    Evname_3 = 'Evname_3'
    Xr_3 = 31
    Yr_3 = 32
    Zelev_3 = 33
    Zhill_3 = 34
    Zflag_3 = 35
    Rng_3 = 36
    Dir_3 = 37

class INCLUDED(Enum):
    INCLUDED = 0
    EventIncFile = 1