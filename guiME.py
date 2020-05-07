from tkinter import *
import constantsME as constME
import meWriter

# ======================================================================================================================
def makeSURFFILE(frm):
    lbl = Label(frm, text=constME.SURFFILE.Sfcfil.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=50)
    ent.pack(side=LEFT, padx=3, pady=3)
    surffileVals[constME.SURFFILE.Sfcfil.name] = ent

# ======================================================================================================================
def makePROFFILE(frm):
    lbl = Label(frm, text=constME.PROFFILE.Profil.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=50)
    ent.pack(side=LEFT, padx=3, pady=3)
    proffileVals[constME.PROFFILE.Profil.name] = ent

# ======================================================================================================================
def makeSURFDATA(frm):
    lblStanum = Label(frm, text=constME.SURFDATA.Stanum.name)
    lblStanum.pack(side=LEFT, padx=3, pady=3)
    entStanum = Entry(frm, width=20)
    entStanum.pack(side=LEFT, padx=3, pady=3)

    lblYear = Label(frm, text=constME.SURFDATA.Year.name)
    lblYear.pack(side=LEFT, padx=3, pady=3)
    entYear = Entry(frm, width=20)
    entYear.pack(side=LEFT, padx=3, pady=3)

    lblName = Label(frm, text=constME.SURFDATA.Name.name)
    lblName.pack(side=LEFT, padx=3, pady=3)
    entName = Entry(frm, width=20)
    entName.pack(side=LEFT, padx=3, pady=3)

    lblXcoord = Label(frm, text=constME.SURFDATA.Xcoord.name)
    lblXcoord.pack(side=LEFT, padx=3, pady=3)
    entXcoord = Entry(frm, width=20)
    entXcoord.pack(side=LEFT, padx=3, pady=3)

    lblYcoord = Label(frm, text=constME.SURFDATA.Ycoord.name)
    lblYcoord.pack(side=LEFT, padx=3, pady=3)
    entYcoord = Entry(frm, width=20)
    entYcoord.pack(side=LEFT, padx=3, pady=3)

    surfdataVals[constME.SURFDATA.Stanum.name] = entStanum
    surfdataVals[constME.SURFDATA.Year.name] = entYear
    surfdataVals[constME.SURFDATA.Name.name] = entName
    surfdataVals[constME.SURFDATA.Xcoord.name] = entXcoord
    surfdataVals[constME.SURFDATA.Ycoord.name] = entYcoord

# ======================================================================================================================
def makeUAIRDATA(frm):
    lblStanum = Label(frm, text=constME.UAIRDATA.Stanum.name)
    lblStanum.pack(side=LEFT, padx=3, pady=3)
    entStanum = Entry(frm, width=20)
    entStanum.pack(side=LEFT, padx=3, pady=3)

    lblYear = Label(frm, text=constME.UAIRDATA.Year.name)
    lblYear.pack(side=LEFT, padx=3, pady=3)
    entYear = Entry(frm, width=20)
    entYear.pack(side=LEFT, padx=3, pady=3)

    lblName = Label(frm, text=constME.UAIRDATA.Name.name)
    lblName.pack(side=LEFT, padx=3, pady=3)
    entName = Entry(frm, width=20)
    entName.pack(side=LEFT, padx=3, pady=3)

    lblXcoord = Label(frm, text=constME.UAIRDATA.Xcoord.name)
    lblXcoord.pack(side=LEFT, padx=3, pady=3)
    entXcoord = Entry(frm, width=20)
    entXcoord.pack(side=LEFT, padx=3, pady=3)

    lblYcoord = Label(frm, text=constME.UAIRDATA.Ycoord.name)
    lblYcoord.pack(side=LEFT, padx=3, pady=3)
    entYcoord = Entry(frm, width=20)
    entYcoord.pack(side=LEFT, padx=3, pady=3)

    uairdataVals[constME.UAIRDATA.Stanum.name] = entStanum
    uairdataVals[constME.UAIRDATA.Year.name] = entYear
    uairdataVals[constME.UAIRDATA.Name.name] = entName
    uairdataVals[constME.UAIRDATA.Xcoord.name] = entXcoord
    uairdataVals[constME.UAIRDATA.Ycoord.name] = entYcoord

# ======================================================================================================================
def makeSITEDATA(frm):
    lblStanum = Label(frm, text=constME.SITEDATA.Stanum.name)
    lblStanum.pack(side=LEFT, padx=3, pady=3)
    entStanum = Entry(frm, width=20)
    entStanum.pack(side=LEFT, padx=3, pady=3)

    lblYear = Label(frm, text=constME.SITEDATA.Year.name)
    lblYear.pack(side=LEFT, padx=3, pady=3)
    entYear = Entry(frm, width=20)
    entYear.pack(side=LEFT, padx=3, pady=3)

    lblName = Label(frm, text=constME.SITEDATA.Name.name)
    lblName.pack(side=LEFT, padx=3, pady=3)
    entName = Entry(frm, width=20)
    entName.pack(side=LEFT, padx=3, pady=3)

    lblXcoord = Label(frm, text=constME.SITEDATA.Xcoord.name)
    lblXcoord.pack(side=LEFT, padx=3, pady=3)
    entXcoord = Entry(frm, width=20)
    entXcoord.pack(side=LEFT, padx=3, pady=3)

    lblYcoord = Label(frm, text=constME.SITEDATA.Ycoord.name)
    lblYcoord.pack(side=LEFT, padx=3, pady=3)
    entYcoord = Entry(frm, width=20)
    entYcoord.pack(side=LEFT, padx=3, pady=3)

    sitedataVals[constME.SITEDATA.Stanum.name] = entStanum
    sitedataVals[constME.SITEDATA.Year.name] = entYear
    sitedataVals[constME.SITEDATA.Name.name] = entName
    sitedataVals[constME.SITEDATA.Xcoord.name] = entXcoord
    sitedataVals[constME.SITEDATA.Ycoord.name] = entYcoord

# ======================================================================================================================
def makePROFBASE(frm):
    lblBase = Label(frm, text=constME.PROFBASE.BaseElev.name)
    lblBase.pack(side=LEFT, padx=3, pady=3)
    entBase = Entry(frm, width=20)
    entBase.pack(side=LEFT, padx=3, pady=3)

    lblUnits = Label(frm, text=constME.PROFBASE.Units.name)
    lblUnits.pack(side=LEFT, padx=3, pady=3)
    choices = ['METERS', 'FEET']
    var = StringVar()
    var.set(choices[0])
    opt = OptionMenu(frm, var, *choices)
    opt.pack(side=LEFT, padx=3, pady=3)

    profbaseVals[constME.PROFBASE.BaseElev.name] = entBase
    profbaseVals[constME.PROFBASE.Units.name] = var

# ======================================================================================================================
def makeSTARTEND(frm):
    lblStrtyr = Label(frm, text=constME.STARTEND.Strtyr.name)
    lblStrtyr.pack(side=LEFT, padx=3, pady=3)
    entStrtyr = Entry(frm, width=15)
    entStrtyr.pack(side=LEFT, padx=3, pady=3)

    lblStrtmn = Label(frm, text=constME.STARTEND.Strtmn.name)
    lblStrtmn.pack(side=LEFT, padx=3, pady=3)
    entStrtmn = Entry(frm, width=15)
    entStrtmn.pack(side=LEFT, padx=3, pady=3)

    lblStrtdy = Label(frm, text=constME.STARTEND.Strtdy.name)
    lblStrtdy.pack(side=LEFT, padx=3, pady=3)
    entStrtdy = Entry(frm, width=15)
    entStrtdy.pack(side=LEFT, padx=3, pady=3)

    lblStrthr = Label(frm, text=constME.STARTEND.Strthr.name)
    lblStrthr.pack(side=LEFT, padx=3, pady=3)
    entStrthr = Entry(frm, width=15)
    entStrthr.pack(side=LEFT, padx=3, pady=3)

    lblEndyr = Label(frm, text=constME.STARTEND.Endyr.name)
    lblEndyr.pack(side=LEFT, padx=3, pady=3)
    entEndyr = Entry(frm, width=15)
    entEndyr.pack(side=LEFT, padx=3, pady=3)

    lblEndmn = Label(frm, text=constME.STARTEND.Endmn.name)
    lblEndmn.pack(side=LEFT, padx=3, pady=3)
    entEndmn = Entry(frm, width=15)
    entEndmn.pack(side=LEFT, padx=3, pady=3)

    lblEnddy = Label(frm, text=constME.STARTEND.Enddy.name)
    lblEnddy.pack(side=LEFT, padx=3, pady=3)
    entEnddy = Entry(frm, width=15)
    entEnddy.pack(side=LEFT, padx=3, pady=3)

    lblEndhr = Label(frm, text=constME.STARTEND.Endhr.name)
    lblEndhr.pack(side=LEFT, padx=3, pady=3)
    entEndhr = Entry(frm, width=15)
    entEndhr.pack(side=LEFT, padx=3, pady=3)

    startendVals[constME.STARTEND.Strtyr.name] = entStrtyr
    startendVals[constME.STARTEND.Strtmn.name] = entStrtmn
    startendVals[constME.STARTEND.Strtdy.name] = entStrtdy
    startendVals[constME.STARTEND.Strthr.name] = entStrthr

    startendVals[constME.STARTEND.Endyr.name] = entEndyr
    startendVals[constME.STARTEND.Endmn.name] = entEndmn
    startendVals[constME.STARTEND.Enddy.name] = entEnddy
    startendVals[constME.STARTEND.Endhr.name] = entEndhr

# ======================================================================================================================
def makeDAYRANGE(frm):
    lbl = Label(frm, text=constME.DAYRANGE.DAYRANGE.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=100)
    ent.pack(side=LEFT, padx=3, pady=3)
    dayrangeVals[constME.DAYRANGE.DAYRANGE.name] = ent

# ======================================================================================================================
def makeNUMYEARS(frm):
    lbl = Label(frm, text=constME.NUMYEARS.NumYrs.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=100)
    ent.pack(side=LEFT, padx=3, pady=3)
    numyearsVals[constME.NUMYEARS.NumYrs.name] = ent

# ======================================================================================================================
def makeSCIMBYHR(frm):
    lblNRegStart = Label(frm, text=constME.SCIMBYHR.NRegStart.name)
    lblNRegStart.pack(side=LEFT, padx=3, pady=3)
    entNRegStart = Entry(frm, width=15)
    entNRegStart.pack(side=LEFT, padx=3, pady=3)

    lblNRegInt = Label(frm, text=constME.SCIMBYHR.NRegInt.name)
    lblNRegInt.pack(side=LEFT, padx=3, pady=3)
    entNRegInt = Entry(frm, width=15)
    entNRegInt.pack(side=LEFT, padx=3, pady=3)

    lblSfcFilnam = Label(frm, text=constME.SCIMBYHR.SfcFilnam.name)
    lblSfcFilnam.pack(side=LEFT, padx=3, pady=3)
    entSfcFilnam = Entry(frm, width=50)
    entSfcFilnam.pack(side=LEFT, padx=3, pady=3)

    lblPflFilnam = Label(frm, text=constME.SCIMBYHR.PflFilnam.name)
    lblPflFilnam.pack(side=LEFT, padx=3, pady=3)
    entPflFilnam = Entry(frm, width=50)
    entPflFilnam.pack(side=LEFT, padx=3, pady=3)

    scimbyhrVals[constME.SCIMBYHR.NRegStart.name] = entNRegStart
    scimbyhrVals[constME.SCIMBYHR.NRegInt.name] = entNRegInt
    scimbyhrVals[constME.SCIMBYHR.SfcFilnam.name] = entSfcFilnam
    scimbyhrVals[constME.SCIMBYHR.PflFilnam.name] = entPflFilnam

# ======================================================================================================================
def makeWDROTATE(frm):
    lbl = Label(frm, text=constME.WDROTATE.Rotang.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=15)
    ent.pack(side=LEFT, padx=3, pady=3)
    wdrotateVals[constME.WDROTATE.Rotang.name] = ent

# ======================================================================================================================
def makeWINDCATS(frm):
    lblWs1 = Label(frm, text=constME.WINDCATS.Ws1.name)
    lblWs1.pack(side=LEFT, padx=3, pady=3)
    entWs1 = Entry(frm, width=15)
    entWs1.pack(side=LEFT, padx=3, pady=3)

    lblWs2 = Label(frm, text=constME.WINDCATS.Ws2.name)
    lblWs2.pack(side=LEFT, padx=3, pady=3)
    entWs2 = Entry(frm, width=15)
    entWs2.pack(side=LEFT, padx=3, pady=3)

    lblWs3 = Label(frm, text=constME.WINDCATS.Ws3.name)
    lblWs3.pack(side=LEFT, padx=3, pady=3)
    entWs3 = Entry(frm, width=15)
    entWs3.pack(side=LEFT, padx=3, pady=3)

    lblWs4 = Label(frm, text=constME.WINDCATS.Ws4.name)
    lblWs4.pack(side=LEFT, padx=3, pady=3)
    entWs4 = Entry(frm, width=15)
    entWs4.pack(side=LEFT, padx=3, pady=3)

    lblWs5 = Label(frm, text=constME.WINDCATS.Ws5.name)
    lblWs5.pack(side=LEFT, padx=3, pady=3)
    entWs5 = Entry(frm, width=15)
    entWs5.pack(side=LEFT, padx=3, pady=3)

    windcatsVals[constME.WINDCATS.Ws1.name] = entWs1
    windcatsVals[constME.WINDCATS.Ws2.name] = entWs2
    windcatsVals[constME.WINDCATS.Ws3.name] = entWs3
    windcatsVals[constME.WINDCATS.Ws4.name] = entWs4
    windcatsVals[constME.WINDCATS.Ws5.name] = entWs5

# ======================================================================================================================
surffileVals = {}
proffileVals = {}
surfdataVals = {}
uairdataVals = {}
sitedataVals = {}
profbaseVals = {}
startendVals = {}
dayrangeVals = {}
numyearsVals = {}
scimbyhrVals = {}
wdrotateVals = {}
windcatsVals = {}

# ======================================================================================================================
def buildTabME(tabME):
    frmIntro = LabelFrame(tabME, bd=0)
    frmIntro.pack(side=TOP, padx=5, pady=0, fill='both')
    introText = Label(frmIntro, text='\nMeteorology Pathway (ME) Keywords and Parameters\n')
    introText.pack(side=LEFT, expand='yes')

    # creates scrollable frame for inputs
    frmInputs = Frame(tabME, bd=0)
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

    frmSURFFILE = LabelFrame(scrollFrmInputs, bd=1, text='SURFFILE')
    frmSURFFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSURFFILE(frmSURFFILE)

    frmPROFFILE = LabelFrame(scrollFrmInputs, bd=1, text='PROFFILE')
    frmPROFFILE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makePROFFILE(frmPROFFILE)

    frmSURFDATA = LabelFrame(scrollFrmInputs, bd=1, text='SURFDATA')
    frmSURFDATA.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSURFDATA(frmSURFDATA)

    frmUAIRDATA = LabelFrame(scrollFrmInputs, bd=1, text='UAIRDATA')
    frmUAIRDATA.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeUAIRDATA(frmUAIRDATA)

    frmSITEDATA = LabelFrame(scrollFrmInputs, bd=1, text='SITEDATA')
    frmSITEDATA.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSITEDATA(frmSITEDATA)

    frmPROFBASE = LabelFrame(scrollFrmInputs, bd=1, text='PROFBASE')
    frmPROFBASE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makePROFBASE(frmPROFBASE)

    frmSTARTEND = LabelFrame(scrollFrmInputs, bd=1, text='STARTEND')
    frmSTARTEND.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSTARTEND(frmSTARTEND)

    frmDAYRANGE = LabelFrame(scrollFrmInputs, bd=1, text='DAYRANGE')
    frmDAYRANGE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeDAYRANGE(frmDAYRANGE)

    frmNUMYEARS = LabelFrame(scrollFrmInputs, bd=1, text='NUMYEARS')
    frmNUMYEARS.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeNUMYEARS(frmNUMYEARS)

    frmSCIMBYHR = LabelFrame(scrollFrmInputs, bd=1, text='SCIMBYHR')
    frmSCIMBYHR.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeSCIMBYHR(frmSCIMBYHR)

    frmWDROTATE = LabelFrame(scrollFrmInputs, bd=1, text='WDROTATE')
    frmWDROTATE.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeWDROTATE(frmWDROTATE)

    frmWINDCATS = LabelFrame(scrollFrmInputs, bd=1, text='WINDCATS')
    frmWINDCATS.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeWINDCATS(frmWINDCATS)

    meInputs = (surffileVals, proffileVals, surfdataVals, uairdataVals, sitedataVals, profbaseVals, startendVals,
                dayrangeVals, numyearsVals, scimbyhrVals, wdrotateVals, windcatsVals)

    frmButtons = Frame(tabME, bd=0)
    frmButtons.pack(side=TOP, padx=5, pady=3, fill="both")
    btn1 = Button(frmButtons, text='Write ME to control file', font=('calibri', 11, 'bold'), width=40,
                  command=(lambda: meWriter.writeControlFile(meInputs)))
    btn1.pack(side=TOP, padx=60, pady=3)
