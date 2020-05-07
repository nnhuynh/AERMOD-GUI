from enum import Enum

class ELEVUNIT(Enum):
    ELEVUNIT = 0
    METERS = 1
    FEET = 2

class LOCATION(Enum):
    LOCATION = 0
    SrcID_t1 = 'SrcID_t1'
    Srctyp_t1 = 'Srctyp_1'
    Xs_t1 = 'Xs_1'
    Ys_t1 = 'Ys_1'
    Zs_t1 = 'Zs_1'
    SrcID_t2 = 'SrcID_t2'
    Srctyp_t2 = 'Srctyp_2'
    Xs1_t2 = 'Xs1_2'
    Ys1_t2 = 'Ys1_2'
    Xs2_t2 = 'Xs2_2'
    Ys2_t2 = 'Ys2_2'
    Zs_t2 = 'Zs_2'
    SrcID_t3 = 'SrcID_t3'
    Srctyp_t3 = 'Srctyp_3'
    Xs1_t3 = 'Xs1_3'
    Ys1_t3 = 'Ys1_3'
    Zs1_t3 = 'Zs1_3'
    Xs2_t3 = 'Xs2_3'
    Ys2_t3 = 'Ys2_3'
    Zs2_t3 = 'Zs2_3'

class SRCPARAM(Enum):
    SRCPARAM = 0
    SrcID_t1 = 1
    Ptemis_t1 = 2
    Stkhgt_t1 = 3
    Stktmp_t1 = 4
    Stkvel_t1 = 5
    Stkdia_t1 = 6
    Vlemis_t1 = 7
    Relhgt_t1 = 8
    Syinit_t1 = 9
    Szinit_t1 = 10
    Aremis_t1 = 11
    Xinit_t1 = 12
    Yinit_t1 = 13
    Angle_t1 = 14
    Nverts_t1 = 15
    Radius_t1 = 16
    Lnemis_t1 = 17
    Width_t1 = 18
    Opemis_t1 = 19
    Pitvol_t1 = 20
    Blemis_t1 = 21
    Qemis_t1 = 22
    DCL_t1 = 23

    SrcID_t2 = 24
    Ptemis_t2 = 25
    Stkhgt_t2 = 26
    Stktmp_t2 = 27
    Stkvel_t2 = 28
    Stkdia_t2 = 29
    Vlemis_t2 = 30
    Relhgt_t2 = 31
    Syinit_t2 = 32
    Szinit_t2 = 33
    Aremis_t2 = 34
    Xinit_t2 = 35
    Yinit_t2 = 36
    Angle_t2 = 37
    Nverts_t2 = 38
    Radius_t2 = 39
    Lnemis_t2 = 40
    Width_t2 = 41
    Opemis_t2 = 42
    Pitvol_t2 = 43
    Blemis_t2 = 44
    Qemis_t2 = 45
    DCL_t2 = 46

    SrcID_t3 = 47
    Ptemis_t3 = 48
    Stkhgt_t3 = 49
    Stktmp_t3 = 50
    Stkvel_t3 = 51
    Stkdia_t3 = 52
    Vlemis_t3 = 53
    Relhgt_t3 = 54
    Syinit_t3 = 55
    Szinit_t3 = 56
    Aremis_t3 = 57
    Xinit_t3 = 58
    Yinit_t3 = 59
    Angle_t3 = 60
    Nverts_t3 = 61
    Radius_t3 = 62
    Lnemis_t3 = 63
    Width_t3 = 64
    Opemis_t3 = 65
    Pitvol_t3 = 66
    Blemis_t3 = 67
    Qemis_t3 = 68
    DCL_t3 = 69

class SRCTYPE(Enum):
    POINT = 0
    POINTCAP = 1
    POINTHOR = 2
    VOLUME = 3
    AREA = 4
    AREAPOLY = 5
    AREACIRC = 6
    OPENPIT = 7
    LINE = 8
    BUOYLINE = 9
    RLINE = 10
    RLINEXT = 11

class BUILDHGT(Enum):
    BUILDHGT = 0
    SrcID_t1 = 1
    Dsbh_t1 = 2
    SrcID_t2 = 3
    Dsbh_t2 = 4
    SrcID_t3 = 5
    Dsbh_t3 = 6

class BUILDLEN(Enum):
    BUILDLEN = 0
    SrcID_t1 = 1
    Dsbl_t1 = 2
    SrcID_t2 = 3
    Dsbl_t2 = 4
    SrcID_t3 = 5
    Dsbl_t3 = 6

class BUILDWID(Enum):
    BUILDWID = 0
    SrcID_t1 = 1
    Dsbw_t1 = 2
    SrcID_t2 = 3
    Dsbw_t2 = 4
    SrcID_t3 = 5
    Dsbw_t3 = 6

class XBADJ(Enum):
    XBADJ = 0
    SrcID_t1 = 1
    Xbadj_t1 = 2
    SrcID_t2 = 3
    Xbadj_t2 = 4
    SrcID_t3 = 5
    Xbadj_t3 = 6

class YBADJ(Enum):
    YBADJ = 0
    SrcID_t1 = 1
    Ybadj_t1 = 2
    SrcID_t2 = 3
    Ybadj_t2 = 4
    SrcID_t3 = 5
    Ybadj_t3 = 6

class AREAVERT(Enum):
    AREAVERT = 0
    SrcID_t1 = 1
    XYv_t1 = 2
    SrcID_t2 = 3
    XYv_t2 = 4
    SrcID_t3 = 5
    XYv_t3 = 6

class RBARRIER(Enum):
    RBARRIER = 0
    SrcID_t1 = 1
    Htwall_t1 = 2
    DCLwall_t1 = 3
    SrcID_t2 = 4
    Htwall_t2 = 5
    DCLwall_t2 = 6
    SrcID_t3 = 7
    Htwall_t3 = 8
    DCLwall_t3 = 9

class RDEPRESS(Enum):
    RDEPRESS = 0
    SrcID_t1 = 1
    Depth_t1 = 2
    Wtop_t1 = 3
    Wbottom_t1 = 4
    SrcID_t2 = 5
    Depth_t2 = 6
    Wtop_t2 = 7
    Wbottom_t2 = 8
    SrcID_t3 = 9
    Depth_t3 = 10
    Wtop_t3 = 11
    Wbottom_t3 = 12

class URBANRSC(Enum):
    URBANSRC = 0
    UrbanID1 = 1
    SrcID1 = 2
    UrbanID2 = 3
    SrcID2 = 4
    UrbanID3 = 5
    SrcID3 = 6
    UrbanID4 = 7
    SrcID4 = 8
    UrbanID5 = 9
    SrcID5 = 10

class EMISFACT(Enum):
    EMISFACT = 0
    SrcID_t1 = 1
    Qflag_t1 = 2
    Qfact_t1 = 3
    SrcID_t2 = 4
    Qflag_t2 = 5
    Qfact_t2 = 6
    SrcID_t3 = 7
    Qflag_t3 = 8
    Qfact_t3 = 9

class EMISFLAG(Enum):
    SEASON = 1
    MONTH = 2
    HROFDY = 3
    WSPEED = 4
    SEASHR = 5
    HRDOW = 6
    HRDOW7 = 7
    SHRDOW = 8
    SHRDOW7 = 9
    MHRDOW = 10
    MHRDOW7 = 11

    @classmethod
    def getListEMISFLAG(cls):
        flagList = []
        for flag in cls:
            flagList.append(flag.name)
        return flagList

class EMISUNIT(Enum):
    EMISUNIT = 0
    Emifac = 1
    Emilbl = 2
    Outlbl = 3

class RLEMCONV(Enum):
    RLEMCONV = 0

class CONCUNIT(Enum):
    CONCUNIT = 0
    Emifac = 1
    Emilbl = 2
    Conlbl = 3

class DEPOUNIT(Enum):
    DEPOUNIT = 0
    Emifac = 1
    Emilbl = 2
    Deplbl = 3

class PARTDIAM(Enum):
    PARTDIAM = 0
    SrcID_t1 = 1
    Pdiam_t1 = 2
    SrcID_t2 = 3
    Pdiam_t2 = 4
    SrcID_t3 = 5
    Pdiam_t3 = 6

class MASSFRAX(Enum):
    MASSFRAX = 0
    SrcID_t1 = 1
    Phi_t1 = 2
    SrcID_t2 = 3
    Phi_t2 = 4
    SrcID_t3 = 5
    Phi_t3 = 6

class PARTDENS(Enum):
    PARTDENS = 0
    SrcID_t1 = 1
    Pdens_t1 = 2
    SrcID_t2 = 3
    Pdens_t2 = 4
    SrcID_t3 = 5
    Pdens_t3 = 6

class METHOD_2(Enum):
    METHOD_2 = 0
    SrcID_t1 = 1
    FineMassFraction_t1 = 2
    Dmm_t1 = 3
    SrcID_t2 = 4
    FineMassFraction_t2 = 5
    Dmm_t2 = 6
    SrcID_t3 = 7
    FineMassFraction_t3 = 8
    Dmm_t3 = 9

class GASDEPOS(Enum):
    GASDEPOS = 0
    SrcID_t1 = 1
    Da_t1 = 2
    Dw_t1 = 3
    rcl_t1 = 4
    Henry_t1 = 5

    SrcID_t2 = 6
    Da_t2 = 7
    Dw_t2 = 8
    rcl_t2 = 9
    Henry_t2 = 10

    SrcID_t3 = 11
    Da_t3 = 12
    Dw_t3 = 13
    rcl_t3 = 14
    Henry_t3 = 15

class NO2RATIO(Enum):
    NO2RATIO = 0
    SrcID_t1 = 1
    NO2Ratio_t1 = 2
    SrcID_t2 = 3
    NO2Ratio_t2 = 4
    SrcID_t3 = 5
    NO2Ratio_t3 = 6

class HOUREMIS(Enum):
    HOUREMIS = 0
    SrcID_t1 = 1
    SrcID_t2 = 2
    SrcID_t3 = 3
    Emifil = 4

class BGSECTOR(Enum):
    BGSECTOR = 0
    StartSect1 = 1
    StartSect2 = 2
    StartSect3 = 3
    StartSect4 = 4
    StartSect5 = 5
    StartSect6 = 6

class BACKGRND(Enum):
    BACKGRND = 0
    BGflag = 1
    BGvalue = 2
    HOURLY = 3
    BGfilnam = 4
    BGformat = 5

class BGFLAG(Enum):
    EMPTY = ''
    ANNUAL = 'ANNUAL'
    SEASON = 'SEASON'
    MONTH = 'MONTH'
    HROFDY = 'HROFDY'
    WSPEED = 'WSPEED'
    SEASHR = 'SEASHR'
    HRDOW = 'HRDOW'
    HRDOW7 = 'HRDOW7'
    SHRDOW = 'SHRDOW'
    SHRDOW7 = 'SHRDOW7'
    MHRDOW = 'MHRDOW'
    MHRDOW7 = 'MHRDOW7'

    @classmethod
    def getListBGFLAG(cls):
        flagList = []
        for flag in cls:
            flagList.append(flag.value)
        return flagList

class BACKUNIT(Enum):
    BACKUNIT = 0
    BGunits = 1

class INCLUDED(Enum):
    INCLUDED = 0
    Incfil = 1

class OLMGROUP(Enum):
    OLMGROUP = 0
    OLMGrpID = 1
    SrcID_t1 = 2
    SrcID_t2 = 3
    SrcID_t3 = 4
    ALL = 5

class PSDGROUP(Enum):
    PSDGROUP = 0
    PSDGrpID = 1
    SrcID_t1 = 2
    SrcID_t2 = 3
    SrcID_t3 = 4

class SRCGROUP(Enum):
    SRCGROUP = 0
    SrcGrpID = 1
    SrcID_t1 = 2
    SrcID_t2 = 3
    SrcID_t3 = 4
    ALL = 5
