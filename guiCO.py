from tkinter import *

import coWriter
import constantsCO as constCO

# ======================================================================================================================
def makeForms(lblfrm, keywords):
    for kword in keywords:
        frm = Frame(lblfrm)
        lab = Label(frm, width=10, text=kword + ": ", anchor='w')
        ent = Entry(frm, width=100)
        #ent.insert(0,'')
        frm.pack(side=LEFT, fill='both', padx=3, pady=3)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, expand=YES, fill=X)
        titles[kword] = ent

# ======================================================================================================================
def makeMODELOPT(lblfrm):

    def chkConflictsDFAULT():
        if chkDFAULT:
            if chkALPHA: chkbtnALPHA.deselect()
            if chkBETA: chkbtnBETA.deselect()
            if chkAREADPLT: chkbtnAREADPLT.deselect()
            if chkFLAT: chkbtnFLAT.deselect()
            if chkNOSTD: chkbtnNOSTD.deselect()
            if chkNOCHKD: chkbtnNOCHKD.deselect()
            if chkSCREEN: chkbtnSCREEN.deselect()
            if chkSCIM: chkbtnSCIM.deselect()
            if chkNOURBTRAN: chkbtnNOURBTRAN.deselect()
            if chkPSDCREDIT: chkbtnPSDCREDIT.deselect()
            radbtnVar2.set(0)

    chkDFAULT = BooleanVar()
    chkDFAULT.set(False)
    chkbtnDFAULT = Checkbutton(lblfrm, text=constCO.MODELOPT.DFAULT.name, var=chkDFAULT,
                               command=chkConflictsDFAULT)
    chkbtnDFAULT.pack(side=LEFT)
    # ==================================================================================================================

    chkALPHA = BooleanVar()
    chkALPHA.set(False)
    chkbtnALPHA = Checkbutton(lblfrm, text=constCO.MODELOPT.ALPHA.name, var=chkALPHA)
    chkbtnALPHA.pack(side=LEFT)
    # ==================================================================================================================

    chkBETA = BooleanVar()
    chkBETA.set(False)
    chkbtnBETA = Checkbutton(lblfrm, text=constCO.MODELOPT.BETA.name, var=chkBETA)
    chkbtnBETA.pack(side=LEFT)
    # ==================================================================================================================

    # FRAME1
    frm1 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm1.pack(side=LEFT, padx=5, pady=3)#, fill='both')

    chkWDEP = BooleanVar()
    chkWDEP.set(False)
    chkbtnWDEP = Checkbutton(frm1, text=constCO.MODELOPT.WDEP.name, var=chkWDEP)
    #chkbtnWDEP.pack(side=TOP,anchor=W)
    chkbtnWDEP.grid(row=0, column=0, padx=1, pady=1)

    chkDDEP = BooleanVar()
    chkDDEP.set(False)
    chkbtnDDEP = Checkbutton(frm1, text=constCO.MODELOPT.DDEP.name, var=chkDDEP)
    #chkbtnDDEP.pack(side=TOP,anchor=W)
    chkbtnDDEP.grid(row=0, column=1, padx=1, pady=1)

    chkDEPOS = BooleanVar()
    chkDEPOS.set(False)
    chkbtnDEPOS = Checkbutton(frm1, text=constCO.MODELOPT.DEPOS.name, var=chkDEPOS)
    #chkbtnDEPOS.pack(side=TOP,anchor=W)
    chkbtnDEPOS.grid(row=1, column=0, padx=1, pady=1)

    chkCONC = BooleanVar()
    chkCONC.set(False)
    chkbtnCONC = Checkbutton(frm1, text=constCO.MODELOPT.CONC.name, var=chkCONC)
    #chkbtnCONC.pack(side=TOP,anchor=W)
    chkbtnCONC.grid(row=1, column=1, padx=1, pady=1)
    # END FRAME1 =======================================================================================================

    chkAREADPLT = BooleanVar()
    chkAREADPLT.set(False)
    chkbtnAREADPLT = Checkbutton(lblfrm, text=constCO.MODELOPT.AREADPLT.name, var=chkAREADPLT)
    chkbtnAREADPLT.pack(side=LEFT)
    # ==================================================================================================================

    # FRAME2
    frm2 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm2.pack(side=LEFT, padx=5, pady=3)#, fill='both')

    chkELEV = BooleanVar()
    chkELEV.set(False)
    chkbtnELEV = Checkbutton(frm2, text=constCO.MODELOPT.ELEV.name, var=chkELEV)
    chkbtnELEV.pack(side=TOP, anchor=W)

    chkFLAT = BooleanVar()
    chkFLAT.set(False)
    chkbtnFLAT = Checkbutton(frm2, text=constCO.MODELOPT.FLAT.name, var=chkFLAT)
    chkbtnFLAT.pack(side=TOP, anchor=W)
    # END FRAME2 =======================================================================================================

    chkNOSTD = BooleanVar()
    chkNOSTD.set(False)
    chkbtnNOSTD = Checkbutton(lblfrm, text=constCO.MODELOPT.NOSTD.name, var=chkNOSTD)
    chkbtnNOSTD.pack(side=LEFT)
    # ==================================================================================================================

    # FRAME3
    frm3 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm3.pack(side=LEFT, padx=5, pady=3)#, fill='both')

    chkWARNCHKD = BooleanVar()
    chkWARNCHKD.set(False)
    chkbtnWARNCHKD = Checkbutton(frm3, text=constCO.MODELOPT.WARNCHKD.name, var=chkWARNCHKD)
    chkbtnWARNCHKD.pack(side=TOP, anchor=W)

    chkNOCHKD = BooleanVar()
    chkNOCHKD.set(False)
    chkbtnNOCHKD = Checkbutton(frm3, text=constCO.MODELOPT.NOCHKD.name, var=chkNOCHKD)
    chkbtnNOCHKD.pack(side=TOP, anchor=W)
    # END FRAME3 =======================================================================================================

    chkNOWARN = BooleanVar()
    chkNOWARN.set(False)
    chkbtnNOWARN = Checkbutton(lblfrm, text=constCO.MODELOPT.NOWARN.name, var=chkNOWARN)
    chkbtnNOWARN.pack(side=LEFT)
    # ==================================================================================================================

    chkSCREEN = BooleanVar()
    chkSCREEN.set(False)
    chkbtnSCREEN = Checkbutton(lblfrm, text=constCO.MODELOPT.SCREEN.name, var=chkSCREEN)
    chkbtnSCREEN.pack(side=LEFT)
    # ==================================================================================================================

    chkSCIM = BooleanVar()
    chkSCIM.set(False)
    chkbtnSCIM = Checkbutton(lblfrm, text=constCO.MODELOPT.SCIM.name, var=chkSCIM)
    chkbtnSCIM.pack(side=LEFT)
    # ==================================================================================================================

    # FRAME4
    frm4 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm4.pack(side=LEFT, padx=5, pady=3)#, fill='both')
    radbtnVar1 = IntVar()
    radbtnPVMRM = Radiobutton(frm4, text=constCO.MODELOPT.PVMRM.name, var=radbtnVar1, value=1)
    radbtnPVMRM.pack(side=TOP, anchor=W)
    radbtnOLM = Radiobutton(frm4, text=constCO.MODELOPT.OLM.name, var=radbtnVar1, value=2)
    radbtnOLM.pack(side=TOP, anchor=W)
    radbtnARM2 = Radiobutton(frm4, text=constCO.MODELOPT.ARM2.name, var=radbtnVar1, value=3)
    radbtnARM2.pack(side=TOP, anchor=W)
    # END FRAME4 =======================================================================================================

    # creates FASTALL and FASTAREA - FRAME 5 ===========================================================================
    frm5 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm5.pack(side=LEFT, padx=5, pady=3)#, fill='both')
    radbtnVar2 = IntVar()
    radbtnFASTALL = Radiobutton(frm5, text=constCO.MODELOPT.FASTALL.name, var=radbtnVar2, value=1)
    radbtnFASTALL.pack(side=TOP, anchor=W)
    radbtnFASTAREA = Radiobutton(frm5, text=constCO.MODELOPT.FASTAREA.name, var=radbtnVar2, value=2)
    radbtnFASTAREA.pack(side=TOP, anchor=W)
    # ==================================================================================================================

    # creates DRYDPLT and NODRYDPLT - FRAME 6 ==========================================================================
    frm6 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm6.pack(side=LEFT, padx=5, pady=3)#, fill='both')
    radbtnVar3 = IntVar()
    radbtnDRYDPLT = Radiobutton(frm6, text=constCO.MODELOPT.DRYDPLT.name, var=radbtnVar3, val=1)
    radbtnDRYDPLT.pack(side=TOP, anchor=W)
    radbtnNODRYDPLT = Radiobutton(frm6, text=constCO.MODELOPT.NODRYDPLT.name, var=radbtnVar3, val=2)
    radbtnNODRYDPLT.pack(side=TOP, anchor=W)
    # ==================================================================================================================

    # creates WETDPLT and NOWETDPLT - FRAME 7 ==========================================================================
    frm7 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm7.pack(side=LEFT, padx=5, pady=3)#, fill='both')
    radbtnVar4 = IntVar()
    radbtnWETDPLT = Radiobutton(frm7, text=constCO.MODELOPT.WETDPLT.name, var=radbtnVar4, val=1)
    radbtnWETDPLT.pack(side=TOP, anchor=W)
    radbtnNOWETDPLT = Radiobutton(frm7, text=constCO.MODELOPT.NOWETDPLT.name, var=radbtnVar4, val=2)
    radbtnNOWETDPLT.pack(side=TOP, anchor=W)
    # ==================================================================================================================

    # creates NOURBTRAN ================================================================================================
    chkNOURBTRAN = BooleanVar()
    chkNOURBTRAN.set(False)
    chkbtnNOURBTRAN = Checkbutton(lblfrm, text=constCO.MODELOPT.NOURBTRAN.name, var=chkNOURBTRAN)
    chkbtnNOURBTRAN.pack(side=LEFT)
    # ==================================================================================================================

    # creates VECTORWS ================================================================================================
    chkVECTORWS = BooleanVar()
    chkVECTORWS.set(False)
    chkbtnVECTORWS = Checkbutton(lblfrm, text=constCO.MODELOPT.VECTORWS.name, var=chkVECTORWS)
    chkbtnVECTORWS.pack(side=LEFT)
    # ==================================================================================================================

    # creates PSDCREDIT ================================================================================================
    chkPSDCREDIT = BooleanVar()
    chkPSDCREDIT.set(False)
    chkbtnPSDCREDIT = Checkbutton(lblfrm, text=constCO.MODELOPT.PSDCREDIT.name, var=chkPSDCREDIT)
    chkbtnPSDCREDIT.pack(side=LEFT)
    # ==================================================================================================================

    modeloptVals[constCO.MODELOPT.DFAULT.name] = chkDFAULT
    modeloptVals[constCO.MODELOPT.ALPHA.name] = chkALPHA
    modeloptVals[constCO.MODELOPT.BETA.name] = chkBETA
    modeloptVals[constCO.MODELOPT.CONC.name] = chkCONC
    modeloptVals[constCO.MODELOPT.DEPOS.name] = chkDEPOS
    modeloptVals[constCO.MODELOPT.DDEP.name] = chkDDEP
    modeloptVals[constCO.MODELOPT.WDEP.name] = chkWDEP
    modeloptVals[constCO.MODELOPT.AREADPLT.name] = chkAREADPLT
    modeloptVals[constCO.MODELOPT.FLAT.name] = chkFLAT
    modeloptVals[constCO.MODELOPT.ELEV.name] = chkELEV
    modeloptVals[constCO.MODELOPT.NOSTD.name] = chkNOSTD
    modeloptVals[constCO.MODELOPT.NOCHKD.name] = chkNOCHKD
    modeloptVals[constCO.MODELOPT.WARNCHKD.name] = chkWARNCHKD
    modeloptVals[constCO.MODELOPT.NOWARN.name] = chkNOWARN
    modeloptVals[constCO.MODELOPT.SCREEN.name] = chkSCREEN
    modeloptVals[constCO.MODELOPT.SCIM.name] = chkSCIM
    modeloptVals['radbtnVar1'] = radbtnVar1
    modeloptVals['radbtnVar2'] = radbtnVar2
    modeloptVals['radbtnVar3'] = radbtnVar3
    modeloptVals['radbtnVar4'] = radbtnVar4
    modeloptVals[constCO.MODELOPT.NOURBTRAN.name] = chkNOURBTRAN
    modeloptVals[constCO.MODELOPT.VECTORWS.name] = chkVECTORWS
    modeloptVals[constCO.MODELOPT.PSDCREDIT.name] = chkPSDCREDIT


# ======================================================================================================================
def makeAVERTIME(lblfrm):
    frm1 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm1.pack(side=LEFT, padx=5, pady=3, fill='both')#, expand='yes')

    chk1Hr = BooleanVar()
    chk1Hr.set(False)
    chkbtn1Hr = Checkbutton(frm1, text=constCO.AVERTIME._1Hr.name, var=chk1Hr)
    chkbtn1Hr.pack(side=LEFT, anchor=W)

    chk2Hr = BooleanVar()
    chk2Hr.set(False)
    chkbtn2Hr = Checkbutton(frm1, text=constCO.AVERTIME._2Hr.name, var=chk2Hr)
    chkbtn2Hr.pack(side=LEFT, anchor=W)

    chk3Hr = BooleanVar()
    chk3Hr.set(False)
    chkbtn3Hr = Checkbutton(frm1, text=constCO.AVERTIME._3Hr.name, var=chk3Hr)
    chkbtn3Hr.pack(side=LEFT, anchor=W)

    chk4Hr = BooleanVar()
    chk4Hr.set(False)
    chkbtn4Hr = Checkbutton(frm1, text=constCO.AVERTIME._4Hr.name, var=chk4Hr)
    chkbtn4Hr.pack(side=LEFT, anchor=W)

    chk6Hr = BooleanVar()
    chk6Hr.set(False)
    chkbtn6Hr = Checkbutton(frm1, text=constCO.AVERTIME._6Hr.name, var=chk6Hr)
    chkbtn6Hr.pack(side=LEFT, anchor=W)

    chk8Hr = BooleanVar()
    chk8Hr.set(False)
    chkbtn8Hr = Checkbutton(frm1, text=constCO.AVERTIME._8Hr.name, var=chk8Hr)
    chkbtn8Hr.pack(side=LEFT, anchor=W)

    chk12Hr = BooleanVar()
    chk12Hr.set(False)
    chkbtn12Hr = Checkbutton(frm1, text=constCO.AVERTIME._12Hr.name, var=chk12Hr)
    chkbtn12Hr.pack(side=LEFT, anchor=W)

    chk24Hr = BooleanVar()
    chk24Hr.set(False)
    chkbtn24Hr = Checkbutton(frm1, text=constCO.AVERTIME._24Hr.name, var=chk24Hr)
    chkbtn24Hr.pack(side=LEFT, anchor=W)

    chkMONTH = BooleanVar()
    chkMONTH.set(False)
    chkbtnMONTH = Checkbutton(lblfrm, text=constCO.AVERTIME.MONTH.name, var=chkMONTH)
    chkbtnMONTH.pack(side=LEFT)

    frm2 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm2.pack(side=LEFT, padx=5, pady=3, fill='both')#, expand='yes')
    radbtnVar1 = IntVar()
    radbtnPERIOD = Radiobutton(frm2, text=constCO.AVERTIME.PERIOD.name, var=radbtnVar1, value=1)
    radbtnPERIOD.pack(side=LEFT, anchor=W)
    radbtnANNUAL = Radiobutton(frm2, text=constCO.AVERTIME.ANNUAL.name, var=radbtnVar1, value=2)
    radbtnANNUAL.pack(side=LEFT, anchor=W)

    avertimeVals[constCO.AVERTIME._1Hr.name] = chk1Hr
    avertimeVals[constCO.AVERTIME._2Hr.name] = chk2Hr
    avertimeVals[constCO.AVERTIME._3Hr.name] = chk3Hr
    avertimeVals[constCO.AVERTIME._4Hr.name] = chk4Hr
    avertimeVals[constCO.AVERTIME._6Hr.name] = chk6Hr
    avertimeVals[constCO.AVERTIME._8Hr.name] = chk8Hr
    avertimeVals[constCO.AVERTIME._12Hr.name] = chk12Hr
    avertimeVals[constCO.AVERTIME._24Hr.name] = chk24Hr
    avertimeVals[constCO.AVERTIME.MONTH.name] = chkMONTH
    avertimeVals['radbtnVar1'] = radbtnVar1


# ======================================================================================================================
def makeURBANOPT(lblfrm):
    frmUrbpop = Frame(lblfrm)
    lblUrbpop = Label(frmUrbpop, width=7, text='Urbpop: ', anchor=W)
    entUrbpop = Entry(frmUrbpop, width=30)
    frmUrbpop.pack(side=LEFT, padx=5, pady=3, anchor=W)
    lblUrbpop.pack(side=LEFT)
    entUrbpop.pack(side=LEFT)

    frmUrbname = Frame(lblfrm)
    lblUrbname = Label(frmUrbname, width=8, text='Urbname: ', anchor=W)
    entUrbname = Entry(frmUrbname, width=30)
    frmUrbname.pack(side=LEFT, padx=5, pady=3, anchor=W)
    lblUrbname.pack(side=LEFT)
    entUrbname.pack(side=LEFT)

    frmUrbroughness = Frame(lblfrm)
    lblUrbroughness = Label(frmUrbroughness, width=12, text='Urbroughness: ', anchor=W)
    entUrbroughness = Entry(frmUrbroughness, width=30)
    frmUrbroughness.pack(side=LEFT, padx=5, pady=3, anchor=W)
    lblUrbroughness.pack(side=LEFT)
    entUrbroughness.pack(side=LEFT)

    urbanoptVals['urbpop'] = entUrbpop
    urbanoptVals['urbname'] = entUrbname
    urbanoptVals['urbroughness'] = entUrbroughness


# ======================================================================================================================
def makePOLLUTID(lblfrm):
    frm1 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm1.pack(side=LEFT, padx=5, pady=3, fill='both')

    radbtnVar1 = IntVar()
    radbtnPM10 = Radiobutton(frm1, text=constCO.POLLUTID.PM10.name, var=radbtnVar1, value=1)
    radbtnPM10.pack(side=LEFT)
    radbtnPM25 = Radiobutton(frm1, text=constCO.POLLUTID.PM25.name, var=radbtnVar1, value=2)
    radbtnPM25.pack(side=LEFT)
    radbtnNO2 = Radiobutton(frm1, text=constCO.POLLUTID.NO2.name, var=radbtnVar1, value=3)
    radbtnNO2.pack(side=LEFT)
    radbtnSO2 = Radiobutton(frm1, text=constCO.POLLUTID.SO2.name, var=radbtnVar1, value=4)
    radbtnSO2.pack(side=LEFT)
    radbtnLEAD = Radiobutton(frm1, text=constCO.POLLUTID.LEAD.name, var=radbtnVar1, value=5)
    radbtnLEAD.pack(side=LEFT)
    radbtnOTHER = Radiobutton(frm1, text=constCO.POLLUTID.OTHER.name, var=radbtnVar1, value=6)
    radbtnOTHER.pack(side=LEFT)
    radbtnUser = Radiobutton(frm1, text=constCO.POLLUTID.UserSpecified.name, var=radbtnVar1, value=7)
    radbtnUser.pack(side=LEFT)
    ent = Entry(frm1, width=30)
    ent.pack(side=LEFT, padx=5, pady=3)

    frm2 = Frame(lblfrm, relief=GROOVE, borderwidth=1)
    frm2.pack(side=LEFT, padx=5, pady=3, fill='both')

    radbtnVar2 = IntVar()
    radbtnH1H = Radiobutton(frm2, text=constCO.POLLUTID.H1H.name, var=radbtnVar2, value=1)
    radbtnH1H.pack(side=LEFT)
    radbtnH2H = Radiobutton(frm2, text=constCO.POLLUTID.H2H.name, var=radbtnVar2, value=2)
    radbtnH2H.pack(side=LEFT)
    radbtnINC = Radiobutton(frm2, text=constCO.POLLUTID.INC.name, var=radbtnVar2, value=3)
    radbtnINC.pack(side=LEFT)

    pollutidVals['radbtnVar1'] = radbtnVar1
    pollutidVals['entry'] = ent
    pollutidVals['radbtnVar2'] = radbtnVar2


# ======================================================================================================================
def makeHALFLIFE(lblfrm):
    lbl = Label(lblfrm, width=15, text='HALFLIFE (s): ', anchor=W)
    ent = Entry(lblfrm, width=20)
    lbl.pack(side=LEFT, padx=5, pady=3)
    ent.pack(side=LEFT, padx=5, pady=3)
    halflifeVals['entry'] = ent

# ======================================================================================================================
def makeDCAYCOEF(lblfrm):
    lbl = Label(lblfrm, width=15, text='DCAYCOEF (s^-1): ', anchor=W)
    ent = Entry(lblfrm, width=20)
    lbl.pack(side=LEFT, padx=5, pady=3)
    ent.pack(side=LEFT, padx=5, pady=3)
    dcaycoefVals['entry'] = ent

# ======================================================================================================================
def makeGASDEPDF(lblfrm):
    frm1 = Frame(lblfrm)
    frm1.pack(side=LEFT, fill='both', padx=5, pady=3)
    lblReact = Label(frm1, width=10, text='%s (f0): ' % constCO.GASDEPDF.React.name, anchor=W)
    entReact = Entry(frm1, width=20)
    lblReact.pack(side=LEFT)
    entReact.pack(side=LEFT)

    frm2 = Frame(lblfrm)
    frm2.pack(side=LEFT, fill='both', padx=5, pady=3)
    lblF_Seas2= Label(frm2, width=10, text='%s: ' % constCO.GASDEPDF.F_Seas2.name, anchor=W)
    entF_Seas2 = Entry(frm2, width=20)
    lblF_Seas2.pack(side=LEFT)
    entF_Seas2.pack(side=LEFT)

    frm3 = Frame(lblfrm)
    frm3.pack(side=LEFT, fill='both', padx=5, pady=3)
    lblF_Seas5 = Label(frm3, width=10, text='%s: ' % constCO.GASDEPDF.F_Seas5.name, anchor=W)
    entF_Seas5 = Entry(frm3, width=20)
    lblF_Seas5.pack(side=LEFT)
    entF_Seas5.pack(side=LEFT)

    frm4 = Frame(lblfrm)
    frm4.pack(side=LEFT, fill='both', padx=5, pady=3)
    lblRefpoll = Label(frm4, width=10, text='%s: ' % constCO.GASDEPDF.Refpoll.name, anchor=W)
    entRefpoll = Entry(frm4, width=30)
    lblRefpoll.pack(side=LEFT)
    entRefpoll.pack(side=LEFT)

    gasdepdfVals[constCO.GASDEPDF.React.name] = entReact
    gasdepdfVals[constCO.GASDEPDF.F_Seas2.name] = entF_Seas2
    gasdepdfVals[constCO.GASDEPDF.F_Seas5.name] = entF_Seas5
    gasdepdfVals[constCO.GASDEPDF.Refpoll.name] = entRefpoll

# ======================================================================================================================
def makeGASDEPVD(lblfrm):
    lbl = Label(lblfrm, width=15, text='GASDEPVD (m/s): ', anchor=W)
    ent = Entry(lblfrm, width=20)
    lbl.pack(side=LEFT, padx=5, pady=3)
    ent.pack(side=LEFT, padx=5, pady=3)
    gasdepvdVals['entry'] = ent

# ======================================================================================================================
def makeGDLANUSE(lblfrm):
    nRows = 3
    nCols = 12
    for iRow in range(nRows):
        for iCol in range(nCols):
            frm = Frame(lblfrm)
            frm.grid(row=iRow, column=iCol, padx=2, pady=2)
            secID = iRow*nCols + iCol+1
            lab = Label(frm, width=7, text='Sector%d:' % secID)
            lab.pack(side=LEFT)
            ent = Entry(frm,width=7)
            ent.pack(side=LEFT)
            gdlanuseVals['Sec%d' % secID] = ent

# ======================================================================================================================
def makeGDSEASON(lblfrm):
    frmLeft = Frame(lblfrm)
    frmLeft.pack(side=LEFT, padx=10, pady=3)
    frmRight = Frame(lblfrm)
    frmRight.pack(side=LEFT, padx=10, pady=3)

    text = Text(frmRight, height=5, width=65)
    choicesTxt = '1 - Midsummer/Lush vegetation\n' \
                 '2 - Autumn/Unharvested cropland\n' \
                 '3 - Late autumn after harvest or Winter with no snow\n' \
                 '4 - Winter with continuous snow cover\n' \
                 '5 - Transitional spring/partial green coverage/short annuals'
    text.pack(side=TOP)
    text.insert(END, choicesTxt)

    nRows = 2
    nCols = 6
    choices = ['1', '2', '3', '4', '5']
    for iRow in range(nRows):
        for iCol in range(nCols):
            frm = Frame(frmLeft)
            frm.grid(row=iRow, column=iCol, padx=2, pady=2)
            monthID = iRow*nCols + iCol+1
            month = constCO.GDSEASON.getMonthbyVal(monthID).name
            lab = Label(frm, width=3, text=month)
            lab.pack(side=LEFT)
            variable = StringVar()
            variable.set(choices[0])
            opt = OptionMenu(frm,variable, *choices)
            opt.config(width=2)
            opt.pack(side=LEFT)
            gdseasonVals[month] = variable

# ======================================================================================================================
def makeLOW_WIND(lblfrm):
    frm1 = Frame(lblfrm)
    frm1.pack(side=LEFT, padx=10, pady=3)
    lblSVmin = Label(frm1, width=20, text='%s (0.01m/s to 1.0m/s): ' % constCO.LOW_WIND.SVmin.name)
    entSVmin = Entry(frm1, width=7)
    lblSVmin.pack(side=LEFT)
    entSVmin.pack(side=LEFT)

    frm2 = Frame(lblfrm)
    frm2.pack(side=LEFT, padx=5, pady=3)
    lblWSmin = Label(frm2, width=22, text='%s (0.01m/s to 1.0m/s): ' % constCO.LOW_WIND.WSmin.name)
    entWSmin = Entry(frm2, width=7)
    lblWSmin.pack(side=LEFT)
    entWSmin.pack(side=LEFT)

    frm3 = Frame(lblfrm)
    frm3.pack(side=LEFT, padx=5, pady=3)
    lblFRANmax = Label(frm3, width=17, text='%s (0.0 to 1.0): ' % constCO.LOW_WIND.WSmin.name)
    entFRANmax = Entry(frm3, width=7)

    lblFRANmax.pack(side=LEFT)
    entFRANmax.pack(side=LEFT)

    low_windVals[constCO.LOW_WIND.SVmin.name] = entSVmin
    low_windVals[constCO.LOW_WIND.WSmin.name] = entWSmin
    low_windVals[constCO.LOW_WIND.FRANmax.name] = entFRANmax

# ======================================================================================================================
def makeAWMADWNW(lblfrm):
    chkAWMAUEFF = BooleanVar()
    chkAWMAUEFF.set(False)
    chkbtnAWMAUEFF = Checkbutton(lblfrm, text=constCO.AWMADWNW.AWMAUEFF.name, var=chkAWMAUEFF)
    chkbtnAWMAUEFF.pack(side=LEFT)

    chkAWMAUTURB = BooleanVar()
    chkAWMAUTURB.set(False)
    chkbtnAWMAUTURB = Checkbutton(lblfrm, text=constCO.AWMADWNW.AWMAUTURB.name, var=chkAWMAUTURB)
    chkbtnAWMAUTURB.pack(side=LEFT)

    chkSTREAMLINE = BooleanVar()
    chkSTREAMLINE.set(False)
    chkbtnSTREAMLINE = Checkbutton(lblfrm, text=constCO.AWMADWNW.STREAMLINE.name, var=chkSTREAMLINE)
    chkbtnSTREAMLINE.pack(side=LEFT)

    awmadwnwVals[constCO.AWMADWNW.AWMAUEFF.name] = chkAWMAUEFF
    awmadwnwVals[constCO.AWMADWNW.AWMAUTURB.name] = chkAWMAUTURB
    awmadwnwVals[constCO.AWMADWNW.STREAMLINE.name] = chkSTREAMLINE

# ======================================================================================================================
def makeORD_DWNW(lblfrm):
    chkORDUEFF = BooleanVar()
    chkORDUEFF.set(False)
    chkbtnORDUEFF = Checkbutton(lblfrm, text=constCO.ORD_DWNW.ORDUEFF.name, var=chkORDUEFF)
    chkbtnORDUEFF.pack(side=LEFT)

    chkORDTURB = BooleanVar()
    chkORDTURB.set(False)
    chkbtnORDTURB = Checkbutton(lblfrm, text=constCO.ORD_DWNW.ORDTURB.name, var=chkORDTURB)
    chkbtnORDTURB.pack(side=LEFT)

    chkORDCAV = BooleanVar()
    chkORDCAV.set(False)
    chkbtnORDCAV = Checkbutton(lblfrm, text=constCO.ORD_DWNW.ORDCAV.name, var=chkORDCAV)
    chkbtnORDCAV.pack(side=LEFT)

    ord_dwnwVals[constCO.ORD_DWNW.ORDUEFF.name] = chkORDUEFF
    ord_dwnwVals[constCO.ORD_DWNW.ORDTURB.name] = chkORDTURB
    ord_dwnwVals[constCO.ORD_DWNW.ORDCAV.name] = chkORDCAV

# ======================================================================================================================
def makeNO2(lblfrm):
    lblNO2EQUIL = Label(lblfrm, text='NO2EQUIL: ', width=10)
    entNO2EQUIL = Entry(lblfrm, width=10)
    lblNO2EQUIL.pack(side=LEFT, padx=3, pady=3)
    entNO2EQUIL.pack(side=LEFT, padx=3, pady=3)

    lblNO2STACK = Label(lblfrm, text='NO2STACK: ', width=10)
    entNO2STACK = Entry(lblfrm, width=10)
    lblNO2STACK.pack(side=LEFT, padx=3, pady=3)
    entNO2STACK.pack(side=LEFT, padx=3, pady=3)

    no2equilVals['entry'] = entNO2EQUIL
    no2stackVals['entry'] = entNO2STACK

# ======================================================================================================================
def makeARMRATIO(lblfrm):
    lblARM2_Min = Label(lblfrm, text=constCO.ARMRATIO.ARM2_Min.name, width=10)
    entARM2_Min = Entry(lblfrm, width=10)
    lblARM2_Min.pack(side=LEFT, padx=3, pady=3)
    entARM2_Min.pack(side=LEFT, padx=3, pady=3)

    lblARM2_Max = Label(lblfrm, text=constCO.ARMRATIO.ARM2_Max.name, width=10)
    entARM2_Max = Entry(lblfrm, width=10)
    lblARM2_Max.pack(side=LEFT, padx=3, pady=3)
    entARM2_Max.pack(side=LEFT, padx=3, pady=3)

    armratioVals[constCO.ARMRATIO.ARM2_Min.name] = entARM2_Min
    armratioVals[constCO.ARMRATIO.ARM2_Max.name] = entARM2_Max

# ======================================================================================================================
def makeO3SECTOR(lblfrm):
    lblSector1 = Label(lblfrm, text='%s: ' % constCO.O3SECTOR.StartSect1.name, width=8)
    entSector1 = Entry(lblfrm, width=5)
    lblSector1.pack(side=LEFT, padx=3, pady=3)
    entSector1.pack(side=LEFT, padx=3, pady=3)

    lblSector2 = Label(lblfrm, text='%s: ' % constCO.O3SECTOR.StartSect2.name, width=8)
    entSector2 = Entry(lblfrm, width=5)
    lblSector2.pack(side=LEFT, padx=3, pady=3)
    entSector2.pack(side=LEFT, padx=3, pady=3)

    lblSector3 = Label(lblfrm, text='%s: ' % constCO.O3SECTOR.StartSect3.name, width=8)
    entSector3 = Entry(lblfrm, width=5)
    lblSector3.pack(side=LEFT, padx=3, pady=3)
    entSector3.pack(side=LEFT, padx=3, pady=3)

    lblSector4 = Label(lblfrm, text='%s: ' % constCO.O3SECTOR.StartSect4.name, width=8)
    entSector4 = Entry(lblfrm, width=5)
    lblSector4.pack(side=LEFT, padx=3, pady=3)
    entSector4.pack(side=LEFT, padx=3, pady=3)

    lblSector5 = Label(lblfrm, text='%s: ' % constCO.O3SECTOR.StartSect5.name, width=8)
    entSector5 = Entry(lblfrm, width=5)
    lblSector5.pack(side=LEFT, padx=3, pady=3)
    entSector5.pack(side=LEFT, padx=3, pady=3)

    lblSector6 = Label(lblfrm, text='%s: ' % constCO.O3SECTOR.StartSect6.name, width=8)
    entSector6 = Entry(lblfrm, width=5)
    lblSector6.pack(side=LEFT, padx=3, pady=3)
    entSector6.pack(side=LEFT, padx=3, pady=3)

    o3sectorVals[constCO.O3SECTOR.StartSect1.name] = entSector1
    o3sectorVals[constCO.O3SECTOR.StartSect2.name] = entSector2
    o3sectorVals[constCO.O3SECTOR.StartSect3.name] = entSector3
    o3sectorVals[constCO.O3SECTOR.StartSect4.name] = entSector4
    o3sectorVals[constCO.O3SECTOR.StartSect5.name] = entSector5
    o3sectorVals[constCO.O3SECTOR.StartSect6.name] = entSector6

# ======================================================================================================================
def makeOZONEFIL(lblfrm):
    lblO3FileName = Label(lblfrm, text='%s: ' % constCO.OZONEFIL.O3FileName.name, width=10)
    entO3FileName = Entry(lblfrm, width=50)
    lblO3FileName.pack(side=LEFT, padx=3, pady=3)
    entO3FileName.pack(side=LEFT, padx=3, pady=3)

    choices = ['PPM', 'PPB', 'UG/M3']
    lblO3Units = Label(lblfrm, text='%s: ' % constCO.OZONEFIL.O3Units.name, width=8)
    lblO3Units.pack(side=LEFT, padx=3, pady=3)
    variable = StringVar()
    variable.set(choices[2])
    opt = OptionMenu(lblfrm, variable, *choices)
    opt.config(width=5)
    opt.pack(side=LEFT, padx=3, pady=3)

    lblO3Format = Label(lblfrm, text='%s: ' % constCO.OZONEFIL.O3Format.name, width=10)
    entO3Format = Entry(lblfrm, width=10)
    lblO3Format.pack(side=LEFT, padx=3, pady=3)
    entO3Format.pack(side=LEFT, padx=3, pady=3)

    ozonefilVals[constCO.OZONEFIL.O3FileName.name] = entO3FileName
    ozonefilVals[constCO.OZONEFIL.O3Units.name] = variable
    ozonefilVals[constCO.OZONEFIL.O3Format.name] = entO3Format

# ======================================================================================================================
def makeOZONEVAL(lblfrm):
    lblO3Value = Label(lblfrm, text='%s: ' % constCO.OZONEVAL.O3Value.name, width=8)
    entO3Value = Entry(lblfrm, width=5)
    lblO3Value.pack(side=LEFT, padx=3, pady=3)
    entO3Value.pack(side=LEFT, padx=3, pady=3)

    choices = ['PPM', 'PPB', 'UG/M3']
    lblO3Units = Label(lblfrm, text='%s: ' % constCO.OZONEFIL.O3Units.name, width=8)
    lblO3Units.pack(side=LEFT, padx=3, pady=3)
    variable = StringVar()
    variable.set(choices[2])
    opt = OptionMenu(lblfrm, variable, *choices)
    opt.config(width=5)
    opt.pack(side=LEFT, padx=3, pady=3)

    ozonevalVals[constCO.OZONEVAL.O3Value.name] = entO3Value
    ozonevalVals[constCO.OZONEVAL.O3Units.name] = variable

# ======================================================================================================================
def makeO3VALUES(lblfrm):
    lblO3Flag = Label(lblfrm, text='%s: ' % constCO.O3VALUES.O3Flag.name, width=10)
    lblO3Flag.pack(side=LEFT, padx=3, pady=0)
    choices = ['ANNUAL', 'SEASON', 'MONTH', 'HROFDY', 'WSPEED', 'SEASHR', 'HRDOW', 'HRDOW7', 'SHRDOW', 'SHRDOW7',
               'MHRDOW', 'MHRDOW7']
    variable = StringVar()
    variable.set(choices[0])
    opt = OptionMenu(lblfrm, variable, *choices)
    opt.config(width=7)
    opt.pack(side=LEFT, padx=3, pady=0)

    lblO3values = Label(lblfrm, text='%s: ' % constCO.O3VALUES.O3values.name, width=10)
    entO3values = Entry(lblfrm, width=100)
    lblO3values.pack(side=LEFT, padx=3, pady=0)
    entO3values.pack(side=LEFT, padx=3, pady=0)

    o3valuesVals[constCO.O3VALUES.O3Flag.name] = variable
    o3valuesVals[constCO.O3VALUES.O3values.name] = entO3values

# ======================================================================================================================
def makeOZONUNIT(frm):
    lbl = Label(frm, text='%s: ' % constCO.OZONUNIT.Ozonunit.name, width=10)
    lbl.pack(side=LEFT, padx=3, pady=3)
    choices = ['PPM', 'PPB', 'UG/M3']
    variable = StringVar()
    variable.set(choices[2])
    opt = OptionMenu(frm, variable, *choices)
    opt.config(width=5)
    opt.pack(side=LEFT, padx=3, pady=3)
    ozonunitVals[constCO.OZONUNIT.Ozonunit.name] = variable

# ======================================================================================================================
def makeFLAGPOLE(frm):
    lbl = Label(frm, text='%s (m):' % constCO.FLAGPOLE.Flagpole.name, width=12)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=15)
    ent.pack(side=LEFT, padx=3, pady=3)
    flagpoleVals[constCO.FLAGPOLE.Flagpole.name] = ent

# ======================================================================================================================
def makeRUNORNOT(frm):
    lbl = Label(frm, text='RUNORNOT: ', width=10)
    lbl.pack(side=LEFT, padx=3, pady=3)

    choices = [constCO.RUNORNOT.Run.name, constCO.RUNORNOT.Not.name]
    variable = StringVar()
    variable.set(choices[0])
    opt = OptionMenu(frm, variable, *choices)
    opt.config(width=5)
    opt.pack(side=LEFT, padx=3, pady=3)
    runornotVals['RUNORNOT'] = variable

# ======================================================================================================================
def makeEVENTFIL(frm):
    lblEvfile = Label(frm, text='%s: ' % constCO.EVENTFIL.Evfile.name)
    lblEvfile.pack(side=LEFT, padx=3, pady=3)
    entEvfile = Entry(frm, width=30)
    entEvfile.pack(side=LEFT, padx=3, pady=3)

    lblEvOpt = Label(frm, text='%s: ' % constCO.EVENTFIL.Evopt.name)
    lblEvOpt.pack(side=LEFT, padx=3, pady=3)
    entEvOpt = Entry(frm, width=30)
    entEvOpt.pack(side=LEFT, padx=3, pady=3)

    eventfilVals[constCO.EVENTFIL.Evfile.name] = entEvfile
    eventfilVals[constCO.EVENTFIL.Evopt.name] = entEvOpt

# ======================================================================================================================
def makeSAVEFILE(frm):
    lblSavfil = Label(frm, text='%s: ' % constCO.SAVEFILE.Savfil.name)
    lblSavfil.pack(side=LEFT, padx=3, pady=3)
    entSavfil = Entry(frm, width=30)
    entSavfil.pack(side=LEFT, padx=3, pady=3)

    lblDayinc = Label(frm, text='%s: ' % constCO.SAVEFILE.Dayinc.name)
    lblDayinc.pack(side=LEFT, padx=3, pady=3)
    entDayinc = Entry(frm, width=5)
    entDayinc.pack(side=LEFT, padx=3, pady=3)

    lblSavfl2 = Label(frm, text='%s: ' % constCO.SAVEFILE.Savfl2.name)
    lblSavfl2.pack(side=LEFT, padx=3, pady=3)
    entSavfl2 = Entry(frm, width=30)
    entSavfl2.pack(side=LEFT, padx=3, pady=3)

    savefileVals[constCO.SAVEFILE.Savfil.name] = entSavfil
    savefileVals[constCO.SAVEFILE.Dayinc.name] = entDayinc
    savefileVals[constCO.SAVEFILE.Savfl2.name] = entSavfl2

# ======================================================================================================================
def makeINITFILE(frm):
    lbl = Label(frm, text='%s: ' % constCO.INITFILE.INITFILE.name)
    ent = Entry(frm, width=30)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent.pack(side=LEFT, padx=3, pady=3)

    initfileVals[constCO.INITFILE.INITFILE.name]= ent

# ======================================================================================================================
def makeERRORFIL(frm):
    lbl = Label(frm, text='%s: ' % constCO.ERRORFIL.ERRORFIL.name)
    ent = Entry(frm, width=30)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent.pack(side=LEFT, padx=3, pady=3)

    errorfilVals[constCO.ERRORFIL.ERRORFIL.name] = ent


# ======================================================================================================================
def makeMULTYEAR(frm):
    chkH6H = BooleanVar()
    chkH6H.set(False)
    chkbtnH6H = Checkbutton(frm, text=constCO.MULTYEAR.H6H.name, var=chkH6H)
    chkbtnH6H.pack(side=LEFT)

    lblSavfil = Label(frm, text='%s: ' % constCO.MULTYEAR.Savfil.name)
    lblSavfil.pack(side=LEFT, padx=3, pady=3)
    entSavfil = Entry(frm, width=30)
    entSavfil.pack(side=LEFT, padx=3, pady=3)

    lblInifil = Label(frm, text='%s: '% constCO.MULTYEAR.Inifil.name)
    lblInifil.pack(side=LEFT, padx=3, pady=3)
    entInifil = Entry(frm, width=30)
    entInifil.pack(side=LEFT, padx=3, pady=3)

    multyearVals[constCO.MULTYEAR.H6H.name] = chkH6H
    multyearVals[constCO.MULTYEAR.Savfil.name] = entSavfil
    multyearVals[constCO.MULTYEAR.Inifil.name] = entInifil

# ======================================================================================================================
def makeDEBUGOPT(frm):
    frmLEFT = Frame(frm)
    frmLEFT.pack(side=LEFT)

    frmMODEL = Frame(frmLEFT)
    frmMODEL.pack(side=TOP, anchor=W)
    chkMODEL = BooleanVar()
    chkMODEL.set(False)
    chkbtnMODEL = Checkbutton(frmMODEL, text=constCO.DEBUGOPT.MODEL.name, var=chkMODEL)
    chkbtnMODEL.pack(side=LEFT, padx=3, pady=3)
    entMODEL = Entry(frmMODEL, width=30)
    entMODEL.pack(side=LEFT, padx=3, pady=3)

    frmMETEOR = Frame(frmLEFT)
    frmMETEOR.pack(side=TOP, anchor=W)
    chkMETEOR= BooleanVar()
    chkMETEOR.set(False)
    chkbtnMETEOR = Checkbutton(frmMETEOR, text=constCO.DEBUGOPT.METEOR.name, var=chkMETEOR)
    chkbtnMETEOR.pack(side=LEFT, padx=3, pady=3)
    entMETEOR = Entry(frmMETEOR, width=30)
    entMETEOR.pack(side=LEFT, padx=3, pady=3)

    frmPRIME = Frame(frmLEFT)
    frmPRIME.pack(side=TOP, anchor=W)
    chkPRIME = BooleanVar()
    chkPRIME.set(False)
    chkbtnPRIME = Checkbutton(frmPRIME, text=constCO.DEBUGOPT.PRIME.name, var=chkPRIME)
    chkbtnPRIME.pack(side=LEFT, padx=3, pady=3)
    entPRIME = Entry(frmPRIME, width=30)
    entPRIME.pack(side=LEFT, padx=3, pady=3)

    frmAWMADW = Frame(frmLEFT)
    frmAWMADW.pack(side=TOP, anchor=W)
    chkAWMADW = BooleanVar()
    chkAWMADW.set(False)
    chkbtnAWMADW = Checkbutton(frmAWMADW, text=constCO.DEBUGOPT.AWMADW.name, var=chkAWMADW)
    chkbtnAWMADW.pack(side=LEFT, padx=3, pady=3)
    entAWMADW = Entry(frmAWMADW, width=30)
    entAWMADW.pack(side=LEFT, padx=3, pady=3)

    frmDEPOS = Frame(frmLEFT)
    frmDEPOS.pack(side=TOP, anchor=W)
    chkDEPOS = BooleanVar()
    chkDEPOS.set(False)
    chkbtnDEPOS = Checkbutton(frmDEPOS, text=constCO.DEBUGOPT.DEPOS.name, var=chkDEPOS)
    chkbtnDEPOS.pack(side=LEFT, padx=3, pady=3)


    frmRIGHT = Frame(frm)
    frmRIGHT.pack(side=RIGHT)

    frmAREALINE = Frame(frmRIGHT, relief=GROOVE, borderwidth=1)
    frmAREALINE.pack(side=TOP, anchor=W, padx=3, pady=3)

    frmAREA = Frame(frmAREALINE)
    frmAREA.pack(side=TOP, anchor=W)
    radbtnVar1 = IntVar()
    radbtnAREA = Radiobutton(frmAREA, text=constCO.DEBUGOPT.AREA.name, var=radbtnVar1, value=1)
    radbtnAREA.pack(side=LEFT, padx=3, pady=3)
    entAREA = Entry(frmAREA, width=30)
    entAREA.pack(side=LEFT, padx=3, pady=3)

    frmLINE = Frame(frmAREALINE)
    frmLINE.pack(side=TOP, anchor=W)
    radbtnLINE = Radiobutton(frmLINE, text=constCO.DEBUGOPT.LINE.name, var=radbtnVar1, value=2)
    radbtnLINE.pack(side=LEFT, padx=3, pady=3)

    frmPVMRM_OLM_ARM2 = Frame(frmRIGHT, relief=GROOVE, borderwidth=1)
    frmPVMRM_OLM_ARM2.pack(side=TOP, anchor=W, padx=3, pady=3)

    frmPVMRM = Frame(frmPVMRM_OLM_ARM2)
    frmPVMRM.pack(side=TOP, anchor=W, fill='both')
    radbtnVar2 = IntVar()
    radbtnPVMRM = Radiobutton(frmPVMRM, text=constCO.DEBUGOPT.PVMRM.name, var=radbtnVar2, value=1)
    radbtnPVMRM.pack(side=LEFT, padx=3, pady=3)
    entPVMRM = Entry(frmPVMRM, width=30)
    entPVMRM.pack(side=LEFT, padx=3, pady=3)

    frmOLM = Frame(frmPVMRM_OLM_ARM2)
    frmOLM.pack(side=TOP, anchor=W, fill='both')
    radbtnOLM = Radiobutton(frmOLM, text=constCO.DEBUGOPT.OLM.name, var=radbtnVar2, value=2)
    radbtnOLM.pack(side=LEFT, padx=3, pady=3)
    entOLM = Entry(frmOLM, width=30)
    entOLM.pack(side=RIGHT, padx=3, pady=3)

    frmARM2 = Frame(frmPVMRM_OLM_ARM2)
    frmARM2.pack(side=TOP, anchor=W, fill='both')
    radbtnARM2 = Radiobutton(frmARM2, text=constCO.DEBUGOPT.ARM2.name, var=radbtnVar2, value=3)
    radbtnARM2.pack(side=LEFT, padx=3, pady=3)
    entARM2 = Entry(frmARM2, width=30)
    entARM2.pack(side=RIGHT, padx=3, pady=3)

    debugoptVals[constCO.DEBUGOPT.MODEL.name] = chkMODEL
    debugoptVals[constCO.DEBUGOPT.Dbgfil.name] = entMODEL
    debugoptVals[constCO.DEBUGOPT.METEOR.name] = chkMETEOR
    debugoptVals[constCO.DEBUGOPT.Dbmfil.name] = entMETEOR
    debugoptVals[constCO.DEBUGOPT.PRIME.name] = chkPRIME
    debugoptVals[constCO.DEBUGOPT.Prmfil.name] = entPRIME
    debugoptVals[constCO.DEBUGOPT.AWMADW.name] = chkAWMADW
    debugoptVals[constCO.DEBUGOPT.AwmaDwfil.name] = entAWMADW
    debugoptVals[constCO.DEBUGOPT.DEPOS.name] = chkDEPOS

    debugoptVals['radbtnVar1'] = radbtnVar1
    debugoptVals[constCO.DEBUGOPT.AreaDbfil.name] = entAREA

    debugoptVals['radbtnVar2'] = radbtnVar2
    debugoptVals[constCO.DEBUGOPT.Dbpvfil.name] = entPVMRM
    debugoptVals[constCO.DEBUGOPT.OLMfil.name] = entOLM
    debugoptVals[constCO.DEBUGOPT.ARM2fil.name] = entARM2

# ======================================================================================================================
titles = {}
modeloptVals = {}
avertimeVals = {}
urbanoptVals = {}
pollutidVals = {}
halflifeVals = {}
dcaycoefVals = {}
gasdepdfVals = {}
gasdepvdVals = {}
gdlanuseVals = {}
gdseasonVals = {}
low_windVals = {}
awmadwnwVals = {}
ord_dwnwVals = {}
no2equilVals = {}
no2stackVals = {}
armratioVals = {}
o3sectorVals = {}
ozonefilVals = {}
ozonevalVals = {}
o3valuesVals = {}
ozonunitVals = {}
flagpoleVals = {}
runornotVals = {}
eventfilVals = {}
savefileVals = {}
initfileVals = {}
errorfilVals = {}
multyearVals = {}
debugoptVals = {}

# ======================================================================================================================
def buildTabCO(tabCO):
    frmIntro = LabelFrame(tabCO, bd=0)
    frmIntro.pack(side=TOP, padx=5, pady=0, fill='both')
    introText = Label(frmIntro, text='\nControl Pathway (CO) Keywords and Parameters\n')
    introText.pack(side=LEFT, expand=True)

    #lblfrmInputs = Frame(tabCO, bd=0)
    #lblfrmInputs.pack(side=TOP, padx=5, pady=0, expand='yes', fill='both')

    # creates scrollable frame for inputs
    frmInputs = Frame(tabCO, bd=0)
    canvas = Canvas(frmInputs)
    scrollbar = Scrollbar(frmInputs, orient='vertical', command=canvas.yview)
    lblfrmInputs = Frame(canvas)

    lblfrmInputs.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=lblfrmInputs, anchor=NW)
    canvas.configure(yscrollcommand=scrollbar.set)

    frmInputs.pack(side=TOP, padx=5, pady=5, expand=True, fill='both')
    canvas.pack(side=LEFT, padx=5, pady=5, fill='both', expand=True)
    scrollbar.pack(side=RIGHT, fill='y')
    # finish creating scrollable input frame


    frmTITLEs = LabelFrame(lblfrmInputs, bd=1, text='Titles')
    frmTITLEs.pack(side=TOP, fill='both', padx=5, pady=3)
    makeForms(frmTITLEs, ['TITLEONE', 'TITLETWO'])

    frmMODELOPT = LabelFrame(lblfrmInputs, bd=1, text='MODELOPT')
    frmMODELOPT.pack(side=TOP, fill='both', padx=5, pady=3)
    makeMODELOPT(frmMODELOPT)

    frmAVERTIME_URBANOPT = Frame(lblfrmInputs)
    frmAVERTIME_URBANOPT.pack(side=TOP, fill='both', padx=5, pady=3)

    frmAVERTIME = LabelFrame(frmAVERTIME_URBANOPT, bd=1, text='AVERTIME')
    frmAVERTIME.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeAVERTIME(frmAVERTIME)

    frmURBANOPT = LabelFrame(frmAVERTIME_URBANOPT, bd=1, text='URBANOPT')
    frmURBANOPT.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeURBANOPT(frmURBANOPT)

    frmPOLLUTID_DCAY = Frame(lblfrmInputs)
    frmPOLLUTID_DCAY.pack(side=TOP, fill='both', padx=5, pady=3)

    frmPOLLUTID = LabelFrame(frmPOLLUTID_DCAY, bd=1, text='POLLUTID')
    frmPOLLUTID.pack(side=LEFT, fill='both', padx=5, pady=3)
    makePOLLUTID(frmPOLLUTID)

    frmDCAY = LabelFrame(frmPOLLUTID_DCAY, bd=1, text='DCAY Parameters')
    frmDCAY.pack(side=LEFT, fill='both', padx=5, pady=3)

    frmHALFLIFE = Frame(frmDCAY)#, bd=1)
    frmHALFLIFE.pack(side=LEFT, fill='both')#, padx=5, pady=5)
    makeHALFLIFE(frmHALFLIFE)

    frmDCAYCOEF = Frame(frmDCAY)#, bd=1)
    frmDCAYCOEF.pack(side=LEFT, fill='both')#, padx=5, pady=5)
    makeDCAYCOEF(frmDCAYCOEF)

    frmGASDEP = Frame(lblfrmInputs)
    frmGASDEP.pack(side=TOP, fill='both', padx=5, pady=3)

    frmGASDEPDF = LabelFrame(frmGASDEP, bd=1, text='GASDEPDF')
    frmGASDEPDF.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeGASDEPDF(frmGASDEPDF)

    frmGASDEPVD = LabelFrame(frmGASDEP, bd=1, text='GASDEPVD')
    frmGASDEPVD.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeGASDEPVD(frmGASDEPVD)

    frmGDLANUSE = LabelFrame(lblfrmInputs, bd=1, text='GDLANUSE')
    frmGDLANUSE.pack(side=TOP, fill='both', padx=5, pady=3)
    makeGDLANUSE(frmGDLANUSE)

    frmGDSEASON = LabelFrame(lblfrmInputs, bd=1, text='GDSEASON')
    frmGDSEASON.pack(side=TOP, fill='both', padx=5, pady=3)
    makeGDSEASON(frmGDSEASON)

    frmLOWWIND_DWNW_NO_ARMRATIO = Frame(lblfrmInputs)
    frmLOWWIND_DWNW_NO_ARMRATIO.pack(side=TOP, anchor=W)

    frmLOW_WIND = LabelFrame(frmLOWWIND_DWNW_NO_ARMRATIO, bd=1, text='LOW_WIND')
    frmLOW_WIND.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeLOW_WIND(frmLOW_WIND)

    frmAWMADWNW = LabelFrame(frmLOWWIND_DWNW_NO_ARMRATIO, bd=1, text='AWMADWNW')
    frmAWMADWNW.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeAWMADWNW(frmAWMADWNW)

    frmORD_DWNW = LabelFrame(frmLOWWIND_DWNW_NO_ARMRATIO, bd=1, text='ORD_DWNW')
    frmORD_DWNW.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeORD_DWNW(frmORD_DWNW)

    #frmNO_ARMRATIO = Frame(lblfrmInputs)
    #frmNO_ARMRATIO.pack(side=TOP)

    frmNO2 = LabelFrame(frmLOWWIND_DWNW_NO_ARMRATIO, bd=1, text='NO2/NOx Parameters')
    frmNO2.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeNO2(frmNO2)

    frmARMRATIO = LabelFrame(frmLOWWIND_DWNW_NO_ARMRATIO, bd=1, text='ARMRATIO')
    frmARMRATIO.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeARMRATIO(frmARMRATIO)

    frmO3_1 = Frame(lblfrmInputs)
    frmO3_1.pack(side=TOP, anchor=W)

    frmO3SECTOR = LabelFrame(frmO3_1, bd=1, text='O3SECTOR')
    frmO3SECTOR.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeO3SECTOR(frmO3SECTOR)

    frmOZONEFIL = LabelFrame(frmO3_1, bd=1, text='OZONEFIL')
    frmOZONEFIL.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeOZONEFIL(frmOZONEFIL)

    frmOZONEVAL = LabelFrame(frmO3_1, bd=1, text='OZONEVAL')
    frmOZONEVAL.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeOZONEVAL(frmOZONEVAL)

    frmO3_2 = Frame(lblfrmInputs)
    frmO3_2.pack(side=TOP, anchor=W)

    frmO3VALUES = LabelFrame(frmO3_2, bd=1, text='O3VALUES')
    frmO3VALUES.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeO3VALUES(frmO3VALUES)

    frmOZONUNIT = LabelFrame(frmO3_2, bd=1, text='OZONUNIT')
    frmOZONUNIT.pack(side=LEFT, fill='both', padx=5, pady=3)
    makeOZONUNIT(frmOZONUNIT)

    frmBOTTOM = Frame(lblfrmInputs)
    frmBOTTOM.pack(side=TOP, fill='both', padx=5, pady=3)

    frmBOTTOMLEFT = Frame(frmBOTTOM)
    frmBOTTOMLEFT.pack(side=LEFT, fill='both', padx=5, pady=0)

    frmFLAGPOLE_RUN = Frame(frmBOTTOMLEFT)
    frmFLAGPOLE_RUN.pack(side=TOP, anchor=W)
    makeFLAGPOLE(frmFLAGPOLE_RUN)
    makeRUNORNOT(frmFLAGPOLE_RUN)

    frmEVENTFIL = LabelFrame(frmBOTTOMLEFT, bd=1, text='EVENTFIL')
    frmEVENTFIL.pack(side=TOP, anchor=W)
    makeEVENTFIL(frmEVENTFIL)

    frmSAVEFILE= LabelFrame(frmBOTTOMLEFT, bd=1, text='SAVEFILE')
    frmSAVEFILE.pack(side=TOP, anchor=W)
    makeSAVEFILE(frmSAVEFILE)

    frmINIT_ERROR = Frame(frmBOTTOMLEFT)
    frmINIT_ERROR.pack(side=TOP, anchor=W)
    makeINITFILE(frmINIT_ERROR)
    makeERRORFIL(frmINIT_ERROR)

    frmMULTYEAR = LabelFrame(frmBOTTOMLEFT, bd=1, text='MULTYEAR')
    frmMULTYEAR.pack(side=TOP, anchor=W)
    makeMULTYEAR(frmMULTYEAR)

    frmBOTTOMRIGHT = Frame(frmBOTTOM)
    frmBOTTOMRIGHT.pack(side=LEFT, fill='both', padx=5, pady=0)

    frmDEBUGOPT = LabelFrame(frmBOTTOMRIGHT, bd=1, text='DEBUGOPT')
    frmDEBUGOPT.pack(side=TOP, anchor=W)
    makeDEBUGOPT(frmDEBUGOPT)

    coInputs = (titles, modeloptVals, avertimeVals, urbanoptVals, pollutidVals, halflifeVals, dcaycoefVals,
                gasdepdfVals, gdlanuseVals, gdseasonVals, low_windVals, awmadwnwVals, ord_dwnwVals,
                no2equilVals, no2stackVals, armratioVals, o3sectorVals, ozonefilVals, ozonevalVals, o3valuesVals,
                ozonunitVals, flagpoleVals, runornotVals, eventfilVals, savefileVals, initfileVals, errorfilVals,
                multyearVals, debugoptVals)

    frmButtons = Frame(tabCO,bd=0)
    frmButtons.pack(side=TOP, padx=5, pady=3, fill="both")
    btn1 = Button(frmButtons, text='Write CO to control file', font=('calibri', 11, 'bold'), width=40,
                command=(lambda: coWriter.writeControlFile(coInputs)))
    btn1.pack(side=TOP, padx=60, pady=3)
