import constantsCO as constCO

# ======================================================================================================================
def writeCO_Titles(titles):
    with open('control.inp', 'a') as f:
        for kw in titles.keys():
            f.write('CO %s %s\n' % (kw, titles[kw].get()))

# ======================================================================================================================
def writeCO_MODELOPT(modelopt):
    dfault = modelopt[constCO.MODELOPT.DFAULT.name]
    alpha = modelopt[constCO.MODELOPT.ALPHA.name]
    beta = modelopt[constCO.MODELOPT.BETA.name]
    conc = modelopt[constCO.MODELOPT.CONC.name]
    depos = modelopt[constCO.MODELOPT.DEPOS.name]
    ddep = modelopt[constCO.MODELOPT.DDEP.name]
    wdep = modelopt[constCO.MODELOPT.WDEP.name]
    areadplt = modelopt[constCO.MODELOPT.AREADPLT.name]
    flat = modelopt[constCO.MODELOPT.FLAT.name]
    elev = modelopt[constCO.MODELOPT.ELEV.name]
    nostd = modelopt[constCO.MODELOPT.NOSTD.name]
    nochkd = modelopt[constCO.MODELOPT.NOCHKD.name]
    warnchkd = modelopt[constCO.MODELOPT.WARNCHKD.name]
    nowarn = modelopt[constCO.MODELOPT.NOWARN.name]
    screen = modelopt[constCO.MODELOPT.SCREEN.name]
    scim = modelopt[constCO.MODELOPT.SCIM.name]
    nourbtran = modelopt[constCO.MODELOPT.NOURBTRAN.name]
    vectorws = modelopt[constCO.MODELOPT.VECTORWS.name]
    psdcredit = modelopt[constCO.MODELOPT.PSDCREDIT.name]

    modelOptStr = 'CO MODELOPT'

    with open('control.inp', 'a') as f:
        if dfault.get():
            modelOptStr = modelOptStr + ' DFAULT'
        if dfault.get() == False and alpha.get():
            modelOptStr = modelOptStr + ' ALPHA'
        if dfault.get() == False and beta.get():
            modelOptStr = modelOptStr + ' BETA'
        if conc.get():
            modelOptStr = modelOptStr + ' CONC'
        if depos.get():
            modelOptStr = modelOptStr + ' DEPOS'
        if ddep.get():
            modelOptStr = modelOptStr + ' DDEP'
        if wdep.get():
            modelOptStr = modelOptStr + ' WDEP'
        if dfault.get() == False and areadplt.get():
            modelOptStr = modelOptStr + ' AREADPLT'
        if dfault.get() == False and flat.get():
            modelOptStr = modelOptStr + ' FLAT'
        if elev.get():
            modelOptStr = modelOptStr + ' ELEV'
        if dfault.get() == False and nostd.get():
            modelOptStr = modelOptStr + ' NOSTD'
        if dfault.get() == False and nochkd.get():
            modelOptStr = modelOptStr + ' NOCHKD'
        if warnchkd.get():
            modelOptStr = modelOptStr + ' WARNCHKD'
        if nowarn.get():
            modelOptStr = modelOptStr + ' NOWARN'
        if dfault.get() == False and screen.get():
            modelOptStr = modelOptStr + ' SCREEN'
        if dfault.get() == False and scim.get():
            modelOptStr = modelOptStr + ' SCIM'

        if modelopt['radbtnVar1'].get() == 1:
            modelOptStr = modelOptStr + ' PVMRM'
        elif modelopt['radbtnVar1'].get() == 2:
            modelOptStr = modelOptStr + ' OLM'
        elif modelopt['radbtnVar1'].get() == 3:
            modelOptStr = modelOptStr + ' ARM2'

        if dfault.get() == False:
            if modelopt['radbtnVar2'].get() == 1:
                modelOptStr = modelOptStr + ' FASTALL'
            elif modelopt['radbtnVar2'].get() == 2:
                modelOptStr = modelOptStr + ' FASTAREA'

        if modelopt['radbtnVar3'].get() == 1:
            modelOptStr = modelOptStr + ' DRYDPLT'
        elif modelopt['radbtnVar3'].get() == 2:
            modelOptStr = modelOptStr + ' NODRYDPLT'

        if modelopt['radbtnVar4'].get() == 1:
            modelOptStr = modelOptStr + ' WETDPLT'
        elif modelopt['radbtnVar4'].get() == 2:
            modelOptStr = modelOptStr + ' NOWETDPLT'

        if dfault.get() == False and nourbtran.get():
            modelOptStr = modelOptStr + ' NOURBTRAN'

        if vectorws.get():
            modelOptStr = modelOptStr + ' VECTORWS'

        if dfault.get() == False and psdcredit.get():
            modelOptStr = modelOptStr + ' PSDCREDIT'

        f.write('%s\n' % modelOptStr)

# ======================================================================================================================
def writeCO_AVERTIME(avertime):
    hr1 = avertime[constCO.AVERTIME._1Hr.name]
    hr2 = avertime[constCO.AVERTIME._2Hr.name]
    hr3 = avertime[constCO.AVERTIME._3Hr.name]
    hr4 = avertime[constCO.AVERTIME._4Hr.name]
    hr6 = avertime[constCO.AVERTIME._6Hr.name]
    hr8 = avertime[constCO.AVERTIME._8Hr.name]
    hr12 = avertime[constCO.AVERTIME._12Hr.name]
    hr24 = avertime[constCO.AVERTIME._24Hr.name]
    month = avertime[constCO.AVERTIME.MONTH.name]
    radbtnVar1 = avertime['radbtnVar1']

    avertimeStr = 'CO AVERTIME'
    with open('control.inp', 'a') as f:
        if hr1.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME._1Hr.value
        if hr2.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME._2Hr.value
        if hr3.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME._3Hr.value
        if hr4.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME._4Hr.value
        if hr6.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME._6Hr.value
        if hr8.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME._8Hr.value
        if hr12.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME._12Hr.value
        if hr24.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME._24Hr.value
        if month.get():
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME.MONTH.value
        if radbtnVar1.get() == 1:
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME.PERIOD.value
        elif radbtnVar1.get() == 2:
            avertimeStr = avertimeStr + ' ' + constCO.AVERTIME.ANNUAL.value

        f.write('%s\n' % avertimeStr)

# ======================================================================================================================
def writeCO_URBANOPT(urbanoptVals):
    with open('control.inp', 'a') as f:
        f.write('CO URBANOPT %s %s %s\n' % (urbanoptVals['urbpop'].get(),
                                            urbanoptVals['urbname'].get(),
                                            urbanoptVals['urbroughness'].get()))

# ======================================================================================================================
def writeCO_POLLUTID(pollutidVals):
    pollutidStr = 'CO POLLUTID'

    if pollutidVals['radbtnVar1'].get()==1:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.PM10.name
    elif pollutidVals['radbtnVar1'].get()==2:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.PM25.name
    elif pollutidVals['radbtnVar1'].get()==3:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.NO2.name
    elif pollutidVals['radbtnVar1'].get()==4:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.SO2.name
    elif pollutidVals['radbtnVar1'].get()==5:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.LEAD.name
    elif pollutidVals['radbtnVar1'].get()==6:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.OTHER.name
    elif pollutidVals['radbtnVar1'].get()==7:
        pollutidStr = pollutidStr + ' ' + pollutidVals['entry'].get()

    if pollutidVals['radbtnVar2'].get()==1:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.H1H.name
    elif pollutidVals['radbtnVar2'].get()==2:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.H2H.name
    elif pollutidVals['radbtnVar2'].get()==3:
        pollutidStr = pollutidStr + ' ' + constCO.POLLUTID.INC.name

    with open('control.inp', 'a') as f:
        f.write('%s\n' % pollutidStr)


# ======================================================================================================================
def writeCO_HALFLIFE(halflife):
    halflifeStr = 'CO HALFLIFE %s' % halflife['entry'].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % halflifeStr)

# ======================================================================================================================
def writeCO_DCAYCOEF(dcaycoef):
    dcaycoefStr = 'CO DCAYCOEF %s' % dcaycoef['entry'].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % dcaycoefStr)

# ======================================================================================================================
def writeCO_GASDEPDF(gasdepdf):
    gasdepdfStr = 'CO GASDEPDF %s %s %s %s' % (gasdepdf[constCO.GASDEPDF.React.name].get(),
                                               gasdepdf[constCO.GASDEPDF.F_Seas2.name].get(),
                                               gasdepdf[constCO.GASDEPDF.F_Seas5.name].get(),
                                               gasdepdf[constCO.GASDEPDF.Refpoll.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % gasdepdfStr)

# ======================================================================================================================
def writeCO_GDLANUSE(gdlanuse):
    gdlanuseStr = 'CO GDLANUSE'
    for iSec in range(36):
        secID = 'Sec%d' % (iSec+1)
        gdlanuseStr = gdlanuseStr + ' ' + gdlanuse[secID].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % gdlanuseStr)

# ======================================================================================================================
def writeCO_GDSEASON(gdseason):
    gdseasonStr = 'CO GDSEASON'
    for month in constCO.GDSEASON:
        gdseasonStr = gdseasonStr + ' ' + gdseason[month.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % gdseasonStr)

# ======================================================================================================================
def writeCO_LOW_WIND(low_wind):
    low_windStr = 'CO LOW_WIND %s %s %s' % (low_wind[constCO.LOW_WIND.SVmin.name].get(),
                                            low_wind[constCO.LOW_WIND.WSmin.name].get(),
                                            low_wind[constCO.LOW_WIND.FRANmax.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % low_windStr)

# ======================================================================================================================
def writeCO_AWMADWNW(awmadwnw):
    awmadwnwStr = 'CO AWMADWNW'
    if awmadwnw[constCO.AWMADWNW.AWMAUEFF.name].get():
        awmadwnwStr = awmadwnwStr + ' ' + constCO.AWMADWNW.AWMAUEFF.name
    if awmadwnw[constCO.AWMADWNW.AWMAUTURB.name].get():
        awmadwnwStr = awmadwnwStr + ' ' + constCO.AWMADWNW.AWMAUTURB.name
    if awmadwnw[constCO.AWMADWNW.STREAMLINE.name].get():
        awmadwnwStr = awmadwnwStr + ' ' + constCO.AWMADWNW.STREAMLINE.name
    with open('control.inp', 'a') as f:
        f.write('%s\n' % awmadwnwStr)

# ======================================================================================================================
def writeCO_ORD_DWNW(ord_dwnw):
    ord_dwnwStr = 'CO ORD_DWNW'
    if ord_dwnw[constCO.ORD_DWNW.ORDUEFF.name].get():
        ord_dwnwStr = ord_dwnwStr + ' ' + constCO.ORD_DWNW.ORDUEFF.name
    if ord_dwnw[constCO.ORD_DWNW.ORDTURB.name].get():
        ord_dwnwStr = ord_dwnwStr + ' ' + constCO.ORD_DWNW.ORDTURB.name
    if ord_dwnw[constCO.ORD_DWNW.ORDCAV.name].get():
        ord_dwnwStr = ord_dwnwStr + ' ' + constCO.ORD_DWNW.ORDCAV.name
    with open('control.inp', 'a') as f:
        f.write('%s\n' % ord_dwnwStr)

# ======================================================================================================================
def writeCO_NO2EQUIL(no2equil):
    no2equilStr = 'CO NO2EQUIL %s' % no2equil['entry'].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % no2equilStr)

# ======================================================================================================================
def writeCO_NO2STACK(no2stack):
    no2stackStr = 'CO NO2STACK %s' % no2stack['entry'].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % no2stackStr)

# ======================================================================================================================
def writeCO_ARMRATIO(armratio):
    armratioStr = 'CO ARMRATIO %s %s' % (armratio[constCO.ARMRATIO.ARM2_Min.name].get(),
                                         armratio[constCO.ARMRATIO.ARM2_Max.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % armratioStr)

# ======================================================================================================================
def writeCO_O3SECTOR(o3sector):
    o3sectorStr = 'CO O3SECTOR %s %s %s %s %s %s' % (o3sector[constCO.O3SECTOR.StartSect1.name].get(),
                                                     o3sector[constCO.O3SECTOR.StartSect2.name].get(),
                                                     o3sector[constCO.O3SECTOR.StartSect3.name].get(),
                                                     o3sector[constCO.O3SECTOR.StartSect4.name].get(),
                                                     o3sector[constCO.O3SECTOR.StartSect5.name].get(),
                                                     o3sector[constCO.O3SECTOR.StartSect6.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % o3sectorStr)

# ======================================================================================================================
def writeCO_OZONEFIL(ozonefil):
    ozonefilStr = 'CO OZONEFIL %s %s %s' % (ozonefil[constCO.OZONEFIL.O3FileName.name].get(),
                                            ozonefil[constCO.OZONEFIL.O3Units.name].get(),
                                            ozonefil[constCO.OZONEFIL.O3Format.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % ozonefilStr)

# ======================================================================================================================
def writeCO_OZONEVAL(ozoneval):
    ozonevalStr = 'CO OZONEVAL %s %s' % (ozoneval[constCO.OZONEVAL.O3Value.name].get(),
                                         ozoneval[constCO.OZONEVAL.O3Units.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % ozonevalStr)

# ======================================================================================================================
def writeCO_O3VALUES(o3values):
    o3valuesStr = 'CO O3VALUES %s %s' % (o3values[constCO.O3VALUES.O3Flag.name].get(),
                                         o3values[constCO.O3VALUES.O3values.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % o3valuesStr)

# ======================================================================================================================
def writeCOL_OZONUNIT(ozonunit):
    ozonunitStr = 'CO OZONUNIT %s' % ozonunit[constCO.OZONUNIT.Ozonunit.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % ozonunitStr)

# ======================================================================================================================
def writeCO_FLAGPOLE(flagpole):
    flagpoleStr = 'CO FLAGPOLE %s' % flagpole[constCO.FLAGPOLE.Flagpole.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % flagpoleStr)

# ======================================================================================================================
def writeCO_RUNORNOT(runornot):
    runornotStr = 'CO RUNORNOT %s' % runornot['RUNORNOT'].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % runornotStr)

# ======================================================================================================================
def writeCO_EVENTFIL(eventfil):
    eventfilStr = 'CO EVENTFIL %s %s' % (eventfil[constCO.EVENTFIL.Evfile.name].get(),
                                         eventfil[constCO.EVENTFIL.Evopt.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % eventfilStr)

# ======================================================================================================================
def writeCO_SAVEFILE(savefile):
    savefileStr = 'CO SAVEFILE %s %s %s' % (savefile[constCO.SAVEFILE.Savfil.name].get(),
                                            savefile[constCO.SAVEFILE.Dayinc.name].get(),
                                            savefile[constCO.SAVEFILE.Savfl2.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % savefileStr)

# ======================================================================================================================
def writeCO_INITFILE(initfile):
    initfileStr = 'CO INITFILE %s' % initfile[constCO.INITFILE.INITFILE.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % initfileStr)

# ======================================================================================================================
def writeCO_ERRORFIL(errorfil):
    errorfilStr = 'CO ERRORFIL %s' % errorfil[constCO.ERRORFIL.ERRORFIL.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % errorfilStr)

# ======================================================================================================================
def writeCO_MULTYEAR(multyear):
    multyearStr = 'CO MULTYEAR'

    if multyear[constCO.MULTYEAR.H6H.name]:
        multyearStr = multyearStr + ' ' + constCO.MULTYEAR.H6H.name

    multyearStr = '%s %s %s' % (multyearStr,
                                multyear[constCO.MULTYEAR.Savfil.name].get(),
                                multyear[constCO.MULTYEAR.Inifil.name].get())

    with open('control.inp', 'a') as f:
        f.write('%s\n' % multyearStr)


# ======================================================================================================================
def writeCO_DEBUGOPT(debugopt):
    debugoptStr = 'CO DEBUGOPT'
    if debugopt[constCO.DEBUGOPT.MODEL.name].get():
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.MODEL.name + ' ' + debugopt[constCO.DEBUGOPT.Dbgfil.name].get()
    if debugopt[constCO.DEBUGOPT.METEOR.name].get():
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.METEOR.name + ' ' + debugopt[constCO.DEBUGOPT.Dbmfil.name].get()
    if debugopt[constCO.DEBUGOPT.PRIME.name].get():
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.PRIME.name + ' ' + debugopt[constCO.DEBUGOPT.Prmfil.name].get()
    if debugopt[constCO.DEBUGOPT.AWMADW.name].get():
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.AWMADW.name + ' ' + debugopt[constCO.DEBUGOPT.AwmaDwfil.name].get()
    if debugopt[constCO.DEBUGOPT.DEPOS.name].get():
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.DEPOS.name

    if debugopt['radbtnVar1'].get()==1:
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.AREA.name + ' ' + debugopt[constCO.DEBUGOPT.AreaDbfil.name].get()
    elif debugopt['radbtnVar1'].get()==2:
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.LINE.name

    if debugopt['radbtnVar2'].get()==1:
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.PVMRM.name + ' ' + debugopt[constCO.DEBUGOPT.Dbpvfil.name].get()
    elif debugopt['radbtnVar2'].get()==2:
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.OLM.name + ' ' + debugopt[constCO.DEBUGOPT.OLMfil.name].get()
    elif debugopt['radbtnVar2'].get()==3:
        debugoptStr = debugoptStr + ' ' + constCO.DEBUGOPT.ARM2.name + ' ' + debugopt[constCO.DEBUGOPT.ARM2fil.name].get()

    with open('control.inp', 'a') as f:
        f.write('%s\n' % debugoptStr)

# ======================================================================================================================
def writeControlFile(coInputs, soInputs=None, reInputs=None, meInputs=None, evInputs=None, ouInputs=None):
    with open('control.inp', 'w') as f:
        f.write('CO STARTING\n')

    titles = coInputs[0]
    writeCO_Titles(titles)

    modelopt = coInputs[1]
    writeCO_MODELOPT(modelopt)

    avertime = coInputs[2]
    writeCO_AVERTIME(avertime)

    urbanopt = coInputs[3]
    writeCO_URBANOPT(urbanopt)

    pollutid = coInputs[4]
    writeCO_POLLUTID(pollutid)

    halflife = coInputs[5]
    writeCO_HALFLIFE(halflife)

    dcaycoef = coInputs[6]
    writeCO_DCAYCOEF(dcaycoef)

    gasdepdf = coInputs[7]
    writeCO_GASDEPDF(gasdepdf)

    gdlanuse = coInputs[8]
    writeCO_GDLANUSE(gdlanuse)

    gdseason = coInputs[9]
    writeCO_GDSEASON(gdseason)

    low_wind = coInputs[10]
    writeCO_LOW_WIND(low_wind)

    awmadwnw = coInputs[11]
    writeCO_AWMADWNW(awmadwnw)

    ord_dwnw = coInputs[12]
    writeCO_ORD_DWNW(ord_dwnw)

    no2equil = coInputs[13]
    writeCO_NO2EQUIL(no2equil)

    no2stack = coInputs[14]
    writeCO_NO2STACK(no2stack)

    armratio = coInputs[15]
    writeCO_ARMRATIO(armratio)

    o3sector = coInputs[16]
    writeCO_O3SECTOR(o3sector)

    ozonefil = coInputs[17]
    writeCO_OZONEFIL(ozonefil)

    ozoneval = coInputs[18]
    writeCO_OZONEVAL(ozoneval)

    o3values = coInputs[19]
    writeCO_O3VALUES(o3values)

    ozonunit = coInputs[20]
    writeCOL_OZONUNIT(ozonunit)

    flagpole = coInputs[21]
    writeCO_FLAGPOLE(flagpole)

    runornot = coInputs[22]
    writeCO_RUNORNOT(runornot)

    eventfil = coInputs[23]
    writeCO_EVENTFIL(eventfil)

    savefile= coInputs[24]
    writeCO_SAVEFILE(savefile)

    initfile = coInputs[25]
    writeCO_INITFILE(initfile)

    errorfil = coInputs[26]
    writeCO_ERRORFIL(errorfil)

    multyear = coInputs[27]
    writeCO_MULTYEAR(multyear)

    debugopt = coInputs[28]
    writeCO_DEBUGOPT(debugopt)

    with open('control.inp', 'a') as f:
        f.write('CO FINISHED\n')

        '''
        f.write('\n')
        f.write('RE STARTING\n')
        f.write('RE FINISHED\n')

        f.write('\n')
        f.write('ME STARTING\n')
        f.write('ME FINISHED\n')

        f.write('\n')
        f.write('EV STARTING\n')
        f.write('EV FINISHED\n')

        f.write('\n')
        f.write('OU STARTING\n')
        f.write('OU FINISHED\n')
        '''