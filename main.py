from tkinter import *
from tkinter import ttk
from tkinter import Frame

import guiCO
import guiSO
import guiRE
import guiME
import guiEV
import guiOU

if __name__=='__main__':
    root = Tk()
    root.title('AERMOD control file generator')
    # maximising GUI window upon startup
    #w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    #root.geometry("%dx%d+0+0" % (w, h))
    root.state('zoomed')

    note = ttk.Notebook()
    tabCO = Frame(note)
    tabSO = Frame(note)
    tabRE = Frame(note)
    tabME = Frame(note)
    tabEV = Frame(note)
    tabOU = Frame(note)

    guiCO.buildTabCO(tabCO)
    guiSO.buildTabSO(tabSO)
    guiRE.buildTabRE(tabRE)
    guiME.buildTabME(tabME)
    guiEV.buildTabEV(tabEV)
    guiOU.buildTabOU(tabOU)

    note.add(tabCO, text="Control Pathway", compound=TOP)
    note.add(tabSO, text="Source Pathway")
    note.add(tabRE, text="Receptor Pathway")
    note.add(tabME, text="Meteorology Pathway")
    note.add(tabEV, text="Event Pathway")
    note.add(tabOU, text="Output Options")

    note.pack(fill='both', expand=True)
    root.mainloop()

    print('yay')