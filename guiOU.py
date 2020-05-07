from tkinter import *
import ouWriter
import constantsOU as constOU

# ======================================================================================================================
def makeRECTABLE(frm):
    chkALLAVE = BooleanVar()
    chkALLAVE.set(False)
    chkbtnALLAVE = Checkbutton(frm, text=constOU.RECTABLE.ALLAEV.name, var=chkALLAVE)
    chkbtnALLAVE.pack(side=LEFT, padx=3, pady=3)
    lbl = Label(frm, text=constOU.RECTABLE.Aveper.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    entAveper = Entry(frm, width=100)
    entAveper.pack(side=LEFT, padx=3, pady=3)

    rectableVals[constOU.RECTABLE.ALLAEV.name] = chkALLAVE
    rectableVals[constOU.RECTABLE.Aveper.name] = entAveper

# ======================================================================================================================
def makeMAXTABLE(frm):
    chkALLAVE = BooleanVar()
    chkALLAVE.set(False)
    chkbtnALLAVE = Checkbutton(frm, text=constOU.MAXTABLE.ALLAEV.name, var=chkALLAVE)
    chkbtnALLAVE.pack(side=LEFT, padx=3, pady=3)
    lblMaxnum = Label(frm, text=constOU.MAXTABLE.Maxnum.name)
    lblMaxnum.pack(side=LEFT, padx=3, pady=3)
    entMaxnum = Entry(frm, width=15)
    entMaxnum.pack(side=LEFT, padx=3, pady=3)
    lbl = Label(frm, text=constOU.MAXTABLE.Aveper.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    entAveper = Entry(frm, width=100)
    entAveper.pack(side=LEFT, padx=3, pady=3)

    maxtableVals[constOU.MAXTABLE.ALLAEV.name] = chkALLAVE
    maxtableVals[constOU.MAXTABLE.Maxnum.name] = entMaxnum
    maxtableVals[constOU.MAXTABLE.Aveper.name] = entAveper

# ======================================================================================================================
def makeDAYTABLE(frm):
    chkALLAVE = BooleanVar()
    chkALLAVE.set(False)
    chkbtnALLAVE = Checkbutton(frm, text=constOU.DAYTABLE.ALLAEV.name, var=chkALLAVE)
    chkbtnALLAVE.pack(side=LEFT, padx=3, pady=3)
    lbl = Label(frm, text=constOU.DAYTABLE.Aveper.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    entAveper = Entry(frm, width=100)
    entAveper.pack(side=LEFT, padx=3, pady=3)

    daytableVals[constOU.DAYTABLE.ALLAEV.name] = chkALLAVE
    daytableVals[constOU.DAYTABLE.Aveper.name] = entAveper

# ======================================================================================================================
def makeMAXIFILE(frm):
    lblAveper = Label(frm, text=constOU.MAXIFILE.Aveper.name)
    lblAveper.pack(side=LEFT, padx=3, pady=3)
    entAveper = Entry(frm, width=100)
    entAveper.pack(side=LEFT, padx=3, pady=3)

    lblGrpID = Label(frm, text=constOU.MAXIFILE.GrpID.name)
    lblGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm, width=15)
    entGrpID.pack(side=LEFT, padx=3, pady=3)

    lblThresh = Label(frm, text=constOU.MAXIFILE.Thresh.name)
    lblThresh.pack(side=LEFT, padx=3, pady=3)
    entThresh = Entry(frm, width=15)
    entThresh.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.MAXIFILE.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.MAXIFILE.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    maxifileVals[constOU.MAXIFILE.Aveper.name] = entAveper
    maxifileVals[constOU.MAXIFILE.GrpID.name] = entGrpID
    maxifileVals[constOU.MAXIFILE.Thresh.name] = entThresh
    maxifileVals[constOU.MAXIFILE.Filnam.name] = entFilnam
    maxifileVals[constOU.MAXIFILE.Funit.name] = entFunit

# ======================================================================================================================
def makePOSTFILE(frm):
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.pack(side=LEFT)

    radbtnVar = IntVar()
    radbtnPERIOD = Radiobutton(frm1, text=constOU.POSTFILE.PERIOD.name, var=radbtnVar, value=1)
    radbtnPERIOD.pack(side=LEFT, padx=3, pady=3)
    radbtnAveper = Radiobutton(frm1, text=constOU.POSTFILE.Aveper.name, var=radbtnVar, value=2)
    radbtnAveper.pack(side=LEFT, padx=3, pady=3)
    entAveper = Entry(frm1, width=50)
    entAveper.pack(side=LEFT, padx=3, pady=3)

    lblGrpID = Label(frm, text=constOU.POSTFILE.GrpID.name)
    lblGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm, width=15)
    entGrpID.pack(side=LEFT, padx=3, pady=3)

    lblFormat = Label(frm, text=constOU.POSTFILE.Format.name)
    lblFormat.pack(side=LEFT, padx=3, pady=3)
    choices = ['UNFORM', 'PLOT']
    var = StringVar()
    var.set(choices[0])
    opt = OptionMenu(frm, var, *choices)
    opt.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.POSTFILE.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.POSTFILE.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    postfileVals['radbtnVar'] = radbtnVar
    postfileVals[constOU.POSTFILE.Aveper.name] = entAveper
    postfileVals[constOU.POSTFILE.GrpID.name] = entGrpID
    postfileVals[constOU.POSTFILE.Format.name] = var
    postfileVals[constOU.POSTFILE.Filnam.name] = entFilnam
    postfileVals[constOU.POSTFILE.Funit.name] = entFunit

# ======================================================================================================================
def makePLOTFILE(frm):
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.pack(side=LEFT)

    radbtnVar = IntVar()
    radbtnPERIOD = Radiobutton(frm1, text=constOU.PLOTFILE.PERIOD.name, var=radbtnVar, value=1)
    radbtnPERIOD.pack(side=LEFT, padx=3, pady=3)
    radbtnAveper = Radiobutton(frm1, text=constOU.PLOTFILE.Aveper.name, var=radbtnVar, value=2)
    radbtnAveper.pack(side=LEFT, padx=3, pady=3)
    entAveper = Entry(frm1, width=50)
    entAveper.pack(side=LEFT, padx=3, pady=3)

    lblGrpID = Label(frm, text=constOU.PLOTFILE.GrpID.name)
    lblGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm, width=15)
    entGrpID.pack(side=LEFT, padx=3, pady=3)

    lblHivalu = Label(frm, text=constOU.PLOTFILE.Hivalu.name)
    lblHivalu.pack(side=LEFT, padx=3, pady=3)
    entHivalu = Entry(frm, width=50)
    entHivalu.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.PLOTFILE.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.PLOTFILE.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    plotfileVals['radbtnVar'] = radbtnVar
    plotfileVals[constOU.PLOTFILE.Aveper.name] = entAveper
    plotfileVals[constOU.PLOTFILE.GrpID.name] = entGrpID
    plotfileVals[constOU.PLOTFILE.Hivalu.name] = entHivalu
    plotfileVals[constOU.PLOTFILE.Filnam.name] = entFilnam
    plotfileVals[constOU.PLOTFILE.Funit.name] = entFunit

# ======================================================================================================================
def makeTOXXFILE(frm):
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.pack(side=LEFT)

    radbtnVar = IntVar()
    radbtnPERIOD = Radiobutton(frm1, text=constOU.TOXXFILE.PERIOD.name, var=radbtnVar, value=1)
    radbtnPERIOD.pack(side=LEFT, padx=3, pady=3)
    radbtnAveper = Radiobutton(frm1, text=constOU.TOXXFILE.Aveper.name, var=radbtnVar, value=2)
    radbtnAveper.pack(side=LEFT, padx=3, pady=3)
    entAveper = Entry(frm1, width=50)
    entAveper.pack(side=LEFT, padx=3, pady=3)

    lblCutoff = Label(frm, text=constOU.TOXXFILE.Cutoff.name)
    lblCutoff.pack(side=LEFT, padx=3, pady=3)
    entCutoff = Entry(frm, width=15)
    entCutoff.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.TOXXFILE.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.TOXXFILE.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    toxxfileVals['radbtnVar'] = radbtnVar
    toxxfileVals[constOU.TOXXFILE.Aveper.name] = entAveper
    toxxfileVals[constOU.TOXXFILE.Cutoff.name] = entCutoff
    toxxfileVals[constOU.TOXXFILE.Filnam.name] = entFilnam
    toxxfileVals[constOU.TOXXFILE.Funit.name] = entFunit

# ======================================================================================================================
def makeRANKFILE(frm):
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.pack(side=LEFT)

    radbtnVar = IntVar()
    radbtnPERIOD = Radiobutton(frm1, text=constOU.RANKFILE.PERIOD.name, var=radbtnVar, value=1)
    radbtnPERIOD.pack(side=LEFT, padx=3, pady=3)
    radbtnAveper = Radiobutton(frm1, text=constOU.RANKFILE.Aveper.name, var=radbtnVar, value=2)
    radbtnAveper.pack(side=LEFT, padx=3, pady=3)
    entAveper = Entry(frm1, width=50)
    entAveper.pack(side=LEFT, padx=3, pady=3)

    lblHinum = Label(frm, text=constOU.RANKFILE.Hinum.name)
    lblHinum.pack(side=LEFT, padx=3, pady=3)
    entHinum = Entry(frm, width=15)
    entHinum.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.RANKFILE.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.RANKFILE.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    rankfileVals['radbtnVar'] = radbtnVar
    rankfileVals[constOU.RANKFILE.Aveper.name] = entAveper
    rankfileVals[constOU.RANKFILE.Hinum.name] = entHinum
    rankfileVals[constOU.RANKFILE.Filnam.name] = entFilnam
    rankfileVals[constOU.RANKFILE.Funit.name] = entFunit

# ======================================================================================================================
def makeEVALFILE(frm):
    lblSrcID = Label(frm, text=constOU.EVALFILE.SrcID.name)
    lblSrcID.pack(side=LEFT, padx=3, pady=3)
    entSrcID = Entry(frm, width=15)
    entSrcID.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.EVALFILE.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.EVALFILE.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    evalfileVals[constOU.EVALFILE.SrcID.name] = entSrcID
    evalfileVals[constOU.EVALFILE.Filnam.name] = entFilnam
    evalfileVals[constOU.EVALFILE.Funit.name] = entFunit

# ======================================================================================================================
def makeSEASONHR(frm):
    lblGrpID = Label(frm, text=constOU.SEASONHR.GrpID.name)
    lblGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm, width=15)
    entGrpID.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.SEASONHR.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.SEASONHR.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    seasonhrVals[constOU.SEASONHR.GrpID.name] = entGrpID
    seasonhrVals[constOU.SEASONHR.Filnam.name] = entFilnam
    seasonhrVals[constOU.SEASONHR.Funit.name] = entFunit

# ======================================================================================================================
def makeMAXDAILY(frm):
    lblGrpID = Label(frm, text=constOU.MAXDAILY.GrpID.name)
    lblGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm, width=15)
    entGrpID.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.MAXDAILY.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.MAXDAILY.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    maxdailyVals[constOU.MAXDAILY.GrpID.name] = entGrpID
    maxdailyVals[constOU.MAXDAILY.Filnam.name] = entFilnam
    maxdailyVals[constOU.MAXDAILY.Funit.name] = entFunit

# ======================================================================================================================
def makeMXDYBYYR(frm):
    lblGrpID = Label(frm, text=constOU.MXDYBYYR.GrpID.name)
    lblGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm, width=15)
    entGrpID.pack(side=LEFT, padx=3, pady=3)

    lblFilnam = Label(frm, text=constOU.MXDYBYYR.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm, width=50)
    entFilnam.pack(side=LEFT, padx=3, pady=3)

    lblFunit = Label(frm, text=constOU.MXDYBYYR.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm, width=15)
    entFunit.pack(side=LEFT, padx=3, pady=3)

    mxdybyyrVals[constOU.MXDYBYYR.GrpID.name] = entGrpID
    mxdybyyrVals[constOU.MXDYBYYR.Filnam.name] = entFilnam
    mxdybyyrVals[constOU.MXDYBYYR.Funit.name] = entFunit

# ======================================================================================================================
def makeMAXDCONT(frm):
    frm00 = Frame(frm)
    frm00.grid(row=0, column=0, sticky=W+E)
    lblGrpID = Label(frm00, text=constOU.MAXDCONT.GrpID.name)
    lblGrpID.pack(side=LEFT, padx=3, pady=3)
    entGrpID = Entry(frm00, width=20)
    entGrpID.pack(side=RIGHT, padx=3, pady=3)

    frm01 = Frame(frm)
    frm01.grid(row=0, column=1, sticky=W + E)
    lblUpperRank = Label(frm01, text=constOU.MAXDCONT.UpperRank.name)
    lblUpperRank.pack(side=LEFT, padx=3, pady=3)
    entUpperRank = Entry(frm01, width=20)
    entUpperRank.pack(side=RIGHT, padx=3, pady=3)

    radbtnVar = IntVar()

    frm02 = Frame(frm)
    frm02.grid(row=0, column=2, sticky=W + E)
    radbtnLowerRank = Radiobutton(frm02, text=constOU.MAXDCONT.LowerRank.name, var=radbtnVar, value=1)
    radbtnLowerRank.pack(side=LEFT, padx=3, pady=3)
    entLowerRank = Entry(frm02, width=20)
    entLowerRank.pack(side=RIGHT, padx=3, pady=3)

    frm12 = Frame(frm)
    frm12.grid(row=1, column=2, sticky=W + E)
    radbtnThresValue = Radiobutton(frm12, text=constOU.MAXDCONT.ThreshValue.name, var=radbtnVar, value=2)
    radbtnThresValue.pack(side=LEFT, padx=3, pady=3)
    entThresValue = Entry(frm12, width=20)
    entThresValue.pack(side=RIGHT, padx=3, pady=3)

    frm03 = Frame(frm)
    frm03.grid(row=0, column=3, sticky=W + E)
    lblFilnam = Label(frm03, text=constOU.MAXDCONT.Filnam.name)
    lblFilnam.pack(side=LEFT, padx=3, pady=3)
    entFilnam = Entry(frm03, width=50)
    entFilnam.pack(side=RIGHT, padx=3, pady=3)

    frm04 = Frame(frm)
    frm04.grid(row=0, column=4, sticky=W + E)
    lblFunit = Label(frm04, text=constOU.MAXDCONT.Funit.name)
    lblFunit.pack(side=LEFT, padx=3, pady=3)
    entFunit = Entry(frm04, width=15)
    entFunit.pack(side=RIGHT, padx=3, pady=3)

    maxdcontVals['radbtnVar'] = radbtnVar
    maxdcontVals[constOU.MAXDCONT.GrpID.name] = entGrpID
    maxdcontVals[constOU.MAXDCONT.UpperRank.name] = entUpperRank
    maxdcontVals[constOU.MAXDCONT.LowerRank.name] = entLowerRank
    maxdcontVals[constOU.MAXDCONT.ThreshValue.name] = entThresValue
    maxdcontVals[constOU.MAXDCONT.Filnam.name] = entFilnam
    maxdcontVals[constOU.MAXDCONT.Funit.name] = entFunit

def makeSUMMFILE(frm):
    lbl = Label(frm, text=constOU.SUMMFILE.SummFilename.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=100)
    ent.pack(side=LEFT, padx=3, pady=3)
    summfileVals[constOU.SUMMFILE.SummFilename.name] = ent

def makeFILEFORM(frm):
    lbl = Label(frm, text=constOU.FILEFORM.FILEFORM.name)
    lbl.pack(side=LEFT, padx=3, pady=3)

    choices = ['EXP', 'FIX']
    var = StringVar()
    var.set(choices[0])
    opt = OptionMenu(frm, var, *choices)
    opt.pack(side=LEFT, padx=3, pady=3)

    fileformVals[constOU.FILEFORM.FILEFORM.name] = var

# ======================================================================================================================
def makeNOHEADER(frm):
    frm0 = Frame(frm)
    frm0.grid(row=0, column=0, sticky=W+E)

    radbtnVar = IntVar()

    radbtnSelect = Radiobutton(frm0, text='FileType', var=radbtnVar, value=1)
    radbtnSelect.pack(side=LEFT, padx=3, pady=3)

    chkPOSTFILE = BooleanVar()
    chkPOSTFILE.set(False)
    chkbtnPOSTFILE = Checkbutton(frm0, text=constOU.NOHEADER.POSTFILE.name, var=chkPOSTFILE)
    chkbtnPOSTFILE.pack(side=LEFT, padx=3, pady=3)

    chkPLOTFILE = BooleanVar()
    chkPLOTFILE.set(False)
    chkbtnPLOTFILE = Checkbutton(frm0, text=constOU.NOHEADER.PLOTFILE.name, var=chkPLOTFILE)
    chkbtnPLOTFILE.pack(side=LEFT, padx=3, pady=3)

    chkMAXIFILE = BooleanVar()
    chkMAXIFILE.set(False)
    chkbtnMAXIFILE = Checkbutton(frm0, text=constOU.NOHEADER.MAXIFILE.name, var=chkMAXIFILE)
    chkbtnMAXIFILE.pack(side=LEFT, padx=3, pady=3)

    chkRANKFILE = BooleanVar()
    chkRANKFILE.set(False)
    chkbtnRANKFILE = Checkbutton(frm0, text=constOU.NOHEADER.RANKFILE.name, var=chkRANKFILE)
    chkbtnRANKFILE.pack(side=LEFT, padx=3, pady=3)

    chkSEASONHR = BooleanVar()
    chkSEASONHR.set(False)
    chkbtnSEASONHR = Checkbutton(frm0, text=constOU.NOHEADER.SEASONHR.name, var=chkSEASONHR)
    chkbtnSEASONHR.pack(side=LEFT, padx=3, pady=3)

    chkMAXDAILY = BooleanVar()
    chkMAXDAILY.set(False)
    chkbtnMAXDAILY = Checkbutton(frm0, text=constOU.NOHEADER.MAXDAILY.name, var=chkMAXDAILY)
    chkbtnMAXDAILY.pack(side=LEFT, padx=3, pady=3)

    chkMXDYBYYR = BooleanVar()
    chkMXDYBYYR.set(False)
    chkbtnMXDYBYYR = Checkbutton(frm0, text=constOU.NOHEADER.MXDYBYYR.name, var=chkMXDYBYYR)
    chkbtnMXDYBYYR.pack(side=LEFT, padx=3, pady=3)

    chkMAXDCONT = BooleanVar()
    chkMAXDCONT.set(False)
    chkbtnMAXDCONT = Checkbutton(frm0, text=constOU.NOHEADER.MAXDCONT.name, var=chkMAXDCONT)
    chkbtnMAXDCONT.pack(side=LEFT, padx=3, pady=3)

    frm1 = Frame(frm)
    frm1.grid(row=1, column=0, sticky=W + E)
    radbtnAll = Radiobutton(frm1, text=constOU.NOHEADER.ALL.name, var=radbtnVar, value=2)
    radbtnAll.pack(side=LEFT, padx=3, pady=3)

    noheaderVals['radbtnVar'] = radbtnVar
    noheaderVals[constOU.NOHEADER.POSTFILE.name] = chkPOSTFILE
    noheaderVals[constOU.NOHEADER.PLOTFILE.name] = chkPLOTFILE
    noheaderVals[constOU.NOHEADER.MAXIFILE.name] = chkMAXIFILE
    noheaderVals[constOU.NOHEADER.RANKFILE.name] = chkRANKFILE
    noheaderVals[constOU.NOHEADER.SEASONHR.name] = chkSEASONHR
    noheaderVals[constOU.NOHEADER.MAXDAILY.name] = chkMAXDAILY
    noheaderVals[constOU.NOHEADER.MXDYBYYR.name] = chkMXDYBYYR
    noheaderVals[constOU.NOHEADER.MAXDCONT.name] = chkMAXDCONT

# ======================================================================================================================
def makeEVENTOUT(frm):
    lbl = Label(frm, text=constOU.EVENTOUT.EVENTOUT.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    choices = ['SOCONT', 'DETAIL']
    var = StringVar()
    var.set(choices[0])
    opt = OptionMenu(frm, var, *choices)
    opt.pack(side=LEFT, padx=3, pady=3)

    eventoutVals[constOU.EVENTOUT.EVENTOUT.name] = var

# ======================================================================================================================
rectableVals = {}
maxtableVals = {}
daytableVals = {}
maxifileVals = {}
postfileVals = {}
plotfileVals = {}
toxxfileVals = {}
rankfileVals = {}
evalfileVals = {}
seasonhrVals = {}
maxdailyVals = {}
mxdybyyrVals = {}
maxdcontVals = {}
summfileVals = {}
fileformVals = {}
noheaderVals = {}
eventoutVals = {}

# ======================================================================================================================
def buildTabOU(tabOU):
    frmIntro = LabelFrame(tabOU, bd=0)
    frmIntro.pack(side=TOP, padx=5, pady=0, fill='both')
    introText = Label(frmIntro, text='\nOutput Options (OU)\n')
    introText.pack(side=LEFT, expand=True)

    # creates scrollable frame for inputs
    frmInputs = Frame(tabOU, bd=0)
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

    frmRECTABLE = LabelFrame(scrollFrmInputs, bd=1, text='RECTABLE')
    frmRECTABLE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeRECTABLE(frmRECTABLE)

    frmMAXTABLE = LabelFrame(scrollFrmInputs, bd=1, text='MAXTABLE')
    frmMAXTABLE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeMAXTABLE(frmMAXTABLE)

    frmDAYTABLE = LabelFrame(scrollFrmInputs, bd=1, text='DAYTABLE')
    frmDAYTABLE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeDAYTABLE(frmDAYTABLE)

    frmMAXIFILE = LabelFrame(scrollFrmInputs, bd=1, text='MAXIFILE')
    frmMAXIFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeMAXIFILE(frmMAXIFILE)

    frmPOSTFILE = LabelFrame(scrollFrmInputs, bd=1, text='POSTFILE')
    frmPOSTFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makePOSTFILE(frmPOSTFILE)

    frmPLOTFILE = LabelFrame(scrollFrmInputs, bd=1, text='PLOTFILE')
    frmPLOTFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makePLOTFILE(frmPLOTFILE)

    frmTOXXFILE = LabelFrame(scrollFrmInputs, bd=1, text='TOXXFILE')
    frmTOXXFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeTOXXFILE(frmTOXXFILE)

    frmRANKFILE = LabelFrame(scrollFrmInputs, bd=1, text='RANKFILE')
    frmRANKFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeRANKFILE(frmRANKFILE)

    frmEVALFILE = LabelFrame(scrollFrmInputs, bd=1, text='EVALFILE')
    frmEVALFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeEVALFILE(frmEVALFILE)

    frmSEASONHR = LabelFrame(scrollFrmInputs, bd=1, text='SEASONHR')
    frmSEASONHR.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSEASONHR(frmSEASONHR)

    frmMAXDAILY = LabelFrame(scrollFrmInputs, bd=1, text='MAXDAILY')
    frmMAXDAILY.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeMAXDAILY(frmMAXDAILY)

    frmMXDYBYYR = LabelFrame(scrollFrmInputs, bd=1, text='MXDYBYYR')
    frmMXDYBYYR.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeMXDYBYYR(frmMXDYBYYR)

    frmMAXDCONT = LabelFrame(scrollFrmInputs, bd=1, text='MAXDCONT')
    frmMAXDCONT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeMAXDCONT(frmMAXDCONT)

    frmSUMMFILE = LabelFrame(scrollFrmInputs, bd=1, text='SUMMFILE')
    frmSUMMFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSUMMFILE(frmSUMMFILE)

    frmFILEFORM = LabelFrame(scrollFrmInputs, bd=1, text='FILEFORM')
    frmFILEFORM.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeFILEFORM(frmFILEFORM)

    frmNOHEADER = LabelFrame(scrollFrmInputs, bd=1, text='NOHEADER')
    frmNOHEADER.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeNOHEADER(frmNOHEADER)

    frmEVENTOUT = LabelFrame(scrollFrmInputs, bd=1, text='EVENTOUT')
    frmEVENTOUT.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeEVENTOUT(frmEVENTOUT)

    ouInputs = (rectableVals, maxtableVals, daytableVals, maxifileVals, postfileVals, plotfileVals, toxxfileVals,
                rankfileVals, evalfileVals, seasonhrVals, maxdailyVals, mxdybyyrVals, maxdcontVals, summfileVals,
                fileformVals, noheaderVals, eventoutVals)

    frmButtons = Frame(tabOU, bd=0)
    frmButtons.pack(side=TOP, padx=5, pady=3, fill="both")
    btn1 = Button(frmButtons, text='Write OU to control file', font=('calibri', 11, 'bold'), width=40,
                  command=(lambda: ouWriter.writeControlFile(ouInputs)))
    btn1.pack(side=TOP, padx=60, pady=3)