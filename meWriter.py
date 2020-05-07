import constantsME as constME

# ======================================================================================================================
def writeSURFFILE(surffile):
    surffileStr = 'ME SURFFILE %s' % surffile[constME.SURFFILE.Sfcfil.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % surffileStr)

# ======================================================================================================================
def writePROFFILE(proffile):
    proffileStr = 'ME PROFFILE %s' % proffile[constME.PROFFILE.Profil.name].get()
    with open('control.inp', 'a') as f:
        f.write('%s\n' % proffileStr)

# ======================================================================================================================
def writeSURFDATA(surfdata):
    str = 'ME SURFDATA %s %s %s %s %s' % (surfdata[constME.SURFDATA.Stanum.name].get(),
                                                  surfdata[constME.SURFDATA.Year.name].get(),
                                                  surfdata[constME.SURFDATA.Name.name].get(),
                                                  surfdata[constME.SURFDATA.Xcoord.name].get(),
                                                  surfdata[constME.SURFDATA.Ycoord.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % str)

# ======================================================================================================================
def writeUAIRDATA(uairdata):
    str = 'ME UAIRDATA %s %s %s %s %s' % (uairdata[constME.UAIRDATA.Stanum.name].get(),
                                          uairdata[constME.UAIRDATA.Year.name].get(),
                                          uairdata[constME.UAIRDATA.Name.name].get(),
                                          uairdata[constME.UAIRDATA.Xcoord.name].get(),
                                          uairdata[constME.UAIRDATA.Ycoord.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % str)


# ======================================================================================================================
def writeSITEDATA(sitedata):
    str = 'ME SITEDATA %s %s %s %s %s' % (sitedata[constME.SITEDATA.Stanum.name].get(),
                                          sitedata[constME.SITEDATA.Year.name].get(),
                                          sitedata[constME.SITEDATA.Name.name].get(),
                                          sitedata[constME.SITEDATA.Xcoord.name].get(),
                                          sitedata[constME.SITEDATA.Ycoord.name].get())
    with open('control.inp', 'a') as f:
        f.write('%s\n' % str)

# ======================================================================================================================
def writePROFBASE(profbase):
    with open('control.inp', 'a') as f:
        f.write('ME PROFBASE %s %s\n' % (profbase[constME.PROFBASE.BaseElev.name].get(),
                                         profbase[constME.PROFBASE.Units.name].get()))

# ======================================================================================================================
def writeSTARTEND(startend):
    with open('control.inp', 'a') as f:
        f.write('ME STARTEND %s %s %s %s %s %s %s %s\n' % (startend[constME.STARTEND.Strtyr.name].get(),
                                                            startend[constME.STARTEND.Strtmn.name].get(),
                                                            startend[constME.STARTEND.Strtdy.name].get(),
                                                            startend[constME.STARTEND.Strthr.name].get(),
                                                            startend[constME.STARTEND.Endyr.name].get(),
                                                            startend[constME.STARTEND.Endmn.name].get(),
                                                            startend[constME.STARTEND.Enddy.name].get(),
                                                            startend[constME.STARTEND.Endhr.name].get()))

# ======================================================================================================================
def writeDAYRANGE(dayrange):
    with open('control.inp', 'a') as f:
        f.write('ME DAYRANGE %s\n' % dayrange[constME.DAYRANGE.DAYRANGE.name].get())

# ======================================================================================================================
def writeNUMYEARS(numyears):
    with open('control.inp', 'a') as f:
        f.write('ME NUMYEARS %s\n' % numyears[constME.NUMYEARS.NumYrs.name].get())

# ======================================================================================================================
def writeSCIMBYHR(scimbyhr):
    with open('control.inp', 'a') as f:
        f.write('ME SCIMBYHR %s %s %s %s\n' % (scimbyhr[constME.SCIMBYHR.NRegStart.name].get(),
                                               scimbyhr[constME.SCIMBYHR.NRegInt.name].get(),
                                               scimbyhr[constME.SCIMBYHR.SfcFilnam.name].get(),
                                               scimbyhr[constME.SCIMBYHR.PflFilnam.name].get()))

# ======================================================================================================================
def writeWDROTATE(wdrotate):
    with open('control.inp', 'a') as f:
        f.write('ME WDROTATE %s\n' % wdrotate[constME.WDROTATE.Rotang.name].get())

# ======================================================================================================================
def writeWINDCATS(windcats):
    with open('control.inp', 'a') as f:
        f.write('ME WINDCATS %s %s %s %s %s\n' % (windcats[constME.WINDCATS.Ws1.name].get(),
                                                     windcats[constME.WINDCATS.Ws2.name].get(),
                                                     windcats[constME.WINDCATS.Ws3.name].get(),
                                                     windcats[constME.WINDCATS.Ws4.name].get(),
                                                     windcats[constME.WINDCATS.Ws5.name].get()))

# ======================================================================================================================
def writeControlFile(meInputs):
    with open('control.inp', 'a') as f:
        f.write('\nME STARTING\n')

    surffile = meInputs[0]
    writeSURFFILE(surffile)

    proffile = meInputs[1]
    writePROFFILE(proffile)

    surfdata = meInputs[2]
    writeSURFDATA(surfdata)

    uairdata = meInputs[3]
    writeUAIRDATA(uairdata)

    sitedata = meInputs[4]
    writeSITEDATA(sitedata)

    profbase = meInputs[5]
    writePROFBASE(profbase)

    startend = meInputs[6]
    writeSTARTEND(startend)

    dayrange = meInputs[7]
    writeDAYRANGE(dayrange)

    numyears = meInputs[8]
    writeNUMYEARS(numyears)

    scimbyhr = meInputs[9]
    writeSCIMBYHR(scimbyhr)

    wdrotate = meInputs[10]
    writeWDROTATE(wdrotate)

    windcats = meInputs[11]
    writeWINDCATS(windcats)

    with open('control.inp', 'a') as f:
        f.write('ME FINISHED\n')