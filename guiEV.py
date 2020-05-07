from tkinter import *
import constantsEV as constEV
import evWriter

# ======================================================================================================================
def makeEVENTPER(frm):
    # event_1 ==========================================================================================================
    frm1 = Frame(frm)
    frm1.grid(row=0, column=0, sticky=W+E)

    lblEvname_1 = Label(frm1, text=constEV.EVENTPER.Evname_1.name)
    lblEvname_1.pack(side=LEFT, padx=3, pady=3)
    entEvname_1 = Entry(frm1, width=20)
    entEvname_1.pack(side=LEFT, padx=3, pady=3)

    lblAveper_1 = Label(frm1, text=constEV.EVENTPER.Aveper_1.name)
    lblAveper_1.pack(side=LEFT, padx=3, pady=3)
    entAveper_1 = Entry(frm1, width=20)
    entAveper_1.pack(side=LEFT, padx=3, pady=3)

    lblGrpid_1 = Label(frm1, text=constEV.EVENTPER.Grpid_1.name)
    lblGrpid_1.pack(side=LEFT, padx=3, pady=3)
    entGrpid_1 = Entry(frm1, width=20)
    entGrpid_1.pack(side=LEFT, padx=3, pady=3)

    lblDate_1 = Label(frm1, text=constEV.EVENTPER.Date_1.name)
    lblDate_1.pack(side=LEFT, padx=3, pady=3)
    entDate_1 = Entry(frm1, width=20)
    entDate_1.pack(side=LEFT, padx=3, pady=3)

    lblConc_1 = Label(frm1, text=constEV.EVENTPER.Conc_1.name)
    lblConc_1.pack(side=LEFT, padx=3, pady=3)
    entConc_1 = Entry(frm1, width=20)
    entConc_1.pack(side=LEFT, padx=3, pady=3)

    eventperVals[constEV.EVENTPER.Evname_1.name] = entEvname_1
    eventperVals[constEV.EVENTPER.Aveper_1.name] = entAveper_1
    eventperVals[constEV.EVENTPER.Grpid_1.name] = entGrpid_1
    eventperVals[constEV.EVENTPER.Date_1.name] = entDate_1
    eventperVals[constEV.EVENTPER.Conc_1.name] = entConc_1

    # event_2 ==========================================================================================================
    frm2 = Frame(frm)
    frm2.grid(row=1, column=0, sticky=W + E)

    lblEvname_2 = Label(frm2, text=constEV.EVENTPER.Evname_2.name)
    lblEvname_2.pack(side=LEFT, padx=3, pady=3)
    entEvname_2 = Entry(frm2, width=20)
    entEvname_2.pack(side=LEFT, padx=3, pady=3)

    lblAveper_2 = Label(frm2, text=constEV.EVENTPER.Aveper_2.name)
    lblAveper_2.pack(side=LEFT, padx=3, pady=3)
    entAveper_2 = Entry(frm2, width=20)
    entAveper_2.pack(side=LEFT, padx=3, pady=3)

    lblGrpid_2 = Label(frm2, text=constEV.EVENTPER.Grpid_2.name)
    lblGrpid_2.pack(side=LEFT, padx=3, pady=3)
    entGrpid_2 = Entry(frm2, width=20)
    entGrpid_2.pack(side=LEFT, padx=3, pady=3)

    lblDate_2 = Label(frm2, text=constEV.EVENTPER.Date_2.name)
    lblDate_2.pack(side=LEFT, padx=3, pady=3)
    entDate_2 = Entry(frm2, width=20)
    entDate_2.pack(side=LEFT, padx=3, pady=3)

    lblConc_2 = Label(frm2, text=constEV.EVENTPER.Conc_2.name)
    lblConc_2.pack(side=LEFT, padx=3, pady=3)
    entConc_2 = Entry(frm2, width=20)
    entConc_2.pack(side=LEFT, padx=3, pady=3)

    eventperVals[constEV.EVENTPER.Evname_2.name] = entEvname_2
    eventperVals[constEV.EVENTPER.Aveper_2.name] = entAveper_2
    eventperVals[constEV.EVENTPER.Grpid_2.name] = entGrpid_2
    eventperVals[constEV.EVENTPER.Date_2.name] = entDate_2
    eventperVals[constEV.EVENTPER.Conc_2.name] = entConc_2

    # event_3 ==========================================================================================================
    frm3 = Frame(frm)
    frm3.grid(row=2, column=0, sticky=W + E)

    lblEvname_3 = Label(frm3, text=constEV.EVENTPER.Evname_3.name)
    lblEvname_3.pack(side=LEFT, padx=3, pady=3)
    entEvname_3 = Entry(frm3, width=20)
    entEvname_3.pack(side=LEFT, padx=3, pady=3)

    lblAveper_3 = Label(frm3, text=constEV.EVENTPER.Aveper_3.name)
    lblAveper_3.pack(side=LEFT, padx=3, pady=3)
    entAveper_3 = Entry(frm3, width=20)
    entAveper_3.pack(side=LEFT, padx=3, pady=3)

    lblGrpid_3 = Label(frm3, text=constEV.EVENTPER.Grpid_3.name)
    lblGrpid_3.pack(side=LEFT, padx=3, pady=3)
    entGrpid_3 = Entry(frm3, width=20)
    entGrpid_3.pack(side=LEFT, padx=3, pady=3)

    lblDate_3 = Label(frm3, text=constEV.EVENTPER.Date_3.name)
    lblDate_3.pack(side=LEFT, padx=3, pady=3)
    entDate_3 = Entry(frm3, width=20)
    entDate_3.pack(side=LEFT, padx=3, pady=3)

    lblConc_3 = Label(frm3, text=constEV.EVENTPER.Conc_3.name)
    lblConc_3.pack(side=LEFT, padx=3, pady=3)
    entConc_3 = Entry(frm3, width=20)
    entConc_3.pack(side=LEFT, padx=3, pady=3)

    eventperVals[constEV.EVENTPER.Evname_3.name] = entEvname_3
    eventperVals[constEV.EVENTPER.Aveper_3.name] = entAveper_3
    eventperVals[constEV.EVENTPER.Grpid_3.name] = entGrpid_3
    eventperVals[constEV.EVENTPER.Date_3.name] = entDate_3
    eventperVals[constEV.EVENTPER.Conc_3.name] = entConc_3


def makeEVENTLOC(frm):
    # event_1 ==========================================================================================================
    frm1 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm1.grid(row=0, column=0, padx=3, pady=3, sticky=W + E)
    radbtnVar_1 = IntVar()

    frm100 = Frame(frm1)
    frm100.grid(row=0, column=0, sticky=W+E)
    lblEvname_1 = Label(frm100, text=constEV.EVENTLOC.Evname_1.name)
    lblEvname_1.pack(side=LEFT, padx=3, pady=3)

    frm110 = Frame(frm1)
    frm110.grid(row=1, column=0, sticky=W+E)
    radbtnXr_1 = Radiobutton(frm110, text=constEV.EVENTLOC.Xr_1.name, var=radbtnVar_1, value=1)
    radbtnXr_1.pack(side=LEFT, padx=3, pady=3)
    entXr_1 = Entry(frm110, width=20)
    entXr_1.pack(side=RIGHT, padx=3, pady=3)

    frm111 = Frame(frm1)
    frm111.grid(row=1, column=1, sticky=W + E)
    lblYr_1 = Label(frm111, text=constEV.EVENTLOC.Yr_1.name)
    lblYr_1.pack(side=LEFT, padx=3, pady=3)
    entYr_1 = Entry(frm111, width=20)
    entYr_1.pack(side=RIGHT, padx=3, pady=3)

    frm120 = Frame(frm1)
    frm120.grid(row=2, column=0, sticky=W + E)
    radbtnRng_1 = Radiobutton(frm120, text=constEV.EVENTLOC.Rng_1.name, var=radbtnVar_1, value=2)
    radbtnRng_1.pack(side=LEFT, padx=3, pady=3)
    entRng_1 = Entry(frm120, width=20)
    entRng_1.pack(side=RIGHT, padx=3, pady=3)

    frm121 = Frame(frm1)
    frm121.grid(row=2, column=1, sticky=W + E)
    lblDir_1 = Label(frm121, text=constEV.EVENTLOC.Dir_1.name)
    lblDir_1.pack(side=LEFT, padx=3, pady=3)
    entDir_1 = Entry(frm121, width=20)
    entDir_1.pack(side=RIGHT, padx=3, pady=3)

    frm130 = Frame(frm1)
    frm130.grid(row=3, column=0, sticky=W + E)
    lblZelev_1 = Label(frm130, text=constEV.EVENTLOC.Zelev_1.name)
    lblZelev_1.pack(side=LEFT, padx=3, pady=3)
    entZelev_1 = Entry(frm130, width=20)
    entZelev_1.pack(side=RIGHT, padx=3, pady=3)

    frm131 = Frame(frm1)
    frm131.grid(row=3, column=1, sticky=W + E)
    lblZhill_1 = Label(frm131, text=constEV.EVENTLOC.Zhill_1.name)
    lblZhill_1.pack(side=LEFT, padx=3, pady=3)
    entZhill_1 = Entry(frm131, width=20)
    entZhill_1.pack(side=RIGHT, padx=3, pady=3)

    frm132 = Frame(frm1)
    frm132.grid(row=3, column=2, sticky=W + E)
    lblZflag_1 = Label(frm132, text=constEV.EVENTLOC.Zflag_1.name)
    lblZflag_1.pack(side=LEFT, padx=3, pady=3)
    entZflag_1 = Entry(frm132, width=20)
    entZflag_1.pack(side=RIGHT, padx=3, pady=3)

    eventlocVals['radbtnVar_1'] = radbtnVar_1
    eventlocVals[constEV.EVENTLOC.Xr_1.name] = entXr_1
    eventlocVals[constEV.EVENTLOC.Yr_1.name] = entYr_1
    eventlocVals[constEV.EVENTLOC.Rng_1.name] = entRng_1
    eventlocVals[constEV.EVENTLOC.Dir_1.name] = entDir_1
    eventlocVals[constEV.EVENTLOC.Zelev_1.name] = entZelev_1
    eventlocVals[constEV.EVENTLOC.Zhill_1.name] = entZhill_1
    eventlocVals[constEV.EVENTLOC.Zflag_1.name] = entZflag_1

    # event_2 ==========================================================================================================
    frm2 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm2.grid(row=0, column=1, padx=3, pady=3, sticky=W + E)
    radbtnVar_2 = IntVar()

    frm200 = Frame(frm2)
    frm200.grid(row=0, column=0, sticky=W + E)
    lblEvname_2 = Label(frm200, text=constEV.EVENTLOC.Evname_2.name)
    lblEvname_2.pack(side=LEFT, padx=3, pady=3)

    frm210 = Frame(frm2)
    frm210.grid(row=1, column=0, sticky=W + E)
    radbtnXr_2 = Radiobutton(frm210, text=constEV.EVENTLOC.Xr_2.name, var=radbtnVar_2, value=1)
    radbtnXr_2.pack(side=LEFT, padx=3, pady=3)
    entXr_2 = Entry(frm210, width=20)
    entXr_2.pack(side=RIGHT, padx=3, pady=3)

    frm211 = Frame(frm2)
    frm211.grid(row=1, column=1, sticky=W + E)
    lblYr_2 = Label(frm211, text=constEV.EVENTLOC.Yr_2.name)
    lblYr_2.pack(side=LEFT, padx=3, pady=3)
    entYr_2 = Entry(frm211, width=20)
    entYr_2.pack(side=RIGHT, padx=3, pady=3)

    frm220 = Frame(frm2)
    frm220.grid(row=2, column=0, sticky=W + E)
    radbtnRng_2 = Radiobutton(frm220, text=constEV.EVENTLOC.Rng_2.name, var=radbtnVar_2, value=2)
    radbtnRng_2.pack(side=LEFT, padx=3, pady=3)
    entRng_2 = Entry(frm220, width=20)
    entRng_2.pack(side=RIGHT, padx=3, pady=3)

    frm221 = Frame(frm2)
    frm221.grid(row=2, column=1, sticky=W + E)
    lblDir_2 = Label(frm221, text=constEV.EVENTLOC.Dir_2.name)
    lblDir_2.pack(side=LEFT, padx=3, pady=3)
    entDir_2 = Entry(frm221, width=20)
    entDir_2.pack(side=RIGHT, padx=3, pady=3)

    frm230 = Frame(frm2)
    frm230.grid(row=3, column=0, sticky=W + E)
    lblZelev_2 = Label(frm230, text=constEV.EVENTLOC.Zelev_2.name)
    lblZelev_2.pack(side=LEFT, padx=3, pady=3)
    entZelev_2 = Entry(frm230, width=20)
    entZelev_2.pack(side=RIGHT, padx=3, pady=3)

    frm231 = Frame(frm2)
    frm231.grid(row=3, column=1, sticky=W + E)
    lblZhill_2 = Label(frm231, text=constEV.EVENTLOC.Zhill_2.name)
    lblZhill_2.pack(side=LEFT, padx=3, pady=3)
    entZhill_2 = Entry(frm231, width=20)
    entZhill_2.pack(side=RIGHT, padx=3, pady=3)

    frm232 = Frame(frm2)
    frm232.grid(row=3, column=2, sticky=W + E)
    lblZflag_2 = Label(frm232, text=constEV.EVENTLOC.Zflag_2.name)
    lblZflag_2.pack(side=LEFT, padx=3, pady=3)
    entZflag_2 = Entry(frm232, width=20)
    entZflag_2.pack(side=RIGHT, padx=3, pady=3)

    eventlocVals['radbtnVar_2'] = radbtnVar_2
    eventlocVals[constEV.EVENTLOC.Xr_2.name] = entXr_2
    eventlocVals[constEV.EVENTLOC.Yr_2.name] = entYr_2
    eventlocVals[constEV.EVENTLOC.Rng_2.name] = entRng_2
    eventlocVals[constEV.EVENTLOC.Dir_2.name] = entDir_2
    eventlocVals[constEV.EVENTLOC.Zelev_2.name] = entZelev_2
    eventlocVals[constEV.EVENTLOC.Zhill_2.name] = entZhill_2
    eventlocVals[constEV.EVENTLOC.Zflag_2.name] = entZflag_2

    # event_3 ==========================================================================================================
    frm3 = Frame(frm, relief=GROOVE, borderwidth=1)
    frm3.grid(row=0, column=2, padx=3, pady=3, sticky=W + E)
    radbtnVar_3 = IntVar()

    frm300 = Frame(frm3)
    frm300.grid(row=0, column=0, sticky=W + E)
    lblEvname_3 = Label(frm300, text=constEV.EVENTLOC.Evname_3.name)
    lblEvname_3.pack(side=LEFT, padx=3, pady=3)

    frm310 = Frame(frm3)
    frm310.grid(row=1, column=0, sticky=W + E)
    radbtnXr_3 = Radiobutton(frm310, text=constEV.EVENTLOC.Xr_3.name, var=radbtnVar_3, value=1)
    radbtnXr_3.pack(side=LEFT, padx=3, pady=3)
    entXr_3 = Entry(frm310, width=20)
    entXr_3.pack(side=RIGHT, padx=3, pady=3)

    frm311 = Frame(frm3)
    frm311.grid(row=1, column=1, sticky=W + E)
    lblYr_3 = Label(frm311, text=constEV.EVENTLOC.Yr_3.name)
    lblYr_3.pack(side=LEFT, padx=3, pady=3)
    entYr_3 = Entry(frm311, width=20)
    entYr_3.pack(side=RIGHT, padx=3, pady=3)

    frm320 = Frame(frm3)
    frm320.grid(row=2, column=0, sticky=W + E)
    radbtnRng_3 = Radiobutton(frm320, text=constEV.EVENTLOC.Rng_3.name, var=radbtnVar_3, value=2)
    radbtnRng_3.pack(side=LEFT, padx=3, pady=3)
    entRng_3 = Entry(frm320, width=20)
    entRng_3.pack(side=RIGHT, padx=3, pady=3)

    frm321 = Frame(frm3)
    frm321.grid(row=2, column=1, sticky=W + E)
    lblDir_3 = Label(frm321, text=constEV.EVENTLOC.Dir_3.name)
    lblDir_3.pack(side=LEFT, padx=3, pady=3)
    entDir_3 = Entry(frm321, width=20)
    entDir_3.pack(side=RIGHT, padx=3, pady=3)

    frm330 = Frame(frm3)
    frm330.grid(row=3, column=0, sticky=W + E)
    lblZelev_3 = Label(frm330, text=constEV.EVENTLOC.Zelev_3.name)
    lblZelev_3.pack(side=LEFT, padx=3, pady=3)
    entZelev_3 = Entry(frm330, width=20)
    entZelev_3.pack(side=RIGHT, padx=3, pady=3)

    frm331 = Frame(frm3)
    frm331.grid(row=3, column=1, sticky=W + E)
    lblZhill_3 = Label(frm331, text=constEV.EVENTLOC.Zhill_3.name)
    lblZhill_3.pack(side=LEFT, padx=3, pady=3)
    entZhill_3 = Entry(frm331, width=20)
    entZhill_3.pack(side=RIGHT, padx=3, pady=3)

    frm332 = Frame(frm3)
    frm332.grid(row=3, column=2, sticky=W + E)
    lblZflag_3 = Label(frm332, text=constEV.EVENTLOC.Zflag_3.name)
    lblZflag_3.pack(side=LEFT, padx=3, pady=3)
    entZflag_3 = Entry(frm332, width=20)
    entZflag_3.pack(side=RIGHT, padx=3, pady=3)

    eventlocVals['radbtnVar_3'] = radbtnVar_3
    eventlocVals[constEV.EVENTLOC.Xr_3.name] = entXr_3
    eventlocVals[constEV.EVENTLOC.Yr_3.name] = entYr_3
    eventlocVals[constEV.EVENTLOC.Rng_3.name] = entRng_3
    eventlocVals[constEV.EVENTLOC.Dir_3.name] = entDir_3
    eventlocVals[constEV.EVENTLOC.Zelev_3.name] = entZelev_3
    eventlocVals[constEV.EVENTLOC.Zhill_3.name] = entZhill_3
    eventlocVals[constEV.EVENTLOC.Zflag_3.name] = entZflag_3

# ======================================================================================================================
def makeINCLUDED(frm):
    lbl = Label(frm, text=constEV.INCLUDED.EventIncFile.name)
    lbl.pack(side=LEFT, padx=3, pady=3)
    ent = Entry(frm, width=100)
    ent.pack(side=LEFT, padx=3, pady=3)

    includedVals[constEV.INCLUDED.EventIncFile.name] = ent

# ======================================================================================================================
eventperVals = {}
eventlocVals = {}
includedVals = {}

# ======================================================================================================================
def buildTabEV(tabEV):
    frmIntro = LabelFrame(tabEV, bd=0)
    frmIntro.pack(side=TOP, padx=5, pady=0, fill='both')
    introText = Label(frmIntro, text='\nEvent Pathway (EV) Keywords and Parameters\n')
    introText.pack(side=LEFT, expand=True)

    # creates scrollable frame for inputs
    frmInputs = Frame(tabEV, bd=0)
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

    frmEVENTPER = LabelFrame(scrollFrmInputs, bd=1, text='EVENTPER')
    frmEVENTPER.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeEVENTPER(frmEVENTPER)

    frmEVENTLOC = LabelFrame(scrollFrmInputs, bd=1, text='EVENTLOC')
    frmEVENTLOC.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeEVENTLOC(frmEVENTLOC)

    frmINCLUDED = LabelFrame(scrollFrmInputs, bd=1, text='INCLUDED')
    frmINCLUDED.pack(side=TOP, anchor=W, padx=5, pady=5, expand='yes', fill='both')
    makeINCLUDED(frmINCLUDED)

    evInputs = (eventperVals, eventlocVals, includedVals)

    frmButtons = Frame(tabEV, bd=0)
    frmButtons.pack(side=TOP, padx=5, pady=3, fill="both")
    btn1 = Button(frmButtons, text='Write EV to control file', font=('calibri', 11, 'bold'), width=40,
                  command=(lambda: evWriter.writeControlFile(evInputs)))
    btn1.pack(side=TOP, padx=60, pady=3)
