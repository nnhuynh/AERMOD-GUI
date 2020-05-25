import constantsSO as constSO

import constantsCO as constCO
import guiCO


# ======================================================================================================================
def writeELEVUNIT(elevunit):
    elevunitStr = 'SO ELEVUNIT %s' % elevunit[constSO.ELEVUNIT.ELEVUNIT.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % elevunitStr)

# ======================================================================================================================
def writeLOCAION(location):
    locationStr = 'SO LOCATION'

    if len(location[constSO.LOCATION.SrcID_t1.name].get())>0:
        locStr1 = '%s %s %s %s %s %s' % (locationStr,
                                         location[constSO.LOCATION.SrcID_t1.name].get(),
                                         location[constSO.LOCATION.Srctyp_t1.name].get(),
                                         location[constSO.LOCATION.Xs_t1.name].get(),
                                         location[constSO.LOCATION.Ys_t1.name].get(),
                                         location[constSO.LOCATION.Zs_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % locStr1)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        locStr2 = '%s %s %s %s %s %s %s %s' % (locationStr,
                                               location[constSO.LOCATION.SrcID_t2.name].get(),
                                               location[constSO.LOCATION.Srctyp_t2.name].get(),
                                               location[constSO.LOCATION.Xs1_t2.name].get(),
                                               location[constSO.LOCATION.Ys1_t2.name].get(),
                                               location[constSO.LOCATION.Zs_t2.name].get(),
                                               location[constSO.LOCATION.Xs2_t2.name].get(),
                                               location[constSO.LOCATION.Ys2_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % locStr2)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        locStr3 = '%s %s %s %s %s %s %s %s %s' % (locationStr,
                                                  location[constSO.LOCATION.SrcID_t3.name].get(),
                                                  location[constSO.LOCATION.Srctyp_t3.name].get(),
                                                  location[constSO.LOCATION.Xs1_t3.name].get(),
                                                  location[constSO.LOCATION.Ys1_t3.name].get(),
                                                  location[constSO.LOCATION.Zs1_t3.name].get(),
                                                  location[constSO.LOCATION.Xs2_t3.name].get(),
                                                  location[constSO.LOCATION.Ys2_t3.name].get(),
                                                  location[constSO.LOCATION.Zs2_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % locStr3)

# ======================================================================================================================
def writeSRCPARAM(srcparam, location):
    srcparamStr = 'SO SRCPARAM'

    # SrcID_t1 =========================================================================================================
    if len(location[constSO.LOCATION.SrcID_t1.name].get())>0:
        if (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.POINT.name) or \
                (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.POINTCAP.name) or \
                (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.POINTHOR.name):
            paramStr1 = '%s %s %s %s %s %s %s' % (srcparamStr,
                                                  location[constSO.LOCATION.SrcID_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Ptemis_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkhgt_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stktmp_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkvel_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkdia_t1.name].get())
        elif (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.VOLUME.name):
            paramStr1 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Vlemis_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Syinit_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t1.name].get())
        elif (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.AREA.name):
            paramStr1 = '%s %s %s %s %s %s %s %s' % (srcparamStr,
                                                     location[constSO.LOCATION.SrcID_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Aremis_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Relhgt_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Xinit_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Yinit_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Angle_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Szinit_t1.name].get())
        elif (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.AREAPOLY.name):
            paramStr1 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Aremis_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Nverts_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t1.name].get())
        elif (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.AREACIRC.name):
            paramStr1 = '%s %s %s %s %s %s %s' % (srcparamStr,
                                                  location[constSO.LOCATION.SrcID_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Aremis_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Relhgt_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Radius_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Nverts_t1.name].get(),
                                                  srcparam[constSO.SRCPARAM.Szinit_t1.name].get())
        elif (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.LINE.name) or \
            (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.RLINE.name):
            paramStr1 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Lnemis_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Width_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t1.name].get())
        elif (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.OPENPIT.name):
            paramStr1 = '%s %s %s %s %s %s %s %s' % (srcparamStr,
                                                     location[constSO.LOCATION.SrcID_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Opemis_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Relhgt_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Xinit_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Yinit_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Pitvol_t1.name].get(),
                                                     srcparam[constSO.SRCPARAM.Angle_t1.name].get())
        elif (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.BUOYLINE.name):
            paramStr1 = '%s %s %s %s' % (srcparamStr,
                                         location[constSO.LOCATION.SrcID_t1.name].get(),
                                         srcparam[constSO.SRCPARAM.Blemis_t1.name].get(),
                                         srcparam[constSO.SRCPARAM.Relhgt_t1.name].get())
        elif (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.RLINEXT.name):
            paramStr1 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Qemis_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.DCL_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Width_t1.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % paramStr1)

    # SrcID_t2 =========================================================================================================
    if len(location[constSO.LOCATION.SrcID_t2.name].get())>0:
        if (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.POINT.name) or \
                (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.POINTCAP.name) or \
                (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.POINTHOR.name):
            paramStr2 = '%s %s %s %s %s %s %s' % (srcparamStr,
                                                  location[constSO.LOCATION.SrcID_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Ptemis_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkhgt_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stktmp_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkvel_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkdia_t2.name].get())
        elif (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.VOLUME.name):
            paramStr2 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Vlemis_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Syinit_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t2.name].get())
        elif (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.AREA.name):
            paramStr2 = '%s %s %s %s %s %s %s %s' % (srcparamStr,
                                                     location[constSO.LOCATION.SrcID_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Aremis_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Relhgt_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Xinit_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Yinit_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Angle_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Szinit_t2.name].get())
        elif (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.AREAPOLY.name):
            paramStr2 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Aremis_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Nverts_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t2.name].get())
        elif (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.AREACIRC.name):
            paramStr2 = '%s %s %s %s %s %s %s' % (srcparamStr,
                                                  location[constSO.LOCATION.SrcID_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Aremis_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Relhgt_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Radius_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Nverts_t2.name].get(),
                                                  srcparam[constSO.SRCPARAM.Szinit_t2.name].get())
        elif (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.LINE.name) or \
            (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.RLINE.name):
            paramStr2 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Lnemis_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Width_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t2.name].get())
        elif (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.OPENPIT.name):
            paramStr2 = '%s %s %s %s %s %s %s %s' % (srcparamStr,
                                                     location[constSO.LOCATION.SrcID_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Opemis_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Relhgt_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Xinit_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Yinit_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Pitvol_t2.name].get(),
                                                     srcparam[constSO.SRCPARAM.Angle_t2.name].get())
        elif (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.BUOYLINE.name):
            paramStr2 = '%s %s %s %s' % (srcparamStr,
                                         location[constSO.LOCATION.SrcID_t2.name].get(),
                                         srcparam[constSO.SRCPARAM.Blemis_t2.name].get(),
                                         srcparam[constSO.SRCPARAM.Relhgt_t2.name].get())
        elif (location[constSO.LOCATION.Srctyp_t2.name].get()==constSO.SRCTYPE.RLINEXT.name):
            paramStr2 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Qemis_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.DCL_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Width_t2.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % paramStr2)

    # SrcID_t3 =========================================================================================================
    if len(location[constSO.LOCATION.SrcID_t3.name].get())>0:
        if (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.POINT.name) or \
                (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.POINTCAP.name) or \
                (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.POINTHOR.name):
            paramStr3 = '%s %s %s %s %s %s %s' % (srcparamStr,
                                                  location[constSO.LOCATION.SrcID_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Ptemis_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkhgt_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stktmp_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkvel_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Stkdia_t3.name].get())
        elif (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.VOLUME.name):
            paramStr3 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Vlemis_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Syinit_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t3.name].get())
        elif (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.AREA.name):
            paramStr3 = '%s %s %s %s %s %s %s %s' % (srcparamStr,
                                                     location[constSO.LOCATION.SrcID_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Aremis_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Relhgt_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Xinit_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Yinit_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Angle_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Szinit_t3.name].get())
        elif (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.AREAPOLY.name):
            paramStr3 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Aremis_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Nverts_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t3.name].get())
        elif (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.AREACIRC.name):
            paramStr3 = '%s %s %s %s %s %s %s' % (srcparamStr,
                                                  location[constSO.LOCATION.SrcID_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Aremis_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Relhgt_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Radius_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Nverts_t3.name].get(),
                                                  srcparam[constSO.SRCPARAM.Szinit_t3.name].get())
        elif (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.LINE.name) or \
            (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.RLINE.name):
            paramStr3 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Lnemis_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Relhgt_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Width_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t3.name].get())
        elif (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.OPENPIT.name):
            paramStr3 = '%s %s %s %s %s %s %s %s' % (srcparamStr,
                                                     location[constSO.LOCATION.SrcID_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Opemis_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Relhgt_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Xinit_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Yinit_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Pitvol_t3.name].get(),
                                                     srcparam[constSO.SRCPARAM.Angle_t3.name].get())
        elif (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.BUOYLINE.name):
            paramStr3 = '%s %s %s %s' % (srcparamStr,
                                         location[constSO.LOCATION.SrcID_t3.name].get(),
                                         srcparam[constSO.SRCPARAM.Blemis_t3.name].get(),
                                         srcparam[constSO.SRCPARAM.Relhgt_t3.name].get())
        elif (location[constSO.LOCATION.Srctyp_t3.name].get()==constSO.SRCTYPE.RLINEXT.name):
            paramStr3 = '%s %s %s %s %s %s' % (srcparamStr,
                                               location[constSO.LOCATION.SrcID_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Qemis_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.DCL_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Width_t3.name].get(),
                                               srcparam[constSO.SRCPARAM.Szinit_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % paramStr3)

# ======================================================================================================================
def writeBUILDHGT(buildhgt, location):
    buildhgtStr = 'SO BUILDHGT'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        bhStr1 = '%s %s %s' % (buildhgtStr,
                               location[constSO.LOCATION.SrcID_t1.name].get(),
                               buildhgt[constSO.BUILDHGT.Dsbh_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % bhStr1)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        bhStr2 = '%s %s %s' % (buildhgtStr,
                               location[constSO.LOCATION.SrcID_t2.name].get(),
                               buildhgt[constSO.BUILDHGT.Dsbh_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % bhStr2)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        bhStr3 = '%s %s %s' % (buildhgtStr,
                               location[constSO.LOCATION.SrcID_t3.name].get(),
                               buildhgt[constSO.BUILDHGT.Dsbh_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % bhStr3)


# ======================================================================================================================
def writeBUILDLEN(buildlen, location):
    buildlenStr = 'SO BUILDLEN'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        blStr1 = '%s %s %s' % (buildlenStr,
                               location[constSO.LOCATION.SrcID_t1.name].get(),
                               buildlen[constSO.BUILDLEN.Dsbl_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % blStr1)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        blStr2 = '%s %s %s' % (buildlenStr,
                               location[constSO.LOCATION.SrcID_t2.name].get(),
                               buildlen[constSO.BUILDLEN.Dsbl_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % blStr2)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        blStr3 = '%s %s %s' % (buildlenStr,
                               location[constSO.LOCATION.SrcID_t3.name].get(),
                               buildlen[constSO.BUILDLEN.Dsbl_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % blStr3)


# ======================================================================================================================
def writeBUILDWID(buildwid, location):
    buildwidStr = 'SO BUILDWID'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        bwStr1 = '%s %s %s' % (buildwidStr,
                               location[constSO.LOCATION.SrcID_t1.name].get(),
                               buildwid[constSO.BUILDWID.Dsbw_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % bwStr1)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        bwStr2 = '%s %s %s' % (buildwidStr,
                               location[constSO.LOCATION.SrcID_t2.name].get(),
                               buildwid[constSO.BUILDWID.Dsbw_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % bwStr2)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        bwStr3 = '%s %s %s' % (buildwidStr,
                               location[constSO.LOCATION.SrcID_t3.name].get(),
                               buildwid[constSO.BUILDWID.Dsbw_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % bwStr3)


# ======================================================================================================================
def writeXBADJ(xbadj, location):
    xbadjStr = 'SO XBADJ'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        str1 = '%s %s %s' % (xbadjStr,
                               location[constSO.LOCATION.SrcID_t1.name].get(),
                               xbadj[constSO.XBADJ.Xbadj_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str1)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        str2 = '%s %s %s' % (xbadjStr,
                               location[constSO.LOCATION.SrcID_t2.name].get(),
                               xbadj[constSO.XBADJ.Xbadj_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str2)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        str3 = '%s %s %s' % (xbadjStr,
                               location[constSO.LOCATION.SrcID_t3.name].get(),
                               xbadj[constSO.XBADJ.Xbadj_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str3)


# ======================================================================================================================
def writeYBADJ(ybadj, location):
    ybadjStr = 'SO YBADJ'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        str1 = '%s %s %s' % (ybadjStr,
                               location[constSO.LOCATION.SrcID_t1.name].get(),
                               ybadj[constSO.YBADJ.Ybadj_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str1)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        str2 = '%s %s %s' % (ybadjStr,
                               location[constSO.LOCATION.SrcID_t2.name].get(),
                               ybadj[constSO.YBADJ.Ybadj_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str2)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        str3 = '%s %s %s' % (ybadjStr,
                               location[constSO.LOCATION.SrcID_t3.name].get(),
                               ybadj[constSO.YBADJ.Ybadj_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str3)

# ======================================================================================================================
def writeAREAVERT(areavert, location):
    areavertStr = 'SO AREAVERT'

    if (len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0) and \
            (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.AREAPOLY.name):
        str1 = '%s %s %s' % (areavertStr,
                             location[constSO.LOCATION.SrcID_t1.name].get(),
                             areavert[constSO.AREAVERT.XYv_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str1)

    if (len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0)  and \
            (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.AREAPOLY.name):
        str2 = '%s %s %s' % (areavertStr,
                             location[constSO.LOCATION.SrcID_t2.name].get(),
                             areavert[constSO.AREAVERT.XYv_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str2)

    if (len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0)  and \
            (location[constSO.LOCATION.Srctyp_t1.name].get()==constSO.SRCTYPE.AREAPOLY.name):
        str3 = '%s %s %s' % (areavertStr,
                             location[constSO.LOCATION.SrcID_t3.name].get(),
                             areavert[constSO.AREAVERT.XYv_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str3)

# ======================================================================================================================
def writeRBARRIER(rbarrier, location, coModelopt):
    if coModelopt[constCO.MODELOPT.ALPHA.name].get()==True:
        rbarrierStr = 'SO RBARRIER'

        if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
            str1 = '%s %s %s %s' % (rbarrierStr,
                                 location[constSO.LOCATION.SrcID_t1.name].get(),
                                 rbarrier[constSO.RBARRIER.Htwall_t1.name].get(),
                                 rbarrier[constSO.RBARRIER.DCLwall_t1.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str1)

        if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
            str2 = '%s %s %s %s' % (rbarrierStr,
                                 location[constSO.LOCATION.SrcID_t2.name].get(),
                                 rbarrier[constSO.RBARRIER.Htwall_t2.name].get(),
                                 rbarrier[constSO.RBARRIER.DCLwall_t2.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str2)

        if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
            str3 = '%s %s %s %s' % (rbarrierStr,
                                 location[constSO.LOCATION.SrcID_t3.name].get(),
                                 rbarrier[constSO.RBARRIER.Htwall_t3.name].get(),
                                 rbarrier[constSO.RBARRIER.DCLwall_t3.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str3)

# ======================================================================================================================
def writeRDEPRESS(rdepress, location, coModelopt):
    if coModelopt[constCO.MODELOPT.ALPHA.name].get()==True:
        rdepressStr = 'SO RDEPRESS'

        if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
            str1 = '%s %s %s %s %s' % (rdepressStr,
                                       location[constSO.LOCATION.SrcID_t1.name].get(),
                                       rdepress[constSO.RDEPRESS.Depth_t1.name].get(),
                                       rdepress[constSO.RDEPRESS.Wtop_t1.name].get(),
                                       rdepress[constSO.RDEPRESS.Wbottom_t1.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str1)

        if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
            str2 = '%s %s %s %s %s' % (rdepressStr,
                                       location[constSO.LOCATION.SrcID_t2.name].get(),
                                       rdepress[constSO.RDEPRESS.Depth_t2.name].get(),
                                       rdepress[constSO.RDEPRESS.Wtop_t2.name].get(),
                                       rdepress[constSO.RDEPRESS.Wbottom_t2.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str2)

        if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
            str3 = '%s %s %s %s %s' % (rdepressStr,
                                       location[constSO.LOCATION.SrcID_t3.name].get(),
                                       rdepress[constSO.RDEPRESS.Depth_t3.name].get(),
                                       rdepress[constSO.RDEPRESS.Wtop_t3.name].get(),
                                       rdepress[constSO.RDEPRESS.Wbottom_t3.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str3)

# ======================================================================================================================
def writeURBANSRC(urbansrc, location):
    urbansrcStr = 'SO URBANSRC'

    if len(urbansrc[constSO.URBANRSC.UrbanID1.name].get()) > 0:
        str1 = '%s %s %s' % (urbansrcStr,
                             urbansrc[constSO.URBANRSC.UrbanID1.name].get(),
                             location[urbansrc[constSO.URBANRSC.SrcID1.name].get()].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str1)

    if len(urbansrc[constSO.URBANRSC.UrbanID2.name].get()) > 0:
        str2 = '%s %s %s' % (urbansrcStr,
                             urbansrc[constSO.URBANRSC.UrbanID2.name].get(),
                             location[urbansrc[constSO.URBANRSC.SrcID2.name].get()].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str2)

    if len(urbansrc[constSO.URBANRSC.UrbanID3.name].get()) > 0:
        str3 = '%s %s %s' % (urbansrcStr,
                             urbansrc[constSO.URBANRSC.UrbanID3.name].get(),
                             location[urbansrc[constSO.URBANRSC.SrcID3.name].get()].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str3)

    if len(urbansrc[constSO.URBANRSC.UrbanID4.name].get()) > 0:
        str4 = '%s %s %s' % (urbansrcStr,
                             urbansrc[constSO.URBANRSC.UrbanID4.name].get(),
                             location[urbansrc[constSO.URBANRSC.SrcID4.name].get()].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str4)

    if len(urbansrc[constSO.URBANRSC.UrbanID5.name].get()) > 0:
        str5 = '%s %s %s' % (urbansrcStr,
                             urbansrc[constSO.URBANRSC.UrbanID5.name].get(),
                             location[urbansrc[constSO.URBANRSC.SrcID5.name].get()].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str5)

# ======================================================================================================================
def writeEMISFACT(emisfact, location):
    emisfactStr = 'SO EMISFACT'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        str = '%s %s %s %s' % (emisfactStr,
                               location[constSO.LOCATION.SrcID_t1.name].get(),
                               emisfact[constSO.EMISFACT.Qflag_t1.name].get(),
                               emisfact[constSO.EMISFACT.Qfact_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        str = '%s %s %s %s' % (emisfactStr,
                               location[constSO.LOCATION.SrcID_t2.name].get(),
                               emisfact[constSO.EMISFACT.Qflag_t2.name].get(),
                               emisfact[constSO.EMISFACT.Qfact_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        str = '%s %s %s %s' % (emisfactStr,
                               location[constSO.LOCATION.SrcID_t3.name].get(),
                               emisfact[constSO.EMISFACT.Qflag_t3.name].get(),
                               emisfact[constSO.EMISFACT.Qfact_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

# ======================================================================================================================
def writeEMISUNIT(emisunit):
    emisunitStr = 'SO EMISUNIT %s %s %s' % (emisunit[constSO.EMISUNIT.Emifac.name].get(),
                                            emisunit[constSO.EMISUNIT.Emilbl.name].get(),
                                            emisunit[constSO.EMISUNIT.Outlbl.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % emisunitStr)

# ======================================================================================================================
def writeRLEMCONV(rlemconv):
    if rlemconv[constSO.RLEMCONV.RLEMCONV.name].get():
        rlemconvStr = 'SO RLEMCONV'
        with open('control.inp', 'a') as f:
            f.write('%s\n' % rlemconvStr)

# ======================================================================================================================
def writeCONCUNIT(concunit):
    concunitStr = 'SO CONCUNIT %s %s %s' % (concunit[constSO.CONCUNIT.Emifac.name].get(),
                                            concunit[constSO.CONCUNIT.Emilbl.name].get(),
                                            concunit[constSO.CONCUNIT.Conlbl.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % concunitStr)

# ======================================================================================================================
def writeDEPOUNIT(depounit):
    depounitStr = 'SO DEPOUNIT %s %s %s' % (depounit[constSO.DEPOUNIT.Emifac.name].get(),
                                            depounit[constSO.DEPOUNIT.Emilbl.name].get(),
                                            depounit[constSO.DEPOUNIT.Deplbl.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % depounitStr)

# ======================================================================================================================
def writePARTDIAM(partdiam, location):
    partdiamStr = 'SO PARTDIAM'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        str = '%s %s %s' % (partdiamStr,
                            location[constSO.LOCATION.SrcID_t1.name].get(),
                            partdiam[constSO.PARTDIAM.Pdiam_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        str = '%s %s %s' % (partdiamStr,
                            location[constSO.LOCATION.SrcID_t2.name].get(),
                            partdiam[constSO.PARTDIAM.Pdiam_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        str = '%s %s %s' % (partdiamStr,
                            location[constSO.LOCATION.SrcID_t3.name].get(),
                            partdiam[constSO.PARTDIAM.Pdiam_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

# ======================================================================================================================
def writeMASSFRAX(massfrax, location):
    massfraxStr = 'SO MASSFRAX'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        str = '%s %s %s' % (massfraxStr,
                            location[constSO.LOCATION.SrcID_t1.name].get(),
                            massfrax[constSO.MASSFRAX.Phi_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        str = '%s %s %s' % (massfraxStr,
                            location[constSO.LOCATION.SrcID_t2.name].get(),
                            massfrax[constSO.MASSFRAX.Phi_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        str = '%s %s %s' % (massfraxStr,
                            location[constSO.LOCATION.SrcID_t3.name].get(),
                            massfrax[constSO.MASSFRAX.Phi_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

# ======================================================================================================================
def writePARTDENS(partdens, location):
    partdensStr = 'SO PARTDENS'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        str = '%s %s %s' % (partdensStr,
                            location[constSO.LOCATION.SrcID_t1.name].get(),
                            partdens[constSO.PARTDENS.Pdens_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        str = '%s %s %s' % (partdensStr,
                            location[constSO.LOCATION.SrcID_t2.name].get(),
                            partdens[constSO.PARTDENS.Pdens_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        str = '%s %s %s' % (partdensStr,
                            location[constSO.LOCATION.SrcID_t3.name].get(),
                            partdens[constSO.PARTDENS.Pdens_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

# ======================================================================================================================
def writeMETHOD_2(method_2, location, coModelopt):
    if coModelopt[constCO.MODELOPT.ALPHA.name].get()==True:
        method_2Str = 'SO METHOD_2'

        if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
            str = '%s %s %s %s' % (method_2Str,
                                   location[constSO.LOCATION.SrcID_t1.name].get(),
                                   method_2[constSO.METHOD_2.FineMassFraction_t1.name].get(),
                                   method_2[constSO.METHOD_2.Dmm_t1.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str)

        if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
            str = '%s %s %s %s' % (method_2Str,
                                   location[constSO.LOCATION.SrcID_t2.name].get(),
                                   method_2[constSO.METHOD_2.FineMassFraction_t2.name].get(),
                                   method_2[constSO.METHOD_2.Dmm_t2.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str)

        if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
            str = '%s %s %s %s' % (method_2Str,
                                   location[constSO.LOCATION.SrcID_t3.name].get(),
                                   method_2[constSO.METHOD_2.FineMassFraction_t3.name].get(),
                                   method_2[constSO.METHOD_2.Dmm_t3.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str)

# ======================================================================================================================
def writeGASDEPOS(gasdepos, location, coModelopt):
    if coModelopt[constCO.MODELOPT.ALPHA.name].get()==True:
        gasdeposStr = 'SO GASDEPOS'

        if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
            str = '%s %s %s %s %s %s' % (gasdeposStr,
                                         location[constSO.LOCATION.SrcID_t1.name].get(),
                                         gasdepos[constSO.GASDEPOS.Da_t1.name].get(),
                                         gasdepos[constSO.GASDEPOS.Dw_t1.name].get(),
                                         gasdepos[constSO.GASDEPOS.rcl_t1.name].get(),
                                         gasdepos[constSO.GASDEPOS.Henry_t1.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str)

        if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
            str = '%s %s %s %s %s %s' % (gasdeposStr,
                                         location[constSO.LOCATION.SrcID_t2.name].get(),
                                         gasdepos[constSO.GASDEPOS.Da_t2.name].get(),
                                         gasdepos[constSO.GASDEPOS.Dw_t2.name].get(),
                                         gasdepos[constSO.GASDEPOS.rcl_t2.name].get(),
                                         gasdepos[constSO.GASDEPOS.Henry_t2.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str)

        if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
            str = '%s %s %s %s %s %s' % (gasdeposStr,
                                         location[constSO.LOCATION.SrcID_t3.name].get(),
                                         gasdepos[constSO.GASDEPOS.Da_t3.name].get(),
                                         gasdepos[constSO.GASDEPOS.Dw_t3.name].get(),
                                         gasdepos[constSO.GASDEPOS.rcl_t3.name].get(),
                                         gasdepos[constSO.GASDEPOS.Henry_t3.name].get())
            with open('control.inp', 'a') as f:
                f.write('%s\n' % str)

# ======================================================================================================================
def writeNO2RATIO(no2ratio, location):
    no2ratioStr = 'SO NO2RATIO'

    if len(location[constSO.LOCATION.SrcID_t1.name].get()) > 0:
        str = '%s %s %s' % (no2ratioStr,
                            location[constSO.LOCATION.SrcID_t1.name].get(),
                            no2ratio[constSO.NO2RATIO.NO2Ratio_t1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t2.name].get()) > 0:
        str = '%s %s %s' % (no2ratioStr,
                            location[constSO.LOCATION.SrcID_t2.name].get(),
                            no2ratio[constSO.NO2RATIO.NO2Ratio_t2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if len(location[constSO.LOCATION.SrcID_t3.name].get()) > 0:
        str = '%s %s %s' % (no2ratioStr,
                            location[constSO.LOCATION.SrcID_t3.name].get(),
                            no2ratio[constSO.NO2RATIO.NO2Ratio_t3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

# ======================================================================================================================
def writeBGSECTOR(bgsector, validBACKGRND):
    if validBACKGRND:
        bgsectorStr = 'SO BGSECTOR %s %s %s %s %s %s' % (bgsector[constSO.BGSECTOR.StartSect1.name].get(),
                                                         bgsector[constSO.BGSECTOR.StartSect2.name].get(),
                                                         bgsector[constSO.BGSECTOR.StartSect3.name].get(),
                                                         bgsector[constSO.BGSECTOR.StartSect4.name].get(),
                                                         bgsector[constSO.BGSECTOR.StartSect5.name].get(),
                                                         bgsector[constSO.BGSECTOR.StartSect6.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % bgsectorStr)

# ======================================================================================================================
def writeHOUREMIS(houremis, location):
    houremisStr = 'SO HOUREMIS'

    srcSpecified = False

    if houremis[constSO.HOUREMIS.SrcID_t1.name].get():
        houremisStr = houremisStr + ' ' + location[constSO.LOCATION.SrcID_t1.name].get()
        srcSpecified = True
    if houremis[constSO.HOUREMIS.SrcID_t2.name].get():
        houremisStr = houremisStr + ' ' + location[constSO.LOCATION.SrcID_t2.name].get()
        srcSpecified = True
    if houremis[constSO.HOUREMIS.SrcID_t3.name].get():
        houremisStr = houremisStr + ' ' + location[constSO.LOCATION.SrcID_t3.name].get()
        srcSpecified = True

    if srcSpecified:
        houremisStr = houremisStr + ' ' + houremis[constSO.HOUREMIS.Emifil.name].get()
        with open('control.inp', 'a') as f:
            f.write('%s\n' % houremisStr)

# ======================================================================================================================
def writeBACKGRND(backgrnd):
    backgrndStr = 'SO BACKGRND'

    valid = False

    if len(backgrnd[constSO.BACKGRND.BGflag.name].get()) > 0:
        backgrndStr = backgrndStr + ' ' + backgrnd[constSO.BACKGRND.BGflag.name].get() + ' ' + \
                      backgrnd[constSO.BACKGRND.BGvalue.name].get()
        valid = True
    if backgrnd[constSO.BACKGRND.HOURLY.name].get():
        backgrndStr = backgrndStr + ' ' + constSO.BACKGRND.HOURLY.name + ' ' + \
                      backgrnd[constSO.BACKGRND.BGfilnam.name].get() + ' ' + \
                      backgrnd[constSO.BACKGRND.BGformat.name].get()
        valid = True

    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % backgrndStr)

    return valid

# ======================================================================================================================
def writeBACKUNIT(backunit):
    backunitStr = 'SO BACKUNIT %s' % backunit[constSO.BACKUNIT.BGunits.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % backunitStr)

# ======================================================================================================================
def writeINCLUDED(included):
    includedStr = 'SO INCLUDED %s' % included[constSO.INCLUDED.Incfil.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % includedStr)

# ======================================================================================================================
def writeOLMGROUP(olmgroup, location):
    olmgroupStr = 'SO OLMGROUP'

    if olmgroup['radbtnVar'].get()==1:
        olmgroupStr = '%s %s' % (olmgroupStr, olmgroup[constSO.OLMGROUP.OLMGrpID.name].get())
        isValid = False
        if olmgroup[constSO.OLMGROUP.SrcID_t1.name].get():
            olmgroupStr = '%s %s' % (olmgroupStr, location[constSO.LOCATION.SrcID_t1.name].get())
            isValid = True
        if olmgroup[constSO.OLMGROUP.SrcID_t2.name].get():
            olmgroupStr = '%s %s' % (olmgroupStr, location[constSO.LOCATION.SrcID_t2.name].get())
            isValid = True
        if olmgroup[constSO.OLMGROUP.SrcID_t3.name].get():
            olmgroupStr = '%s %s' % (olmgroupStr, location[constSO.LOCATION.SrcID_t3.name].get())
            isValid = True
        if isValid:
            with open('control.inp', 'a') as f:
                f.write('%s\n' % olmgroupStr)
    elif olmgroup['radbtnVar'].get()==2:
        olmgroupStr = '%s %s' % (olmgroupStr, constSO.OLMGROUP.ALL.name)
        with open('control.inp', 'a') as f:
            f.write('%s\n' % olmgroupStr)

# ======================================================================================================================
def writePSDGROUP(psdgroup, location):
    psdgroupStr = 'SO PSDGROUP %s' % psdgroup[constSO.PSDGROUP.PSDGrpID.name].get()
    isValid = False
    if psdgroup[constSO.PSDGROUP.SrcID_t1.name].get():
        psdgroupStr = '%s %s' % (psdgroupStr, location[constSO.LOCATION.SrcID_t1.name].get())
        isValid = True
    if psdgroup[constSO.PSDGROUP.SrcID_t2.name].get():
        psdgroupStr = '%s %s' % (psdgroupStr, location[constSO.LOCATION.SrcID_t2.name].get())
        isValid = True
    if psdgroup[constSO.PSDGROUP.SrcID_t3.name].get():
        psdgroupStr = '%s %s' % (psdgroupStr, location[constSO.LOCATION.SrcID_t3.name].get())
        isValid = True
    if isValid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % psdgroupStr)

# ======================================================================================================================
def writeSRCGROUP(srcgroup, location):
    srcgroupStr = 'SO SRCGROUP'

    if srcgroup['radbtnVar'].get() == 1:
        srcgroupStr = '%s %s' % (srcgroupStr, srcgroup[constSO.SRCGROUP.SrcGrpID.name].get())
        isValid = False
        if srcgroup[constSO.SRCGROUP.SrcID_t1.name].get():
            srcgroupStr = '%s %s' % (srcgroupStr, location[constSO.LOCATION.SrcID_t1.name].get())
            isValid = True
        if srcgroup[constSO.SRCGROUP.SrcID_t2.name].get():
            srcgroupStr = '%s %s' % (srcgroupStr, location[constSO.LOCATION.SrcID_t2.name].get())
            isValid = True
        if srcgroup[constSO.SRCGROUP.SrcID_t3.name].get():
            srcgroupStr = '%s %s' % (srcgroupStr, location[constSO.LOCATION.SrcID_t3.name].get())
            isValid = True
        if isValid:
            with open('control.inp', 'a') as f:
                f.write('%s\n' % srcgroupStr)
    elif srcgroup['radbtnVar'].get() == 2:
        srcgroupStr = '%s %s' % (srcgroupStr, constSO.SRCGROUP.ALL.name)
        with open('control.inp', 'a') as f:
            f.write('%s\n' % srcgroupStr)

# ======================================================================================================================
def writeControlFile(soInputs):
    with open('control.inp', 'a') as f:
        f.write('\nSO STARTING\n')

    elevunit = soInputs[0]
    writeELEVUNIT(elevunit)

    location = soInputs[1]
    writeLOCAION(location)

    srcparam = soInputs[2]
    writeSRCPARAM(srcparam, location)

    buildhgt = soInputs[3]
    writeBUILDHGT(buildhgt, location)

    buildlen = soInputs[4]
    writeBUILDLEN(buildlen, location)

    buildwid = soInputs[5]
    writeBUILDWID(buildwid, location)

    xbadj = soInputs[6]
    writeXBADJ(xbadj, location)

    ybadj = soInputs[7]
    writeYBADJ(ybadj, location)

    areavert = soInputs[8]
    writeAREAVERT(areavert, location)

    rbarrier = soInputs[9]
    writeRBARRIER(rbarrier,location, guiCO.modeloptVals)

    rdepress = soInputs[10]
    writeRDEPRESS(rdepress, location, guiCO.modeloptVals)

    urbansrc = soInputs[11]
    writeURBANSRC(urbansrc, location)

    emisfact = soInputs[12]
    writeEMISFACT(emisfact, location)

    emisunit = soInputs[13]
    writeEMISUNIT(emisunit)

    rlemconv = soInputs[14]
    writeRLEMCONV(rlemconv)

    concunit = soInputs[15]
    writeCONCUNIT(concunit)

    depounit = soInputs[16]
    writeDEPOUNIT(depounit)

    partdiam = soInputs[17]
    writePARTDIAM(partdiam, location)

    massfrax = soInputs[18]
    writeMASSFRAX(massfrax, location)

    partdens = soInputs[19]
    writePARTDENS(partdens, location)

    method_2 = soInputs[20]
    writeMETHOD_2(method_2, location, guiCO.modeloptVals)

    gasdepos = soInputs[21]
    writeGASDEPOS(gasdepos, location, guiCO.modeloptVals)

    no2ratio = soInputs[22]
    writeNO2RATIO(no2ratio, location)

    houremis = soInputs[23]
    writeHOUREMIS(houremis, location)

    backgrnd = soInputs[25]
    validBACKGRND = writeBACKGRND(backgrnd)

    bgsector = soInputs[24]
    writeBGSECTOR(bgsector, validBACKGRND)

    backunit = soInputs[26]
    writeBACKUNIT(backunit)

    included = soInputs[27]
    writeINCLUDED(included)

    olmgroup = soInputs[28]
    writeOLMGROUP(olmgroup, location)

    psdgroup = soInputs[29]
    writePSDGROUP(psdgroup, location)

    srcgroup = soInputs[30]
    writeSRCGROUP(srcgroup, location)

    with open('control.inp', 'a') as f:
        f.write('SO FINISHED\n')

