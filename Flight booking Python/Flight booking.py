from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import csv

mywin=Tk()                                #สร้างหน้าต่าง
mywin.title('AIRLINE')                    
mywin.minsize(400,120)
mywin.configure(background='#FF9966')    
    
name       =StringVar()
phonenumber=StringVar()
time       =IntVar()
place      =IntVar()
classs     =IntVar()
cmbdayy    =StringVar()
cmbmonthh  =StringVar()
lstplace   =[[1,'Thai-England'],[2,'Thai-Korea'],[3,'Thai-Japan'],[4,'Thai-China'],[5,'Thai-Hong kong'],[6,'Thai-Taiwan']]
lsttime    =[[1,'8.00'],[2,'12.00'],[3,'16.00'],[4,'20.00']]
lstclass   =[[1,'First class'],[2,'Business class'],[3,'Economy Class']]
photoplane =PhotoImage(file='plane.png')


filepath   ='บันทึกการจองตั๋ว.csv'


lwelcome=Label(mywin,text='         FLIGHTS BOOKING',background='#CC0033',font=100) #ข้อมูล
lwelcome.grid(row=0,column=1,sticky=W)
lphplane=Label(mywin,image=photoplane,height=30,width=30)
lphplane.grid(row=0,column=1,sticky=W)
lphplane=Label(mywin,image=photoplane,height=30,width=30)
lphplane.grid(row=0,column=2,sticky=W)
lspace=Label(mywin,background='#FF9966')
lspace.grid(row=1,column=0,sticky=W)
lname   =Label(mywin,text='Name - Surname',background='#FF9966',font=20)
lname.grid(row=2,column=0,sticky=W)
lphone  =Label(mywin,text='Phone number',background='#FF9966',font=20)
lphone.grid(row=3,column=0,sticky=W)
lspace=Label(mywin,background='#FF9966')
lspace.grid(row=4,column=0,sticky=W)
lplace  =Label(mywin,text='Please select country',background='#FF9966',font=20)
lplace.grid(row=5,column=0,sticky=W)
ltime   =Label(mywin,text='Please select time',background='#FF9966',font=20)
ltime.grid(row=5,column=1,sticky=W)
lclasss   =Label(mywin,text='Please select class',background='#FF9966',font=20)
lclasss.grid(row=7,column=2,sticky=W)

lcmb=Label(mywin,text='Please select day',background='#FF9966',font=20)  
lcmb.grid(row=2,column=2,sticky=W)
lcmb1=Label(mywin,text='Please select month',background='#FF9966',font=20)
lcmb1.grid(row=4,column=2,sticky=W)
  
cmbday=ttk.Combobox(mywin,value=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18',
                                 '19','20','21','22','23','24','25','26','27','28','29','30','31'),textvariable=cmbdayy)
cmbday.current(0)
cmbday.grid(row=3,column=2,sticky=W)        #ทำตัวเลือก combobox

cmbmonth=ttk.Combobox(mywin,value=('January','February','March','April','May','June','July',
                                   'August','September','October','November','December'),textvariable=cmbmonthh)	
cmbmonth.current(0)
cmbmonth.grid(row=5,column=2,sticky=W)      #ทำตัวเลือก combobox
 

entname=Entry(mywin,textvariable=name)          #ช่องให้ใส่ข้อมูล
entname.grid(row=2,column=1,sticky=W)
entphone=Entry(mywin,textvariable=phonenumber)
entphone.grid(row=3,column=1,sticky=W)


for kk,label in lstplace:       #ทำช้อย
    adtime=Radiobutton(mywin,text=label,variable=place,value=kk,background='#FF9966',font=20)
    adtime.grid(row=5+kk,column=0,sticky=W)

for kk,label in lsttime:        #ทำช้อย
    rdtime=Radiobutton(mywin,text=label,variable=time,value=kk,background='#FF9966',font=20)
    rdtime.grid(row=5+kk,column=1,sticky=W)

for kk,label in lstclass:        #ทำช้อย
    ratime=Radiobutton(mywin,text=label,variable=classs,value=kk,background='#FF9966',font=20)
    ratime.grid(row=7+kk,column=2,sticky=W)

def bookingbutton():  #สร้างฟังชั่น สำหรับปุ่ม
    myout=Tk()          #สร้างหน้าต่างใหม่
    myout.title(' ')
    myout.minsize(200,60)
    myout.configure(background='#FF9966')

    loutput=Label(myout,background='#FF9966')
    loutput.grid(row=0,column=0,sticky=W)

    loutputprice=Label(myout,background='#FF9966')
    loutputprice.grid(row=1,column=0,sticky=W)

    lspace=Label(myout,background='#FF9966')
    lspace.grid(row=3,column=0,sticky=W)

    btclose1=Button(myout,text='Close',command=myout.destroy)   #ปุ่มปิด
    btclose1.grid(row=5,column=1)
    
    places=StringVar()
    if place.get()==1:
        places=' England'
    elif place.get()==2:
        places=' Korea'
    elif place.get()==3:
        places=' Japan'
    elif place.get()==4:
        places=' China'
    elif place.get()==5:
        places=' Hong Kong'
    elif place.get()==6:
        places=' Taiwan'    
    else:
        def bookingbutton():
            mynew.Tk()
            mynew.title(' ')
            mynew.minsize(100,50)

            noout=Label(mynew,text='กรุณากรอกรายละเอียดให้ครบ',font=50)
            noout.grid(row=0,column=0,sticky=W)

        
    timetell=StringVar()
    if time.get()==1:
        timetell=' Flights at 8.00 o clock '
    elif time.get()==2:
        timetell=' Flights at 12.00 o clock '
    elif time.get()==3:
        timetell=' Flights at 16.00 o clock '
    elif time.get()==4:
        timetell=' Flights at 20.00 o clock '
    else:
        def bookingbutton():
            mynew=Tk()
            mynew.title(' ')
            mynew.minsize(100,50)

            noout=Label(mynew,text='กรุณากรอกรายละเอียดให้ครบ',font=50)
            noout.grid(row=0,column=0,sticky=W)
            
    priceout=StringVar()
    #
    if place.get()==1 and classs.get()==1:
        priceout='First class 100,000'
    elif place.get()==1 and classs.get()==2:
        priceout='60,000'
    elif place.get()==1 and classs.get()==3:
        priceout='Economy Class 30,000'
    #     
    elif place.get()==2 and classs.get()==1:
        priceout='First class 35,000'
    elif place.get()==2 and classs.get()==2:
        priceout='Business class 25,000'
    elif place.get()==2 and classs.get()==3:
        priceout='Economy Class 15,000'
            
    elif place.get()==3 and classs.get()==1:
        priceout='First class 70,000'
    elif place.get()==3 and classs.get()==2:
        priceout='Business class 50,000'
    elif place.get()==3 and classs.get()==3:
        priceout='Economy Class 20,000'
    #        
    elif place.get()==4 and classs.get()==1:
        priceout='First class 40,000'
    elif place.get()==4 and classs.get()==2:
        priceout='Business class 18,000'
    elif place.get()==4 and classs.get()==3:  
        priceout='Economy Class 12,000'
    #
    elif place.get()==5 and classs.get()==1:
        priceout='First class 20,000'
    elif place.get()==5 and classs.get()==2:
        priceout='Business class 12,000'
    elif place.get()==5 and classs.get()==3:  
        priceout='Economy Class 8,000'
    #
    elif place.get()==6 and classs.get()==1:
        priceout='First class 25,000'
    elif place.get()==6 and classs.get()==2:
        priceout='Business class 19,000'
    elif place.get()==6 and classs.get()==3:  
        priceout='Economy Class 10,000'
    else:
        def bookingbutton():
            mynew=Tk()
            mynew.title(' ERROR ')
            mynew.minsize(100,50)

            noout=Label(mynew,text='กรุณากรอกรายละเอียดให้ครบ',font=50)
            noout.grid(row=0,column=0,sticky=W)
               
    try:

        with open(filepath,'a',encoding='utf-8')as f:
            f.write(name.get()+' ')
            f.write(phonenumber.get()+'   Thai to')
            f.write(places+'   ')
            f.write(timetell+'   Date ')
            f.write(cmbday.get()+'  ')
            f.write(cmbmonth.get()+' 2021 \n')
        loutput.config(text='  '+name.get()+'  ' +phonenumber.get()+' has booked a ticket from Thailand to '+
                       places+' Date '+cmbdayy.get()+' '+cmbmonthh.get()+' 2021 '+timetell+' ',font=70)
        loutput.grid(row=0,column=0,sticky=W)
        loutputprice.config(text='                                   The ticket price '+priceout+' Baht '
                            ,background='#FF9966',font=70)
        loutputprice.grid(row=1,column=0,sticky=W)
        loutputpay=Label(myout,text='                     Please pay in due time',background='#FF9966',font=70)
        loutputpay.grid(row=4,column=0,sticky=W)

                
    except Exception as e:
        messagebox.showerror("Failed","Please choose all of the choice ")
        
bt     =Button(mywin,text='Booking',command=bookingbutton)
bt.grid(row=13,column=1)


btclose=Button(mywin,text='Cancel',command=mywin.destroy)
btclose.grid(row=13,column=2)

mywin.mainloop()



















