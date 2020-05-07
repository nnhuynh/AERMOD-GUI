from tkinter import *
import reWriter
import constantsRE as constRE

# ======================================================================================================================
def makeELEVUNIT(frm):
    lbl = Label(frm, text=constRE.ELEVUNIT.ELEVUNIT.name)
    lbl.pack(side=LEFT, padx=3, pady=3)

    choices = [constRE.ELEVUNIT.METERS.name, constRE.ELEVUNIT.FEET.name]
    variable = StringVar()
    variable.set(choices[0])
    opt = OptionMenu(frm, variable, *choices)
    opt.config(width=7)
    opt.pack(side=LEFT, padx=3, pady=3)

    elevunitVals[constRE.ELEVUNIT.ELEVUNIT.name] = variable

# ======================================================================================================================
def makeGRIDCART(frm):
    # Netid_1 ==========================================================================================================
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.grid(row=0, column=0, padx=3, pady=3, sticky=W + E)

    radbtnVar_1 = IntVar()

    frm10 = Frame(frm1)
    frm10.grid(row=0, column=0, sticky=W + E)
    lblNetId_1 = Label(frm10, text=constRE.GRIDCART.NetId_1.name)
    lblNetId_1.pack(side=LEFT, padx=3, pady=3)
    entNetId_1 = Entry(frm10, width=15)
    entNetId_1.pack(side=LEFT, padx=3, pady=3)

    frm11 = Frame(frm1)
    frm11.grid(row=1, column=0, sticky=W + E)
    radbtnXYINC_1 = Radiobutton(frm11, text=constRE.GRIDCART.XYINC_1.name, var=radbtnVar_1, value=1)
    radbtnXYINC_1.pack(side=LEFT, padx=3, pady=3)
    entXYINC_1 = Entry(frm11, width=80)
    entXYINC_1.pack(side=RIGHT, padx=3, pady=3)

    frm12 = Frame(frm1)
    frm12.grid(row=2, column=0, sticky=W + E)
    radbtnXPNTS_1 = Radiobutton(frm12, text=constRE.GRIDCART.XPNTS_1.name, var=radbtnVar_1, value=2)
    radbtnXPNTS_1.pack(side=LEFT, padx=3, pady=3)
    entXPNTS_1 = Entry(frm12, width=80)
    entXPNTS_1.pack(side=RIGHT, padx=3, pady=3)

    frm13 = Frame(frm1)
    frm13.grid(row=3, column=0, sticky=W + E)
    lblYPNTS_1 = Label(frm13, text=constRE.GRIDCART.YPNTS_1.name)
    lblYPNTS_1.pack(side=LEFT, padx=3, pady=3)
    entYPNTS_1 = Entry(frm13, width=80)
    entYPNTS_1.pack(side=RIGHT, padx=3, pady=3)

    frm14 = Frame(frm1)
    frm14.grid(row=4, column=0, sticky=W + E)
    chkELEV_1 = BooleanVar()
    chkELEV_1.set(False)
    chkbtnELEV_1 = Checkbutton(frm14, text=constRE.GRIDCART.ELEV_1.name, var=chkELEV_1)
    chkbtnELEV_1.pack(side=LEFT, padx=3, pady=3)
    entELEV_1 = Entry(frm14, width=80)
    entELEV_1.pack(side=RIGHT, padx=3, pady=3)

    frm15 = Frame(frm1)
    frm15.grid(row=5, column=0, sticky=W + E)
    chkHILL_1 = BooleanVar()
    chkHILL_1.set(False)
    chkbtnHILL_1 = Checkbutton(frm15, text=constRE.GRIDCART.HILL_1.name, var=chkHILL_1)
    chkbtnHILL_1.pack(side=LEFT, padx=3, pady=3)
    entHILL_1 = Entry(frm15, width=80)
    entHILL_1.pack(side=RIGHT, padx=3, pady=3)

    frm16 = Frame(frm1)
    frm16.grid(row=6, column=0, sticky=W + E)
    chkFLAG_1 = BooleanVar()
    chkFLAG_1.set(False)
    chkbtnFLAG_1 = Checkbutton(frm16, text=constRE.GRIDCART.FLAG_1.name, var=chkFLAG_1)
    chkbtnFLAG_1.pack(side=LEFT, padx=3, pady=3)
    entFLAG_1 = Entry(frm16, width=80)
    entFLAG_1.pack(side=RIGHT, padx=3, pady=3)

    gridcartVals['radbtnVar_1'] = radbtnVar_1
    gridcartVals[constRE.GRIDCART.NetId_1.name] = entNetId_1
    gridcartVals[constRE.GRIDCART.XYINC_1.name] = entXYINC_1
    gridcartVals[constRE.GRIDCART.XPNTS_1.name] = entXPNTS_1
    gridcartVals[constRE.GRIDCART.YPNTS_1.name] = entYPNTS_1
    gridcartVals['chkELEV_1'] = chkELEV_1
    gridcartVals[constRE.GRIDCART.ELEV_1.name] = entELEV_1
    gridcartVals['chkHILL_1'] = chkHILL_1
    gridcartVals[constRE.GRIDCART.HILL_1.name] = entHILL_1
    gridcartVals['chkFLAG_1'] = chkFLAG_1
    gridcartVals[constRE.GRIDCART.FLAG_1.name] = entFLAG_1

    # Netid_2 ==========================================================================================================
    frm2 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm2.grid(row=0, column=1, padx=3, pady=3, sticky=W + E)

    radbtnVar_2 = IntVar()

    frm20 = Frame(frm2)
    frm20.grid(row=0, column=0, sticky=W + E)
    lblNetId_2 = Label(frm20, text=constRE.GRIDCART.NetId_2.name)
    lblNetId_2.pack(side=LEFT, padx=3, pady=3)
    entNetId_2 = Entry(frm20, width=15)
    entNetId_2.pack(side=LEFT, padx=3, pady=3)

    frm21 = Frame(frm2)
    frm21.grid(row=1, column=0, sticky=W + E)
    radbtnXYINC_2 = Radiobutton(frm21, text=constRE.GRIDCART.XYINC_2.name, var=radbtnVar_2, value=1)
    radbtnXYINC_2.pack(side=LEFT, padx=3, pady=3)
    entXYINC_2 = Entry(frm21, width=80)
    entXYINC_2.pack(side=RIGHT, padx=3, pady=3)

    frm22 = Frame(frm2)
    frm22.grid(row=2, column=0, sticky=W + E)
    radbtnXPNTS_2 = Radiobutton(frm22, text=constRE.GRIDCART.XPNTS_2.name, var=radbtnVar_2, value=2)
    radbtnXPNTS_2.pack(side=LEFT, padx=3, pady=3)
    entXPNTS_2 = Entry(frm22, width=80)
    entXPNTS_2.pack(side=RIGHT, padx=3, pady=3)

    frm23 = Frame(frm2)
    frm23.grid(row=3, column=0, sticky=W + E)
    lblYPNTS_2 = Label(frm23, text=constRE.GRIDCART.YPNTS_2.name)
    lblYPNTS_2.pack(side=LEFT, padx=3, pady=3)
    entYPNTS_2 = Entry(frm23, width=80)
    entYPNTS_2.pack(side=RIGHT, padx=3, pady=3)

    frm24 = Frame(frm2)
    frm24.grid(row=4, column=0, sticky=W + E)
    chkELEV_2 = BooleanVar()
    chkELEV_2.set(False)
    chkbtnELEV_2 = Checkbutton(frm24, text=constRE.GRIDCART.ELEV_2.name, var=chkELEV_2)
    chkbtnELEV_2.pack(side=LEFT, padx=3, pady=3)
    entELEV_2 = Entry(frm24, width=80)
    entELEV_2.pack(side=RIGHT, padx=3, pady=3)

    frm25 = Frame(frm2)
    frm25.grid(row=5, column=0, sticky=W + E)
    chkHILL_2 = BooleanVar()
    chkHILL_2.set(False)
    chkbtnHILL_2 = Checkbutton(frm25, text=constRE.GRIDCART.HILL_2.name, var=chkHILL_2)
    chkbtnHILL_2.pack(side=LEFT, padx=3, pady=3)
    entHILL_2 = Entry(frm25, width=80)
    entHILL_2.pack(side=RIGHT, padx=3, pady=3)

    frm26 = Frame(frm2)
    frm26.grid(row=6, column=0, sticky=W + E)
    chkFLAG_2 = BooleanVar()
    chkFLAG_2.set(False)
    chkbtnFLAG_2 = Checkbutton(frm26, text=constRE.GRIDCART.FLAG_2.name, var=chkFLAG_2)
    chkbtnFLAG_2.pack(side=LEFT, padx=3, pady=3)
    entFLAG_2 = Entry(frm26, width=80)
    entFLAG_2.pack(side=RIGHT, padx=3, pady=3)

    gridcartVals['radbtnVar_2'] = radbtnVar_2
    gridcartVals[constRE.GRIDCART.NetId_2.name] = entNetId_2
    gridcartVals[constRE.GRIDCART.XYINC_2.name] = entXYINC_2
    gridcartVals[constRE.GRIDCART.XPNTS_2.name] = entXPNTS_2
    gridcartVals[constRE.GRIDCART.YPNTS_2.name] = entYPNTS_2
    gridcartVals['chkELEV_2'] = chkELEV_2
    gridcartVals[constRE.GRIDCART.ELEV_2.name] = entELEV_2
    gridcartVals['chkHILL_2'] = chkHILL_2
    gridcartVals[constRE.GRIDCART.HILL_2.name] = entHILL_2
    gridcartVals['chkFLAG_2'] = chkFLAG_2
    gridcartVals[constRE.GRIDCART.FLAG_2.name] = entFLAG_2

    # Netid_3 ==========================================================================================================
    frm3 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm3.grid(row=0, column=2, padx=3, pady=3, sticky=W + E)

    radbtnVar_3 = IntVar()

    frm30 = Frame(frm3)
    frm30.grid(row=0, column=0, sticky=W + E)
    lblNetId_3 = Label(frm30, text=constRE.GRIDCART.NetId_3.name)
    lblNetId_3.pack(side=LEFT, padx=3, pady=3)
    entNetId_3 = Entry(frm30, width=15)
    entNetId_3.pack(side=LEFT, padx=3, pady=3)

    frm31 = Frame(frm3)
    frm31.grid(row=1, column=0, sticky=W + E)
    radbtnXYINC_3 = Radiobutton(frm31, text=constRE.GRIDCART.XYINC_3.name, var=radbtnVar_3, value=1)
    radbtnXYINC_3.pack(side=LEFT, padx=3, pady=3)
    entXYINC_3 = Entry(frm31, width=80)
    entXYINC_3.pack(side=RIGHT, padx=3, pady=3)

    frm32 = Frame(frm3)
    frm32.grid(row=2, column=0, sticky=W + E)
    radbtnXPNTS_3 = Radiobutton(frm32, text=constRE.GRIDCART.XPNTS_3.name, var=radbtnVar_3, value=2)
    radbtnXPNTS_3.pack(side=LEFT, padx=3, pady=3)
    entXPNTS_3 = Entry(frm32, width=80)
    entXPNTS_3.pack(side=RIGHT, padx=3, pady=3)

    frm33 = Frame(frm3)
    frm33.grid(row=3, column=0, sticky=W + E)
    lblYPNTS_3 = Label(frm33, text=constRE.GRIDCART.YPNTS_3.name)
    lblYPNTS_3.pack(side=LEFT, padx=3, pady=3)
    entYPNTS_3 = Entry(frm33, width=80)
    entYPNTS_3.pack(side=RIGHT, padx=3, pady=3)

    frm34 = Frame(frm3)
    frm34.grid(row=4, column=0, sticky=W + E)
    chkELEV_3 = BooleanVar()
    chkELEV_3.set(False)
    chkbtnELEV_3 = Checkbutton(frm34, text=constRE.GRIDCART.ELEV_3.name, var=chkELEV_3)
    chkbtnELEV_3.pack(side=LEFT, padx=3, pady=3)
    entELEV_3 = Entry(frm34, width=80)
    entELEV_3.pack(side=RIGHT, padx=3, pady=3)

    frm35 = Frame(frm3)
    frm35.grid(row=5, column=0, sticky=W + E)
    chkHILL_3 = BooleanVar()
    chkHILL_3.set(False)
    chkbtnHILL_3 = Checkbutton(frm35, text=constRE.GRIDCART.HILL_3.name, var=chkHILL_3)
    chkbtnHILL_3.pack(side=LEFT, padx=3, pady=3)
    entHILL_3 = Entry(frm35, width=80)
    entHILL_3.pack(side=RIGHT, padx=3, pady=3)

    frm36 = Frame(frm3)
    frm36.grid(row=6, column=0, sticky=W + E)
    chkFLAG_3 = BooleanVar()
    chkFLAG_3.set(False)
    chkbtnFLAG_3 = Checkbutton(frm36, text=constRE.GRIDCART.FLAG_3.name, var=chkFLAG_3)
    chkbtnFLAG_3.pack(side=LEFT, padx=3, pady=3)
    entFLAG_3 = Entry(frm36, width=80)
    entFLAG_3.pack(side=RIGHT, padx=3, pady=3)

    gridcartVals['radbtnVar_3'] = radbtnVar_3
    gridcartVals[constRE.GRIDCART.NetId_3.name] = entNetId_3
    gridcartVals[constRE.GRIDCART.XYINC_3.name] = entXYINC_3
    gridcartVals[constRE.GRIDCART.XPNTS_3.name] = entXPNTS_3
    gridcartVals[constRE.GRIDCART.YPNTS_3.name] = entYPNTS_3
    gridcartVals['chkELEV_3'] = chkELEV_3
    gridcartVals[constRE.GRIDCART.ELEV_3.name] = entELEV_3
    gridcartVals['chkHILL_3'] = chkHILL_3
    gridcartVals[constRE.GRIDCART.HILL_3.name] = entHILL_3
    gridcartVals['chkFLAG_3'] = chkFLAG_3
    gridcartVals[constRE.GRIDCART.FLAG_3.name] = entFLAG_3

# ======================================================================================================================
def makeGRIDPOLR(frm):
    # NetID_1 ==========================================================================================================
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.grid(row=0, column=0, padx=3, pady=3, sticky=W+E)

    frm10 = Frame(frm1)
    frm10.grid(row=0, column=0, sticky=W+E)
    lblNetId_1 = Label(frm10, text=constRE.GRIDPOLR.NetId_1.name)
    lblNetId_1.pack(side=LEFT, padx=3, pady=3)
    entNetId_1 = Entry(frm10, width=15)
    entNetId_1.pack(side=LEFT, padx=3, pady=3)

    frm11 = Frame(frm1)
    frm11.grid(row=1, column=0, sticky=W + E)
    chkORIG_1 = BooleanVar()
    chkORIG_1.set(False)
    chkbtnORIG_1 = Checkbutton(frm11, text=constRE.GRIDPOLR.ORIG_1.name, var=chkORIG_1)
    chkbtnORIG_1.pack(side=LEFT, padx=3, pady=3)
    entORIG_1 = Entry(frm11, width=80)
    entORIG_1.pack(side=RIGHT, padx=3, pady=3)

    frm12 = Frame(frm1)
    frm12.grid(row=2, column=0, sticky=W + E)
    chkDIST_1 = BooleanVar()
    chkDIST_1.set(False)
    chkbtnDIST_1 = Checkbutton(frm12, text=constRE.GRIDPOLR.DIST_1.name, var=chkDIST_1)
    chkbtnDIST_1.pack(side=LEFT, padx=3, pady=3)
    entDIST_1 = Entry(frm12, width=80)
    entDIST_1.pack(side=RIGHT, padx=3, pady=3)

    radbtnVar_1 = IntVar()

    frm13 = Frame(frm1)
    frm13.grid(row=3, column=0, sticky=W + E)
    radbtnDDIR_1 = Radiobutton(frm13, text=constRE.GRIDPOLR.DDIR_1.name, var=radbtnVar_1, value=1)
    radbtnDDIR_1.pack(side=LEFT, padx=3, pady=3)
    entDDIR_1 = Entry(frm13, width=80)
    entDDIR_1.pack(side=RIGHT, padx=3, pady=3)

    frm14 = Frame(frm1)
    frm14.grid(row=4, column=0, sticky=W + E)
    radbtnGDIR_1 = Radiobutton(frm14, text=constRE.GRIDPOLR.GDIR_1.name, var=radbtnVar_1, value=2)
    radbtnGDIR_1.pack(side=LEFT, padx=3, pady=3)
    entGDIR_1 = Entry(frm14, width=80)
    entGDIR_1.pack(side=RIGHT, padx=3, pady=3)

    frm15 = Frame(frm1)
    frm15.grid(row=5, column=0, sticky=W + E)
    chkELEV_1 = BooleanVar()
    chkELEV_1.set(False)
    chkbtnELEV_1 = Checkbutton(frm15, text=constRE.GRIDPOLR.ELEV_1.name, var=chkELEV_1)
    chkbtnELEV_1.pack(side=LEFT, padx=3, pady=3)
    entELEV_1 = Entry(frm15, width=80)
    entELEV_1.pack(side=RIGHT, padx=3, pady=3)

    frm16 = Frame(frm1)
    frm16.grid(row=6, column=0, sticky=W + E)
    chkHILL_1 = BooleanVar()
    chkHILL_1.set(False)
    chkbtnHILL_1 = Checkbutton(frm16, text=constRE.GRIDPOLR.HILL_1.name, var=chkHILL_1)
    chkbtnHILL_1.pack(side=LEFT, padx=3, pady=3)
    entHILL_1 = Entry(frm16, width=80)
    entHILL_1.pack(side=RIGHT, padx=3, pady=3)

    frm17 = Frame(frm1)
    frm17.grid(row=7, column=0, sticky=W + E)
    chkFLAG_1 = BooleanVar()
    chkFLAG_1.set(False)
    chkbtnFLAG_1 = Checkbutton(frm17, text=constRE.GRIDPOLR.FLAG_1.name, var=chkFLAG_1)
    chkbtnFLAG_1.pack(side=LEFT, padx=3, pady=3)
    entFLAG_1 = Entry(frm17, width=80)
    entFLAG_1.pack(side=RIGHT, padx=3, pady=3)

    gridpolrVals[constRE.GRIDPOLR.NetId_1.name] = entNetId_1
    gridpolrVals['chkORIG_1'] = chkORIG_1
    gridpolrVals[constRE.GRIDPOLR.ORIG_1.name] = entORIG_1
    gridpolrVals['chkDIST_1'] = chkDIST_1
    gridpolrVals[constRE.GRIDPOLR.DIST_1.name] = entDIST_1
    gridpolrVals['radbtnVar_1'] = radbtnVar_1
    gridpolrVals[constRE.GRIDPOLR.DDIR_1.name] = entDDIR_1
    gridpolrVals[constRE.GRIDPOLR.GDIR_1.name] = entGDIR_1
    gridpolrVals['chkELEV_1'] = chkELEV_1
    gridpolrVals[constRE.GRIDPOLR.ELEV_1.name] = entELEV_1
    gridpolrVals['chkHILL_1'] = chkHILL_1
    gridpolrVals[constRE.GRIDPOLR.HILL_1.name] = entHILL_1
    gridpolrVals['chkFLAG_1'] = chkFLAG_1
    gridpolrVals[constRE.GRIDPOLR.FLAG_1.name] = entFLAG_1

    # NetID_2 ==========================================================================================================
    frm2 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm2.grid(row=0, column=1, padx=3, pady=3, sticky=W + E)

    frm20 = Frame(frm2)
    frm20.grid(row=0, column=0, sticky=W + E)
    lblNetId_2 = Label(frm20, text=constRE.GRIDPOLR.NetId_2.name)
    lblNetId_2.pack(side=LEFT, padx=3, pady=3)
    entNetId_2 = Entry(frm20, width=15)
    entNetId_2.pack(side=LEFT, padx=3, pady=3)

    frm21 = Frame(frm2)
    frm21.grid(row=1, column=0, sticky=W + E)
    chkORIG_2 = BooleanVar()
    chkORIG_2.set(False)
    chkbtnORIG_2 = Checkbutton(frm21, text=constRE.GRIDPOLR.ORIG_2.name, var=chkORIG_2)
    chkbtnORIG_2.pack(side=LEFT, padx=3, pady=3)
    entORIG_2 = Entry(frm21, width=80)
    entORIG_2.pack(side=RIGHT, padx=3, pady=3)

    frm22 = Frame(frm2)
    frm22.grid(row=2, column=0, sticky=W + E)
    chkDIST_2 = BooleanVar()
    chkDIST_2.set(False)
    chkbtnDIST_2 = Checkbutton(frm22, text=constRE.GRIDPOLR.DIST_2.name, var=chkDIST_2)
    chkbtnDIST_2.pack(side=LEFT, padx=3, pady=3)
    entDIST_2 = Entry(frm22, width=80)
    entDIST_2.pack(side=RIGHT, padx=3, pady=3)

    radbtnVar_2 = IntVar()

    frm23 = Frame(frm2)
    frm23.grid(row=3, column=0, sticky=W + E)
    radbtnDDIR_2 = Radiobutton(frm23, text=constRE.GRIDPOLR.DDIR_2.name, var=radbtnVar_2, value=1)
    radbtnDDIR_2.pack(side=LEFT, padx=3, pady=3)
    entDDIR_2 = Entry(frm23, width=80)
    entDDIR_2.pack(side=RIGHT, padx=3, pady=3)

    frm24 = Frame(frm2)
    frm24.grid(row=4, column=0, sticky=W + E)
    radbtnGDIR_2 = Radiobutton(frm24, text=constRE.GRIDPOLR.GDIR_2.name, var=radbtnVar_2, value=2)
    radbtnGDIR_2.pack(side=LEFT, padx=3, pady=3)
    entGDIR_2 = Entry(frm24, width=80)
    entGDIR_2.pack(side=RIGHT, padx=3, pady=3)

    frm25 = Frame(frm2)
    frm25.grid(row=5, column=0, sticky=W + E)
    chkELEV_2 = BooleanVar()
    chkELEV_2.set(False)
    chkbtnELEV_2 = Checkbutton(frm25, text=constRE.GRIDPOLR.ELEV_2.name, var=chkELEV_2)
    chkbtnELEV_2.pack(side=LEFT, padx=3, pady=3)
    entELEV_2 = Entry(frm25, width=80)
    entELEV_2.pack(side=RIGHT, padx=3, pady=3)

    frm26 = Frame(frm2)
    frm26.grid(row=6, column=0, sticky=W + E)
    chkHILL_2 = BooleanVar()
    chkHILL_2.set(False)
    chkbtnHILL_2 = Checkbutton(frm26, text=constRE.GRIDPOLR.HILL_2.name, var=chkHILL_2)
    chkbtnHILL_2.pack(side=LEFT, padx=3, pady=3)
    entHILL_2 = Entry(frm26, width=80)
    entHILL_2.pack(side=RIGHT, padx=3, pady=3)

    frm27 = Frame(frm2)
    frm27.grid(row=7, column=0, sticky=W + E)
    chkFLAG_2 = BooleanVar()
    chkFLAG_2.set(False)
    chkbtnFLAG_2 = Checkbutton(frm27, text=constRE.GRIDPOLR.FLAG_2.name, var=chkFLAG_2)
    chkbtnFLAG_2.pack(side=LEFT, padx=3, pady=3)
    entFLAG_2 = Entry(frm27, width=80)
    entFLAG_2.pack(side=RIGHT, padx=3, pady=3)

    gridpolrVals[constRE.GRIDPOLR.NetId_2.name] = entNetId_2
    gridpolrVals['chkORIG_2'] = chkORIG_2
    gridpolrVals[constRE.GRIDPOLR.ORIG_2.name] = entORIG_2
    gridpolrVals['chkDIST_2'] = chkDIST_2
    gridpolrVals[constRE.GRIDPOLR.DIST_2.name] = entDIST_2
    gridpolrVals['radbtnVar_2'] = radbtnVar_2
    gridpolrVals[constRE.GRIDPOLR.DDIR_2.name] = entDDIR_2
    gridpolrVals[constRE.GRIDPOLR.GDIR_2.name] = entGDIR_2
    gridpolrVals['chkELEV_2'] = chkELEV_2
    gridpolrVals[constRE.GRIDPOLR.ELEV_2.name] = entELEV_2
    gridpolrVals['chkHILL_2'] = chkHILL_2
    gridpolrVals[constRE.GRIDPOLR.HILL_2.name] = entHILL_2
    gridpolrVals['chkFLAG_2'] = chkFLAG_2
    gridpolrVals[constRE.GRIDPOLR.FLAG_2.name] = entFLAG_2

	# NetID_3 ==========================================================================================================
    frm3 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm3.grid(row=0, column=2, padx=3, pady=3, sticky=W + E)

    frm30 = Frame(frm3)
    frm30.grid(row=0, column=0, sticky=W + E)
    lblNetId_3 = Label(frm30, text=constRE.GRIDPOLR.NetId_3.name)
    lblNetId_3.pack(side=LEFT, padx=3, pady=3)
    entNetId_3 = Entry(frm30, width=15)
    entNetId_3.pack(side=LEFT, padx=3, pady=3)

    frm31 = Frame(frm3)
    frm31.grid(row=1, column=0, sticky=W + E)
    chkORIG_3 = BooleanVar()
    chkORIG_3.set(False)
    chkbtnORIG_3 = Checkbutton(frm31, text=constRE.GRIDPOLR.ORIG_3.name, var=chkORIG_3)
    chkbtnORIG_3.pack(side=LEFT, padx=3, pady=3)
    entORIG_3 = Entry(frm31, width=80)
    entORIG_3.pack(side=RIGHT, padx=3, pady=3)

    frm32 = Frame(frm3)
    frm32.grid(row=2, column=0, sticky=W + E)
    chkDIST_3 = BooleanVar()
    chkDIST_3.set(False)
    chkbtnDIST_3 = Checkbutton(frm32, text=constRE.GRIDPOLR.DIST_3.name, var=chkDIST_3)
    chkbtnDIST_3.pack(side=LEFT, padx=3, pady=3)
    entDIST_3 = Entry(frm32, width=80)
    entDIST_3.pack(side=RIGHT, padx=3, pady=3)

    radbtnVar_3 = IntVar()

    frm33 = Frame(frm3)
    frm33.grid(row=3, column=0, sticky=W + E)
    radbtnDDIR_3 = Radiobutton(frm33, text=constRE.GRIDPOLR.DDIR_3.name, var=radbtnVar_3, value=1)
    radbtnDDIR_3.pack(side=LEFT, padx=3, pady=3)
    entDDIR_3 = Entry(frm33, width=80)
    entDDIR_3.pack(side=RIGHT, padx=3, pady=3)

    frm34 = Frame(frm3)
    frm34.grid(row=4, column=0, sticky=W + E)
    radbtnGDIR_3 = Radiobutton(frm34, text=constRE.GRIDPOLR.GDIR_3.name, var=radbtnVar_3, value=2)
    radbtnGDIR_3.pack(side=LEFT, padx=3, pady=3)
    entGDIR_3 = Entry(frm34, width=80)
    entGDIR_3.pack(side=RIGHT, padx=3, pady=3)

    frm35 = Frame(frm3)
    frm35.grid(row=5, column=0, sticky=W + E)
    chkELEV_3 = BooleanVar()
    chkELEV_3.set(False)
    chkbtnELEV_3 = Checkbutton(frm35, text=constRE.GRIDPOLR.ELEV_3.name, var=chkELEV_3)
    chkbtnELEV_3.pack(side=LEFT, padx=3, pady=3)
    entELEV_3 = Entry(frm35, width=80)
    entELEV_3.pack(side=RIGHT, padx=3, pady=3)

    frm36 = Frame(frm3)
    frm36.grid(row=6, column=0, sticky=W + E)
    chkHILL_3 = BooleanVar()
    chkHILL_3.set(False)
    chkbtnHILL_3 = Checkbutton(frm36, text=constRE.GRIDPOLR.HILL_3.name, var=chkHILL_3)
    chkbtnHILL_3.pack(side=LEFT, padx=3, pady=3)
    entHILL_3 = Entry(frm36, width=80)
    entHILL_3.pack(side=RIGHT, padx=3, pady=3)

    frm37 = Frame(frm3)
    frm37.grid(row=7, column=0, sticky=W + E)
    chkFLAG_3 = BooleanVar()
    chkFLAG_3.set(False)
    chkbtnFLAG_3 = Checkbutton(frm37, text=constRE.GRIDPOLR.FLAG_3.name, var=chkFLAG_3)
    chkbtnFLAG_3.pack(side=LEFT, padx=3, pady=3)
    entFLAG_3 = Entry(frm37, width=80)
    entFLAG_3.pack(side=RIGHT, padx=3, pady=3)

    gridpolrVals[constRE.GRIDPOLR.NetId_3.name] = entNetId_3
    gridpolrVals['chkORIG_3'] = chkORIG_3
    gridpolrVals[constRE.GRIDPOLR.ORIG_3.name] = entORIG_3
    gridpolrVals['chkDIST_3'] = chkDIST_3
    gridpolrVals[constRE.GRIDPOLR.DIST_3.name] = entDIST_3
    gridpolrVals['radbtnVar_3'] = radbtnVar_3
    gridpolrVals[constRE.GRIDPOLR.DDIR_3.name] = entDDIR_3
    gridpolrVals[constRE.GRIDPOLR.GDIR_3.name] = entGDIR_3
    gridpolrVals['chkELEV_3'] = chkELEV_3
    gridpolrVals[constRE.GRIDPOLR.ELEV_3.name] = entELEV_3
    gridpolrVals['chkHILL_3'] = chkHILL_3
    gridpolrVals[constRE.GRIDPOLR.HILL_3.name] = entHILL_3
    gridpolrVals['chkFLAG_3'] = chkFLAG_3
    gridpolrVals[constRE.GRIDPOLR.FLAG_3.name] = entFLAG_3

# ======================================================================================================================
def makeDISCCART(frm):
    # _1 ===============================================================================================================
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.grid(row=0, column=0, padx=3, pady=3, sticky=W + E)

    lblX_1 = Label(frm1, text=constRE.DISCCART.Xcoord_1.name)
    lblX_1.pack(side=LEFT, padx=3, pady=3)
    entX_1 = Entry(frm1, width=20)
    entX_1.pack(side=LEFT, padx=3, pady=3)

    lblY_1 = Label(frm1, text=constRE.DISCCART.Ycoord_1.name)
    lblY_1.pack(side=LEFT, padx=3, pady=3)
    entY_1 = Entry(frm1, width=20)
    entY_1.pack(side=LEFT, padx=3, pady=3)

    lblZelev_1 = Label(frm1, text=constRE.DISCCART.Zelev_1.name)
    lblZelev_1.pack(side=LEFT, padx=3, pady=3)
    entZelev_1 = Entry(frm1, width=20)
    entZelev_1.pack(side=LEFT, padx=3, pady=3)

    lblZhill_1 = Label(frm1, text=constRE.DISCCART.Zhill_1.name)
    lblZhill_1.pack(side=LEFT, padx=3, pady=3)
    entZhill_1 = Entry(frm1, width=20)
    entZhill_1.pack(side=LEFT, padx=3, pady=3)

    lblZflag_1 = Label(frm1, text=constRE.DISCCART.Zflag_1.name)
    lblZflag_1.pack(side=LEFT, padx=3, pady=3)
    entZflag_1 = Entry(frm1, width=20)
    entZflag_1.pack(side=LEFT, padx=3, pady=3)

    disccartVals[constRE.DISCCART.Xcoord_1.name] = entX_1
    disccartVals[constRE.DISCCART.Ycoord_1.name] = entY_1
    disccartVals[constRE.DISCCART.Zelev_1.name] = entZelev_1
    disccartVals[constRE.DISCCART.Zhill_1.name] = entZhill_1
    disccartVals[constRE.DISCCART.Zflag_1.name] = entZflag_1

    # _2 ===============================================================================================================
    frm2 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm2.grid(row=1, column=0, padx=3, pady=3, sticky=W + E)

    lblX_2 = Label(frm2, text=constRE.DISCCART.Xcoord_2.name)
    lblX_2.pack(side=LEFT, padx=3, pady=3)
    entX_2 = Entry(frm2, width=20)
    entX_2.pack(side=LEFT, padx=3, pady=3)

    lblY_2 = Label(frm2, text=constRE.DISCCART.Ycoord_2.name)
    lblY_2.pack(side=LEFT, padx=3, pady=3)
    entY_2 = Entry(frm2, width=20)
    entY_2.pack(side=LEFT, padx=3, pady=3)

    lblZelev_2 = Label(frm2, text=constRE.DISCCART.Zelev_2.name)
    lblZelev_2.pack(side=LEFT, padx=3, pady=3)
    entZelev_2 = Entry(frm2, width=20)
    entZelev_2.pack(side=LEFT, padx=3, pady=3)

    lblZhill_2 = Label(frm2, text=constRE.DISCCART.Zhill_2.name)
    lblZhill_2.pack(side=LEFT, padx=3, pady=3)
    entZhill_2 = Entry(frm2, width=20)
    entZhill_2.pack(side=LEFT, padx=3, pady=3)

    lblZflag_2 = Label(frm2, text=constRE.DISCCART.Zflag_2.name)
    lblZflag_2.pack(side=LEFT, padx=3, pady=3)
    entZflag_2 = Entry(frm2, width=20)
    entZflag_2.pack(side=LEFT, padx=3, pady=3)

    disccartVals[constRE.DISCCART.Xcoord_2.name] = entX_2
    disccartVals[constRE.DISCCART.Ycoord_2.name] = entY_2
    disccartVals[constRE.DISCCART.Zelev_2.name] = entZelev_2
    disccartVals[constRE.DISCCART.Zhill_2.name] = entZhill_2
    disccartVals[constRE.DISCCART.Zflag_2.name] = entZflag_2

    # _3 ===============================================================================================================
    frm3 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm3.grid(row=2, column=0, padx=3, pady=3, sticky=W + E)

    lblX_3 = Label(frm3, text=constRE.DISCCART.Xcoord_3.name)
    lblX_3.pack(side=LEFT, padx=3, pady=3)
    entX_3 = Entry(frm3, width=20)
    entX_3.pack(side=LEFT, padx=3, pady=3)

    lblY_3 = Label(frm3, text=constRE.DISCCART.Ycoord_3.name)
    lblY_3.pack(side=LEFT, padx=3, pady=3)
    entY_3 = Entry(frm3, width=20)
    entY_3.pack(side=LEFT, padx=3, pady=3)

    lblZelev_3 = Label(frm3, text=constRE.DISCCART.Zelev_3.name)
    lblZelev_3.pack(side=LEFT, padx=3, pady=3)
    entZelev_3 = Entry(frm3, width=20)
    entZelev_3.pack(side=LEFT, padx=3, pady=3)

    lblZhill_3 = Label(frm3, text=constRE.DISCCART.Zhill_3.name)
    lblZhill_3.pack(side=LEFT, padx=3, pady=3)
    entZhill_3 = Entry(frm3, width=20)
    entZhill_3.pack(side=LEFT, padx=3, pady=3)

    lblZflag_3 = Label(frm3, text=constRE.DISCCART.Zflag_3.name)
    lblZflag_3.pack(side=LEFT, padx=3, pady=3)
    entZflag_3 = Entry(frm3, width=20)
    entZflag_3.pack(side=LEFT, padx=3, pady=3)

    disccartVals[constRE.DISCCART.Xcoord_3.name] = entX_3
    disccartVals[constRE.DISCCART.Ycoord_3.name] = entY_3
    disccartVals[constRE.DISCCART.Zelev_3.name] = entZelev_3
    disccartVals[constRE.DISCCART.Zhill_3.name] = entZhill_3
    disccartVals[constRE.DISCCART.Zflag_3.name] = entZflag_3

# ======================================================================================================================
def makeDISCPOLR(frm):
    # _1 ===============================================================================================================
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.grid(row=0, column=0, padx=3, pady=3, sticky=W + E)

    lblSrcid_1 = Label(frm1, text=constRE.DISCPOLR.Srcid_1.name)
    lblSrcid_1.pack(side=LEFT, padx=3, pady=3)
    entSrcid_1 = Entry(frm1, width=20)
    entSrcid_1.pack(side=LEFT, padx=3, pady=3)

    lblDist_1 = Label(frm1, text=constRE.DISCPOLR.Dist_1.name)
    lblDist_1.pack(side=LEFT, padx=3, pady=3)
    entDist_1 = Entry(frm1, width=20)
    entDist_1.pack(side=LEFT, padx=3, pady=3)

    lblDirect_1 = Label(frm1, text=constRE.DISCPOLR.Direct_1.name)
    lblDirect_1.pack(side=LEFT, padx=3, pady=3)
    entDirect_1 = Entry(frm1, width=20)
    entDirect_1.pack(side=LEFT, padx=3, pady=3)

    lblZelev_1 = Label(frm1, text=constRE.DISCPOLR.Zelev_1.name)
    lblZelev_1.pack(side=LEFT, padx=3, pady=3)
    entZelev_1 = Entry(frm1, width=20)
    entZelev_1.pack(side=LEFT, padx=3, pady=3)

    lblZhill_1 = Label(frm1, text=constRE.DISCPOLR.Zhill_1.name)
    lblZhill_1.pack(side=LEFT, padx=3, pady=3)
    entZhill_1 = Entry(frm1, width=20)
    entZhill_1.pack(side=LEFT, padx=3, pady=3)

    lblZflag_1 = Label(frm1, text=constRE.DISCPOLR.Zflag_1.name)
    lblZflag_1.pack(side=LEFT, padx=3, pady=3)
    entZflag_1 = Entry(frm1, width=20)
    entZflag_1.pack(side=LEFT, padx=3, pady=3)

    discpolrVals[constRE.DISCPOLR.Srcid_1.name] = entSrcid_1
    discpolrVals[constRE.DISCPOLR.Dist_1.name] = entDist_1
    discpolrVals[constRE.DISCPOLR.Direct_1.name] = entDirect_1
    discpolrVals[constRE.DISCPOLR.Zelev_1.name] = entZelev_1
    discpolrVals[constRE.DISCPOLR.Zhill_1.name] = entZhill_1
    discpolrVals[constRE.DISCPOLR.Zflag_1.name] = entZflag_1

    # _2 ===============================================================================================================
    frm2 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm2.grid(row=1, column=0, padx=3, pady=3, sticky=W + E)

    lblSrcid_2 = Label(frm2, text=constRE.DISCPOLR.Srcid_2.name)
    lblSrcid_2.pack(side=LEFT, padx=3, pady=3)
    entSrcid_2 = Entry(frm2, width=20)
    entSrcid_2.pack(side=LEFT, padx=3, pady=3)

    lblDist_2 = Label(frm2, text=constRE.DISCPOLR.Dist_2.name)
    lblDist_2.pack(side=LEFT, padx=3, pady=3)
    entDist_2 = Entry(frm2, width=20)
    entDist_2.pack(side=LEFT, padx=3, pady=3)

    lblDirect_2 = Label(frm2, text=constRE.DISCPOLR.Direct_2.name)
    lblDirect_2.pack(side=LEFT, padx=3, pady=3)
    entDirect_2 = Entry(frm2, width=20)
    entDirect_2.pack(side=LEFT, padx=3, pady=3)

    lblZelev_2 = Label(frm2, text=constRE.DISCPOLR.Zelev_2.name)
    lblZelev_2.pack(side=LEFT, padx=3, pady=3)
    entZelev_2 = Entry(frm2, width=20)
    entZelev_2.pack(side=LEFT, padx=3, pady=3)

    lblZhill_2 = Label(frm2, text=constRE.DISCPOLR.Zhill_2.name)
    lblZhill_2.pack(side=LEFT, padx=3, pady=3)
    entZhill_2 = Entry(frm2, width=20)
    entZhill_2.pack(side=LEFT, padx=3, pady=3)

    lblZflag_2 = Label(frm2, text=constRE.DISCPOLR.Zflag_2.name)
    lblZflag_2.pack(side=LEFT, padx=3, pady=3)
    entZflag_2 = Entry(frm2, width=20)
    entZflag_2.pack(side=LEFT, padx=3, pady=3)

    discpolrVals[constRE.DISCPOLR.Srcid_2.name] = entSrcid_2
    discpolrVals[constRE.DISCPOLR.Dist_2.name] = entDist_2
    discpolrVals[constRE.DISCPOLR.Direct_2.name] = entDirect_2
    discpolrVals[constRE.DISCPOLR.Zelev_2.name] = entZelev_2
    discpolrVals[constRE.DISCPOLR.Zhill_2.name] = entZhill_2
    discpolrVals[constRE.DISCPOLR.Zflag_2.name] = entZflag_2

    # _3 ===============================================================================================================
    frm3 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm3.grid(row=2, column=0, padx=3, pady=3, sticky=W + E)

    lblSrcid_3 = Label(frm3, text=constRE.DISCPOLR.Srcid_3.name)
    lblSrcid_3.pack(side=LEFT, padx=3, pady=3)
    entSrcid_3 = Entry(frm3, width=20)
    entSrcid_3.pack(side=LEFT, padx=3, pady=3)

    lblDist_3 = Label(frm3, text=constRE.DISCPOLR.Dist_3.name)
    lblDist_3.pack(side=LEFT, padx=3, pady=3)
    entDist_3 = Entry(frm3, width=20)
    entDist_3.pack(side=LEFT, padx=3, pady=3)

    lblDirect_3 = Label(frm3, text=constRE.DISCPOLR.Direct_3.name)
    lblDirect_3.pack(side=LEFT, padx=3, pady=3)
    entDirect_3 = Entry(frm3, width=20)
    entDirect_3.pack(side=LEFT, padx=3, pady=3)

    lblZelev_3 = Label(frm3, text=constRE.DISCPOLR.Zelev_3.name)
    lblZelev_3.pack(side=LEFT, padx=3, pady=3)
    entZelev_3 = Entry(frm3, width=20)
    entZelev_3.pack(side=LEFT, padx=3, pady=3)

    lblZhill_3 = Label(frm3, text=constRE.DISCPOLR.Zhill_3.name)
    lblZhill_3.pack(side=LEFT, padx=3, pady=3)
    entZhill_3 = Entry(frm3, width=20)
    entZhill_3.pack(side=LEFT, padx=3, pady=3)

    lblZflag_3 = Label(frm3, text=constRE.DISCPOLR.Zflag_3.name)
    lblZflag_3.pack(side=LEFT, padx=3, pady=3)
    entZflag_3 = Entry(frm3, width=20)
    entZflag_3.pack(side=LEFT, padx=3, pady=3)

    discpolrVals[constRE.DISCPOLR.Srcid_3.name] = entSrcid_3
    discpolrVals[constRE.DISCPOLR.Dist_3.name] = entDist_3
    discpolrVals[constRE.DISCPOLR.Direct_3.name] = entDirect_3
    discpolrVals[constRE.DISCPOLR.Zelev_3.name] = entZelev_3
    discpolrVals[constRE.DISCPOLR.Zhill_3.name] = entZhill_3
    discpolrVals[constRE.DISCPOLR.Zflag_3.name] = entZflag_3

# ======================================================================================================================
def makeEVALCART(frm):
    # _1 ===============================================================================================================
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.grid(row=0, column=0, padx=3, pady=3, sticky=W + E)

    lblX_1 = Label(frm1, text=constRE.EVALCART.Xcoord_1.name)
    lblX_1.pack(side=LEFT, padx=3, pady=3)
    entX_1 = Entry(frm1, width=20)
    entX_1.pack(side=LEFT, padx=3, pady=3)

    lblY_1 = Label(frm1, text=constRE.EVALCART.Ycoord_1.name)
    lblY_1.pack(side=LEFT, padx=3, pady=3)
    entY_1 = Entry(frm1, width=20)
    entY_1.pack(side=LEFT, padx=3, pady=3)

    lblZelev_1 = Label(frm1, text=constRE.EVALCART.Zelev_1.name)
    lblZelev_1.pack(side=LEFT, padx=3, pady=3)
    entZelev_1 = Entry(frm1, width=20)
    entZelev_1.pack(side=LEFT, padx=3, pady=3)

    lblZhill_1 = Label(frm1, text=constRE.EVALCART.Zhill_1.name)
    lblZhill_1.pack(side=LEFT, padx=3, pady=3)
    entZhill_1 = Entry(frm1, width=20)
    entZhill_1.pack(side=LEFT, padx=3, pady=3)

    lblZflag_1 = Label(frm1, text=constRE.EVALCART.Zflag_1.name)
    lblZflag_1.pack(side=LEFT, padx=3, pady=3)
    entZflag_1 = Entry(frm1, width=20)
    entZflag_1.pack(side=LEFT, padx=3, pady=3)

    lblArcid_1 = Label(frm1, text=constRE.EVALCART.Arcid_1.name)
    lblArcid_1.pack(side=LEFT, padx=3, pady=3)
    entArcid_1 = Entry(frm1, width=20)
    entArcid_1.pack(side=LEFT, padx=3, pady=3)

    lblName_1 = Label(frm1, text=constRE.EVALCART.Name_1.name)
    lblName_1.pack(side=LEFT, padx=3, pady=3)
    entName_1 = Entry(frm1, width=20)
    entName_1.pack(side=LEFT, padx=3, pady=3)

    evalcartVals[constRE.EVALCART.Xcoord_1.name] = entX_1
    evalcartVals[constRE.EVALCART.Ycoord_1.name] = entY_1
    evalcartVals[constRE.EVALCART.Zelev_1.name] = entZelev_1
    evalcartVals[constRE.EVALCART.Zhill_1.name] = entZhill_1
    evalcartVals[constRE.EVALCART.Zflag_1.name] = entZflag_1
    evalcartVals[constRE.EVALCART.Arcid_1.name] = entArcid_1
    evalcartVals[constRE.EVALCART.Name_1.name] = entName_1

    # _2 ===============================================================================================================
    frm2 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm2.grid(row=1, column=0, padx=3, pady=3, sticky=W + E)

    lblX_2 = Label(frm2, text=constRE.EVALCART.Xcoord_2.name)
    lblX_2.pack(side=LEFT, padx=3, pady=3)
    entX_2 = Entry(frm2, width=20)
    entX_2.pack(side=LEFT, padx=3, pady=3)

    lblY_2 = Label(frm2, text=constRE.EVALCART.Ycoord_2.name)
    lblY_2.pack(side=LEFT, padx=3, pady=3)
    entY_2 = Entry(frm2, width=20)
    entY_2.pack(side=LEFT, padx=3, pady=3)

    lblZelev_2 = Label(frm2, text=constRE.EVALCART.Zelev_2.name)
    lblZelev_2.pack(side=LEFT, padx=3, pady=3)
    entZelev_2 = Entry(frm2, width=20)
    entZelev_2.pack(side=LEFT, padx=3, pady=3)

    lblZhill_2 = Label(frm2, text=constRE.EVALCART.Zhill_2.name)
    lblZhill_2.pack(side=LEFT, padx=3, pady=3)
    entZhill_2 = Entry(frm2, width=20)
    entZhill_2.pack(side=LEFT, padx=3, pady=3)

    lblZflag_2 = Label(frm2, text=constRE.EVALCART.Zflag_2.name)
    lblZflag_2.pack(side=LEFT, padx=3, pady=3)
    entZflag_2 = Entry(frm2, width=20)
    entZflag_2.pack(side=LEFT, padx=3, pady=3)

    lblArcid_2 = Label(frm2, text=constRE.EVALCART.Arcid_2.name)
    lblArcid_2.pack(side=LEFT, padx=3, pady=3)
    entArcid_2 = Entry(frm2, width=20)
    entArcid_2.pack(side=LEFT, padx=3, pady=3)

    lblName_2 = Label(frm2, text=constRE.EVALCART.Name_2.name)
    lblName_2.pack(side=LEFT, padx=3, pady=3)
    entName_2 = Entry(frm2, width=20)
    entName_2.pack(side=LEFT, padx=3, pady=3)

    evalcartVals[constRE.EVALCART.Xcoord_2.name] = entX_2
    evalcartVals[constRE.EVALCART.Ycoord_2.name] = entY_2
    evalcartVals[constRE.EVALCART.Zelev_2.name] = entZelev_2
    evalcartVals[constRE.EVALCART.Zhill_2.name] = entZhill_2
    evalcartVals[constRE.EVALCART.Zflag_2.name] = entZflag_2
    evalcartVals[constRE.EVALCART.Arcid_2.name] = entArcid_2
    evalcartVals[constRE.EVALCART.Name_2.name] = entName_2

    # _3 ===============================================================================================================
    frm3 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm3.grid(row=2, column=0, padx=3, pady=3, sticky=W + E)

    lblX_3 = Label(frm3, text=constRE.EVALCART.Xcoord_3.name)
    lblX_3.pack(side=LEFT, padx=3, pady=3)
    entX_3 = Entry(frm3, width=20)
    entX_3.pack(side=LEFT, padx=3, pady=3)

    lblY_3 = Label(frm3, text=constRE.EVALCART.Ycoord_3.name)
    lblY_3.pack(side=LEFT, padx=3, pady=3)
    entY_3 = Entry(frm3, width=20)
    entY_3.pack(side=LEFT, padx=3, pady=3)

    lblZelev_3 = Label(frm3, text=constRE.EVALCART.Zelev_3.name)
    lblZelev_3.pack(side=LEFT, padx=3, pady=3)
    entZelev_3 = Entry(frm3, width=20)
    entZelev_3.pack(side=LEFT, padx=3, pady=3)

    lblZhill_3 = Label(frm3, text=constRE.EVALCART.Zhill_3.name)
    lblZhill_3.pack(side=LEFT, padx=3, pady=3)
    entZhill_3 = Entry(frm3, width=20)
    entZhill_3.pack(side=LEFT, padx=3, pady=3)

    lblZflag_3 = Label(frm3, text=constRE.EVALCART.Zflag_3.name)
    lblZflag_3.pack(side=LEFT, padx=3, pady=3)
    entZflag_3 = Entry(frm3, width=20)
    entZflag_3.pack(side=LEFT, padx=3, pady=3)

    lblArcid_3 = Label(frm3, text=constRE.EVALCART.Arcid_3.name)
    lblArcid_3.pack(side=LEFT, padx=3, pady=3)
    entArcid_3 = Entry(frm3, width=20)
    entArcid_3.pack(side=LEFT, padx=3, pady=3)

    lblName_3 = Label(frm3, text=constRE.EVALCART.Name_3.name)
    lblName_3.pack(side=LEFT, padx=3, pady=3)
    entName_3 = Entry(frm3, width=20)
    entName_3.pack(side=LEFT, padx=3, pady=3)

    evalcartVals[constRE.EVALCART.Xcoord_3.name] = entX_3
    evalcartVals[constRE.EVALCART.Ycoord_3.name] = entY_3
    evalcartVals[constRE.EVALCART.Zelev_3.name] = entZelev_3
    evalcartVals[constRE.EVALCART.Zhill_3.name] = entZhill_3
    evalcartVals[constRE.EVALCART.Zflag_3.name] = entZflag_3
    evalcartVals[constRE.EVALCART.Arcid_3.name] = entArcid_3
    evalcartVals[constRE.EVALCART.Name_3.name] = entName_3

# ======================================================================================================================
def makeINCLUDED(frm):
    lbl = Label(frm, text=constRE.INCLUDED.RecIncFile.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=100)
    ent.pack(side=LEFT, padx=3, pady=3)
    includedVals[constRE.INCLUDED.RecIncFile.name] = ent

# ======================================================================================================================
elevunitVals = {}
gridcartVals = {}
gridpolrVals = {}
disccartVals = {}
discpolrVals = {}
evalcartVals = {}
includedVals = {}

# ======================================================================================================================
def buildTabRE(tabRE):
    frmIntro = LabelFrame(tabRE, bd=0)
    frmIntro.pack(side=TOP, padx=5, pady=0, fill='both')
    introText = Label(frmIntro, text='\nReceptor Pathway (RE) Keywords and Parameters\n')
    introText.pack(side=TOP, expand='yes')

    # creates scrollable frame for inputs
    frmInputs = Frame(tabRE, bd=0)
    canvas = Canvas(frmInputs)
    scrollbar = Scrollbar(frmInputs, orient='vertical', command=canvas.yview)
    scrollFrmInputs = Frame(canvas)

    scrollFrmInputs.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollFrmInputs, anchor=NW)
    canvas.configure(yscrollcommand=scrollbar.set)

    frmInputs.pack(side=TOP, padx=5, pady=5, expand=True, fill='both')
    canvas.pack(side=LEFT, padx=5, pady=5, fill='both', expand=True)
    scrollbar.pack(side=RIGHT, fill='y')
    # finish creating scrollable input frame

    frmELEVUNIT = LabelFrame(scrollFrmInputs, bd=1, text='ELEVUNIT')
    frmELEVUNIT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeELEVUNIT(frmELEVUNIT)

    frmGRIDCART = LabelFrame(scrollFrmInputs, bd=1, text='GRIDCART')
    frmGRIDCART.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeGRIDCART(frmGRIDCART)

    frmGRIDPOLR = LabelFrame(scrollFrmInputs, bd=1, text='GRIDPOLR')
    frmGRIDPOLR.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeGRIDPOLR(frmGRIDPOLR)

    frmDISCCART = LabelFrame(scrollFrmInputs, bd=1, text='DISCCART')
    frmDISCCART.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeDISCCART(frmDISCCART)

    frmDISCPOLR = LabelFrame(scrollFrmInputs, bd=1, text='DISCPOLR')
    frmDISCPOLR.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeDISCPOLR(frmDISCPOLR)

    frmEVALCART = LabelFrame(scrollFrmInputs, bd=1, text='EVALCART')
    frmEVALCART.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeEVALCART(frmEVALCART)

    frmINCLUDED = LabelFrame(scrollFrmInputs, bd=1, text='INCLUDED')
    frmINCLUDED.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeINCLUDED(frmINCLUDED)

    reInputs = (elevunitVals, gridcartVals, gridpolrVals, disccartVals, discpolrVals, evalcartVals, includedVals)

    frmButtons = Frame(tabRE, bd=0)
    frmButtons.pack(side=TOP, padx=5, pady=3, fill="both")
    btn1 = Button(frmButtons, text='Write RE to control file', font=('calibri', 11, 'bold'), width=40,
                  command=(lambda: reWriter.writeControlFile(reInputs)))
    btn1.pack(side=TOP, padx=60, pady=3)