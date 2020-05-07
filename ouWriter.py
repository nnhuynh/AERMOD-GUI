import constantsOU as constOU

# ======================================================================================================================
def writeRECTABLE(rectable):
    rectableStr = 'OU RECTABLE'
    valid = False
    if rectable[constOU.RECTABLE.ALLAEV.name].get()==True:
        rectableStr = rectableStr + ' ' + constOU.RECTABLE.ALLAEV.name
    if len(rectable[constOU.RECTABLE.Aveper.name].get())>0:
        valid = True
        rectableStr = rectableStr + ' ' + rectable[constOU.RECTABLE.Aveper.name].get()
    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % rectableStr)

# ======================================================================================================================
def writeMAXTABLE(maxtable):
    maxtableStr = 'OU MAXTABLE'
    valid = False
    if maxtable[constOU.MAXTABLE.ALLAEV.name].get()==True:
        maxtableStr = maxtableStr + ' ' + constOU.MAXTABLE.ALLAEV.name
    if len(maxtable[constOU.MAXTABLE.Aveper.name].get())>0:
        valid = True
        maxtableStr = maxtableStr + ' ' + maxtable[constOU.MAXTABLE.Aveper.name].get() + ' ' + \
                      maxtable[constOU.MAXTABLE.Maxnum.name].get()
    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % maxtableStr)

# ======================================================================================================================
def writeDAYTABLE(daytable):
    daytableStr = 'OU DAYTABLE'
    valid = False
    if daytable[constOU.DAYTABLE.ALLAEV.name].get()==True:
        daytableStr = daytableStr + ' ' + constOU.DAYTABLE.ALLAEV.name
    if len(daytable[constOU.DAYTABLE.Aveper.name].get())>0:
        valid = True
        daytableStr = daytableStr + ' ' + daytable[constOU.DAYTABLE.Aveper.name].get()
    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % daytableStr)

# ======================================================================================================================
def writeMAXIFILE(maxifile):
    if len(maxifile[constOU.MAXIFILE.Aveper.name].get()) > 0:
        with open('control.inp', 'a') as f:
            f.write('OU MAXIFILE %s %s %s %s %s\n' % (maxifile[constOU.MAXIFILE.Aveper.name].get(),
                                                      maxifile[constOU.MAXIFILE.GrpID.name].get(),
                                                      maxifile[constOU.MAXIFILE.Thresh.name].get(),
                                                      maxifile[constOU.MAXIFILE.Filnam.name].get(),
                                                      maxifile[constOU.MAXIFILE.Funit.name].get()))

# ======================================================================================================================
def writePOSTFILE(postfile):
    postfileStr = 'OU POSTFILE'
    valid = False
    if postfile['radbtnVar'].get()==1:
        valid = True
        postfileStr = '%s %s %s %s %s %s' % (postfileStr,
                                             constOU.POSTFILE.PERIOD.name,
                                             postfile[constOU.POSTFILE.GrpID.name].get(),
                                             postfile[constOU.POSTFILE.Format.name].get(),
                                             postfile[constOU.POSTFILE.Filnam.name].get(),
                                             postfile[constOU.POSTFILE.Funit.name].get())
    elif postfile['radbtnVar'].get()==2:
        if len(postfile[constOU.POSTFILE.Aveper.name].get()) > 0:
            valid = True
            postfileStr = '%s %s %s %s %s %s' % (postfileStr,
                                                 postfile[constOU.POSTFILE.Aveper.name].get(),
                                                 postfile[constOU.POSTFILE.GrpID.name].get(),
                                                 postfile[constOU.POSTFILE.Format.name].get(),
                                                 postfile[constOU.POSTFILE.Filnam.name].get(),
                                                 postfile[constOU.POSTFILE.Funit.name].get())

    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % postfileStr)

# ======================================================================================================================
def writePLOTFILE(plotfile):
    plotfileStr = 'OU PLOTFILE'
    valid = False
    if plotfile['radbtnVar'].get() == 1:
        valid = True
        plotfileStr = '%s %s %s %s %s' % (plotfileStr,
                                          constOU.PLOTFILE.PERIOD.name,
                                          plotfile[constOU.PLOTFILE.GrpID.name].get(),
                                          plotfile[constOU.PLOTFILE.Filnam.name].get(),
                                          plotfile[constOU.PLOTFILE.Funit.name].get())
    elif plotfile['radbtnVar'].get() == 2:
        if len(plotfile[constOU.PLOTFILE.Aveper.name].get()) > 0:
            valid = True
            plotfileStr = '%s %s %s %s %s %s' % (plotfileStr,
                                                 plotfile[constOU.PLOTFILE.Aveper.name].get(),
                                                 plotfile[constOU.PLOTFILE.GrpID.name].get(),
                                                 plotfile[constOU.PLOTFILE.Hivalu.name].get(),
                                                 plotfile[constOU.PLOTFILE.Filnam.name].get(),
                                                 plotfile[constOU.PLOTFILE.Funit.name].get())

    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % plotfileStr)

# ======================================================================================================================
def writeTOXXFILE(toxxfile):
    toxxfileStr = 'OU TOXXFILE'
    valid = False
    if toxxfile['radbtnVar'].get() == 1:
        valid = True
        toxxfileStr = '%s %s %s %s %s ' % (toxxfileStr,
                                           constOU.TOXXFILE.PERIOD.name,
                                           toxxfile[constOU.TOXXFILE.Cutoff.name].get(),
                                           toxxfile[constOU.TOXXFILE.Filnam.name].get(),
                                           toxxfile[constOU.TOXXFILE.Funit.name].get())
    elif toxxfile['radbtnVar'].get() == 2:
        if len(toxxfile[constOU.TOXXFILE.Aveper.name].get()) > 0:
            valid = True
            toxxfileStr = '%s %s %s %s %s' % (toxxfileStr,
                                              toxxfile[constOU.TOXXFILE.Aveper.name].get(),
                                              toxxfile[constOU.TOXXFILE.Cutoff.name].get(),
                                              toxxfile[constOU.TOXXFILE.Filnam.name].get(),
                                              toxxfile[constOU.TOXXFILE.Funit.name].get())

    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % toxxfileStr)

# ======================================================================================================================
def writeRANKFILE(rankfile):
    rankfileStr = 'OU RANKFILE'
    valid = False
    if rankfile['radbtnVar'].get() == 1:
        valid = True
        rankfileStr = '%s %s %s %s %s ' % (rankfileStr,
                                           constOU.RANKFILE.PERIOD.name,
                                           rankfile[constOU.RANKFILE.Hinum.name].get(),
                                           rankfile[constOU.RANKFILE.Filnam.name].get(),
                                           rankfile[constOU.RANKFILE.Funit.name].get())
    elif rankfile['radbtnVar'].get() == 2:
        if len(rankfile[constOU.RANKFILE.Aveper.name].get()) > 0:
            valid = True
            rankfileStr = '%s %s %s %s %s' % (rankfileStr,
                                              rankfile[constOU.RANKFILE.Aveper.name].get(),
                                              rankfile[constOU.RANKFILE.Hinum.name].get(),
                                              rankfile[constOU.RANKFILE.Filnam.name].get(),
                                              rankfile[constOU.RANKFILE.Funit.name].get())

    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % rankfileStr)

# ======================================================================================================================
def writeEVALFILE(evalfile):
    if len(evalfile[constOU.EVALFILE.SrcID.name].get())>0 and len(evalfile[constOU.EVALFILE.Filnam.name].get())>0:
        with open('control.inp', 'a') as f:
            f.write('OU EVALFILE %s %s %s\n' % (evalfile[constOU.EVALFILE.SrcID.name].get(),
                                                evalfile[constOU.EVALFILE.Filnam.name].get(),
                                                evalfile[constOU.EVALFILE.Funit.name].get()))

# ======================================================================================================================
def writeSEASONHR(seasonhr):
    if len(seasonhr[constOU.SEASONHR.GrpID.name].get())>0 and len(seasonhr[constOU.SEASONHR.Filnam.name].get())>0:
        with open('control.inp', 'a') as f:
            f.write('OU SEASONHR %s %s %s\n' % (seasonhr[constOU.SEASONHR.GrpID.name].get(),
                                                seasonhr[constOU.SEASONHR.Filnam.name].get(),
                                                seasonhr[constOU.SEASONHR.Funit.name].get()))

# ======================================================================================================================
def writeMAXDAILY(maxdaily):
    if len(maxdaily[constOU.MAXDAILY.GrpID.name].get())>0 and len(maxdaily[constOU.MAXDAILY.Filnam.name].get())>0:
        with open('control.inp', 'a') as f:
            f.write('OU MAXDAILY %s %s %s\n' % (maxdaily[constOU.MAXDAILY.GrpID.name].get(),
                                                maxdaily[constOU.MAXDAILY.Filnam.name].get(),
                                                maxdaily[constOU.MAXDAILY.Funit.name].get()))

# ======================================================================================================================
def writeMXDYBYYR(mxdybyyr):
    if len(mxdybyyr[constOU.MXDYBYYR.GrpID.name].get())>0 and len(mxdybyyr[constOU.MXDYBYYR.Filnam.name].get())>0:
        with open('control.inp', 'a') as f:
            f.write('OU MXDYBYYR %s %s %s\n' % (mxdybyyr[constOU.MXDYBYYR.GrpID.name].get(),
                                                mxdybyyr[constOU.MXDYBYYR.Filnam.name].get(),
                                                mxdybyyr[constOU.MXDYBYYR.Funit.name].get()))

# ======================================================================================================================
def writeMAXDCONT(maxdcont):
    if len(maxdcont[constOU.MAXDCONT.GrpID.name].get()) > 0:
        with open('control.inp', 'a') as f:
            if maxdcont['radbtnVar'].get()==1:
                f.write('OU MAXDCONT %s %s %s %s %s\n' % (maxdcont[constOU.MAXDCONT.GrpID.name].get(),
                                                          maxdcont[constOU.MAXDCONT.UpperRank.name].get(),
                                                          maxdcont[constOU.MAXDCONT.LowerRank.name].get(),
                                                          maxdcont[constOU.MAXDCONT.Filnam.name].get(),
                                                          maxdcont[constOU.MAXDCONT.Funit.name].get()))
            elif maxdcont['radbtnVar'].get()==2:
                f.write('OU MAXDCONT %s %s %s %s %s %s\n' % (maxdcont[constOU.MAXDCONT.GrpID.name].get(),
                                                             maxdcont[constOU.MAXDCONT.UpperRank.name].get(),
                                                             constOU.MAXDCONT.THRESH.name,
                                                             maxdcont[constOU.MAXDCONT.ThreshValue.name].get(),
                                                             maxdcont[constOU.MAXDCONT.Filnam.name].get(),
                                                             maxdcont[constOU.MAXDCONT.Funit.name].get()))

# ======================================================================================================================
def writeSUMMFILE(summfile):
    if len(summfile[constOU.SUMMFILE.SummFilename.name].get()) > 0:
        with open('control.inp', 'a') as f:
            f.write('OU SUMMFILE %s\n' % summfile[constOU.SUMMFILE.SummFilename.name].get())

# ======================================================================================================================
def writeFILEFORM(fileform):
    with open('control.inp', 'a') as f:
        f.write('OU FILEFORM %s\n' % fileform[constOU.FILEFORM.FILEFORM.name].get())

# ======================================================================================================================
def writeNOHEADER(noheader):
    noheaderStr = 'OU NOHEADER'
    valid = False
    if noheader['radbtnVar'].get()==1:
        if noheader[constOU.NOHEADER.POSTFILE.name].get():
            noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.POSTFILE.name)
            valid = True
        if noheader[constOU.NOHEADER.PLOTFILE.name].get():
            noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.PLOTFILE.name)
            valid = True
        if noheader[constOU.NOHEADER.MAXIFILE.name].get():
            noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.MAXIFILE.name)
            valid = True
        if noheader[constOU.NOHEADER.RANKFILE.name].get():
            noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.RANKFILE.name)
            valid = True
        if noheader[constOU.NOHEADER.SEASONHR.name].get():
            noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.SEASONHR.name)
            valid = True
        if noheader[constOU.NOHEADER.MAXDAILY.name].get():
            noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.MAXDAILY.name)
            valid = True
        if noheader[constOU.NOHEADER.MXDYBYYR.name].get():
            noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.MXDYBYYR.name)
            valid = True
        if noheader[constOU.NOHEADER.MAXDCONT.name].get():
            noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.MAXDCONT.name)
            valid = True
    elif noheader['radbtnVar'].get()==2:
        noheaderStr = '%s %s' % (noheaderStr, constOU.NOHEADER.ALL.name)
        valid = True

    if valid:
        with open('control.inp', 'a') as f:
            f.write('%s\n' % noheaderStr)

# ======================================================================================================================
def writeEVENTOUT(eventout):
    with open('control.inp', 'a') as f:
        f.write('OU EVENTOUT %s\n' % eventout[constOU.EVENTOUT.EVENTOUT.name].get())

# ======================================================================================================================
def writeControlFile(ouInputs):
    with open('control.inp', 'a') as f:
        f.write('\nOU STARTING\n')

    rectable = ouInputs[0]
    writeRECTABLE(rectable)

    maxtable = ouInputs[1]
    writeMAXTABLE(maxtable)

    daytable = ouInputs[2]
    writeDAYTABLE(daytable)

    maxifile = ouInputs[3]
    writeMAXIFILE(maxifile)

    postfile = ouInputs[4]
    writePOSTFILE(postfile)

    plotfile = ouInputs[5]
    writePLOTFILE(plotfile)

    toxxfile = ouInputs[6]
    writeTOXXFILE(toxxfile)

    rankfile = ouInputs[7]
    writeRANKFILE(rankfile)

    evalfile = ouInputs[8]
    writeEVALFILE(evalfile)

    seasonhr = ouInputs[9]
    writeSEASONHR(seasonhr)

    maxdaily = ouInputs[10]
    writeMAXDAILY(maxdaily)

    mxdybyyr = ouInputs[11]
    writeMXDYBYYR(mxdybyyr)

    maxdcont = ouInputs[12]
    writeMAXDCONT(maxdcont)

    summfile = ouInputs[13]
    writeSUMMFILE(summfile)

    fileform = ouInputs[14]
    writeFILEFORM(fileform)

    noheader = ouInputs[15]
    writeNOHEADER(noheader)

    eventout = ouInputs[16]
    writeEVENTOUT(eventout)

    with open('control.inp', 'a') as f:
        f.write('OU FINISHED\n')
