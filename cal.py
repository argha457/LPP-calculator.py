from tkinter import *
from tkinter import messagebox
#matplotlib.org
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as mygraph
import numpy as np
mygraph.style.use('fivethirtyeight')


class LPP():
    
    def __init__(self):
        self.main()
    
    def main(self):
        self.window = Tk()
        self.window.config(background = 'Orange')
        self.window.attributes('-alpha',0.99)
        self.window.minsize(700,800)
        self.window.maxsize(700,800)
        self.window.title('MyLPP Calculator')

        self.Lab1 = Label(self.window,text = 'LPP Calculator (2 Variables)',font = ('Arial',21,'bold'),bg = 'orange')
        self.Lab1.pack()

        self.But1 = Button(self.window,text = 'Click to Start',relief = 'sunken',command = self.endbut,font = ('Arial',17,'italic'))
        self.But1.pack(pady=10)

        self.window.mainloop()
    
    def coeffx(self):
        intolist = StringVar()
        self.lab = Label(self.window,text = 'Enter coefficients of x (separated by comma):',font = ('Arial',21,'bold'),bg='orange')
        self.lab.pack(pady = 10)
        self.entry = Entry(self.window,textvariable = intolist,font = ('Arial',21,'bold'))
        self.entry.pack(pady = 10)
        self.butsubmit = Button(self.window,text = 'Submit',font = ('Arial',21,'bold'),command = self.values)
        self.butsubmit.pack(pady = 10)
    
    def coeffy(self):
        intolisty = StringVar()
        self.laby = Label(self.window,text = 'Enter coefficients of y (separated by comma):',font = ('Arial',21,'bold'),bg='orange')
        self.laby.pack(pady = 10)
        self.entryy = Entry(self.window,textvariable = intolisty,font = ('Arial',21,'bold'))
        self.entryy.pack(pady = 10)
        self.butsubmity = Button(self.window,text = 'Submit',font = ('Arial',21,'bold'),command = self.valuesy)
        self.butsubmity.pack(pady = 10)

    def coeffco(self):
        intolistco = StringVar()
        self.labco = Label(self.window,text = 'Enter coefficients of constants (separated by comma):',font = ('Arial',21,'bold'),bg='orange')
        self.labco.pack(pady = 10)
        self.entryco = Entry(self.window,textvariable = intolistco,font = ('Arial',21,'bold'))
        self.entryco.pack(pady = 10)
        self.butsubmitco = Button(self.window,text = 'Submit',font = ('Arial',21,'bold'),command = self.valuesco)
        self.butsubmitco.pack(pady = 10)
    
    def signs(self):
        intolist = StringVar()
        self.labsign = Label(self.window,text = 'Enter signs (> or <)(separated by comma):',font = ('Arial',21,'bold'),bg='orange')
        self.labsign.pack(pady = 10)
        self.entrysign = Entry(self.window,textvariable = intolist,font = ('Arial',21,'bold'))
        self.entrysign.pack(pady = 10)
        self.butsubmitsign = Button(self.window,text = 'Submit',font = ('Arial',21,'bold'),command = self.valsigns)
        self.butsubmitsign.pack(pady=10)
    
    def endbut(self):
        self.But1.destroy()
        self.eqns()

    def dest(self):
        self.eqnno = self.enteqn.get()
        if int(self.eqnno) != 0:
            self.eqns.destroy()
            self.coeffx()
        else:
            messagebox.showerror('Error','Can\'t keep zero as a field value !!')

    def eqns(self):
        num_eqn = IntVar()
        num_eqn.set(1)
        self.eqns = Toplevel(self.window)
        self.Labeqn = Label(self.eqns,text = 'How many equations are there?')
        self.Labeqn.pack()
        self.enteqn =  Entry(self.eqns,textvariable = num_eqn)
        self.enteqn.pack()
        self.Butend = Button(self.eqns,text = 'Submit',command = self.dest)
        self.Butend.pack()

    def values(self):
        value_sep_by_comma = self.entry.get()
        self.listvalue = value_sep_by_comma.split(',')
        if self.listvalue != ['']:
            if len(self.listvalue) == int(self.eqnno):
                #go ahead
                messagebox.showinfo('Match','Let\'s go ahead')
                self.butsubmit.destroy()
                self.coeffy()
            else:
                messagebox.showerror('Mismatch','Your number of equations and number of coeffiecients do not match !!                                       OR                                                                                                                                 You must have put extra commas.Please Check !!')
        elif self.listvalue == ['']:
            messagebox.showinfo('Error','Can\'t keep the field empty !!')
    
    def valuesy(self):
        value_sep_by_comma = self.entryy.get()
        self.listvaluey = value_sep_by_comma.split(',')
        if self.listvaluey != ['']:
            if len(self.listvaluey) == int(self.eqnno):
                #go ahead
                messagebox.showinfo('Match','Let\'s go ahead')
                self.butsubmity.destroy()
                self.coeffco()
            else:
                messagebox.showerror('Mismatch','Your number of equations and number of coefficients do not match !!                                       OR                                                                                                                                 You must have put extra commas.Please Check !!')
        elif self.listvaluey == ['']:
            messagebox.showinfo('Error','Can\'t keep the field empty !!')
    
    def valuesco(self):
        value_sep_by_comma = self.entryco.get()
        self.listvalueco = value_sep_by_comma.split(',')
        if self.listvalueco != ['']:
            if len(self.listvalueco) == int(self.eqnno):
                #go ahead
                messagebox.showinfo('Match','Let\'s go ahead')
                self.butsubmitco.destroy()
                self.signs()
            else:
                messagebox.showerror('Mismatch','Your number of equations and number of constants do not match !!                                       OR                                                                                                                                 You must have put extra commas.Please Check !!')
        elif self.listvalueco == ['']:
            messagebox.showinfo('Error','Can\'t keep the field empty !!')
    
    def valsigns(self):
        value_sep_by_comma = self.entrysign.get()
        self.listvaluesigns = value_sep_by_comma.split(',')
        if self.listvaluesigns != ['']:
            if len(self.listvaluesigns) == int(self.eqnno):
                messagebox.showinfo('Match','Let\'s go ahead')
                showgraphbut = Button(self.window,text = 'Show Graph',command = self.graph)
                self.butsubmitsign.destroy()
                showgraphbut.pack(pady = 10)
            else:
                messagebox.showerror('Mismatch','Your number of equations and number of constants do not match !!                                       OR                                                                                                                                 You must have put extra commas.Please Check !!')
        elif self.listvaluesigns == ['']:
            messagebox.showinfo('Error','Can\'t keep the field empty !!')
    
    def graph(self):
        mygraph.style.use('ggplot')
        xvals = [float(i) for i in self.listvalue]
        yvals = [float(i) for i in self.listvaluey]
        covals = [float(i) for i in self.listvalueco]
        signvals = [i for i in self.listvaluesigns]

        def intersection(lst1, lst2):
            lst3 = [value for value in lst1 if value in lst2]
            return(lst3)
        try:
            xran = max(covals)/max(xvals)
        except:
            xran = 100
        try:
            yran = max(covals)/max(yvals)
        except:
            yran = 100
        colordict = {0:'#e36414',1:'#2a9d8f',2:'#4d194d',3:'#3a0ca3',4:'#e76f51'}
        #listpoint = []
        for i in range(len(xvals)):
            if xvals[i] < 0:
                xvals[i] = -xvals[i]
                yvals[i] = -yvals[i]
                covals[i] = -covals[i]
            else:
                pass
            if yvals[i] != 0:
                p1 = np.arange(-1000,1000,0.01)
                p2 = [(covals[i]-xvals[i]*j)/yvals[i] for j in p1]
                text = str(xvals[i])+'x +' + str(yvals[i]) + 'y = ' +str(covals[i])
                mygraph.plot(list(p1),list(p2),label = text,color = colordict[i])
                '''list1 = []
                for b in range(len(list(p1))):
                    list1.append([p1[b],p2[b]])
                listpoint.append(list1)'''
            else:
                p1 = np.arange(-1000,1000,0.01)
                p2 = [(covals[i]-yvals[i]*j)/xvals[i] for j in p1]
                text = str(xvals[i])+'x +' + str(yvals[i]) + 'y = ' +str(covals[i])
                mygraph.plot(list(p2),list(p1),label = text,color = colordict[i])
                '''list1 = []
                for a in range(len(list(p1))):
                    list1.append([p2[a],p1[a]])
                listpoint.append(list1)'''
            if yvals[i] != 0:
                x = np.arange(0,1000,0.01)
                y = [(covals[i] - (xvals[i]*j))/(yvals[i]) for j in x]
            else:
                y = np.arange(0,1000,0.01)
                x = [(covals[i] - (yvals[i]*j))/(xvals[i]) for j in y]
            '''xlong = np.arange((covals[i]/xvals[i]),1000,0.01)
            ylong = [(0*k + 100) for k in xlong]'''
            try:
                slope = -yvals[i]/xvals[i]
            except:
                pass
            if covals[i] == 0:
                if signvals[i] == '>' and slope > 0:
                    mygraph.fill_between(x,y,-10000,color = colordict[i],alpha = 0.4)
                elif signvals[i] == '<' and slope > 0:
                    mygraph.fill_between(x,y,10000,color = colordict[i],alpha = 0.4)
                elif signvals[i] == '>' and slope < 0:
                    mygraph.fill_between(x,y,10000,color = colordict[i],alpha = 0.4)
                elif signvals[i] == '<' and slope < 0:
                    mygraph.fill_between(x,y,-10000,color = colordict[i],alpha = 0.4)
                else:
                    pass

            elif covals[i] > 0 and signvals[i] == '<' and (xvals[i] != 0 and yvals[i] != 0) and slope < 0:
                mygraph.fill_between(x,y,-10000,color = colordict[i],alpha = 0.4)
            elif covals[i] > 0 and signvals[i] == '<' and (xvals[i] != 0 and yvals[i] != 0) and slope > 0:
                mygraph.fill_between(x,y,10000,color = colordict[i],alpha = 0.4)
            elif covals[i] > 0 and signvals[i] == '>' and (xvals[i] != 0 and yvals[i] != 0) and slope < 0:
                mygraph.fill_between(x,y,10000,color = colordict[i],alpha = 0.4)
            elif covals[i] > 0 and signvals[i] == '>' and (xvals[i] != 0 and yvals[i] != 0) and slope > 0:
                mygraph.fill_between(x,y,-10000,color = colordict[i],alpha = 0.4)
            elif covals[i] < 0 and signvals[i] == '<' and (xvals[i] != 0 and yvals[i] != 0) and slope < 0:
                mygraph.fill_between(x,y,10000,color = colordict[i],alpha = 0.4)
            elif covals[i] < 0 and signvals[i] == '<' and (xvals[i] != 0 and yvals[i] != 0) and slope > 0:
                mygraph.fill_between(x,y,-10000,color = colordict[i],alpha = 0.4)
            elif covals[i] < 0 and signvals[i] == '>' and (xvals[i] != 0 and yvals[i] != 0) and slope < 0:
                mygraph.fill_between(x,y,-10000,color = colordict[i],alpha = 0.4)
            elif covals[i] < 0 and signvals[i] == '>' and (xvals[i] != 0 and yvals[i] != 0) and slope < 0:
                mygraph.fill_between(x,y,10000,color = colordict[i],alpha = 0.4)
            elif covals[i] > 0 and (xvals[i] == 0 or yvals[i] == 0):
                if xvals[i] == 0:
                    if signvals[i] == '>':
                        mygraph.fill_between(x,y,10000,color = colordict[i],alpha = 0.4)
                    else:
                        mygraph.fill_between(x,y,-10000,color = colordict[i],alpha = 0.4)
                else:
                    if signvals[i] == '>':
                        mygraph.fill_betweenx(y,x,10000,color = colordict[i],alpha = 0.4)
                    else:
                        mygraph.fill_betweenx(y,x,-10000,color = colordict[i],alpha = 0.4)
            else:
                pass
        '''for i in range(len(listpoint)):
            for j in range(i+1,len(listpoint)):
                common = intersection(listpoint[i],listpoint[j])
                for i in common:
                    mygraph.plot(i[0],i[1],'ro',color = colordict[i])'''
        mygraph.title('Equations')
        mygraph.legend()
        mygraph.xlim([0,(xran+10)])
        mygraph.ylim([0,yran+10])
        mygraph.grid(True, which = 'both')
        mygraph.tight_layout()
        mygraph.show()

LPP()