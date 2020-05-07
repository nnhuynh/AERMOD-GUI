from enum import Enum

class ELEVUNIT(Enum):
    ELEVUNIT = 0
    METERS = 1
    FEET = 2

class GRIDCART(Enum):
    GRIDCART = 0
    NetId_1 = 1
    XYINC_1 = 2
    XPNTS_1 = 3
    YPNTS_1 = 4
    ELEV_1 = 5
    HILL_1 = 6
    FLAG_1 = 7

    NetId_2 = 21
    XYINC_2 = 22
    XPNTS_2 = 23
    YPNTS_2 = 24
    ELEV_2 = 25
    HILL_2 = 26
    FLAG_2 = 27

    NetId_3 = 31
    XYINC_3 = 32
    XPNTS_3 = 33
    YPNTS_3 = 34
    ELEV_3 = 35
    HILL_3 = 36
    FLAG_3 = 37

class GRIDPOLR(Enum):
    GRIDPOLR = 0
    NetId_1 = 1
    ORIG_1 = 2
    DIST_1 = 3
    DDIR_1 = 4
    GDIR_1 = 5
    ELEV_1 = 6
    HILL_1 = 7
    FLAG_1 = 8

    NetId_2 = 21
    ORIG_2 = 22
    DIST_2 = 23
    DDIR_2 = 24
    GDIR_2 = 25
    ELEV_2 = 26
    HILL_2 = 27
    FLAG_2 = 28

    NetId_3 = 31
    ORIG_3 = 32
    DIST_3 = 33
    DDIR_3 = 34
    GDIR_3 = 35
    ELEV_3 = 36
    HILL_3 = 37
    FLAG_3 = 38

class DISCCART(Enum):
    DISCCART = 0

    Xcoord_1 = 1
    Ycoord_1 = 2
    Zelev_1 = 3
    Zhill_1 = 4
    Zflag_1 = 5

    Xcoord_2 = 21
    Ycoord_2 = 22
    Zelev_2 = 23
    Zhill_2 = 24
    Zflag_2 = 25

    Xcoord_3 = 31
    Ycoord_3 = 32
    Zelev_3 = 33
    Zhill_3 = 34
    Zflag_3 = 35

class DISCPOLR(Enum):
    DISCPOLR = 0

    Srcid_1 = 1
    Dist_1 = 2
    Direct_1 = 3
    Zelev_1 = 4
    Zhill_1 = 5
    Zflag_1 = 6

    Srcid_2 = 21
    Dist_2 = 22
    Direct_2 = 23
    Zelev_2 = 24
    Zhill_2 = 25
    Zflag_2 = 26

    Srcid_3 = 31
    Dist_3 = 32
    Direct_3 = 33
    Zelev_3 = 34
    Zhill_3 = 35
    Zflag_3 = 36

class EVALCART(Enum):
    EVALCART = 0

    Xcoord_1 = 1
    Ycoord_1 = 2
    Zelev_1 = 3
    Zhill_1 = 4
    Zflag_1 = 5
    Arcid_1 = 6
    Name_1 = 7

    Xcoord_2 = 21
    Ycoord_2 = 22
    Zelev_2 = 23
    Zhill_2 = 24
    Zflag_2 = 25
    Arcid_2 = 26
    Name_2 = 27

    Xcoord_3 = 31
    Ycoord_3 = 32
    Zelev_3 = 33
    Zhill_3 = 34
    Zflag_3 = 35
    Arcid_3 = 36
    Name_3 = 37

class INCLUDED(Enum):
    INLCUDED = 0
    RecIncFile = 1