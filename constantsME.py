from enum import Enum

class SURFFILE(Enum):
    SURFFILE = 0
    Sfcfil = 1

class PROFFILE(Enum):
    PROFFILE = 0
    Profil = 1

class SURFDATA(Enum):
    SURFDATA = 0
    Stanum = 1
    Year = 2
    Name = 3
    Xcoord = 4
    Ycoord = 5

class UAIRDATA(Enum):
    UAIRDATA = 0
    Stanum = 1
    Year = 2
    Name = 3
    Xcoord = 4
    Ycoord = 5

class SITEDATA(Enum):
    SITEDATA = 0
    Stanum = 1
    Year = 2
    Name = 3
    Xcoord = 4
    Ycoord = 5

class PROFBASE(Enum):
    PROFBASE = 0
    BaseElev = 1
    Units = 2

class STARTEND(Enum):
    STARTEND = 0
    Strtyr = 1
    Strtmn = 2
    Strtdy = 3
    Strthr = 4
    Endyr = 5
    Endmn = 6
    Enddy = 7
    Endhr = 8

class DAYRANGE(Enum):
    DAYRANGE = 0

class NUMYEARS(Enum):
    NUMYEARS = 0
    NumYrs = 1

class SCIMBYHR(Enum):
    SCIMBYHR = 0
    NRegStart = 1
    NRegInt = 2
    SfcFilnam = 3
    PflFilnam = 4

class WDROTATE(Enum):
    WDROTATE = 0
    Rotang = 1

class WINDCATS(Enum):
    WINDCATS = 0
    Ws1 = 1
    Ws2 = 2
    Ws3 = 3
    Ws4 = 4
    Ws5 = 5


