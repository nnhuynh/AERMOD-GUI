from enum import Enum

class MODELOPT(Enum):
    DFAULT = 0
    ALPHA = 1
    BETA = 2
    CONC = 3
    DEPOS = 4
    DDEP = 5
    WDEP = 6
    AREADPLT = 7
    FLAT = 8
    ELEV = 9
    NOSTD = 10
    NOCHKD = 11
    WARNCHKD = 12
    NOWARN = 13
    SCREEN = 14
    SCIM = 15
    PVMRM = 16
    OLM = 17
    ARM2 = 18
    PSDCREDIT = 19
    FASTALL = 20
    FASTAREA = 21
    DRYDPLT = 22
    NODRYDPLT = 23
    WETDPLT = 24
    NOWETDPLT = 25
    NOURBTRAN = 26
    VECTORWS = 27

class AVERTIME(Enum):
    _1Hr = '1'
    _2Hr = '2'
    _3Hr = '3'
    _4Hr = '4'
    _6Hr = '6'
    _8Hr = '8'
    _12Hr = '12'
    _24Hr = '24'
    MONTH = 'MONTH'
    PERIOD = 'PERIOD'
    ANNUAL = 'ANNUAL'

class POLLUTID(Enum):
    PM10 = 'PM10'
    PM25 = 'PM25'
    NO2 = 'NO2'
    SO2 = 'SO2'
    LEAD = 'LEAD'
    OTHER = 'OTHER'
    UserSpecified = 'User Specified'
    H1H = 'H1H'
    H2H = 'H2H'
    INC = 'INC'

class GASDEPDF(Enum):
    React = 'React'
    F_Seas2 = 'F_Seas2'
    F_Seas5 = 'F_Seas5'
    Refpoll = 'Refpoll'

class GDLANUSE(Enum):
    Sec1 = 'Sec1'
    Sec2 = 'Sec2'
    Sec3 = 'Sec3'
    Sec4 = 'Sec4'
    Sec5 = 'Sec5'
    Sec6 = 'Sec6'
    Sec7 = 'Sec7'
    Sec8 = 'Sec8'
    Sec9 = 'Sec9'
    Sec10 = 'Sec10'
    Sec11 = 'Sec11'
    Sec12 = 'Sec12'
    Sec13 = 'Sec13'
    Sec14 = 'Sec14'
    Sec15 = 'Sec15'
    Sec16 = 'Sec16'
    Sec17 = 'Sec17'
    Sec18 = 'Sec18'
    Sec19 = 'Sec19'
    Sec20 = 'Sec20'
    Sec21 = 'Sec21'
    Sec22 = 'Sec22'
    Sec23 = 'Sec23'
    Sec24 = 'Sec24'
    Sec25 = 'Sec25'
    Sec26 = 'Sec26'
    Sec27 = 'Sec27'
    Sec28 = 'Sec28'
    Sec29 = 'Sec29'
    Sec30 = 'Sec30'
    Sec31 = 'Sec31'
    Sec32 = 'Sec32'
    Sec33 = 'Sec33'
    Sec34 = 'Sec34'
    Sec35 = 'Sec35'
    Sec36 = 'Sec36'

class GDSEASON(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12

    @classmethod
    def getMonthbyVal(cls, val):
        for month in cls:
            if month.value == val:
                return month
        return None

class LOW_WIND(Enum):
    SVmin = 1
    WSmin = 2
    FRANmax = 3

class AWMADWNW(Enum):
    AWMAUEFF = 1
    AWMAUTURB = 2
    STREAMLINE = 3

class ORD_DWNW(Enum):
    ORDUEFF = 1
    ORDTURB = 2
    ORDCAV = 3

class ARMRATIO(Enum):
    ARM2_Min = 1
    ARM2_Max = 2

class O3SECTOR(Enum):
    StartSect1 = 1
    StartSect2 = 2
    StartSect3 = 3
    StartSect4 = 4
    StartSect5 = 5
    StartSect6 = 6

class OZONEFIL(Enum):
    O3FileName = 1
    O3Units = 2
    O3Format = 3

class OZONEVAL(Enum):
    O3Value = 1
    O3Units = 2

class O3VALUES(Enum):
    O3Flag = 1
    O3values = 2

class OZONUNIT(Enum):
    Ozonunit = 1

class FLAGPOLE(Enum):
    Flagpole = 1

class RUNORNOT(Enum):
    Run = 1
    Not = 2

class EVENTFIL(Enum):
    Evfile = 1
    Evopt = 2

class SAVEFILE(Enum):
    Savfil = 1
    Dayinc = 2
    Savfl2 = 3

class INITFILE(Enum):
    INITFILE = 1

class ERRORFIL(Enum):
    ERRORFIL = 1

class MULTYEAR(Enum):
    H6H = 1
    Savfil = 2
    Inifil = 3

class DEBUGOPT(Enum):
    MODEL = 1
    Dbgfil = 2
    METEOR = 3
    Dbmfil = 4
    PRIME = 5
    Prmfil = 6
    AWMADW = 7
    AwmaDwfil = 8
    DEPOS = 9
    AREA = 10
    LINE = 11
    AreaDbfil = 12
    PVMRM = 13
    Dbpvfil = 14
    OLM = 15
    OLMfil = 16
    ARM2 = 17
    ARM2fil = 18