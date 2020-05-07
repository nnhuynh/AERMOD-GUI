import constantsEV as constEV

# ======================================================================================================================
def writeEVENTPER(eventper):
    with open('control.inp', 'a') as f:
        if len(eventper[constEV.EVENTPER.Evname_1.name].get()) > 0:
            f.write('EV EVENTPER %s %s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_1.name].get(),
                                                    eventper[constEV.EVENTPER.Aveper_1.name].get(),
                                                    eventper[constEV.EVENTPER.Grpid_1.name].get(),
                                                    eventper[constEV.EVENTPER.Date_1.name].get(),
                                                    eventper[constEV.EVENTPER.Conc_1.name].get()))


        if len(eventper[constEV.EVENTPER.Evname_2.name].get()) > 0:
            f.write('EV EVENTPER %s %s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_2.name].get(),
                                                    eventper[constEV.EVENTPER.Aveper_2.name].get(),
                                                    eventper[constEV.EVENTPER.Grpid_2.name].get(),
                                                    eventper[constEV.EVENTPER.Date_2.name].get(),
                                                    eventper[constEV.EVENTPER.Conc_2.name].get()))

        if len(eventper[constEV.EVENTPER.Evname_3.name].get()) > 0:
            f.write('EV EVENTPER %s %s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_3.name].get(),
                                                    eventper[constEV.EVENTPER.Aveper_3.name].get(),
                                                    eventper[constEV.EVENTPER.Grpid_3.name].get(),
                                                    eventper[constEV.EVENTPER.Date_3.name].get(),
                                                    eventper[constEV.EVENTPER.Conc_3.name].get()))

# ======================================================================================================================
def writeEVENTLOC(eventloc, eventper):
    with open('control.inp', 'a') as f:
        # event_1
        if len(eventper[constEV.EVENTPER.Evname_1.name].get()) > 0:
            if eventloc['radbtnVar_1'].get()==1:
                f.write('EV EVENTLOC %s XR=%s YR=%s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Xr_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Yr_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zelev_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zhill_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zflag_1.name].get()))
            elif eventloc['radbtnVar_1'].get()==2:
                f.write('EV EVENTLOC %s RNG=%s DIR=%s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Rng_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Dir_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zelev_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zhill_1.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zflag_1.name].get()))

        # event_2
        if len(eventper[constEV.EVENTPER.Evname_2.name].get()) > 0:
            if eventloc['radbtnVar_2'].get() == 1:
                f.write('EV EVENTLOC %s XR=%s YR=%s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Xr_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Yr_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zelev_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zhill_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zflag_2.name].get()))
            elif eventloc['radbtnVar_2'].get() == 2:
                f.write('EV EVENTLOC %s RNG=%s DIR=%s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Rng_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Dir_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zelev_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zhill_2.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zflag_2.name].get()))

        # event_3
        if len(eventper[constEV.EVENTPER.Evname_3.name].get()) > 0:
            if eventloc['radbtnVar_3'].get() == 1:
                f.write('EV EVENTLOC %s XR=%s YR=%s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Xr_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Yr_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zelev_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zhill_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zflag_3.name].get()))
            elif eventloc['radbtnVar_3'].get() == 2:
                f.write('EV EVENTLOC %s RNG=%s DIR=%s %s %s %s\n' % (eventper[constEV.EVENTPER.Evname_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Rng_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Dir_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zelev_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zhill_3.name].get(),
                                                             eventloc[constEV.EVENTLOC.Zflag_3.name].get()))

# ======================================================================================================================
def writeINCLUDED(included):
    if len(included[constEV.INCLUDED.EventIncFile.name].get()) > 0:
        with open('control.inp', 'a') as f:
            f.write('EV INCLUDED %s\n' % included[constEV.INCLUDED.EventIncFile.name].get())

# ======================================================================================================================
def writeControlFile(evInputs):
    with open('control.inp', 'a') as f:
        f.write('\nEV STARTING\n')

    eventper = evInputs[0]
    writeEVENTPER(eventper)

    eventloc = evInputs[1]
    writeEVENTLOC(eventloc, eventper)

    included = evInputs[2]
    writeINCLUDED(included)

    with open('control.inp', 'a') as f:
        f.write('EV FINISHED\n')