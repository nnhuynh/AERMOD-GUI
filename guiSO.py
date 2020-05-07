from tkinter import *
import constantsSO as constSO
import soWriter

# ======================================================================================================================
def makeELEVUNIT(frm):
    lbl = Label(frm, text=constSO.ELEVUNIT.ELEVUNIT.name)
    lbl.pack(side=LEFT, padx=3, pady=3)

    choices = [constSO.ELEVUNIT.METERS.name, constSO.ELEVUNIT.FEET.name]
    variable = StringVar()
    variable.set(choices[0])
    opt = OptionMenu(frm, variable, *choices)
    opt.config(width=7)
    opt.pack(side=LEFT, padx=3, pady=3)

    elevunitVals[constSO.ELEVUNIT.ELEVUNIT.name] = variable

# ======================================================================================================================
def makeLOCATION(frm):
    frmt1 = Frame(frm)
    frmt1.grid(row=0, column=0, padx=0, pady=0)

    lblSrcID_t1 = Label(frmt1, text=constSO.LOCATION.SrcID_t1.value)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    entSrcID_t1 = Entry(frmt1, width=15)
    entSrcID_t1.pack(side=LEFT, padx=3, pady=3)

    lblSrctyp_t1 = Label(frmt1, text=constSO.LOCATION.Srctyp_t1.value)
    lblSrctyp_t1.pack(side=LEFT, padx=3, pady=3)
    choices_t1 = ['POINT', 'POINTCAP', 'POINTHOR', 'VOLUME', 'AREA', 'AREAPOLY', 'AREACIRC', 'OPENPIT']
    var_t1 = StringVar()
    var_t1.set(choices_t1[0])
    opt_t1 = OptionMenu(frmt1, var_t1, *choices_t1)
    opt_t1.config(width=10)
    opt_t1.pack(side=LEFT, padx=3, pady=3)

    frmXs_t1 = Frame(frm)
    frmXs_t1.grid(row=0, column=1, padx=0, pady=0)
    lblXs_t1 = Label(frmXs_t1, text=constSO.LOCATION.Xs_t1.value)
    lblXs_t1.pack(side=LEFT, padx=3, pady=3)
    entXs_t1 = Entry(frmXs_t1, width=50)
    entXs_t1.pack(side=LEFT, padx=3, pady=3)

    frmYs_t1 = Frame(frm)
    frmYs_t1.grid(row=0, column=2, padx=0, pady=0)
    lblYs_t1 = Label(frmYs_t1, text=constSO.LOCATION.Ys_t1.value)
    lblYs_t1.pack(side=LEFT, padx=3, pady=3)
    entYs_t1 = Entry(frmYs_t1, width=50)
    entYs_t1.pack(side=LEFT, padx=3, pady=3)

    frmZs_t1 = Frame(frm)
    frmZs_t1.grid(row=0, column=3, padx=0, pady=0)
    lblZs_t1 = Label(frmZs_t1, text=constSO.LOCATION.Zs_t1.value)
    lblZs_t1.pack(side=LEFT, padx=3, pady=3)
    entZs_t1 = Entry(frmZs_t1, width=50)
    entZs_t1.pack(side=LEFT, padx=3, pady=3)

    frmt2 = Frame(frm)
    frmt2.grid(row=1, column=0, padx=0, pady=0)
    lblSrcID_t2 = Label(frmt2, text=constSO.LOCATION.SrcID_t2.value)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    entSrcID_t2 = Entry(frmt2, width=15)
    entSrcID_t2.pack(side=LEFT, padx=3, pady=3)

    lblSrctyp_t2 = Label(frmt2, text=constSO.LOCATION.Srctyp_t2.value)
    lblSrctyp_t2.pack(side=LEFT, padx=3, pady=3)
    choices_t2 = ['LINE', 'BUOYLINE', 'RLINE']
    var_t2 = StringVar()
    var_t2.set(choices_t2[0])
    opt_t2 = OptionMenu(frmt2, var_t2, *choices_t2)
    opt_t2.config(width=10)
    opt_t2.pack(side=LEFT, padx=3, pady=3)

    frmXs1_t2 = Frame(frm)
    frmXs1_t2.grid(row=1, column=1, padx=0, pady=0)
    lblXs1_t2 = Label(frmXs1_t2, text=constSO.LOCATION.Xs1_t2.value)
    lblXs1_t2.pack(side=LEFT, padx=3, pady=3)
    entXs1_t2 = Entry(frmXs1_t2, width=50)
    entXs1_t2.pack(side=LEFT, padx=3, pady=3)

    frmYs1_t2 = Frame(frm)
    frmYs1_t2.grid(row=1, column=2, padx=0, pady=0)
    lblYs1_t2 = Label(frmYs1_t2, text=constSO.LOCATION.Ys1_t2.value)
    lblYs1_t2.pack(side=LEFT, padx=3, pady=3)
    entYs1_t2 = Entry(frmYs1_t2, width=50)
    entYs1_t2.pack(side=LEFT, padx=3, pady=3)

    frmZs_t2 = Frame(frm)
    frmZs_t2.grid(row=1, column=3, padx=0, pady=0)
    lblZs_t2 = Label(frmZs_t2, text=constSO.LOCATION.Zs_t2.value)
    lblZs_t2.pack(side=LEFT, padx=3, pady=3)
    entZs_t2 = Entry(frmZs_t2, width=50)
    entZs_t2.pack(side=LEFT, padx=3, pady=3)

    frmXs2_t2 = Frame(frm)
    frmXs2_t2.grid(row=2, column=1, padx=0, pady=0)
    lblXs2_t2 = Label(frmXs2_t2, text=constSO.LOCATION.Xs2_t2.value)
    lblXs2_t2.pack(side=LEFT, padx=3, pady=3)
    entXs2_t2 = Entry(frmXs2_t2, width=50)
    entXs2_t2.pack(side=LEFT, padx=3, pady=3)

    frmYs2_t2 = Frame(frm)
    frmYs2_t2.grid(row=2, column=2, padx=0, pady=0)
    lblYs2_t2 = Label(frmYs2_t2, text=constSO.LOCATION.Ys2_t2.value)
    lblYs2_t2.pack(side=LEFT, padx=3, pady=3)
    entYs2_t2 = Entry(frmYs2_t2, width=50)
    entYs2_t2.pack(side=LEFT, padx=3, pady=3)

    frmt3 = Frame(frm)
    frmt3.grid(row=3, column=0, padx=0, pady=0)
    lblSrcID_t3 = Label(frmt3, text=constSO.LOCATION.SrcID_t3.value)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    entSrcID_t3 = Entry(frmt3, width=15)
    entSrcID_t3.pack(side=LEFT, padx=3, pady=3)

    lblSrctyp_t3 = Label(frmt3, text=constSO.LOCATION.Srctyp_t3.value)
    lblSrctyp_t3.pack(side=LEFT, padx=3, pady=3)
    choices_t3 = ['RLINEXT']
    var_t3 = StringVar()
    var_t3.set(choices_t3[0])
    opt_t3 = OptionMenu(frmt3, var_t3, *choices_t3)
    opt_t3.config(width=10)
    opt_t3.pack(side=LEFT, padx=3, pady=3)

    frmXs1_t3 = Frame(frm)
    frmXs1_t3.grid(row=3, column=1, padx=0, pady=0)
    lblXs1_t3 = Label(frmXs1_t3, text=constSO.LOCATION.Xs1_t3.value)
    lblXs1_t3.pack(side=LEFT, padx=3, pady=3)
    entXs1_t3 = Entry(frmXs1_t3, width=50)
    entXs1_t3.pack(side=LEFT, padx=3, pady=3)

    frmYs1_t3 = Frame(frm)
    frmYs1_t3.grid(row=3, column=2, padx=0, pady=0)
    lblYs1_t3 = Label(frmYs1_t3, text=constSO.LOCATION.Ys1_t3.value)
    lblYs1_t3.pack(side=LEFT, padx=3, pady=3)
    entYs1_t3 = Entry(frmYs1_t3, width=50)
    entYs1_t3.pack(side=LEFT, padx=3, pady=3)

    frmZs1_t3 = Frame(frm)
    frmZs1_t3.grid(row=3, column=3, padx=0, pady=0)
    lblZs1_t3 = Label(frmZs1_t3, text=constSO.LOCATION.Zs1_t3.value)
    lblZs1_t3.pack(side=LEFT, padx=3, pady=3)
    entZs1_t3 = Entry(frmZs1_t3, width=50)
    entZs1_t3.pack(side=LEFT, padx=3, pady=3)

    frmXs2_t3 = Frame(frm)
    frmXs2_t3.grid(row=4, column=1, padx=0, pady=0)
    lblXs2_t3 = Label(frmXs2_t3, text=constSO.LOCATION.Xs2_t3.value)
    lblXs2_t3.pack(side=LEFT, padx=3, pady=3)
    entXs2_t3 = Entry(frmXs2_t3, width=50)
    entXs2_t3.pack(side=LEFT, padx=3, pady=3)

    frmYs2_t3 = Frame(frm)
    frmYs2_t3.grid(row=4, column=2, padx=0, pady=0)
    lblYs2_t3 = Label(frmYs2_t3, text=constSO.LOCATION.Ys2_t3.value)
    lblYs2_t3.pack(side=LEFT, padx=3, pady=3)
    entYs2_t3 = Entry(frmYs2_t3, width=50)
    entYs2_t3.pack(side=LEFT, padx=3, pady=3)

    frmZs2_t3 = Frame(frm)
    frmZs2_t3.grid(row=4, column=3, padx=0, pady=0)
    lblZs2_t3 = Label(frmZs2_t3, text=constSO.LOCATION.Zs2_t3.value)
    lblZs2_t3.pack(side=LEFT, padx=3, pady=3)
    entZs2_t3 = Entry(frmZs2_t3, width=50)
    entZs2_t3.pack(side=LEFT, padx=3, pady=3)


    locationVals[constSO.LOCATION.SrcID_t1.name] = entSrcID_t1
    locationVals[constSO.LOCATION.Srctyp_t1.name] = var_t1
    locationVals[constSO.LOCATION.Xs_t1.name] = entXs_t1
    locationVals[constSO.LOCATION.Ys_t1.name] = entYs_t1
    locationVals[constSO.LOCATION.Zs_t1.name] = entZs_t1

    locationVals[constSO.LOCATION.SrcID_t2.name] = entSrcID_t2
    locationVals[constSO.LOCATION.Srctyp_t2.name] = var_t2
    locationVals[constSO.LOCATION.Xs1_t2.name] = entXs1_t2
    locationVals[constSO.LOCATION.Ys1_t2.name] = entYs1_t2
    locationVals[constSO.LOCATION.Zs_t2.name] = entZs_t2
    locationVals[constSO.LOCATION.Xs2_t2.name] = entXs2_t2
    locationVals[constSO.LOCATION.Ys2_t2.name] = entYs2_t2

    locationVals[constSO.LOCATION.SrcID_t3.name] = entSrcID_t3
    locationVals[constSO.LOCATION.Srctyp_t3.name] = var_t3
    locationVals[constSO.LOCATION.Xs1_t3.name] = entXs1_t3
    locationVals[constSO.LOCATION.Ys1_t3.name] = entYs1_t3
    locationVals[constSO.LOCATION.Zs1_t3.name] = entZs1_t3
    locationVals[constSO.LOCATION.Xs2_t3.name] = entXs2_t3
    locationVals[constSO.LOCATION.Ys2_t3.name] = entYs2_t3
    locationVals[constSO.LOCATION.Zs2_t3.name] = entZs2_t3

# ======================================================================================================================
def makeSRCPARAM(frm):
    # frmLEFT SrcID_t1 ==================================================================================================
    frmLEFT = LabelFrame(frm, bd=1, text=constSO.SRCPARAM.SrcID_t1.name)
    frmLEFT.grid(row=0, column=0)

    frmPtemis1 = Frame(frmLEFT)
    frmPtemis1.grid(row=1, column=0, sticky=W+E)
    lblPtemis1 = Label(frmPtemis1, text=constSO.SRCPARAM.Ptemis_t1.name)
    lblPtemis1.pack(side=LEFT, padx=2, pady=3)
    entPtemis1 = Entry(frmPtemis1, width=7)
    entPtemis1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Ptemis_t1.name] = entPtemis1

    frmStkhgt1 = Frame(frmLEFT)
    frmStkhgt1.grid(row=1, column=1, sticky=W+E)
    lblStkhgt1 = Label(frmStkhgt1, text=constSO.SRCPARAM.Stkhgt_t1.name)
    lblStkhgt1.pack(side=LEFT, padx=2, pady=3)
    entStkhgt1 = Entry(frmStkhgt1, width=7)
    entStkhgt1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkhgt_t1.name] = entStkhgt1

    frmStktmp1 = Frame(frmLEFT)
    frmStktmp1.grid(row=1, column=2, sticky=W+E)
    lblStktmp1 = Label(frmStktmp1, text=constSO.SRCPARAM.Stktmp_t1.name)
    lblStktmp1.pack(side=LEFT, padx=2, pady=3)
    entStktmp1 = Entry(frmStktmp1, width=7)
    entStktmp1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stktmp_t1.name] = entStktmp1

    frmStkvel1 = Frame(frmLEFT)
    frmStkvel1.grid(row=1, column=3, sticky=W+E)
    lblStkvel1 = Label(frmStkvel1, text=constSO.SRCPARAM.Stkvel_t1.name)
    lblStkvel1.pack(side=LEFT, padx=2, pady=3)
    entStkvel1 = Entry(frmStkvel1, width=7)
    entStkvel1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkvel_t1.name] = entStkvel1

    frmStkdia1 = Frame(frmLEFT)
    frmStkdia1.grid(row=1, column=4, sticky=W+E)
    lblStkdia1 = Label(frmStkdia1, text=constSO.SRCPARAM.Stkdia_t1.name)
    lblStkdia1.pack(side=LEFT, padx=2, pady=3)
    entStkdia1 = Entry(frmStkdia1, width=7)
    entStkdia1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkdia_t1.name] = entStkdia1

    frmVlemis1 = Frame(frmLEFT)
    frmVlemis1.grid(row=2, column=0, sticky=W+E)
    lblVlemis1 = Label(frmVlemis1, text=constSO.SRCPARAM.Vlemis_t1.name)
    lblVlemis1.pack(side=LEFT, padx=2, pady=3)
    entVlemis1 = Entry(frmVlemis1, width=7)
    entVlemis1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Vlemis_t1.name] = entVlemis1

    frmRelhgt1 = Frame(frmLEFT)
    frmRelhgt1.grid(row=2, column=1, sticky=W+E)
    lblRelhgt1 = Label(frmRelhgt1, text=constSO.SRCPARAM.Relhgt_t1.name)
    lblRelhgt1.pack(side=LEFT, padx=2, pady=3)
    entRelhgt1 = Entry(frmRelhgt1, width=7)
    entRelhgt1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Relhgt_t1.name] = entRelhgt1

    frmSyinit1 = Frame(frmLEFT)
    frmSyinit1.grid(row=2, column=2, sticky=W+E)
    lblSyinit1 = Label(frmSyinit1, text=constSO.SRCPARAM.Syinit_t1.name)
    lblSyinit1.pack(side=LEFT, padx=2, pady=3)
    entSyinit1 = Entry(frmSyinit1, width=7)
    entSyinit1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Syinit_t1.name] = entSyinit1

    frmSzinit1 = Frame(frmLEFT)
    frmSzinit1.grid(row=2, column=3, sticky=W+E)
    lblSzinit1 = Label(frmSzinit1, text=constSO.SRCPARAM.Szinit_t1.name)
    lblSzinit1.pack(side=LEFT, padx=2, pady=3)
    entSzinit1 = Entry(frmSzinit1, width=7)
    entSzinit1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Szinit_t1.name] = entSzinit1

    frmAremis1 = Frame(frmLEFT)
    frmAremis1.grid(row=3, column=0, sticky=W+E)
    lblAremis1 = Label(frmAremis1, text=constSO.SRCPARAM.Aremis_t1.name)
    lblAremis1.pack(side=LEFT, padx=2, pady=3)
    entAremis1 = Entry(frmAremis1, width=7)
    entAremis1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Aremis_t1.name] = entAremis1

    frmXinit1 = Frame(frmLEFT)
    frmXinit1.grid(row=3, column=2, sticky=W+E)
    lblXinit1 = Label(frmXinit1, text=constSO.SRCPARAM.Xinit_t1.name)
    lblXinit1.pack(side=LEFT, padx=2, pady=3)
    entXinit1 = Entry(frmXinit1, width=7)
    entXinit1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Xinit_t1.name] = entXinit1

    frmYinit1 = Frame(frmLEFT)
    frmYinit1.grid(row=3, column=3, sticky=W+E)
    lblYinit1 = Label(frmYinit1, text=constSO.SRCPARAM.Yinit_t1.name)
    lblYinit1.pack(side=LEFT, padx=2, pady=3)
    entYinit1 = Entry(frmYinit1, width=7)
    entYinit1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Yinit_t1.name] = entYinit1

    frmAngle1 = Frame(frmLEFT)
    frmAngle1.grid(row=3, column=4, sticky=W+E)
    lblAngle1 = Label(frmAngle1, text=constSO.SRCPARAM.Angle_t1.name)
    lblAngle1.pack(side=LEFT, padx=2, pady=3)
    entAngle1 = Entry(frmAngle1, width=7)
    entAngle1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Angle_t1.name] = entAngle1

    frmNverts1 = Frame(frmLEFT)
    frmNverts1.grid(row=4, column=2, sticky=W+E)
    lblNverts1 = Label(frmNverts1, text=constSO.SRCPARAM.Nverts_t1.name)
    lblNverts1.pack(side=LEFT, padx=2, pady=3)
    entNverts1 = Entry(frmNverts1, width=7)
    entNverts1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Nverts_t1.name] = entNverts1

    frmRadius1 = Frame(frmLEFT)
    frmRadius1.grid(row=5, column=2, sticky=W+E)
    lblRadius1 = Label(frmRadius1, text=constSO.SRCPARAM.Radius_t1.name)
    lblRadius1.pack(side=LEFT, padx=2, pady=3)
    entRadius1 = Entry(frmRadius1, width=7)
    entRadius1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Radius_t1.name] = entRadius1

    frmLnemis1 = Frame(frmLEFT)
    frmLnemis1.grid(row=6, column=0, sticky=W+E)
    lblLnemis1 = Label(frmLnemis1, text=constSO.SRCPARAM.Lnemis_t1.name)
    lblLnemis1.pack(side=LEFT, padx=2, pady=3)
    entLnemis1 = Entry(frmLnemis1, width=7)
    entLnemis1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Lnemis_t1.name] = entLnemis1

    frmWidth1 = Frame(frmLEFT)
    frmWidth1.grid(row=6, column=2, sticky=W+E)
    lblWidth1 = Label(frmWidth1, text=constSO.SRCPARAM.Width_t1.name)
    lblWidth1.pack(side=LEFT, padx=2, pady=3)
    entWidth1 = Entry(frmWidth1, width=7)
    entWidth1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Width_t1.name] = entWidth1

    frmOpemis1 = Frame(frmLEFT)
    frmOpemis1.grid(row=7, column=0, sticky=W+E)
    lblOpemis1 = Label(frmOpemis1, text=constSO.SRCPARAM.Opemis_t1.name)
    lblOpemis1.pack(side=LEFT, padx=2, pady=3)
    entOpemis1 = Entry(frmOpemis1, width=7)
    entOpemis1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Opemis_t1.name] = entOpemis1

    frmPitvol1 = Frame(frmLEFT)
    frmPitvol1.grid(row=7, column=4, sticky=W+E)
    lblPitvol1 = Label(frmPitvol1, text=constSO.SRCPARAM.Pitvol_t1.name)
    lblPitvol1.pack(side=LEFT, anchor=W, padx=2, pady=3)
    entPitvol1 = Entry(frmPitvol1, width=7)
    entPitvol1.pack(side=RIGHT, anchor=E, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Pitvol_t1.name] = entPitvol1

    frmBlemis1 = Frame(frmLEFT)
    frmBlemis1.grid(row=8, column=0, sticky=W+E)
    lblBlemis1 = Label(frmBlemis1, text=constSO.SRCPARAM.Blemis_t1.name)
    lblBlemis1.pack(side=LEFT, padx=2, pady=3)
    entBlemis1 = Entry(frmBlemis1, width=7)
    entBlemis1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Blemis_t1.name] = entBlemis1

    frmQemis1 = Frame(frmLEFT)
    frmQemis1.grid(row=9, column=0, sticky=W+E)
    lblQemis1 = Label(frmQemis1, text=constSO.SRCPARAM.Qemis_t1.name)
    lblQemis1.pack(side=LEFT, padx=2, pady=3)
    entQemis1 = Entry(frmQemis1, width=7)
    entQemis1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Qemis_t1.name] = entQemis1

    frmDCL1 = Frame(frmLEFT)
    frmDCL1.grid(row=9, column=1, sticky=W+E)
    lblDCL1 = Label(frmDCL1, text=constSO.SRCPARAM.DCL_t1.name)
    lblDCL1.pack(side=LEFT, padx=2, pady=3)
    entDCL1 = Entry(frmDCL1, width=7)
    entDCL1.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.DCL_t1.name] = entDCL1

    # frmMID SrcID_t2 ==================================================================================================
    frmMID = LabelFrame(frm, bd=1, text=constSO.SRCPARAM.SrcID_t2.name)
    frmMID.grid(row=0, column=1)

    frmPtemis2 = Frame(frmMID)
    frmPtemis2.grid(row=1, column=0, sticky=W + E)
    lblPtemis2 = Label(frmPtemis2, text=constSO.SRCPARAM.Ptemis_t2.name)
    lblPtemis2.pack(side=LEFT, padx=2, pady=3)
    entPtemis2 = Entry(frmPtemis2, width=7)
    entPtemis2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Ptemis_t2.name] = entPtemis2

    frmStkhgt2 = Frame(frmMID)
    frmStkhgt2.grid(row=1, column=1, sticky=W + E)
    lblStkhgt2 = Label(frmStkhgt2, text=constSO.SRCPARAM.Stkhgt_t2.name)
    lblStkhgt2.pack(side=LEFT, padx=2, pady=3)
    entStkhgt2 = Entry(frmStkhgt2, width=7)
    entStkhgt2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkhgt_t2.name] = entStkhgt2

    frmStktmp2 = Frame(frmMID)
    frmStktmp2.grid(row=1, column=2, sticky=W + E)
    lblStktmp2 = Label(frmStktmp2, text=constSO.SRCPARAM.Stktmp_t2.name)
    lblStktmp2.pack(side=LEFT, padx=2, pady=3)
    entStktmp2 = Entry(frmStktmp2, width=7)
    entStktmp2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stktmp_t2.name] = entStktmp2

    frmStkvel2 = Frame(frmMID)
    frmStkvel2.grid(row=1, column=3, sticky=W + E)
    lblStkvel2 = Label(frmStkvel2, text=constSO.SRCPARAM.Stkvel_t2.name)
    lblStkvel2.pack(side=LEFT, padx=2, pady=3)
    entStkvel2 = Entry(frmStkvel2, width=7)
    entStkvel2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkvel_t2.name] = entStkvel2

    frmStkdia2 = Frame(frmMID)
    frmStkdia2.grid(row=1, column=4, sticky=W + E)
    lblStkdia2 = Label(frmStkdia2, text=constSO.SRCPARAM.Stkdia_t2.name)
    lblStkdia2.pack(side=LEFT, padx=2, pady=3)
    entStkdia2 = Entry(frmStkdia2, width=7)
    entStkdia2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkdia_t2.name] = entStkdia2

    frmVlemis2 = Frame(frmMID)
    frmVlemis2.grid(row=2, column=0, sticky=W + E)
    lblVlemis2 = Label(frmVlemis2, text=constSO.SRCPARAM.Vlemis_t2.name)
    lblVlemis2.pack(side=LEFT, padx=2, pady=3)
    entVlemis2 = Entry(frmVlemis2, width=7)
    entVlemis2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Vlemis_t2.name] = entVlemis2

    frmRelhgt2 = Frame(frmMID)
    frmRelhgt2.grid(row=2, column=1, sticky=W + E)
    lblRelhgt2 = Label(frmRelhgt2, text=constSO.SRCPARAM.Relhgt_t2.name)
    lblRelhgt2.pack(side=LEFT, padx=2, pady=3)
    entRelhgt2 = Entry(frmRelhgt2, width=7)
    entRelhgt2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Relhgt_t2.name] = entRelhgt2

    frmSyinit2 = Frame(frmMID)
    frmSyinit2.grid(row=2, column=2, sticky=W + E)
    lblSyinit2 = Label(frmSyinit2, text=constSO.SRCPARAM.Syinit_t2.name)
    lblSyinit2.pack(side=LEFT, padx=2, pady=3)
    entSyinit2 = Entry(frmSyinit2, width=7)
    entSyinit2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Syinit_t2.name] = entSyinit2

    frmSzinit2 = Frame(frmMID)
    frmSzinit2.grid(row=2, column=3, sticky=W + E)
    lblSzinit2 = Label(frmSzinit2, text=constSO.SRCPARAM.Szinit_t2.name)
    lblSzinit2.pack(side=LEFT, padx=2, pady=3)
    entSzinit2 = Entry(frmSzinit2, width=7)
    entSzinit2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Szinit_t2.name] = entSzinit2

    frmAremis2 = Frame(frmMID)
    frmAremis2.grid(row=3, column=0, sticky=W + E)
    lblAremis2 = Label(frmAremis2, text=constSO.SRCPARAM.Aremis_t2.name)
    lblAremis2.pack(side=LEFT, padx=2, pady=3)
    entAremis2 = Entry(frmAremis2, width=7)
    entAremis2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Aremis_t2.name] = entAremis2

    frmXinit2 = Frame(frmMID)
    frmXinit2.grid(row=3, column=2, sticky=W + E)
    lblXinit2 = Label(frmXinit2, text=constSO.SRCPARAM.Xinit_t2.name)
    lblXinit2.pack(side=LEFT, padx=2, pady=3)
    entXinit2 = Entry(frmXinit2, width=7)
    entXinit2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Xinit_t2.name] = entXinit2

    frmYinit2 = Frame(frmMID)
    frmYinit2.grid(row=3, column=3, sticky=W + E)
    lblYinit2 = Label(frmYinit2, text=constSO.SRCPARAM.Yinit_t2.name)
    lblYinit2.pack(side=LEFT, padx=2, pady=3)
    entYinit2 = Entry(frmYinit2, width=7)
    entYinit2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Yinit_t2.name] = entYinit2

    frmAngle2 = Frame(frmMID)
    frmAngle2.grid(row=3, column=4, sticky=W + E)
    lblAngle2 = Label(frmAngle2, text=constSO.SRCPARAM.Angle_t2.name)
    lblAngle2.pack(side=LEFT, padx=2, pady=3)
    entAngle2 = Entry(frmAngle2, width=7)
    entAngle2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Angle_t2.name] = entAngle2

    frmNverts2 = Frame(frmMID)
    frmNverts2.grid(row=4, column=2, sticky=W + E)
    lblNverts2 = Label(frmNverts2, text=constSO.SRCPARAM.Nverts_t2.name)
    lblNverts2.pack(side=LEFT, padx=2, pady=3)
    entNverts2 = Entry(frmNverts2, width=7)
    entNverts2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Nverts_t2.name] = entNverts2

    frmRadius2 = Frame(frmMID)
    frmRadius2.grid(row=5, column=2, sticky=W + E)
    lblRadius2 = Label(frmRadius2, text=constSO.SRCPARAM.Radius_t2.name)
    lblRadius2.pack(side=LEFT, padx=2, pady=3)
    entRadius2 = Entry(frmRadius2, width=7)
    entRadius2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Radius_t2.name] = entRadius2

    frmLnemis2 = Frame(frmMID)
    frmLnemis2.grid(row=6, column=0, sticky=W + E)
    lblLnemis2 = Label(frmLnemis2, text=constSO.SRCPARAM.Lnemis_t2.name)
    lblLnemis2.pack(side=LEFT, padx=2, pady=3)
    entLnemis2 = Entry(frmLnemis2, width=7)
    entLnemis2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Lnemis_t2.name] = entLnemis2

    frmWidth2 = Frame(frmMID)
    frmWidth2.grid(row=6, column=2, sticky=W + E)
    lblWidth2 = Label(frmWidth2, text=constSO.SRCPARAM.Width_t2.name)
    lblWidth2.pack(side=LEFT, padx=2, pady=3)
    entWidth2 = Entry(frmWidth2, width=7)
    entWidth2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Width_t2.name] = entWidth2

    frmOpemis2 = Frame(frmMID)
    frmOpemis2.grid(row=7, column=0, sticky=W + E)
    lblOpemis2 = Label(frmOpemis2, text=constSO.SRCPARAM.Opemis_t2.name)
    lblOpemis2.pack(side=LEFT, padx=2, pady=3)
    entOpemis2 = Entry(frmOpemis2, width=7)
    entOpemis2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Opemis_t2.name] = entOpemis2

    frmPitvol2 = Frame(frmMID)
    frmPitvol2.grid(row=7, column=4, sticky=W + E)
    lblPitvol2 = Label(frmPitvol2, text=constSO.SRCPARAM.Pitvol_t2.name)
    lblPitvol2.pack(side=LEFT, anchor=W, padx=2, pady=3)
    entPitvol2 = Entry(frmPitvol2, width=7)
    entPitvol2.pack(side=RIGHT, anchor=E, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Pitvol_t2.name] = entPitvol2

    frmBlemis2 = Frame(frmMID)
    frmBlemis2.grid(row=8, column=0, sticky=W + E)
    lblBlemis2 = Label(frmBlemis2, text=constSO.SRCPARAM.Blemis_t2.name)
    lblBlemis2.pack(side=LEFT, padx=2, pady=3)
    entBlemis2 = Entry(frmBlemis2, width=7)
    entBlemis2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Blemis_t2.name] = entBlemis2

    frmQemis2 = Frame(frmMID)
    frmQemis2.grid(row=9, column=0, sticky=W + E)
    lblQemis2 = Label(frmQemis2, text=constSO.SRCPARAM.Qemis_t2.name)
    lblQemis2.pack(side=LEFT, padx=2, pady=3)
    entQemis2 = Entry(frmQemis2, width=7)
    entQemis2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Qemis_t2.name] = entQemis2

    frmDCL2 = Frame(frmMID)
    frmDCL2.grid(row=9, column=1, sticky=W + E)
    lblDCL2 = Label(frmDCL2, text=constSO.SRCPARAM.DCL_t2.name)
    lblDCL2.pack(side=LEFT, padx=2, pady=3)
    entDCL2 = Entry(frmDCL2, width=7)
    entDCL2.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.DCL_t2.name] = entDCL2

    # frmRIGHT SrcID_t3 ================================================================================================
    frmRIGHT = LabelFrame(frm, bd=1, text=constSO.SRCPARAM.SrcID_t3.name)
    frmRIGHT.grid(row=0, column=2)

    frmPtemis3 = Frame(frmRIGHT)
    frmPtemis3.grid(row=1, column=0, sticky=W + E)
    lblPtemis3 = Label(frmPtemis3, text=constSO.SRCPARAM.Ptemis_t3.name)
    lblPtemis3.pack(side=LEFT, padx=2, pady=3)
    entPtemis3 = Entry(frmPtemis3, width=7)
    entPtemis3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Ptemis_t3.name] = entPtemis3

    frmStkhgt3 = Frame(frmRIGHT)
    frmStkhgt3.grid(row=1, column=1, sticky=W + E)
    lblStkhgt3 = Label(frmStkhgt3, text=constSO.SRCPARAM.Stkhgt_t3.name)
    lblStkhgt3.pack(side=LEFT, padx=2, pady=3)
    entStkhgt3 = Entry(frmStkhgt3, width=7)
    entStkhgt3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkhgt_t3.name] = entStkhgt3

    frmStktmp3 = Frame(frmRIGHT)
    frmStktmp3.grid(row=1, column=2, sticky=W + E)
    lblStktmp3 = Label(frmStktmp3, text=constSO.SRCPARAM.Stktmp_t3.name)
    lblStktmp3.pack(side=LEFT, padx=2, pady=3)
    entStktmp3 = Entry(frmStktmp3, width=7)
    entStktmp3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stktmp_t3.name] = entStktmp3

    frmStkvel3 = Frame(frmRIGHT)
    frmStkvel3.grid(row=1, column=3, sticky=W + E)
    lblStkvel3 = Label(frmStkvel3, text=constSO.SRCPARAM.Stkvel_t3.name)
    lblStkvel3.pack(side=LEFT, padx=2, pady=3)
    entStkvel3 = Entry(frmStkvel3, width=7)
    entStkvel3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkvel_t3.name] = entStkvel3

    frmStkdia3 = Frame(frmRIGHT)
    frmStkdia3.grid(row=1, column=4, sticky=W + E)
    lblStkdia3 = Label(frmStkdia3, text=constSO.SRCPARAM.Stkdia_t3.name)
    lblStkdia3.pack(side=LEFT, padx=2, pady=3)
    entStkdia3 = Entry(frmStkdia3, width=7)
    entStkdia3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Stkdia_t3.name] = entStkdia3

    frmVlemis3 = Frame(frmRIGHT)
    frmVlemis3.grid(row=2, column=0, sticky=W + E)
    lblVlemis3 = Label(frmVlemis3, text=constSO.SRCPARAM.Vlemis_t3.name)
    lblVlemis3.pack(side=LEFT, padx=2, pady=3)
    entVlemis3 = Entry(frmVlemis3, width=7)
    entVlemis3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Vlemis_t3.name] = entVlemis3

    frmRelhgt3 = Frame(frmRIGHT)
    frmRelhgt3.grid(row=2, column=1, sticky=W + E)
    lblRelhgt3 = Label(frmRelhgt3, text=constSO.SRCPARAM.Relhgt_t3.name)
    lblRelhgt3.pack(side=LEFT, padx=2, pady=3)
    entRelhgt3 = Entry(frmRelhgt3, width=7)
    entRelhgt3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Relhgt_t3.name] = entRelhgt3

    frmSyinit3 = Frame(frmRIGHT)
    frmSyinit3.grid(row=2, column=2, sticky=W + E)
    lblSyinit3 = Label(frmSyinit3, text=constSO.SRCPARAM.Syinit_t3.name)
    lblSyinit3.pack(side=LEFT, padx=2, pady=3)
    entSyinit3 = Entry(frmSyinit3, width=7)
    entSyinit3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Syinit_t3.name] = entSyinit3

    frmSzinit3 = Frame(frmRIGHT)
    frmSzinit3.grid(row=2, column=3, sticky=W + E)
    lblSzinit3 = Label(frmSzinit3, text=constSO.SRCPARAM.Szinit_t3.name)
    lblSzinit3.pack(side=LEFT, padx=2, pady=3)
    entSzinit3 = Entry(frmSzinit3, width=7)
    entSzinit3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Szinit_t3.name] = entSzinit3

    frmAremis3 = Frame(frmRIGHT)
    frmAremis3.grid(row=3, column=0, sticky=W + E)
    lblAremis3 = Label(frmAremis3, text=constSO.SRCPARAM.Aremis_t3.name)
    lblAremis3.pack(side=LEFT, padx=2, pady=3)
    entAremis3 = Entry(frmAremis3, width=7)
    entAremis3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Aremis_t3.name] = entAremis3

    frmXinit3 = Frame(frmRIGHT)
    frmXinit3.grid(row=3, column=2, sticky=W + E)
    lblXinit3 = Label(frmXinit3, text=constSO.SRCPARAM.Xinit_t3.name)
    lblXinit3.pack(side=LEFT, padx=2, pady=3)
    entXinit3 = Entry(frmXinit3, width=7)
    entXinit3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Xinit_t3.name] = entXinit3

    frmYinit3 = Frame(frmRIGHT)
    frmYinit3.grid(row=3, column=3, sticky=W + E)
    lblYinit3 = Label(frmYinit3, text=constSO.SRCPARAM.Yinit_t3.name)
    lblYinit3.pack(side=LEFT, padx=2, pady=3)
    entYinit3 = Entry(frmYinit3, width=7)
    entYinit3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Yinit_t3.name] = entYinit3

    frmAngle3 = Frame(frmRIGHT)
    frmAngle3.grid(row=3, column=4, sticky=W + E)
    lblAngle3 = Label(frmAngle3, text=constSO.SRCPARAM.Angle_t3.name)
    lblAngle3.pack(side=LEFT, padx=2, pady=3)
    entAngle3 = Entry(frmAngle3, width=7)
    entAngle3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Angle_t3.name] = entAngle3

    frmNverts3 = Frame(frmRIGHT)
    frmNverts3.grid(row=4, column=2, sticky=W + E)
    lblNverts3 = Label(frmNverts3, text=constSO.SRCPARAM.Nverts_t3.name)
    lblNverts3.pack(side=LEFT, padx=2, pady=3)
    entNverts3 = Entry(frmNverts3, width=7)
    entNverts3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Nverts_t3.name] = entNverts3

    frmRadius3 = Frame(frmRIGHT)
    frmRadius3.grid(row=5, column=2, sticky=W + E)
    lblRadius3 = Label(frmRadius3, text=constSO.SRCPARAM.Radius_t3.name)
    lblRadius3.pack(side=LEFT, padx=2, pady=3)
    entRadius3 = Entry(frmRadius3, width=7)
    entRadius3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Radius_t3.name] = entRadius3

    frmLnemis3 = Frame(frmRIGHT)
    frmLnemis3.grid(row=6, column=0, sticky=W + E)
    lblLnemis3 = Label(frmLnemis3, text=constSO.SRCPARAM.Lnemis_t3.name)
    lblLnemis3.pack(side=LEFT, padx=2, pady=3)
    entLnemis3 = Entry(frmLnemis3, width=7)
    entLnemis3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Lnemis_t3.name] = entLnemis3

    frmWidth3 = Frame(frmRIGHT)
    frmWidth3.grid(row=6, column=2, sticky=W + E)
    lblWidth3 = Label(frmWidth3, text=constSO.SRCPARAM.Width_t3.name)
    lblWidth3.pack(side=LEFT, padx=2, pady=3)
    entWidth3 = Entry(frmWidth3, width=7)
    entWidth3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Width_t3.name] = entWidth3

    frmOpemis3 = Frame(frmRIGHT)
    frmOpemis3.grid(row=7, column=0, sticky=W + E)
    lblOpemis3 = Label(frmOpemis3, text=constSO.SRCPARAM.Opemis_t3.name)
    lblOpemis3.pack(side=LEFT, padx=2, pady=3)
    entOpemis3 = Entry(frmOpemis3, width=7)
    entOpemis3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Opemis_t3.name] = entOpemis3

    frmPitvol3 = Frame(frmRIGHT)
    frmPitvol3.grid(row=7, column=4, sticky=W + E)
    lblPitvol3 = Label(frmPitvol3, text=constSO.SRCPARAM.Pitvol_t3.name)
    lblPitvol3.pack(side=LEFT, anchor=W, padx=2, pady=3)
    entPitvol3 = Entry(frmPitvol3, width=7)
    entPitvol3.pack(side=RIGHT, anchor=E, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Pitvol_t3.name] = entPitvol3

    frmBlemis3 = Frame(frmRIGHT)
    frmBlemis3.grid(row=8, column=0, sticky=W + E)
    lblBlemis3 = Label(frmBlemis3, text=constSO.SRCPARAM.Blemis_t3.name)
    lblBlemis3.pack(side=LEFT, padx=2, pady=3)
    entBlemis3 = Entry(frmBlemis3, width=7)
    entBlemis3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Blemis_t3.name] = entBlemis3

    frmQemis3 = Frame(frmRIGHT)
    frmQemis3.grid(row=9, column=0, sticky=W + E)
    lblQemis3 = Label(frmQemis3, text=constSO.SRCPARAM.Qemis_t3.name)
    lblQemis3.pack(side=LEFT, padx=2, pady=3)
    entQemis3 = Entry(frmQemis3, width=7)
    entQemis3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.Qemis_t3.name] = entQemis3

    frmDCL3 = Frame(frmRIGHT)
    frmDCL3.grid(row=9, column=1, sticky=W + E)
    lblDCL3 = Label(frmDCL3, text=constSO.SRCPARAM.DCL_t3.name)
    lblDCL3.pack(side=LEFT, padx=2, pady=3)
    entDCL3 = Entry(frmDCL3, width=7)
    entDCL3.pack(side=RIGHT, padx=2, pady=3)
    srcparamVals[constSO.SRCPARAM.DCL_t3.name] = entDCL3

def makeBUILDHGT(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.BUILDHGT.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblDsbh_t1 = Label(frm1, text=constSO.BUILDHGT.Dsbh_t1.name)
    lblDsbh_t1.pack(side=LEFT, padx=3, pady=3)
    entDsbh_t1 = Entry(frm1, width=200)
    entDsbh_t1.pack(side=LEFT, padx=3, pady=3)
    buildhgtVals[constSO.BUILDHGT.Dsbh_t1.name] = entDsbh_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.BUILDHGT.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblDsbh_t2 = Label(frm2, text=constSO.BUILDHGT.Dsbh_t2.name)
    lblDsbh_t2.pack(side=LEFT, padx=3, pady=3)
    entDsbh_t2 = Entry(frm2, width=200)
    entDsbh_t2.pack(side=LEFT, padx=3, pady=3)
    buildhgtVals[constSO.BUILDHGT.Dsbh_t2.name] = entDsbh_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.BUILDHGT.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblDsbh_t3 = Label(frm3, text=constSO.BUILDHGT.Dsbh_t3.name)
    lblDsbh_t3.pack(side=LEFT, padx=3, pady=3)
    entDsbh_t3 = Entry(frm3, width=200)
    entDsbh_t3.pack(side=LEFT, padx=3, pady=3)
    buildhgtVals[constSO.BUILDHGT.Dsbh_t3.name] = entDsbh_t3

# ======================================================================================================================
def makeBUILDLEN(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.BUILDLEN.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblDsbl_t1 = Label(frm1, text=constSO.BUILDLEN.Dsbl_t1.name)
    lblDsbl_t1.pack(side=LEFT, padx=3, pady=3)
    entDsbl_t1 = Entry(frm1, width=200)
    entDsbl_t1.pack(side=LEFT, padx=3, pady=3)
    buildlenVals[constSO.BUILDLEN.Dsbl_t1.name] = entDsbl_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.BUILDLEN.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblDsbl_t2 = Label(frm2, text=constSO.BUILDLEN.Dsbl_t2.name)
    lblDsbl_t2.pack(side=LEFT, padx=3, pady=3)
    entDsbl_t2 = Entry(frm2, width=200)
    entDsbl_t2.pack(side=LEFT, padx=3, pady=3)
    buildlenVals[constSO.BUILDLEN.Dsbl_t2.name] = entDsbl_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.BUILDLEN.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblDsbl_t3 = Label(frm3, text=constSO.BUILDLEN.Dsbl_t3.name)
    lblDsbl_t3.pack(side=LEFT, padx=3, pady=3)
    entDsbl_t3 = Entry(frm3, width=200)
    entDsbl_t3.pack(side=LEFT, padx=3, pady=3)
    buildlenVals[constSO.BUILDLEN.Dsbl_t3.name] = entDsbl_t3

# ======================================================================================================================
def makeBUILDWID(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.BUILDWID.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblDsbw_t1 = Label(frm1, text=constSO.BUILDWID.Dsbw_t1.name)
    lblDsbw_t1.pack(side=LEFT, padx=3, pady=3)
    entDsbw_t1 = Entry(frm1, width=200)
    entDsbw_t1.pack(side=LEFT, padx=3, pady=3)
    buildwidVals[constSO.BUILDWID.Dsbw_t1.name] = entDsbw_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.BUILDWID.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblDsbw_t2 = Label(frm2, text=constSO.BUILDWID.Dsbw_t2.name)
    lblDsbw_t2.pack(side=LEFT, padx=3, pady=3)
    entDsbw_t2 = Entry(frm2, width=200)
    entDsbw_t2.pack(side=LEFT, padx=3, pady=3)
    buildwidVals[constSO.BUILDWID.Dsbw_t2.name] = entDsbw_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.BUILDWID.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblDsbw_t3 = Label(frm3, text=constSO.BUILDWID.Dsbw_t3.name)
    lblDsbw_t3.pack(side=LEFT, padx=3, pady=3)
    entDsbw_t3 = Entry(frm3, width=200)
    entDsbw_t3.pack(side=LEFT, padx=3, pady=3)
    buildwidVals[constSO.BUILDWID.Dsbw_t3.name] = entDsbw_t3

# ======================================================================================================================
def makeXBADJ(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.XBADJ.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblXbadj_t1 = Label(frm1, text=constSO.XBADJ.Xbadj_t1.name)
    lblXbadj_t1.pack(side=LEFT, padx=3, pady=3)
    entXbadj_t1 = Entry(frm1, width=200)
    entXbadj_t1.pack(side=LEFT, padx=3, pady=3)
    xbadjVals[constSO.XBADJ.Xbadj_t1.name] = entXbadj_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.XBADJ.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblXbadj_t2 = Label(frm2, text=constSO.XBADJ.Xbadj_t2.name)
    lblXbadj_t2.pack(side=LEFT, padx=3, pady=3)
    entXbadj_t2 = Entry(frm2, width=200)
    entXbadj_t2.pack(side=LEFT, padx=3, pady=3)
    xbadjVals[constSO.XBADJ.Xbadj_t2.name] = entXbadj_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.XBADJ.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblXbadj_t3 = Label(frm3, text=constSO.XBADJ.Xbadj_t3.name)
    lblXbadj_t3.pack(side=LEFT, padx=3, pady=3)
    entXbadj_t3 = Entry(frm3, width=200)
    entXbadj_t3.pack(side=LEFT, padx=3, pady=3)
    xbadjVals[constSO.XBADJ.Xbadj_t3.name] = entXbadj_t3

# ======================================================================================================================
def makeYBADJ(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.YBADJ.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblYbadj_t1 = Label(frm1, text=constSO.YBADJ.Ybadj_t1.name)
    lblYbadj_t1.pack(side=LEFT, padx=3, pady=3)
    entYbadj_t1 = Entry(frm1, width=200)
    entYbadj_t1.pack(side=LEFT, padx=3, pady=3)
    ybadjVals[constSO.YBADJ.Ybadj_t1.name] = entYbadj_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.YBADJ.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblYbadj_t2 = Label(frm2, text=constSO.YBADJ.Ybadj_t2.name)
    lblYbadj_t2.pack(side=LEFT, padx=3, pady=3)
    entYbadj_t2 = Entry(frm2, width=200)
    entYbadj_t2.pack(side=LEFT, padx=3, pady=3)
    ybadjVals[constSO.YBADJ.Ybadj_t2.name] = entYbadj_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.YBADJ.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblYbadj_t3 = Label(frm3, text=constSO.YBADJ.Ybadj_t3.name)
    lblYbadj_t3.pack(side=LEFT, padx=3, pady=3)
    entYbadj_t3 = Entry(frm3, width=200)
    entYbadj_t3.pack(side=LEFT, padx=3, pady=3)
    ybadjVals[constSO.YBADJ.Ybadj_t3.name] = entYbadj_t3


# ======================================================================================================================
def makeAREAVERT(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.AREAVERT.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblXYv_t1 = Label(frm1, text=constSO.AREAVERT.XYv_t1.name)
    lblXYv_t1.pack(side=LEFT, padx=3, pady=3)
    entXYv_t1 = Entry(frm1, width=200)
    entXYv_t1.pack(side=LEFT, padx=3, pady=3)
    areavertVals[constSO.AREAVERT.XYv_t1.name] = entXYv_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.AREAVERT.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblXYv_t2 = Label(frm2, text=constSO.AREAVERT.XYv_t2.name)
    lblXYv_t2.pack(side=LEFT, padx=3, pady=3)
    entXYv_t2 = Entry(frm2, width=200)
    entXYv_t2.pack(side=LEFT, padx=3, pady=3)
    areavertVals[constSO.AREAVERT.XYv_t2.name] = entXYv_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.AREAVERT.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblXYv_t3 = Label(frm3, text=constSO.AREAVERT.XYv_t3.name)
    lblXYv_t3.pack(side=LEFT, padx=3, pady=3)
    entXYv_t3 = Entry(frm3, width=200)
    entXYv_t3.pack(side=LEFT, padx=3, pady=3)
    areavertVals[constSO.AREAVERT.XYv_t3.name] = entXYv_t3

# ======================================================================================================================
def makeRBARRIER(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.RBARRIER.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblHtwall_t1 = Label(frm1, text=constSO.RBARRIER.Htwall_t1.name)
    lblHtwall_t1.pack(side=LEFT, padx=3, pady=3)
    entHtwall_t1 = Entry(frm1, width=50)
    entHtwall_t1.pack(side=LEFT, padx=3, pady=3)
    lblDCLwall_t1 = Label(frm1, text=constSO.RBARRIER.DCLwall_t1.name)
    lblDCLwall_t1.pack(side=LEFT, padx=3, pady=3)
    entDCLwall_t1 = Entry(frm1, width=50)
    entDCLwall_t1.pack(side=LEFT, padx=3, pady=3)
    rbarrierVals[constSO.RBARRIER.Htwall_t1.name] = entHtwall_t1
    rbarrierVals[constSO.RBARRIER.DCLwall_t1.name] = entDCLwall_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.RBARRIER.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblHtwall_t2 = Label(frm2, text=constSO.RBARRIER.Htwall_t2.name)
    lblHtwall_t2.pack(side=LEFT, padx=3, pady=3)
    entHtwall_t2 = Entry(frm2, width=50)
    entHtwall_t2.pack(side=LEFT, padx=3, pady=3)
    lblDCLwall_t2 = Label(frm2, text=constSO.RBARRIER.DCLwall_t2.name)
    lblDCLwall_t2.pack(side=LEFT, padx=3, pady=3)
    entDCLwall_t2 = Entry(frm2, width=50)
    entDCLwall_t2.pack(side=LEFT, padx=3, pady=3)
    rbarrierVals[constSO.RBARRIER.Htwall_t2.name] = entHtwall_t2
    rbarrierVals[constSO.RBARRIER.DCLwall_t2.name] = entDCLwall_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.RBARRIER.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblHtwall_t3 = Label(frm3, text=constSO.RBARRIER.Htwall_t3.name)
    lblHtwall_t3.pack(side=LEFT, padx=3, pady=3)
    entHtwall_t3 = Entry(frm3, width=50)
    entHtwall_t3.pack(side=LEFT, padx=3, pady=3)
    lblDCLwall_t3 = Label(frm3, text=constSO.RBARRIER.DCLwall_t3.name)
    lblDCLwall_t3.pack(side=LEFT, padx=3, pady=3)
    entDCLwall_t3 = Entry(frm3, width=50)
    entDCLwall_t3.pack(side=LEFT, padx=3, pady=3)
    rbarrierVals[constSO.RBARRIER.Htwall_t3.name] = entHtwall_t3
    rbarrierVals[constSO.RBARRIER.DCLwall_t3.name] = entDCLwall_t3

# ======================================================================================================================
def makeRDEPRESS(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.RDEPRESS.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblDepth_t1 = Label(frm1, text=constSO.RDEPRESS.Depth_t1.name)
    lblDepth_t1.pack(side=LEFT, padx=3, pady=3)
    entDepth_t1 = Entry(frm1, width=50)
    entDepth_t1.pack(side=LEFT, padx=3, pady=3)
    lblWtop_t1 = Label(frm1, text=constSO.RDEPRESS.Wtop_t1.name)
    lblWtop_t1.pack(side=LEFT, padx=3, pady=3)
    entWtop_t1 = Entry(frm1, width=50)
    entWtop_t1.pack(side=LEFT, padx=3, pady=3)
    lblWbottom_t1 = Label(frm1, text=constSO.RDEPRESS.Wbottom_t1.name)
    lblWbottom_t1.pack(side=LEFT, padx=3, pady=3)
    entWbottom_t1 = Entry(frm1, width=50)
    entWbottom_t1.pack(side=LEFT, padx=3, pady=3)
    rdepressVals[constSO.RDEPRESS.Depth_t1.name] = entDepth_t1
    rdepressVals[constSO.RDEPRESS.Wtop_t1.name] = entWtop_t1
    rdepressVals[constSO.RDEPRESS.Wbottom_t1.name] = entWbottom_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.RDEPRESS.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblDepth_t2 = Label(frm2, text=constSO.RDEPRESS.Depth_t2.name)
    lblDepth_t2.pack(side=LEFT, padx=3, pady=3)
    entDepth_t2 = Entry(frm2, width=50)
    entDepth_t2.pack(side=LEFT, padx=3, pady=3)
    lblWtop_t2 = Label(frm2, text=constSO.RDEPRESS.Wtop_t2.name)
    lblWtop_t2.pack(side=LEFT, padx=3, pady=3)
    entWtop_t2 = Entry(frm2, width=50)
    entWtop_t2.pack(side=LEFT, padx=3, pady=3)
    lblWbottom_t2 = Label(frm2, text=constSO.RDEPRESS.Wbottom_t2.name)
    lblWbottom_t2.pack(side=LEFT, padx=3, pady=3)
    entWbottom_t2 = Entry(frm2, width=50)
    entWbottom_t2.pack(side=LEFT, padx=3, pady=3)
    rdepressVals[constSO.RDEPRESS.Depth_t2.name] = entDepth_t2
    rdepressVals[constSO.RDEPRESS.Wtop_t2.name] = entWtop_t2
    rdepressVals[constSO.RDEPRESS.Wbottom_t2.name] = entWbottom_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.RDEPRESS.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblDepth_t3 = Label(frm3, text=constSO.RDEPRESS.Depth_t3.name)
    lblDepth_t3.pack(side=LEFT, padx=3, pady=3)
    entDepth_t3 = Entry(frm3, width=50)
    entDepth_t3.pack(side=LEFT, padx=3, pady=3)
    lblWtop_t3 = Label(frm3, text=constSO.RDEPRESS.Wtop_t3.name)
    lblWtop_t3.pack(side=LEFT, padx=3, pady=3)
    entWtop_t3 = Entry(frm3, width=50)
    entWtop_t3.pack(side=LEFT, padx=3, pady=3)
    lblWbottom_t3 = Label(frm3, text=constSO.RDEPRESS.Wbottom_t3.name)
    lblWbottom_t3.pack(side=LEFT, padx=3, pady=3)
    entWbottom_t3 = Entry(frm3, width=50)
    entWbottom_t3.pack(side=LEFT, padx=3, pady=3)
    rdepressVals[constSO.RDEPRESS.Depth_t3.name] = entDepth_t3
    rdepressVals[constSO.RDEPRESS.Wtop_t3.name] = entWtop_t3
    rdepressVals[constSO.RDEPRESS.Wbottom_t3.name] = entWbottom_t3

# ======================================================================================================================
def makeURBANSRC(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblUrbanID1= Label(frm1, text=constSO.URBANRSC.UrbanID1.name)
    lblUrbanID1.pack(side=LEFT, padx=3, pady=3)
    entUrbanID1 = Entry(frm1, width=20)
    entUrbanID1.pack(side=LEFT, padx=3,pady=3)
    lblSrcID1 = Label(frm1, text=constSO.URBANRSC.SrcID1.name)
    lblSrcID1.pack(side=LEFT, padx=3,pady=3)
    choices1 = [constSO.LOCATION.SrcID_t1.name, constSO.LOCATION.SrcID_t2.name, constSO.LOCATION.SrcID_t3.name]
    var1 = StringVar()
    var1.set(choices1[0])
    opt1 = OptionMenu(frm1, var1, *choices1)
    opt1.config(width=7)
    opt1.pack(side=LEFT,padx=3,pady=3)
    urbansrcVals[constSO.URBANRSC.UrbanID1.name] = entUrbanID1
    urbansrcVals[constSO.URBANRSC.SrcID1.name] = var1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblUrbanID2= Label(frm2, text=constSO.URBANRSC.UrbanID2.name)
    lblUrbanID2.pack(side=LEFT, padx=3, pady=3)
    entUrbanID2 = Entry(frm2, width=20)
    entUrbanID2.pack(side=LEFT, padx=3,pady=3)
    lblSrcID2 = Label(frm2, text=constSO.URBANRSC.SrcID2.name)
    lblSrcID2.pack(side=LEFT, padx=3,pady=3)
    choices2 = [constSO.LOCATION.SrcID_t1.name, constSO.LOCATION.SrcID_t2.name, constSO.LOCATION.SrcID_t3.name]
    var2 = StringVar()
    var2.set(choices2[0])
    opt2 = OptionMenu(frm2, var2, *choices2)
    opt2.config(width=7)
    opt2.pack(side=LEFT,padx=3,pady=3)
    urbansrcVals[constSO.URBANRSC.UrbanID2.name] = entUrbanID2
    urbansrcVals[constSO.URBANRSC.SrcID2.name] = var2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblUrbanID3= Label(frm3, text=constSO.URBANRSC.UrbanID3.name)
    lblUrbanID3.pack(side=LEFT, padx=3, pady=3)
    entUrbanID3 = Entry(frm3, width=20)
    entUrbanID3.pack(side=LEFT, padx=3,pady=3)
    lblSrcID3 = Label(frm3, text=constSO.URBANRSC.SrcID3.name)
    lblSrcID3.pack(side=LEFT, padx=3,pady=3)
    choices3 = [constSO.LOCATION.SrcID_t1.name, constSO.LOCATION.SrcID_t2.name, constSO.LOCATION.SrcID_t3.name]
    var3 = StringVar()
    var3.set(choices3[0])
    opt3 = OptionMenu(frm3, var3, *choices3)
    opt3.config(width=7)
    opt3.pack(side=LEFT,padx=3,pady=3)
    urbansrcVals[constSO.URBANRSC.UrbanID3.name] = entUrbanID3
    urbansrcVals[constSO.URBANRSC.SrcID3.name] = var3

    frm4 = Frame(frm)
    frm4.pack(side=TOP, anchor=W)
    lblUrbanID4 = Label(frm4, text=constSO.URBANRSC.UrbanID4.name)
    lblUrbanID4.pack(side=LEFT, padx=3, pady=3)
    entUrbanID4 = Entry(frm4, width=20)
    entUrbanID4.pack(side=LEFT, padx=3, pady=3)
    lblSrcID4 = Label(frm4, text=constSO.URBANRSC.SrcID4.name)
    lblSrcID4.pack(side=LEFT, padx=3, pady=3)
    choices4 = [constSO.LOCATION.SrcID_t1.name, constSO.LOCATION.SrcID_t2.name, constSO.LOCATION.SrcID_t3.name]
    var4 = StringVar()
    var4.set(choices4[0])
    opt4 = OptionMenu(frm4, var4, *choices4)
    opt4.config(width=7)
    opt4.pack(side=LEFT, padx=3, pady=3)
    urbansrcVals[constSO.URBANRSC.UrbanID4.name] = entUrbanID4
    urbansrcVals[constSO.URBANRSC.SrcID4.name] = var4

    frm5 = Frame(frm)
    frm5.pack(side=TOP, anchor=W)
    lblUrbanID5 = Label(frm5, text=constSO.URBANRSC.UrbanID5.name)
    lblUrbanID5.pack(side=LEFT, padx=3, pady=3)
    entUrbanID5 = Entry(frm5, width=20)
    entUrbanID5.pack(side=LEFT, padx=3, pady=3)
    lblSrcID5 = Label(frm5, text=constSO.URBANRSC.SrcID5.name)
    lblSrcID5.pack(side=LEFT, padx=3, pady=3)
    choices5 = [constSO.LOCATION.SrcID_t1.name, constSO.LOCATION.SrcID_t2.name, constSO.LOCATION.SrcID_t3.name]
    var5 = StringVar()
    var5.set(choices4[0])
    opt5 = OptionMenu(frm5, var5, *choices5)
    opt5.config(width=7)
    opt5.pack(side=LEFT, padx=3, pady=3)
    urbansrcVals[constSO.URBANRSC.UrbanID5.name] = entUrbanID5
    urbansrcVals[constSO.URBANRSC.SrcID5.name] = var5


def makeEMISFACT(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.EMISFACT.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    choices1 = constSO.EMISFLAG.getListEMISFLAG()
    var1 = StringVar()
    var1.set(choices1[0])
    opt1 = OptionMenu(frm1, var1, *choices1)
    opt1.config(width=8)
    opt1.pack(side=LEFT, padx=3, pady=3)
    lblQfact_t1 = Label(frm1, text=constSO.EMISFACT.Qfact_t1.name)
    lblQfact_t1.pack(side=LEFT, padx=3, pady=3)
    entQfact_t1 = Entry(frm1, width=200)
    entQfact_t1.pack(side=LEFT, padx=3, pady=3)
    emisfactVals[constSO.EMISFACT.Qflag_t1.name] = var1
    emisfactVals[constSO.EMISFACT.Qfact_t1.name] = entQfact_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.EMISFACT.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    choices2 = constSO.EMISFLAG.getListEMISFLAG()
    var2 = StringVar()
    var2.set(choices2[0])
    opt2 = OptionMenu(frm2, var2, *choices2)
    opt2.config(width=8)
    opt2.pack(side=LEFT, padx=3, pady=3)
    lblQfact_t2 = Label(frm2, text=constSO.EMISFACT.Qfact_t2.name)
    lblQfact_t2.pack(side=LEFT, padx=3, pady=3)
    entQfact_t2 = Entry(frm2, width=200)
    entQfact_t2.pack(side=LEFT, padx=3, pady=3)
    emisfactVals[constSO.EMISFACT.Qflag_t2.name] = var2
    emisfactVals[constSO.EMISFACT.Qfact_t2.name] = entQfact_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.EMISFACT.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    choices3 = constSO.EMISFLAG.getListEMISFLAG()
    var3 = StringVar()
    var3.set(choices3[0])
    opt3 = OptionMenu(frm3, var3, *choices3)
    opt3.config(width=8)
    opt3.pack(side=LEFT, padx=3, pady=3)
    lblQfact_t3 = Label(frm3, text=constSO.EMISFACT.Qfact_t3.name)
    lblQfact_t3.pack(side=LEFT, padx=3, pady=3)
    entQfact_t3 = Entry(frm3, width=200)
    entQfact_t3.pack(side=LEFT, padx=3, pady=3)
    emisfactVals[constSO.EMISFACT.Qflag_t3.name] = var3
    emisfactVals[constSO.EMISFACT.Qfact_t3.name] = entQfact_t3

# ======================================================================================================================
def makeEMISUNIT(frm):
    lblEmifac = Label(frm, text=constSO.EMISUNIT.Emifac.name)
    lblEmifac.pack(side=LEFT, padx=3, pady=3)
    entEmifac = Entry(frm, width=50)
    entEmifac.pack(side=LEFT, padx=3, pady=3)

    lblEmilbl = Label(frm, text=constSO.EMISUNIT.Emilbl.name)
    lblEmilbl.pack(side=LEFT, padx=3, pady=3)
    entEmilbl = Entry(frm, width=50)
    entEmilbl.pack(side=LEFT, padx=3, pady=3)

    lblOutlbl = Label(frm, text=constSO.EMISUNIT.Outlbl.name)
    lblOutlbl.pack(side=LEFT, padx=3, pady=3)
    entOutlbl = Entry(frm, width=50)
    entOutlbl.pack(side=LEFT, padx=3, pady=3)

    emisunitVals[constSO.EMISUNIT.Emifac.name] = entEmifac
    emisunitVals[constSO.EMISUNIT.Emilbl.name] = entEmilbl
    emisunitVals[constSO.EMISUNIT.Outlbl.name] = entOutlbl

# ======================================================================================================================
def makeRLEMCONV(frm):
    chkRLEM = BooleanVar()
    chkRLEM.set(False)
    chkbtnRLEM = Checkbutton(frm, text=constSO.RLEMCONV.RLEMCONV.name, var=chkRLEM)
    chkbtnRLEM.pack(side=LEFT, padx=3, pady=3)
    rlemconvVals[constSO.RLEMCONV.RLEMCONV.name] =chkRLEM

# ======================================================================================================================
def makeCONCUNIT(frm):
    lblEmifac = Label(frm, text=constSO.CONCUNIT.Emifac.name)
    lblEmifac.pack(side=LEFT, padx=3, pady=3)
    entEmifac = Entry(frm, width=50)
    entEmifac.pack(side=LEFT, padx=3, pady=3)

    lblEmilbl = Label(frm, text=constSO.CONCUNIT.Emilbl.name)
    lblEmilbl.pack(side=LEFT, padx=3, pady=3)
    entEmilbl = Entry(frm, width=50)
    entEmilbl.pack(side=LEFT, padx=3, pady=3)

    lblConlbl = Label(frm, text=constSO.CONCUNIT.Conlbl.name)
    lblConlbl.pack(side=LEFT, padx=3, pady=3)
    entConlbl = Entry(frm, width=50)
    entConlbl.pack(side=LEFT, padx=3, pady=3)

    concunitVals[constSO.CONCUNIT.Emifac.name] = entEmifac
    concunitVals[constSO.CONCUNIT.Emilbl.name] = entEmilbl
    concunitVals[constSO.CONCUNIT.Conlbl.name] = entConlbl

# ======================================================================================================================
def makeDEPOUNIT(frm):
    lblEmifac = Label(frm, text=constSO.DEPOUNIT.Emifac.name)
    lblEmifac.pack(side=LEFT, padx=3, pady=3)
    entEmifac = Entry(frm, width=50)
    entEmifac.pack(side=LEFT, padx=3, pady=3)

    lblEmilbl = Label(frm, text=constSO.DEPOUNIT.Emilbl.name)
    lblEmilbl.pack(side=LEFT, padx=3, pady=3)
    entEmilbl = Entry(frm, width=50)
    entEmilbl.pack(side=LEFT, padx=3, pady=3)

    lblDeplbl = Label(frm, text=constSO.DEPOUNIT.Deplbl.name)
    lblDeplbl.pack(side=LEFT, padx=3, pady=3)
    entDeplbl = Entry(frm, width=50)
    entDeplbl.pack(side=LEFT, padx=3, pady=3)

    depounitVals[constSO.CONCUNIT.Emifac.name] = entEmifac
    depounitVals[constSO.CONCUNIT.Emilbl.name] = entEmilbl
    depounitVals[constSO.DEPOUNIT.Deplbl.name] = entDeplbl

# ======================================================================================================================
def makePARTDIAM(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.PARTDIAM.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblPdiam_t1 = Label(frm1, text=constSO.PARTDIAM.Pdiam_t1.name)
    lblPdiam_t1.pack(side=LEFT, padx=3, pady=3)
    entPdiam_t1 = Entry(frm1, width=200)
    entPdiam_t1.pack(side=LEFT, padx=3, pady=3)
    partdiamVals[constSO.PARTDIAM.Pdiam_t1.name] = entPdiam_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.PARTDIAM.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblPdiam_t2 = Label(frm2, text=constSO.PARTDIAM.Pdiam_t2.name)
    lblPdiam_t2.pack(side=LEFT, padx=3, pady=3)
    entPdiam_t2 = Entry(frm2, width=200)
    entPdiam_t2.pack(side=LEFT, padx=3, pady=3)
    partdiamVals[constSO.PARTDIAM.Pdiam_t2.name] = entPdiam_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.PARTDIAM.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblPdiam_t3 = Label(frm3, text=constSO.PARTDIAM.Pdiam_t3.name)
    lblPdiam_t3.pack(side=LEFT, padx=3, pady=3)
    entPdiam_t3 = Entry(frm3, width=200)
    entPdiam_t3.pack(side=LEFT, padx=3, pady=3)
    partdiamVals[constSO.PARTDIAM.Pdiam_t3.name] = entPdiam_t3

# ======================================================================================================================
def makeMASSFRAX(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.MASSFRAX.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblPhi_t1 = Label(frm1, text=constSO.MASSFRAX.Phi_t1.name)
    lblPhi_t1.pack(side=LEFT, padx=3, pady=3)
    entPhi_t1 = Entry(frm1, width=200)
    entPhi_t1.pack(side=LEFT, padx=3, pady=3)
    massfraxVals[constSO.MASSFRAX.Phi_t1.name] = entPhi_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.MASSFRAX.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblPhi_t2 = Label(frm2, text=constSO.MASSFRAX.Phi_t2.name)
    lblPhi_t2.pack(side=LEFT, padx=3, pady=3)
    entPhi_t2 = Entry(frm2, width=200)
    entPhi_t2.pack(side=LEFT, padx=3, pady=3)
    massfraxVals[constSO.MASSFRAX.Phi_t2.name] = entPhi_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.MASSFRAX.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblPhi_t3 = Label(frm3, text=constSO.MASSFRAX.Phi_t3.name)
    lblPhi_t3.pack(side=LEFT, padx=3, pady=3)
    entPhi_t3 = Entry(frm3, width=200)
    entPhi_t3.pack(side=LEFT, padx=3, pady=3)
    massfraxVals[constSO.MASSFRAX.Phi_t3.name] = entPhi_t3

# ======================================================================================================================
def makePARTDENS(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.PARTDENS.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblPdens_t1 = Label(frm1, text=constSO.PARTDENS.Pdens_t1.name)
    lblPdens_t1.pack(side=LEFT, padx=3, pady=3)
    entPdens_t1 = Entry(frm1, width=200)
    entPdens_t1.pack(side=LEFT, padx=3, pady=3)
    partdensVals[constSO.PARTDENS.Pdens_t1.name] = entPdens_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.PARTDENS.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblPdens_t2 = Label(frm2, text=constSO.PARTDENS.Pdens_t2.name)
    lblPdens_t2.pack(side=LEFT, padx=3, pady=3)
    entPdens_t2 = Entry(frm2, width=200)
    entPdens_t2.pack(side=LEFT, padx=3, pady=3)
    partdensVals[constSO.PARTDENS.Pdens_t2.name] = entPdens_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.PARTDENS.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblPdens_t3 = Label(frm3, text=constSO.PARTDENS.Pdens_t3.name)
    lblPdens_t3.pack(side=LEFT, padx=3, pady=3)
    entPdens_t3 = Entry(frm3, width=200)
    entPdens_t3.pack(side=LEFT, padx=3, pady=3)
    partdensVals[constSO.PARTDENS.Pdens_t3.name] = entPdens_t3

# ======================================================================================================================
def makeMETHOD_2(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.METHOD_2.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblFMF_t1 = Label(frm1, text=constSO.METHOD_2.FineMassFraction_t1.name)
    lblFMF_t1.pack(side=LEFT, padx=3, pady=3)
    entFMF_t1 = Entry(frm1, width=50)
    entFMF_t1.pack(side=LEFT, padx=3, pady=3)
    lblDmm_t1 = Label(frm1, text=constSO.METHOD_2.Dmm_t1.name)
    lblDmm_t1.pack(side=LEFT, padx=3, pady=3)
    entDmm_t1 = Entry(frm1, width=50)
    entDmm_t1.pack(side=LEFT, padx=3, pady=3)
    method_2Vals[constSO.METHOD_2.FineMassFraction_t1.name] = entFMF_t1
    method_2Vals[constSO.METHOD_2.Dmm_t1.name] = entDmm_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.METHOD_2.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblFMF_t2 = Label(frm2, text=constSO.METHOD_2.FineMassFraction_t2.name)
    lblFMF_t2.pack(side=LEFT, padx=3, pady=3)
    entFMF_t2 = Entry(frm2, width=50)
    entFMF_t2.pack(side=LEFT, padx=3, pady=3)
    lblDmm_t2 = Label(frm2, text=constSO.METHOD_2.Dmm_t2.name)
    lblDmm_t2.pack(side=LEFT, padx=3, pady=3)
    entDmm_t2 = Entry(frm2, width=50)
    entDmm_t2.pack(side=LEFT, padx=3, pady=3)
    method_2Vals[constSO.METHOD_2.FineMassFraction_t2.name] = entFMF_t2
    method_2Vals[constSO.METHOD_2.Dmm_t2.name] = entDmm_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.METHOD_2.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblFMF_t3 = Label(frm3, text=constSO.METHOD_2.FineMassFraction_t3.name)
    lblFMF_t3.pack(side=LEFT, padx=3, pady=3)
    entFMF_t3 = Entry(frm3, width=50)
    entFMF_t3.pack(side=LEFT, padx=3, pady=3)
    lblDmm_t3 = Label(frm3, text=constSO.METHOD_2.Dmm_t2.name)
    lblDmm_t3.pack(side=LEFT, padx=3, pady=3)
    entDmm_t3 = Entry(frm3, width=50)
    entDmm_t3.pack(side=LEFT, padx=3, pady=3)
    method_2Vals[constSO.METHOD_2.FineMassFraction_t3.name] = entFMF_t3
    method_2Vals[constSO.METHOD_2.Dmm_t3.name] = entDmm_t3

# ======================================================================================================================
def makeGASDEPOS(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.GASDEPOS.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblDa_t1 = Label(frm1, text=constSO.GASDEPOS.Da_t1.name)
    lblDa_t1.pack(side=LEFT, padx=3, pady=3)
    entDa_t1 = Entry(frm1, width=50)
    entDa_t1.pack(side=LEFT, padx=3, pady=3)
    lblDw_t1 = Label(frm1, text=constSO.GASDEPOS.Dw_t1.name)
    lblDw_t1.pack(side=LEFT, padx=3, pady=3)
    entDw_t1 = Entry(frm1, width=50)
    entDw_t1.pack(side=LEFT, padx=3, pady=3)
    lblrcl_t1 = Label(frm1, text=constSO.GASDEPOS.rcl_t1.name)
    lblrcl_t1.pack(side=LEFT, padx=3, pady=3)
    entrcl_t1 = Entry(frm1, width=50)
    entrcl_t1.pack(side=LEFT, padx=3, pady=3)
    lblHenry_t1 = Label(frm1, text=constSO.GASDEPOS.Henry_t1.name)
    lblHenry_t1.pack(side=LEFT, padx=3, pady=3)
    entHenry_t1 = Entry(frm1, width=50)
    entHenry_t1.pack(side=LEFT, padx=3, pady=3)
    gasdeposVals[constSO.GASDEPOS.Da_t1.name] = entDa_t1
    gasdeposVals[constSO.GASDEPOS.Dw_t1.name] = entDw_t1
    gasdeposVals[constSO.GASDEPOS.rcl_t1.name] = entrcl_t1
    gasdeposVals[constSO.GASDEPOS.Henry_t1.name] = entHenry_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.GASDEPOS.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblDa_t2 = Label(frm2, text=constSO.GASDEPOS.Da_t2.name)
    lblDa_t2.pack(side=LEFT, padx=3, pady=3)
    entDa_t2 = Entry(frm2, width=50)
    entDa_t2.pack(side=LEFT, padx=3, pady=3)
    lblDw_t2 = Label(frm2, text=constSO.GASDEPOS.Dw_t2.name)
    lblDw_t2.pack(side=LEFT, padx=3, pady=3)
    entDw_t2 = Entry(frm2, width=50)
    entDw_t2.pack(side=LEFT, padx=3, pady=3)
    lblrcl_t2 = Label(frm2, text=constSO.GASDEPOS.rcl_t2.name)
    lblrcl_t2.pack(side=LEFT, padx=3, pady=3)
    entrcl_t2 = Entry(frm2, width=50)
    entrcl_t2.pack(side=LEFT, padx=3, pady=3)
    lblHenry_t2 = Label(frm2, text=constSO.GASDEPOS.Henry_t2.name)
    lblHenry_t2.pack(side=LEFT, padx=3, pady=3)
    entHenry_t2 = Entry(frm2, width=50)
    entHenry_t2.pack(side=LEFT, padx=3, pady=3)
    gasdeposVals[constSO.GASDEPOS.Da_t2.name] = entDa_t2
    gasdeposVals[constSO.GASDEPOS.Dw_t2.name] = entDw_t2
    gasdeposVals[constSO.GASDEPOS.rcl_t2.name] = entrcl_t2
    gasdeposVals[constSO.GASDEPOS.Henry_t2.name] = entHenry_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.GASDEPOS.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblDa_t3 = Label(frm3, text=constSO.GASDEPOS.Da_t3.name)
    lblDa_t3.pack(side=LEFT, padx=3, pady=3)
    entDa_t3 = Entry(frm3, width=50)
    entDa_t3.pack(side=LEFT, padx=3, pady=3)
    lblDw_t3 = Label(frm3, text=constSO.GASDEPOS.Dw_t3.name)
    lblDw_t3.pack(side=LEFT, padx=3, pady=3)
    entDw_t3 = Entry(frm3, width=50)
    entDw_t3.pack(side=LEFT, padx=3, pady=3)
    lblrcl_t3 = Label(frm3, text=constSO.GASDEPOS.rcl_t3.name)
    lblrcl_t3.pack(side=LEFT, padx=3, pady=3)
    entrcl_t3 = Entry(frm3, width=50)
    entrcl_t3.pack(side=LEFT, padx=3, pady=3)
    lblHenry_t3 = Label(frm3, text=constSO.GASDEPOS.Henry_t3.name)
    lblHenry_t3.pack(side=LEFT, padx=3, pady=3)
    entHenry_t3 = Entry(frm3, width=50)
    entHenry_t3.pack(side=LEFT, padx=3, pady=3)
    gasdeposVals[constSO.GASDEPOS.Da_t3.name] = entDa_t3
    gasdeposVals[constSO.GASDEPOS.Dw_t3.name] = entDw_t3
    gasdeposVals[constSO.GASDEPOS.rcl_t3.name] = entrcl_t3
    gasdeposVals[constSO.GASDEPOS.Henry_t3.name] = entHenry_t3

# ======================================================================================================================
def makeNO2RATIO(frm):
    frm1 = Frame(frm)
    frm1.pack(side=TOP, anchor=W)
    lblSrcID_t1 = Label(frm1, text=constSO.NO2RATIO.SrcID_t1.name)
    lblSrcID_t1.pack(side=LEFT, padx=3, pady=3)
    lblNO2Ratio_t1 = Label(frm1, text=constSO.NO2RATIO.NO2Ratio_t1.name)
    lblNO2Ratio_t1.pack(side=LEFT, padx=3, pady=3)
    entNo2Ratio_t1 = Entry(frm1, width=50)
    entNo2Ratio_t1.pack(side=LEFT, padx=3, pady=3)
    no2ratioVals[constSO.NO2RATIO.NO2Ratio_t1.name] = entNo2Ratio_t1

    frm2 = Frame(frm)
    frm2.pack(side=TOP, anchor=W)
    lblSrcID_t2 = Label(frm2, text=constSO.NO2RATIO.SrcID_t2.name)
    lblSrcID_t2.pack(side=LEFT, padx=3, pady=3)
    lblNO2Ratio_t2 = Label(frm2, text=constSO.NO2RATIO.NO2Ratio_t2.name)
    lblNO2Ratio_t2.pack(side=LEFT, padx=3, pady=3)
    entNo2Ratio_t2 = Entry(frm2, width=50)
    entNo2Ratio_t2.pack(side=LEFT, padx=3, pady=3)
    no2ratioVals[constSO.NO2RATIO.NO2Ratio_t2.name] = entNo2Ratio_t2

    frm3 = Frame(frm)
    frm3.pack(side=TOP, anchor=W)
    lblSrcID_t3 = Label(frm3, text=constSO.NO2RATIO.SrcID_t3.name)
    lblSrcID_t3.pack(side=LEFT, padx=3, pady=3)
    lblNO2Ratio_t3 = Label(frm3, text=constSO.NO2RATIO.NO2Ratio_t3.name)
    lblNO2Ratio_t3.pack(side=LEFT, padx=3, pady=3)
    entNo2Ratio_t3 = Entry(frm3, width=50)
    entNo2Ratio_t3.pack(side=LEFT, padx=3, pady=3)
    no2ratioVals[constSO.NO2RATIO.NO2Ratio_t3.name] = entNo2Ratio_t3

# ======================================================================================================================
def makeHOUREMIS(frm):
    chkSrcID_t1 = BooleanVar()
    chkSrcID_t1.set(False)
    chkbtnSrcID_t1 = Checkbutton(frm, text=constSO.HOUREMIS.SrcID_t1.name, var=chkSrcID_t1)
    chkbtnSrcID_t1.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t2 = BooleanVar()
    chkSrcID_t2.set(False)
    chkbtnSrcID_t2 = Checkbutton(frm, text=constSO.HOUREMIS.SrcID_t2.name, var=chkSrcID_t2)
    chkbtnSrcID_t2.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t3 = BooleanVar()
    chkSrcID_t3.set(False)
    chkbtnSrcID_t3 = Checkbutton(frm, text=constSO.HOUREMIS.SrcID_t3.name, var=chkSrcID_t3)
    chkbtnSrcID_t3.pack(side=LEFT, padx=3, pady=3)

    lblFil = Label(frm, text=constSO.HOUREMIS.Emifil.name)
    lblFil.pack(side=LEFT, padx=3, pady=3)
    entFil = Entry(frm, width=100)
    entFil.pack(side=LEFT, padx=3, pady=3)

    houremisVals[constSO.HOUREMIS.SrcID_t1.name] = chkSrcID_t1
    houremisVals[constSO.HOUREMIS.SrcID_t2.name] = chkSrcID_t2
    houremisVals[constSO.HOUREMIS.SrcID_t3.name] = chkSrcID_t3
    houremisVals[constSO.HOUREMIS.Emifil.name] = entFil

# ======================================================================================================================
def makeBGSECTOR(frm):
    lblSect1 = Label(frm, text=constSO.BGSECTOR.StartSect1.name)
    lblSect1.pack(side=LEFT, padx=3, pady=3)
    entSect1 = Entry(frm, width=20)
    entSect1.pack(side=LEFT, padx=3, pady=3)
    bgsectorVals[constSO.BGSECTOR.StartSect1.name] = entSect1

    lblSect2 = Label(frm, text=constSO.BGSECTOR.StartSect2.name)
    lblSect2.pack(side=LEFT, padx=3, pady=3)
    entSect2 = Entry(frm, width=20)
    entSect2.pack(side=LEFT, padx=3, pady=3)
    bgsectorVals[constSO.BGSECTOR.StartSect2.name] = entSect2

    lblSect3 = Label(frm, text=constSO.BGSECTOR.StartSect3.name)
    lblSect3.pack(side=LEFT, padx=3, pady=3)
    entSect3 = Entry(frm, width=20)
    entSect3.pack(side=LEFT, padx=3, pady=3)
    bgsectorVals[constSO.BGSECTOR.StartSect3.name] = entSect3

    lblSect4 = Label(frm, text=constSO.BGSECTOR.StartSect4.name)
    lblSect4.pack(side=LEFT, padx=3, pady=3)
    entSect4 = Entry(frm, width=20)
    entSect4.pack(side=LEFT, padx=3, pady=3)
    bgsectorVals[constSO.BGSECTOR.StartSect4.name] = entSect4

    lblSect5 = Label(frm, text=constSO.BGSECTOR.StartSect5.name)
    lblSect5.pack(side=LEFT, padx=3, pady=3)
    entSect5 = Entry(frm, width=20)
    entSect5.pack(side=LEFT, padx=3, pady=3)
    bgsectorVals[constSO.BGSECTOR.StartSect5.name] = entSect5

    lblSect6 = Label(frm, text=constSO.BGSECTOR.StartSect6.name)
    lblSect6.pack(side=LEFT, padx=3, pady=3)
    entSect6 = Entry(frm, width=20)
    entSect6.pack(side=LEFT, padx=3, pady=3)
    bgsectorVals[constSO.BGSECTOR.StartSect6.name] = entSect6

# ======================================================================================================================
def makeBACKGRND(frm):
    frm1 = Frame(frm)
    frm1.grid(row=0, column=0, sticky=W+E)
    lblBGflag = Label(frm1, text=constSO.BACKGRND.BGflag.name)
    lblBGflag.pack(side=LEFT, padx=3, pady=3)
    flagChoices = constSO.BGFLAG.getListBGFLAG()
    var = StringVar()
    var.set(flagChoices[0])
    optFlag = OptionMenu(frm1, var, *flagChoices)
    optFlag.pack(side=LEFT, padx=3, pady=3)
    backgrndVals[constSO.BACKGRND.BGflag.name] = var

    lblBGvalue = Label(frm1, text=constSO.BACKGRND.BGvalue.name)
    lblBGvalue.pack(side=LEFT, padx=3, pady=3)
    entBGvalue = Entry(frm1, width=100)
    entBGvalue.pack(side=LEFT, padx=3, pady=3)
    backgrndVals[constSO.BACKGRND.BGvalue.name] = entBGvalue

    frm2 = Frame(frm)
    frm2.grid(row=1, column=0, sticky=W+E)
    lblAndOr = Label(frm2, text='and/or', width=20)
    lblAndOr.pack(side=LEFT, padx=3, pady=3)

    frm3 = Frame(frm)
    frm3.grid(row=2, column=0, sticky=W + E)
    chkHOURLY = BooleanVar()
    chkHOURLY.set(False)
    chkbtnHOURLY = Checkbutton(frm3, text=constSO.BACKGRND.HOURLY.name, var=chkHOURLY)
    chkbtnHOURLY.pack(side=LEFT, padx=3, pady=3)
    backgrndVals[constSO.BACKGRND.HOURLY.name] = chkHOURLY

    lblBGfilnam = Label(frm3, text=constSO.BACKGRND.BGfilnam.name)
    lblBGfilnam.pack(side=LEFT, padx=3, pady=3)
    entBGfilnam = Entry(frm3, width=100)
    entBGfilnam.pack(side=LEFT, padx=3, pady=3)
    backgrndVals[constSO.BACKGRND.BGfilnam.name] = entBGfilnam

    lblBGformat = Label(frm3, text=constSO.BACKGRND.BGformat.name)
    lblBGformat.pack(side=LEFT, padx=3, pady=3)
    entBGformat = Entry(frm3, width=20)
    entBGformat.pack(side=LEFT, padx=3, pady=3)
    backgrndVals[constSO.BACKGRND.BGformat.name] = entBGformat

# ======================================================================================================================
def makeBACKUNIT(frm):
    lbl = Label(frm, text=constSO.BACKUNIT.BGunits.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    choices = ['PPB', 'PPM', 'UG/M3']
    var = StringVar()
    var.set(choices[0])
    opt = OptionMenu(frm, var, *choices)
    opt.pack(side=LEFT, padx=3, pady=3)
    backunitVals[constSO.BACKUNIT.BGunits.name] = var

# ======================================================================================================================
def makeINCLUDED(frm):
    lbl = Label(frm, text=constSO.INCLUDED.Incfil.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=100)
    ent.pack(side=LEFT, padx=3, pady=3)
    includedVals[constSO.INCLUDED.Incfil.name] = ent

# ======================================================================================================================
def makeOLMGROUP(frm):
    frm1 = Frame(frm)
    frm1.grid(row=0, column=0, sticky=W+E)

    radbtnVar = IntVar()

    radbtnGrpID = Radiobutton(frm1, text=constSO.OLMGROUP.OLMGrpID.name, var=radbtnVar, value=1)
    radbtnGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm1, width=20)
    entGrpID.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t1 = BooleanVar()
    chkSrcID_t1.set(False)
    chkbtnSrcID_t1 = Checkbutton(frm1, text=constSO.OLMGROUP.SrcID_t1.name, var=chkSrcID_t1)
    chkbtnSrcID_t1.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t2 = BooleanVar()
    chkSrcID_t2.set(False)
    chkbtnSrcID_t2 = Checkbutton(frm1, text=constSO.OLMGROUP.SrcID_t2.name, var=chkSrcID_t2)
    chkbtnSrcID_t2.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t3 = BooleanVar()
    chkSrcID_t3.set(False)
    chkbtnSrcID_t3 = Checkbutton(frm1, text=constSO.OLMGROUP.SrcID_t3.name, var=chkSrcID_t3)
    chkbtnSrcID_t3.pack(side=LEFT, padx=3, pady=3)

    frm2 = Frame(frm)
    frm2.grid(row=1, column=0, sticky=W+E)
    lblAndOr = Label(frm2, text='and/or')
    lblAndOr.pack(side=LEFT, padx=3, pady=3)

    frm3 = Frame(frm)
    frm3.grid(row=2, column=0, sticky=W+E)
    radbtnGrpID = Radiobutton(frm3, text=constSO.OLMGROUP.ALL.name, var=radbtnVar, value=2)
    radbtnGrpID.pack(side=LEFT, padx=3, pady=3)

    olmgroupVals['radbtnVar'] = radbtnVar
    olmgroupVals[constSO.OLMGROUP.OLMGrpID.name] = entGrpID
    olmgroupVals[constSO.OLMGROUP.SrcID_t1.name] = chkSrcID_t1
    olmgroupVals[constSO.OLMGROUP.SrcID_t2.name] = chkSrcID_t2
    olmgroupVals[constSO.OLMGROUP.SrcID_t3.name] = chkSrcID_t3

# ======================================================================================================================
def makePSDGROUP(frm):
    lbl = Label(frm, text=constSO.PSDGROUP.PSDGrpID.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    choices = ['INCRCONS', 'NONRBASE', 'RETRBASE']
    var = StringVar()
    var.set(choices[0])
    opt = OptionMenu(frm, var, *choices)
    opt.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t1 = BooleanVar()
    chkSrcID_t1.set(False)
    chkbtnSrcID_t1 = Checkbutton(frm, text=constSO.PSDGROUP.SrcID_t1.name, var=chkSrcID_t1)
    chkbtnSrcID_t1.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t2 = BooleanVar()
    chkSrcID_t2.set(False)
    chkbtnSrcID_t2 = Checkbutton(frm, text=constSO.PSDGROUP.SrcID_t2.name, var=chkSrcID_t2)
    chkbtnSrcID_t2.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t3 = BooleanVar()
    chkSrcID_t3.set(False)
    chkbtnSrcID_t3 = Checkbutton(frm, text=constSO.PSDGROUP.SrcID_t3.name, var=chkSrcID_t3)
    chkbtnSrcID_t3.pack(side=LEFT, padx=3, pady=3)

    psdgroupVals[constSO.PSDGROUP.PSDGrpID.name] = var
    psdgroupVals[constSO.PSDGROUP.SrcID_t1.name] = chkSrcID_t1
    psdgroupVals[constSO.PSDGROUP.SrcID_t2.name] = chkSrcID_t2
    psdgroupVals[constSO.PSDGROUP.SrcID_t3.name] = chkSrcID_t3

# ======================================================================================================================
def makeSRCGROUP(frm):
    frm1 = Frame(frm)
    frm1.grid(row=0, column=0, sticky=W + E)

    radbtnVar = IntVar()

    radbtnGrpID = Radiobutton(frm1, text=constSO.SRCGROUP.SrcGrpID.name, var=radbtnVar, value=1)
    radbtnGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm1, width=20)
    entGrpID.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t1 = BooleanVar()
    chkSrcID_t1.set(False)
    chkbtnSrcID_t1 = Checkbutton(frm1, text=constSO.SRCGROUP.SrcID_t1.name, var=chkSrcID_t1)
    chkbtnSrcID_t1.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t2 = BooleanVar()
    chkSrcID_t2.set(False)
    chkbtnSrcID_t2 = Checkbutton(frm1, text=constSO.SRCGROUP.SrcID_t2.name, var=chkSrcID_t2)
    chkbtnSrcID_t2.pack(side=LEFT, padx=3, pady=3)

    chkSrcID_t3 = BooleanVar()
    chkSrcID_t3.set(False)
    chkbtnSrcID_t3 = Checkbutton(frm1, text=constSO.SRCGROUP.SrcID_t3.name, var=chkSrcID_t3)
    chkbtnSrcID_t3.pack(side=LEFT, padx=3, pady=3)

    frm2 = Frame(frm)
    frm2.grid(row=1, column=0, sticky=W + E)
    lblAndOr = Label(frm2, text='and/or')
    lblAndOr.pack(side=LEFT, padx=3, pady=3)

    frm3 = Frame(frm)
    frm3.grid(row=2, column=0, sticky=W + E)
    radbtnGrpID = Radiobutton(frm3, text=constSO.SRCGROUP.ALL.name, var=radbtnVar, value=2)
    radbtnGrpID.pack(side=LEFT, padx=3, pady=3)

    srcgroupVals['radbtnVar'] = radbtnVar
    srcgroupVals[constSO.SRCGROUP.SrcGrpID.name] = entGrpID
    srcgroupVals[constSO.SRCGROUP.SrcID_t1.name] = chkSrcID_t1
    srcgroupVals[constSO.SRCGROUP.SrcID_t2.name] = chkSrcID_t2
    srcgroupVals[constSO.SRCGROUP.SrcID_t3.name] = chkSrcID_t3

# ======================================================================================================================
elevunitVals = {}
locationVals = {}
srcparamVals = {}
buildhgtVals = {}
buildlenVals = {}
buildwidVals = {}
xbadjVals = {}
ybadjVals = {}
areavertVals = {}
rbarrierVals = {}
rdepressVals = {}
urbansrcVals = {}
emisfactVals = {}
emisunitVals = {}
rlemconvVals = {}
concunitVals = {}
depounitVals = {}
partdiamVals = {}
massfraxVals = {}
partdensVals = {}
method_2Vals = {}
gasdeposVals = {}
no2ratioVals = {}
houremisVals = {}
bgsectorVals = {}
backgrndVals = {}
backunitVals = {}
includedVals = {}
olmgroupVals = {}
psdgroupVals = {}
srcgroupVals = {}

# ======================================================================================================================
def buildTabSO(tabSO):
    frmIntro = LabelFrame(tabSO, bd=0)
    frmIntro.pack(side=TOP, padx=5, pady=0, fill='both')
    introText = Label(frmIntro, text='\nSource Pathway (SO) Keywords and Parameters\n')
    introText.pack(side=TOP, expand='yes')

    # creates scrollable frame for inputs
    frmInputs = Frame(tabSO, bd=0)
    canvas = Canvas(frmInputs)
    scrollbar = Scrollbar(frmInputs, orient='vertical', command=canvas.yview)
    scrollFrmInputs = Frame(canvas)

    scrollFrmInputs.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0,0), window=scrollFrmInputs, anchor=NW)
    canvas.configure(yscrollcommand=scrollbar.set)

    frmInputs.pack(side=TOP, padx=5, pady=5, expand=True, fill='both')
    canvas.pack(side=LEFT, padx=5, pady=5, fill='both', expand=True)
    scrollbar.pack(side=RIGHT, fill='y')
    # finish creating scrollable input frame

    frmELEVUNIT = LabelFrame(scrollFrmInputs, bd=1, text='ELEVUNIT')
    frmELEVUNIT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeELEVUNIT(frmELEVUNIT)

    frmLOCATION = LabelFrame(scrollFrmInputs, bd=1, text='LOCATION')
    frmLOCATION.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeLOCATION(frmLOCATION)

    frmSRCPARAM = LabelFrame(scrollFrmInputs, bd=1, text='SRCPARAM')
    frmSRCPARAM.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSRCPARAM(frmSRCPARAM)

    frmBUILDHGT = LabelFrame(scrollFrmInputs, bd=1, text='BUILDHGT')
    frmBUILDHGT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeBUILDHGT(frmBUILDHGT)

    frmBUILDLEN = LabelFrame(scrollFrmInputs, bd=1, text='BUILDLEN')
    frmBUILDLEN.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeBUILDLEN(frmBUILDLEN)

    frmBUILDWID = LabelFrame(scrollFrmInputs, bd=1, text='BUILDWID')
    frmBUILDWID.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeBUILDWID(frmBUILDWID)

    frmXBADJ = LabelFrame(scrollFrmInputs, bd=1, text='XBADJ')
    frmXBADJ.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeXBADJ(frmXBADJ)

    frmYBADJ = LabelFrame(scrollFrmInputs, bd=1, text='YBADJ')
    frmYBADJ.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeYBADJ(frmYBADJ)

    frmAREAVERT = LabelFrame(scrollFrmInputs, bd=1, text='AREAVERT')
    frmAREAVERT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeAREAVERT(frmAREAVERT)

    frmRBARRIER = LabelFrame(scrollFrmInputs, bd=1, text='RBARRIER')
    frmRBARRIER.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeRBARRIER(frmRBARRIER)

    frmRDEPRESS = LabelFrame(scrollFrmInputs, bd=1, text='RDEPRESS')
    frmRDEPRESS.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeRDEPRESS(frmRDEPRESS)

    frmURBANSRC = LabelFrame(scrollFrmInputs, bd=1, text='URBANSRC')
    frmURBANSRC.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeURBANSRC(frmURBANSRC)

    frmEMISFACT = LabelFrame(scrollFrmInputs,bd=1, text='EMISFACT')
    frmEMISFACT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeEMISFACT(frmEMISFACT)

    frmEMISUNIT = LabelFrame(scrollFrmInputs,bd=1, text='EMISUNIT')
    frmEMISUNIT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeEMISUNIT(frmEMISUNIT)

    frmRLEMCONV = LabelFrame(scrollFrmInputs, bd=1, text='RLEMCONV')
    frmRLEMCONV.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeRLEMCONV(frmRLEMCONV)

    frmCONCUNIT = LabelFrame(scrollFrmInputs, bd=1, text='CONCUNIT')
    frmCONCUNIT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeCONCUNIT(frmCONCUNIT)

    frmDEPOUNIT = LabelFrame(scrollFrmInputs, bd=1, text='DEPOUNIT')
    frmDEPOUNIT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeDEPOUNIT(frmDEPOUNIT)

    frmPARTDIAM = LabelFrame(scrollFrmInputs, bd=1, text='PARTDIAM')
    frmPARTDIAM.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makePARTDIAM(frmPARTDIAM)

    frmMASSFRAX = LabelFrame(scrollFrmInputs, bd=1, text='MASSFRAX')
    frmMASSFRAX.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeMASSFRAX(frmMASSFRAX)

    frmPARTDENS = LabelFrame(scrollFrmInputs, bd=1, text='PARTDENS')
    frmPARTDENS.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makePARTDENS(frmPARTDENS)

    frmMETHOD_2 = LabelFrame(scrollFrmInputs, bd=1, text='METHOD_2')
    frmMETHOD_2.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeMETHOD_2(frmMETHOD_2)

    frmGASDEPOS = LabelFrame(scrollFrmInputs, bd=1, text='GASDEPOS')
    frmGASDEPOS.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeGASDEPOS(frmGASDEPOS)

    frmNO2RATIO = LabelFrame(scrollFrmInputs, bd=1, text='NO2RATIO')
    frmNO2RATIO.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeNO2RATIO(frmNO2RATIO)

    frmHOUREMIS = LabelFrame(scrollFrmInputs, bd=1, text='HOUREMIS')
    frmHOUREMIS.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeHOUREMIS(frmHOUREMIS)

    frmBGSECTOR = LabelFrame(scrollFrmInputs, bd=1, text='BGSECTOR')
    frmBGSECTOR.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeBGSECTOR(frmBGSECTOR)

    frmBACKGRND = LabelFrame(scrollFrmInputs, bd=1, text='BACKGRND')
    frmBACKGRND.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeBACKGRND(frmBACKGRND)

    frmBACKUNIT = LabelFrame(scrollFrmInputs, bd=1, text='BACKUNIT')
    frmBACKUNIT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeBACKUNIT(frmBACKUNIT)

    frmINCLUDED = LabelFrame(scrollFrmInputs, bd=1, text='INCLUDED')
    frmINCLUDED.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeINCLUDED(frmINCLUDED)

    frmOLMGROUP = LabelFrame(scrollFrmInputs, bd=1, text='OLMGROUP')
    frmOLMGROUP.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeOLMGROUP(frmOLMGROUP)

    frmPSDGROUP = LabelFrame(scrollFrmInputs, bd=1, text='PSDGROUP')
    frmPSDGROUP.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makePSDGROUP(frmPSDGROUP)

    frmSRCGROUP = LabelFrame(scrollFrmInputs, bd=1, text='SRCGROUP')
    frmSRCGROUP.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSRCGROUP(frmSRCGROUP)

    soInputs = (elevunitVals, locationVals, srcparamVals, buildhgtVals, buildlenVals, buildwidVals, xbadjVals,
                ybadjVals, areavertVals, rbarrierVals, rdepressVals, urbansrcVals, emisfactVals, emisunitVals,
                rlemconvVals, concunitVals, depounitVals, partdiamVals, massfraxVals, partdensVals, method_2Vals,
                gasdeposVals, no2ratioVals, houremisVals, bgsectorVals, backgrndVals, backunitVals, includedVals,
                olmgroupVals, psdgroupVals, srcgroupVals)


    frmButtons = Frame(tabSO,bd=0)
    frmButtons.pack(side=TOP, padx=5, pady=3, fill="both")
    btn1 = Button(frmButtons, text='Write SO to control file', font=('calibri', 11, 'bold'), width=40,
                command=(lambda: soWriter.writeControlFile(soInputs)))
    btn1.pack(side=TOP, padx=60, pady=3)
