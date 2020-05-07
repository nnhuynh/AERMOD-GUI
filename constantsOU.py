from enum import Enum

class RECTABLE(Enum):
    RECTABLE = 0
    Aveper = 1
    ALLAEV = 2

class MAXTABLE(Enum):
    MAXTABLE = 0
    Aveper = 1
    Maxnum = 2
    ALLAEV = 3

class DAYTABLE(Enum):
    DAYTABLE = 0
    Aveper = 1
    ALLAEV = 2

class MAXIFILE(Enum):
    MAXIFILE = 0
    Aveper = 1
    GrpID = 2
    Thresh = 3
    Filnam = 4
    Funit = 5

class POSTFILE(Enum):
    POSTFILE = 0
    Aveper = 1
    GrpID = 2
    Format = 3
    Filnam = 4
    Funit = 5
    PERIOD = 6

class PLOTFILE(Enum):
    PLOTFILE = 0
    Aveper = 1
    GrpID = 2
    Hivalu = 3
    Filnam = 4
    Funit = 5
    PERIOD = 6

class TOXXFILE(Enum):
    TOXXFILE = 0
    Aveper = 1
    Cutoff = 2
    Filnam = 3
    Funit = 4
    PERIOD = 5

class RANKFILE(Enum):
    RANKFILE = 0
    Aveper = 1
    Hinum = 2
    Filnam = 3
    Funit = 4
    PERIOD = 5

class EVALFILE(Enum):
    EVALFILE = 0
    SrcID = 1
    Filnam = 2
    Funit = 3

class SEASONHR(Enum):
    SEASONHR = 0
    GrpID = 1
    Filnam = 2
    Funit = 3

class MAXDAILY(Enum):
    MAXDAILY = 0
    GrpID = 1
    Filnam = 2
    Funit = 3

class MXDYBYYR(Enum):
    MXDYBYYR = 0
    GrpID = 1
    Filnam = 2
    Funit = 3

class MAXDCONT(Enum):
    MAXDCONT = 0
    GrpID = 1
    UpperRank = 2
    LowerRank = 3
    Filnam = 4
    Funit = 5
    THRESH = 6
    ThreshValue = 7

class SUMMFILE(Enum):
    SUMMFILE = 0
    SummFilename = 1

class FILEFORM(Enum):
    FILEFORM = 0

class NOHEADER(Enum):
    NOHEADER = 0
    POSTFILE = 1
    PLOTFILE = 2
    MAXIFILE = 3
    RANKFILE = 4
    SEASONHR = 5
    MAXDAILY = 6
    MXDYBYYR = 7
    MAXDCONT = 8
    ALL = 9

class EVENTOUT(Enum):
    EVENTOUT = 0
