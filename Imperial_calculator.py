from tkinter import *
import math
import fractions

win=Tk()

#Function for converting string(in feet-inches) to float(in inch)
def to_inch(x):
    a = str(x)
    unit = tkvar1.get()

    mcount = a.count('-')
    scount = a.count(' ')
    dtcount = a.count('.')
    dvcount  = a.count('/')
    error = ''
    sp = a.find(' ')
    mi = a.find('-')
    se = 0
    me = 0
    
    if sp!=-1:
        try:
            if not(a[sp-1].isdigit() and a[sp+1].isdigit() and (a[sp+2]=='/' or a[sp+3]=='/')):
                se += 1
        except:
            se += 1
            
    if mi!=-1:
        try:
            if not(a[:mi].isdigit() and a[mi+1].isdigit()):
                me += 1
        except:
            me += 1

    if mcount>1 or scount>1 or dtcount>1 or dvcount>1:
        
        if mcount>1:
            error+='"-" '
        if scount>1:
            error+='"space" '
        if dtcount>1:
            error+='"." '
        if dvcount>1:
            error+='"/" '
        inch ='Extra ' + error + 'found in ' + a + '. Remove it'
        
    elif se!=0:
        inch = 'Invalid syntax in ' + a + '. Space error'
    
    elif me!=0:
        inch = 'Invalid syntax in ' + a 
    else:
        try:
            if len(a)==0:
                inch = 0
            elif a.find(' ') == -1 and a.find('/') ==-1 and a.find('-')==-1:
                if unit == 'Feet-inches':
                    inch = float(a)*12
                elif unit == 'Inches':
                    inch = float(a)

            elif a.find('-') != -1:
                b = a.split('-')

                if b[1].find(' ') != -1:
                    c = b[1].split(' ')
                    d = c[1].split('/')
                    i1 = int(b[0])*12 + int(c[0])
                    try:
                        i2 = float(d[0])/float(d[1])
                        inch = i1 + i2
                    except:
                        inch = 'Cannot divide by zero in ' + a


                elif b[1].find('/') != -1:
                    c = b[1].split('/')
                    i1 = int(b[0])*12
                    try:
                        i2 = float(c[0])/float(c[1])
                        inch = i1 + i2
                    except:
                        inch = 'Cannot divide by zero in ' + a
                else:
                    inch = int(b[0])*12 + float(b[1])

            elif a.find(' ') != -1 and a.find('/') !=-1 and a.find('-') ==-1:
                b = a.split(' ')
                c = b[1].split('/')
                i1 = int(b[0])
                try:
                    i2 = float(c[0])/float(c[1])
                    inch = i1 + i2
                except:
                    inch = 'Cannot divide by zero in ' + a

            elif a.find(' ') == -1 and a.find('/') !=-1 and a.find('-') ==-1:
                b = a.split('/')
                try:
                    inch = float(b[0])/float(b[1])
                except:
                    inch = 'Cannot divide by zero in ' + a
        except:
            inch = 'Syntax error'

    try:
        return float(inch)
    except:
        return inch

#Function for converting float(in inch) to string(in feet-inch)
def inch_to_feet(x):
    
    try:
        decimal=abs(x)
        tol = round(decimal * 16)
        a = math.modf(tol / 16)

        feet = int(a[1] // 12)
        inch = int(a[1] % 12)
        fract = fractions.Fraction(a[0])

        if fract == 0:
            fi = str(feet) + "-" + str(inch)
        else:
            fi = str(feet) + "-" + str(inch) + " " + str(fract)
        if x<0:
            return '-' + fi
        else:
            return fi
       
    except:
        return decimal


def reset(dummy=None):
    ee.delete(0, 'end')
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    ee.insert(END, 'Enter value below')
    e2.insert(END, '0')
    e3.insert(END, '0')
    
def close(dummy=None):
    win.destroy()
    

def entry_validation(input_value, action_type):
    if action_type == '1': #insert
        if input_value[-1].isdigit() or input_value[-1] in ('+', '-', '*', '/', ' ', '.'):

            if input_value[-1] =='.':
                if len(input_value) == 1:
                    return False
                elif len(input_value)>1:
                    if input_value[-2].isdigit():
                        return True
                    else:
                        return False

            elif input_value[-1] ==' ':
                if len(input_value) == 1:
                    return False
                elif len(input_value)>2:
                    if input_value[-2].isdigit() and (input_value[-4] == '-' or input_value[-3] == '-'):
                        return True
                    else:
                        return False
                    
            elif input_value[-1] =='+' or input_value[-1] == '*':
                if len(input_value) == 1:
                    return False
                elif len(input_value)>2:
                    if input_value[-2].isdigit():
                        return True
                    else:
                        return False
            
            elif input_value[-1] == '//':
                if len(input_value) == 1:
                    return False
                elif len(input_value)>1:
                    pass
                    
            return True
        else:
            return False
    return True

def metric_calc(a):
    unit1 = tkvar1.get()
    unit2 = tkvar2.get()
    unit3 = tkvar3.get()
    
    b = str(a)
    c = eval(b)
    banner = a

    if unit1=='Millimeters':
        if unit2 == 'Feet-inches':
            val = inch_to_feet(c/25.4)

        elif unit2 == 'Feet-decimal':
            val = round((c/304.8),3)
            
        elif unit2 == 'Inches':
            val = round((c/25.4),3)
                  
        else:
            val = 'Error'
        
        if unit3 == 'Millimeters':
            val_in_mm = c
        
        elif unit3 == 'Meters':
            val_in_mm = round((c/1000),3)
        
        else:
            val_in_mm = 'Error'
            
    elif unit1=='Meters':
        if unit2 == 'Feet-inches':
            val = inch_to_feet(c*39.37)

        elif unit2 == 'Feet-decimal':
            val = round((c*3.281),3)
            
        elif unit2 == 'Inches':
            val = round((c/39.37),3)
            
        else:
            val = 'Error'
        
        if unit3 == 'Millimeters':
            val_in_mm = round((c * 1000),3)
        
        elif unit3 == 'Meters':
            val_in_mm = round((c),3)
        
        else:
            val_in_mm = 'Error'
            
    
    return banner, val, val_in_mm 

def imperial_calc(a):
    unit2 = tkvar2.get()
    unit3 = tkvar3.get()
    
    if a.find('*') == -1 and a.find('//') == -1:
        
        b=a.split('+')
        x, y = [], []
        sum_p, sum_n =0,0
        p,n = '', ''
        
        for i in b:
            c = i.split('--')
            x.append(c[0])
            for i in c[1:]:
                y.append(i)
        for i in x:
            if type(to_inch(i)) == str:
                p += to_inch(i)
            else:
                sum_p += to_inch(i)
        for i in y:
            if type(to_inch(i)) == str:
                n += to_inch(i)
            else:
                sum_n += to_inch(i)
        if len(p)==0 and len(n)==0:
            val = sum_p - sum_n
        else:
            val = p+n

    elif a.find('*') !=-1:
        
        b=a.split('*')

        if len(b[1])==0:
            b[1]=0
        try:
            float(b[1])
            num = 0
        except:
            num = 1
            
        if a.find('--')==-1:
            if type(to_inch(b[0])) == str:
                val = to_inch(b[0])
            else:
                if num == 0:
                    val = to_inch(b[0])*float(b[1])
                else:
                    val = 'Second value should be a number'
        
        elif a.find('--')!=-1:
            if type(to_inch(b[0][2:])) == str:
                val = to_inch(b[0][2:])
            else:
                if num == 0:
                    val=-(to_inch(b[0][2:])*float(b[1]))
                else:
                    val = 'Second value should be a number'
        
    elif a.find('//') !=-1:
        
        b=a.split('//')
        if len(b[1])==0:
            b[1]=0
        try:
            float(b[1])
            num = 0
        except:
            num = 1
        if a.find('--')==-1:
            if type(to_inch(b[0])) == str:
                val = to_inch(b[0])
            else:
                if float(b[1]) ==0:
                    val = 'Cannot divide by zero in ' + a
                else:
                    if num == 0:
                        val=to_inch(b[0])/float(b[1])
                    else:
                        val='Second value should be a number'
        
        elif a.find('--')!=-1:
            if type(to_inch(b[0][2:])) == str:
                val = to_inch(b[0][2:])
            else:
                if float(b[1]) ==0:
                    val = 'Cannot divide by zero in ' + a
                else:
                    if num ==0:
                        val=-(to_inch(b[0][2:])/float(b[1]))
                    else:
                        val='Second value should be a number'
                
    try:
        float(val)
        banner = a
    except:
        banner = val
    
    if unit3 == 'Millimeters':
        try:
            if val<0:
                val_mm = (abs(val))*25.4
                val_in_mm  = '-' + str(round(val_mm ,2))

            else:
                val_mm = (val)*25.4
                val_in_mm  = round(val_mm ,2)

        except:
            val_in_mm = 'Error'
            
    elif unit3 == 'Meters':
        try:            
            if val<0:
                val_mm = (abs(val))/39.37
                val_in_mm  = '-' + str(round(val_mm ,2))

            else:
                val_mm = val/39.37
                val_in_mm  = round(val_mm ,2)

        except:
            val_in_mm = 'Error'
            
    if unit2 == 'Feet-inches':
        try:
            if val<0:
                val = '-' + inch_to_feet(abs(val))
            else:
                val = inch_to_feet(val)
        except:
            val='Error'

    elif unit2 == 'Inches':
        try:
            val = round(val, 3)
        except:
            val='Error'

    elif unit2 == 'Feet-decimal':
        try:
            val = round((val//12 + (val%12)/12),3)
        except:
            val='Error'

    
    return banner, val, val_in_mm


#Function for about window
def about():
    top = Toplevel()
    top.title('About')
    top.geometry('290x130')
    top.resizable(0,0)
    f1 = Frame(top, height=235, width=500)
    f1.grid(row=0, column=0)
    l1 = Label(f1, text='Description  :  Imperial Calculator')
    l1.place(x=40,y=20)
    l2 = Label(f1, text='Version  :  v1.0')
    l2.place(x=62,y=45)
    l3 = Label(f1, text='Author  :  Aravind Selvan')
    l3.place(x=64,y=70)


#Function for help window
def help_win():
    top = Toplevel()
    top.title('Help')
    top.geometry('402x380')
    top.resizable(0,0)
    
    
    f1 = Frame(top, height=380, width=500)
    f1.grid(row=0, column=0)
    
    l1 = Label(f1, text='General:')
    l1.place(x=5,y=2)
    l2 = Label(f1, text='► Press Enter key to display the answer.')
    l2.place(x=5,y=27)
    l3 = Label(f1, text='► Press Esc key to clear all the values.')
    l3.place(x=5,y=52)

    
   
    l10 = Label(f1, text='Imperial units:')
    l10.place(x=5,y=77)
    l11 = Label(f1, text='► The input can be given in feet-inch or inch or feet-decimal or all', )
    l11.place(x=5,y=102)
    l12 = Label(f1, text='together (Ex: 1-0+1/2+0.0625).')
    l12.place(x=17,y=120)
    l13 = Label(f1, text='►  For subtraction & division, use "--" & "//" instead of "-" & "/"')
    l13.place(x=5,y=145)
    l14 = Label(f1, text='(Only for imperial, not metric units). Ex:5-0--2-0 or 5-0//2')
    l14.place(x=17,y=163)
    l15 = Label(f1, text='► For multplication & division, you can input only 2 values. The first')
    l15.place(x=5,y=188)
    l16 = Label(f1, text='value should be in imperial units and the second should be numerical.')
    l16.place(x=17,y=206)
    l17 = Label(f1, text='Ex:1-0 1/2*2 or 2-1 11/16//3.5.')
    l17.place(x=17,y=223)
    l17 = Label(f1, text='► The least count will be 1/16.')
    l17.place(x=5,y=249)
    
    l20 = Label(f1, text='Metric units:')
    l20.place(x=5,y=273)
    l21 = Label(f1, text='►  For subtraction & division, use "-" & "/".')
    l21.place(x=5,y=299)
    l22 = Label(f1, text='►  For multplication & division, you can input only 2 values.')
    l22.place(x=5,y=324)
    l23 = Label(f1, text='Ex:11.5*2 or 12/2.5.')
    l23.place(x=17,y=342)


def calc(dummy=None):
    a = e1.get()
    b = str(a)
    
    try:
        if len(b)==0:
            banner = 'Enter value to calculate'
            val = 'Error'
            val_in_mm = 'Error'   

        else:
            char = ['+', '-', '*', '/', '.', ' ']
            error=''

            for i in b:
                if i.isdigit() or i in char:
                    pass
                else:
                    error += "'" + i + "'"

            if len(error) != 0:
                banner = 'Remove ' + error + 'to calculate'
                val = 'Error'
                val_in_mm = 'Error'            

            elif b.find('+')!=-1 and b.find('*')!=-1:
                banner = 'Cannot perform addition & multiplication simultaneously'
                val = 'Error'
                val_in_mm = 'Error'

            elif b.find('+')!=-1 and b.find('//')!=-1:
                banner = 'Cannot perform addition & division simultaneously'
                val = 'Error'
                val_in_mm = 'Error'

            elif b.find('*')!=-1 and b.find('//')!=-1:
                banner = 'Cannot perform multiplication & division simultaneously'
                val = 'Error'
                val_in_mm = 'Error'

            elif b.count('*')>1:
                banner = 'Cannot perform more than one multiplication simultaneously'
                val = 'Error'
                val_in_mm = 'Error'

            elif b.count('//')>1:
                banner = 'Cannot perform more than one division simultaneously'
                val = 'Error'
                val_in_mm = 'Error'

            elif b.find('---')!=-1:
                banner = 'Remove extra "-" to calculate'
                val = 'Error'
                val_in_mm = 'Error'  

            elif b.find('///')!=-1:
                banner = 'Remove extra "/" to calculate'
                val = 'Error'
                val_in_mm = 'Error'            

            else:
                unit1 = tkvar1.get()

                if unit1=='Feet-inches' or unit1=='Inches':
                    banner, val, val_in_mm = imperial_calc(b)

                elif unit1=='Millimeters' or unit1=='Meters':
                    banner, val, val_in_mm = metric_calc(b)

    except:
        val, val_in_mm, banner = 'Error', 'Error', 'Invalid syntax'
        
    e2.delete(0, 'end')
    e2.insert(END, str(val))

    e3.delete(0, 'end')
    e3.insert(END, str(val_in_mm))

    ee.delete(0, 'end')
    ee.insert(END, str(banner))

            
win.title('Calculator')
win.geometry('440x250')
win.configure(bg='#e0e0e0')
win.resizable(0,0)



win.bind('<Escape>', reset)
win.bind('<Return>', calc)

tkvar1 = StringVar(win)

choices1 = {'Feet-inches','Inches','Meters','Millimeters'}
tkvar1.set('Feet-inches') 

tkvar2 = StringVar(win)

choices2 = {'Feet-inches','Inches', 'Feet-decimal'}
tkvar2.set('Feet-inches')

tkvar3 = StringVar(win)

choices3 = {'Meters','Millimeters'}
tkvar3.set('Millimeters')


f1 = Frame(win, bg='#e0e0e0')
f1.pack()

ee = Entry(f1, font = ("Helvetica", 11, 'bold'), bg='#e0e0e0', foreground='black', relief='flat',
           width = 100, justify = 'right', validate='key')
ee.insert(END, 'Enter value below')
ee.pack()

e1 = Entry(f1, font = ("Helvetica", 17), bg='#e0e0e0', foreground='black', relief='flat',
           width = 35, justify = 'right', validate='key')
e1.focus_set()
e1['validatecommand'] = (e1.register(entry_validation),'%P','%d')
e1.insert(END,'0')
e1.pack()

m1 = OptionMenu(f1, tkvar1, *choices1, command=reset)
m1.config(font = ('Helvetica', 10, 'bold'), bg='#e0e0e0',
          highlightbackground='#e0e0e0', foreground='black', highlightcolor='#e0e0e0', relief='flat')
m1.pack()

ff = Frame(win, bg='#e0e0e0')
ff.pack()

f2 = Frame(ff, bg='#e0e0e0')
f2.grid(row=0, column=0, padx=10)

e2 = Entry(f2, font = ("Helvetica", 20, 'bold'), cursor='arrow', foreground='black', bg='#e0e0e0',
           width = 15, justify = 'center', relief='flat', validate='key')

e2.insert(END,'0')
e2.pack(pady=10)

m2 = OptionMenu(f2, tkvar2, *choices2, command=calc)
m2.config(font = ('Helvetica', 10, 'bold'), bg='#e0e0e0',
          highlightbackground='#e0e0e0', foreground='black', highlightcolor='#e0e0e0', relief='flat')
m2.pack()

f3 = Frame(ff, bg='#e0e0e0')
f3.grid(row=0, column=1, padx=10)

e3 = Entry(f3, font = ("Helvetica", 20, 'bold'), cursor='arrow', foreground='black', bg='#e0e0e0',
           width = 10, justify = 'center', relief='flat', validate='key')
e3.insert(END,'0')
e3.pack(pady=10)

m3 = OptionMenu(f3, tkvar3, *choices3, command=calc)
m3.config(font = ('Helvetica', 10, 'bold'), bg='#e0e0e0',
          highlightbackground='#e0e0e0', foreground='black', highlightcolor='#e0e0e0', relief='flat')
m3.pack()

f4 = Frame(win, bg='#e0e0e0', height=200, width=500)
f4.pack(pady=20)

b1 = Button(f4, text='About', width=7, command=about)
b2 = Button(f4, text='Help', width=7, command=help_win)
b3 = Button(f4, text='Close', width=7, command=close)

b1.place(x=30, y=10)
b2.place(x=290, y=10)
b3.place(x=370, y=10)

win.mainloop()