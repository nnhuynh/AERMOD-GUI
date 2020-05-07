import constantsRE as constRE

# ======================================================================================================================
def writeELEVUNIT(elevunit):
    elevunitStr = 'RE ELEVUNIT %s' % elevunit[constRE.ELEVUNIT.ELEVUNIT.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % elevunitStr)

# ======================================================================================================================
def writeGRIDCART(gridcart):
    # Netid_1 ==========================================================================================================
    gridcartStr = 'RE GRIDCART %s' % gridcart[constRE.GRIDCART.NetId_1.name].get()

    with open('control.inp', 'a') as f:
        f.write('%s STA\n' % gridcartStr)

    if gridcart['radbtnVar_1'].get()==1:
        str = '%s XYINC %s' % (gridcartStr, gridcart[constRE.GRIDCART.XYINC_1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)
    elif gridcart['radbtnVar_1'].get()==2:
        str1 = '%s XPNTS %s' % (gridcartStr, gridcart[constRE.GRIDCART.XPNTS_1.name].get())
        str2 = '%s YPNTS %s' % (gridcartStr, gridcart[constRE.GRIDCART.YPNTS_1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str1)
            f.write('%s\n' % str2)

    if gridcart['chkELEV_1'].get():
        str = '%s ELEV %s' % (gridcartStr, gridcart[constRE.GRIDCART.ELEV_1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if gridcart['chkHILL_1'].get():
        str = '%s HILL %s' % (gridcartStr, gridcart[constRE.GRIDCART.HILL_1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if gridcart['chkFLAG_1'].get():
        str = '%s FLAG %s' % (gridcartStr, gridcart[constRE.GRIDCART.FLAG_1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    with open('control.inp', 'a') as f:
        f.write('%s END\n' % gridcartStr)

    # Netid_2 ==========================================================================================================
    gridcartStr = 'RE GRIDCART %s' % gridcart[constRE.GRIDCART.NetId_2.name].get()

    with open('control.inp', 'a') as f:
        f.write('%s STA\n' % gridcartStr)

    if gridcart['radbtnVar_2'].get() == 1:
        str = '%s XYINC %s' % (gridcartStr, gridcart[constRE.GRIDCART.XYINC_2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)
    elif gridcart['radbtnVar_2'].get() == 2:
        str1 = '%s XPNTS %s' % (gridcartStr, gridcart[constRE.GRIDCART.XPNTS_2.name].get())
        str2 = '%s YPNTS %s' % (gridcartStr, gridcart[constRE.GRIDCART.YPNTS_2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str1)
            f.write('%s\n' % str2)

    if gridcart['chkELEV_2'].get():
        str = '%s ELEV %s' % (gridcartStr, gridcart[constRE.GRIDCART.ELEV_2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if gridcart['chkHILL_2'].get():
        str = '%s HILL %s' % (gridcartStr, gridcart[constRE.GRIDCART.HILL_2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if gridcart['chkFLAG_2'].get():
        str = '%s FLAG %s' % (gridcartStr, gridcart[constRE.GRIDCART.FLAG_2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    with open('control.inp', 'a') as f:
        f.write('%s END\n' % gridcartStr)

    # Netid_3 ==========================================================================================================
    gridcartStr = 'RE GRIDCART %s' % gridcart[constRE.GRIDCART.NetId_3.name].get()

    with open('control.inp', 'a') as f:
        f.write('%s STA\n' % gridcartStr)

    if gridcart['radbtnVar_3'].get() == 1:
        str = '%s XYINC %s' % (gridcartStr, gridcart[constRE.GRIDCART.XYINC_3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)
    elif gridcart['radbtnVar_3'].get() == 2:
        str1 = '%s XPNTS %s' % (gridcartStr, gridcart[constRE.GRIDCART.XPNTS_3.name].get())
        str2 = '%s YPNTS %s' % (gridcartStr, gridcart[constRE.GRIDCART.YPNTS_3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str1)
            f.write('%s\n' % str2)

    if gridcart['chkELEV_3'].get():
        str = '%s ELEV %s' % (gridcartStr, gridcart[constRE.GRIDCART.ELEV_3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if gridcart['chkHILL_3'].get():
        str = '%s HILL %s' % (gridcartStr, gridcart[constRE.GRIDCART.HILL_3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    if gridcart['chkFLAG_3'].get():
        str = '%s FLAG %s' % (gridcartStr, gridcart[constRE.GRIDCART.FLAG_3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % str)

    with open('control.inp', 'a') as f:
        f.write('%s END\n' % gridcartStr)

# ======================================================================================================================
def writeGRIDPOLR(gridpolr):
    # NetId_1 ==========================================================================================================
    gridpolrStr = 'RE GRIDPOLR %s' % gridpolr[constRE.GRIDPOLR.NetId_1.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s STA\n' % gridpolrStr)

    if gridpolr['chkORIG_1'].get():
        with open('control.inp', 'a') as f:
            f.write('%s ORIG %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.ORIG_1.name].get()))

    if gridpolr['chkDIST_1'].get():
        with open('control.inp', 'a') as f:
            f.write('%s DIST %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.DIST_1.name].get()))

    if gridpolr['radbtnVar_1'].get()==1:
        with open('control.inp', 'a') as f:
            f.write('%s DDIR %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.DDIR_1.name].get()))
    elif gridpolr['radbtnVar_1'].get()==2:
        with open('control.inp', 'a') as f:
            f.write('%s GDIR %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.GDIR_1.name].get()))

    if gridpolr['chkELEV_1'].get():
        with open('control.inp', 'a') as f:
            f.write('%s ELEV %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.ELEV_1.name].get()))

    if gridpolr['chkHILL_1'].get():
        with open('control.inp', 'a') as f:
            f.write('%s HILL %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.HILL_1.name].get()))

    if gridpolr['chkFLAG_1'].get():
        with open('control.inp', 'a') as f:
            f.write('%s FLAG %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.FLAG_1.name].get()))

    with open('control.inp', 'a') as f:
        f.write('%s END\n' % gridpolrStr)

    # NetId_2 ==========================================================================================================
    gridpolrStr = 'RE GRIDPOLR %s' % gridpolr[constRE.GRIDPOLR.NetId_2.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s STA\n' % gridpolrStr)

    if gridpolr['chkORIG_2'].get():
        with open('control.inp', 'a') as f:
            f.write('%s ORIG %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.ORIG_2.name].get()))

    if gridpolr['chkDIST_2'].get():
        with open('control.inp', 'a') as f:
            f.write('%s DIST %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.DIST_2.name].get()))

    if gridpolr['radbtnVar_2'].get() == 1:
        with open('control.inp', 'a') as f:
            f.write('%s DDIR %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.DDIR_2.name].get()))
    elif gridpolr['radbtnVar_2'].get() == 2:
        with open('control.inp', 'a') as f:
            f.write('%s GDIR %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.GDIR_2.name].get()))

    if gridpolr['chkELEV_2'].get():
        with open('control.inp', 'a') as f:
            f.write('%s ELEV %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.ELEV_2.name].get()))

    if gridpolr['chkHILL_2'].get():
        with open('control.inp', 'a') as f:
            f.write('%s HILL %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.HILL_2.name].get()))

    if gridpolr['chkFLAG_2'].get():
        with open('control.inp', 'a') as f:
            f.write('%s FLAG %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.FLAG_2.name].get()))

    with open('control.inp', 'a') as f:
        f.write('%s END\n' % gridpolrStr)

    # NetId_3 ==========================================================================================================
    gridpolrStr = 'RE GRIDPOLR %s' % gridpolr[constRE.GRIDPOLR.NetId_3.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s STA\n' % gridpolrStr)

    if gridpolr['chkORIG_3'].get():
        with open('control.inp', 'a') as f:
            f.write('%s ORIG %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.ORIG_3.name].get()))

    if gridpolr['chkDIST_3'].get():
        with open('control.inp', 'a') as f:
            f.write('%s DIST %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.DIST_3.name].get()))

    if gridpolr['radbtnVar_3'].get() == 1:
        with open('control.inp', 'a') as f:
            f.write('%s DDIR %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.DDIR_3.name].get()))
    elif gridpolr['radbtnVar_3'].get() == 2:
        with open('control.inp', 'a') as f:
            f.write('%s GDIR %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.GDIR_3.name].get()))

    if gridpolr['chkELEV_3'].get():
        with open('control.inp', 'a') as f:
            f.write('%s ELEV %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.ELEV_3.name].get()))

    if gridpolr['chkHILL_3'].get():
        with open('control.inp', 'a') as f:
            f.write('%s HILL %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.HILL_3.name].get()))

    if gridpolr['chkFLAG_3'].get():
        with open('control.inp', 'a') as f:
            f.write('%s FLAG %s\n' % (gridpolrStr, gridpolr[constRE.GRIDPOLR.FLAG_3.name].get()))

    with open('control.inp', 'a') as f:
        f.write('%s END\n' % gridpolrStr)

# ======================================================================================================================
def writeDISCCART(disccart):
    if len(disccart[constRE.DISCCART.Xcoord_1.name].get()) > 0 and \
            len(disccart[constRE.DISCCART.Ycoord_1.name].get()) > 0:
        disccartStr = 'RE DISCCART %s %s %s %s %s' % (disccart[constRE.DISCCART.Xcoord_1.name].get(),
                                                      disccart[constRE.DISCCART.Ycoord_1.name].get(),
                                                      disccart[constRE.DISCCART.Zelev_1.name].get(),
                                                      disccart[constRE.DISCCART.Zhill_1.name].get(),
                                                      disccart[constRE.DISCCART.Zflag_1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % disccartStr)

    if len(disccart[constRE.DISCCART.Xcoord_2.name].get()) > 0 and \
            len(disccart[constRE.DISCCART.Ycoord_2.name].get()) > 0:
        disccartStr = 'RE DISCCART %s %s %s %s %s' % (disccart[constRE.DISCCART.Xcoord_2.name].get(),
                                                      disccart[constRE.DISCCART.Ycoord_2.name].get(),
                                                      disccart[constRE.DISCCART.Zelev_2.name].get(),
                                                      disccart[constRE.DISCCART.Zhill_2.name].get(),
                                                      disccart[constRE.DISCCART.Zflag_2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % disccartStr)

    if len(disccart[constRE.DISCCART.Xcoord_3.name].get()) > 0 and \
            len(disccart[constRE.DISCCART.Ycoord_3.name].get()) > 0:
        disccartStr = 'RE DISCCART %s %s %s %s %s' % (disccart[constRE.DISCCART.Xcoord_3.name].get(),
                                                      disccart[constRE.DISCCART.Ycoord_3.name].get(),
                                                      disccart[constRE.DISCCART.Zelev_3.name].get(),
                                                      disccart[constRE.DISCCART.Zhill_3.name].get(),
                                                      disccart[constRE.DISCCART.Zflag_3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % disccartStr)

# ======================================================================================================================
def writeDISCPOLR(discpolr):
    if len(discpolr[constRE.DISCPOLR.Srcid_1.name].get()) > 0 and \
            len(discpolr[constRE.DISCPOLR.Dist_1.name].get()) > 0 and \
            len(discpolr[constRE.DISCPOLR.Direct_1.name].get()):
        discpolrStr = 'RE DISPOLR %s %s %s %s %s %s' % (discpolr[constRE.DISCPOLR.Srcid_1.name].get(),
                                                        discpolr[constRE.DISCPOLR.Dist_1.name].get(),
                                                        discpolr[constRE.DISCPOLR.Direct_1.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zelev_1.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zhill_1.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zflag_1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % discpolrStr)

    if len(discpolr[constRE.DISCPOLR.Srcid_2.name].get()) > 0 and \
            len(discpolr[constRE.DISCPOLR.Dist_2.name].get()) > 0 and \
            len(discpolr[constRE.DISCPOLR.Direct_2.name].get()):
        discpolrStr = 'RE DISPOLR %s %s %s %s %s %s' % (discpolr[constRE.DISCPOLR.Srcid_2.name].get(),
                                                        discpolr[constRE.DISCPOLR.Dist_2.name].get(),
                                                        discpolr[constRE.DISCPOLR.Direct_2.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zelev_2.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zhill_2.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zflag_2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % discpolrStr)

    if len(discpolr[constRE.DISCPOLR.Srcid_3.name].get()) > 0 and \
            len(discpolr[constRE.DISCPOLR.Dist_3.name].get()) > 0 and \
            len(discpolr[constRE.DISCPOLR.Direct_3.name].get()):
        discpolrStr = 'RE DISPOLR %s %s %s %s %s %s' % (discpolr[constRE.DISCPOLR.Srcid_3.name].get(),
                                                        discpolr[constRE.DISCPOLR.Dist_3.name].get(),
                                                        discpolr[constRE.DISCPOLR.Direct_3.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zelev_3.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zhill_3.name].get(),
                                                        discpolr[constRE.DISCPOLR.Zflag_3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % discpolrStr)

# ======================================================================================================================
def writeEVALCART(evalcart):
    if len(evalcart[constRE.EVALCART.Xcoord_1.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Ycoord_1.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zelev_1.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zhill_1.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zflag_1.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Arcid_1.name].get()) > 0:
        evalcartStr = 'RE EVALCART %s %s %s %s %s %s %s' % (evalcart[constRE.EVALCART.Xcoord_1.name].get(),
                                                      evalcart[constRE.EVALCART.Ycoord_1.name].get(),
                                                      evalcart[constRE.EVALCART.Zelev_1.name].get(),
                                                      evalcart[constRE.EVALCART.Zhill_1.name].get(),
                                                      evalcart[constRE.EVALCART.Zflag_1.name].get(),
                                                      evalcart[constRE.EVALCART.Arcid_1.name].get(),
                                                      evalcart[constRE.EVALCART.Name_1.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % evalcartStr)

    if len(evalcart[constRE.EVALCART.Xcoord_2.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Ycoord_2.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zelev_2.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zhill_2.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zflag_2.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Arcid_2.name].get()) > 0:
        evalcartStr = 'RE EVALCART %s %s %s %s %s %s %s' % (evalcart[constRE.EVALCART.Xcoord_2.name].get(),
                                                      evalcart[constRE.EVALCART.Ycoord_2.name].get(),
                                                      evalcart[constRE.EVALCART.Zelev_2.name].get(),
                                                      evalcart[constRE.EVALCART.Zhill_2.name].get(),
                                                      evalcart[constRE.EVALCART.Zflag_2.name].get(),
                                                      evalcart[constRE.EVALCART.Arcid_2.name].get(),
                                                      evalcart[constRE.EVALCART.Name_2.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % evalcartStr)

    if len(evalcart[constRE.EVALCART.Xcoord_3.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Ycoord_3.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zelev_3.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zhill_3.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Zflag_3.name].get()) > 0 and \
            len(evalcart[constRE.EVALCART.Arcid_3.name].get()) > 0:
        evalcartStr = 'RE EVALCART %s %s %s %s %s %s %s' % (evalcart[constRE.EVALCART.Xcoord_3.name].get(),
                                                      evalcart[constRE.EVALCART.Ycoord_3.name].get(),
                                                      evalcart[constRE.EVALCART.Zelev_3.name].get(),
                                                      evalcart[constRE.EVALCART.Zhill_3.name].get(),
                                                      evalcart[constRE.EVALCART.Zflag_3.name].get(),
                                                      evalcart[constRE.EVALCART.Arcid_3.name].get(),
                                                      evalcart[constRE.EVALCART.Name_3.name].get())
        with open('control.inp', 'a') as f:
            f.write('%s\n' % evalcartStr)

def writeINCLUDED(included):
    if len(included[constRE.INCLUDED.RecIncFile.name].get())>0:
        with open('control.inp', 'a') as f:
            f.write('RE INCLUDED %s\n' % included[constRE.INCLUDED.RecIncFile.name].get())

# ======================================================================================================================
def writeControlFile(reInputs):
    with open('control.inp', 'a') as f:
        f.write('\nRE STARTING\n')

    elevunit = reInputs[0]
    writeELEVUNIT(elevunit)

    gridcart = reInputs[1]
    writeGRIDCART(gridcart)

    gridpolr = reInputs[2]
    writeGRIDPOLR(gridpolr)

    disccart = reInputs[3]
    writeDISCCART(disccart)

    discpolr = reInputs[4]
    writeDISCPOLR(discpolr)

    evalcart = reInputs[5]
    writeEVALCART(evalcart)

    included = reInputs[6]
    writeINCLUDED(included)

    with open('control.inp', 'a') as f:
        f.write('RE FINISHED\n')