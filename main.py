from logging import config
from msilib.schema import SelfReg
from typing import Self
from kivy.app import App
from kivy.uix.label import Label
from kivymd.toast import toast
from kivy.uix.screenmanager import ScreenManager,NoTransition
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
import arabic_reshaper
import bidi.algorithm
import smtplib, ssl
from kivymd.uix.screen import Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
import kivy.factory
import kivy
from kivy.properties import ObjectProperty
import pypyodbc as odbc
from arabic_reshaper import reshape     #pip install arabic_reshaper
from bidi.algorithm import get_display 
import arabic_reshaper
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
import main 
from kivy.uix.textinput import TextInput
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from kivymd.uix.snackbar import Snackbar
import encodings  
import re
from datetime import datetime
from kivymd.uix.filemanager import MDFileManager
import os
from PIL import Image
from textwrap import dedent
import shutil
from plyer import filechooser

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button
import pyodbc 
from flask import Flask, request, session, redirect
from kivymd.uix.pickers import MDDatePicker

kivy.require('1.0.1')
Builder.load_file("regster.kv")

Builder.load_file("loginin.kv")
#Builder.load_file("screen_home.kv")
Builder.load_file("servic.kv")
Builder.load_file("raseedstart.kv")
Builder.load_file("msrofat.kv")
Builder.load_file("profile.kv")
Builder.load_file("tsgeel.kv")

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=alialshhry.com;DATABASE=alyalshhry_shhry;UID=alyalshhry_ali1391;PWD=0et&S74l8') 
iduserV=0
Window.size = (350,580)

app = Flask(__name__)
app.secret_key = 'your_secret_key'


KV = '''
#:import arabic_reshaper arabic_reshaper
#:import get_display bidi.algorithm.get_display

MDBoxLayout:
    orientation: "vertical"
    md_bg_color: "#1E1E15"

    MDTopAppBar:
        title: get_display(arabic_reshaper.reshape('مرحبا بكم '))

    MDLabel:
        text: "Content"
        halign: "center"
'''
class tsgeelScreen(Screen):
    emailInput:ObjectProperty(None)
    mobilenumInput:ObjectProperty(None)
    progress:ObjectProperty(None)
    lblpro:ObjectProperty(None)
    ch1:ObjectProperty(None)
    ch2:ObjectProperty(None)
    contry:ObjectProperty(None)
    
    def tsgeelshow(self,*arg):
        #screen_manager.current = "login"      
        screen_manager.current = "tsgeel"     
    pass
    def Checkbox_click(self,instanc,value):
        print(value)
        pass
    # def on_text(self, instance, value):
    #     #if len(self.text.strip()) >= 10:
    #     #  self.readonly = True
    #     pass
    def addR(self):
        print("900")
        current = self.ids.progress.value
        if current==100:
            current=0
        current +=25
        self.ids.progress.value= current
        self.ids.lblpro.text= str(current)+ get_display(arabic_reshaper.reshape(' الرضاء%:'))
        #print(current)
    pass
    def valPhone(selef,number):
    
            if  len(number)==12:
                #return number[0] =="0" and number[1]=="5" and number.isdigit()
                return  number.isdigit()
            else:
               return False
    def checkemail(selef,email):
            #email = selef.ids.emailInput.text
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
            if(re.fullmatch(regex, email)):
                #print("Valid Email")
                return True
            else:
                #print("Invalid Email")
                return False
     
    def addtsgeel(self) :
        s=screen_manager.get_screen("home").iduser.text    
        R=self.emailInput.text
        b=self.ids.mobilenumInput.text
        #contry=self.contry.text
        #mob=contry +b
        progress=self.ids.progress.value
        lblpro=self.ids.lblpro.text
        ch1=self.ids.ch1.active
        ch2=self.ids.ch2.active
        #if (ch2)=='':
        #ch2=False
        
        if  (R) == "" or (b) == ""  :
                f=1
                re_text="هناك حقول فارغة "
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.mylabel.text =ressh_sen[::-1]
                self.ids.mylabel.font_name="arial.ttf"
        else:
            f=0  
       
        mobile_chis=self.valPhone(b)
        chiic_email= self.checkemail(R)
        if chiic_email :    
            e=0
            re_text=""  
        else:
            e=1
            re_text="البريد الالكتورني خاطئ"
            ressh_sen=arabic_reshaper.reshape(re_text)
            self.ids.mylabel.text =ressh_sen[::-1]
            self.ids.mylabel.font_name="arial.ttf"

        if  mobile_chis:    
            flag=0
            re_text=""      
        else:
            flag=1
                       
            re_text="تأكد من رقم الجوال وانه  اثناعشر خانة"
            ressh_sen=arabic_reshaper.reshape(re_text)
            self.ids.mylabel.text =ressh_sen[::-1]
            self.ids.mylabel.font_name="arial.ttf"


       

        if  (flag)==0  and (e)==0 :  
       
        
            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=alialshhry.com;DATABASE=alyalshhry_shhry;UID=alyalshhry_ali1391;PWD=0et&S74l8') 
            c = conn.cursor()          
            query2 = "INSERT INTO Tsgeel (iduser,Email, Mobile,NmaecorseP1,NmaecorseC2,tgeem) VALUES ('"+str(s)+"','"+R+"', '"+b+"','"+str(ch1)+"','"+str(ch2)+"','"+str(progress)+"')"
            c.execute(query2)
            c.commit()
                
            
            re_text="تمت الاضافة بنجاح"
            ressh_sen=arabic_reshaper.reshape(re_text)
            self.ids.mylabel.text =ressh_sen[::-1]
            self.ids.mylabel.font_name="arial.ttf"

class msrofatScreen(Screen):
    nav_drawer3:ObjectProperty(None)
    raseed:ObjectProperty(None)
    raseed2:ObjectProperty(None)
    msg:ObjectProperty(None)
    mblgsrf:ObjectProperty(None)
    byansrf:ObjectProperty(None)
    datesrf:ObjectProperty(None)
    raseedLhale:ObjectProperty(None)
    maillabel:ObjectProperty(None)
    #rseedhale:ObjectProperty(None)
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.ids.datesrf.text=str(value)
        print(instance, value, date_range)
        print(value)
    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    
    def addsrv(self):
            s=screen_manager.get_screen("home").iduser.text    
            R= self.mblgsrf.text
            b=self.byansrf.text
            d=self.datesrf.text
            f=0
            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=alialshhry.com;DATABASE=alyalshhry_shhry;UID=alyalshhry_ali1391;PWD=0et&S74l8') 
   
            c = conn.cursor()    

            if  (R) == "" or (b) == "" or (d) == "" :
                f=1
                re_text="هناك حقول فارغة "
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.msg.text =ressh_sen[::-1]
                self.ids.msg.font_name="arial.ttf"
            else:
                f=0     
            if (f)==0:
                s=screen_manager.get_screen("home").iduser.text    
   
                sql = "SELECT sum(RAssedRS) as xc FROM raseed WHERE ID_user = '" + str(s) + "'"
             
   
                c.execute(sql)
                result = c.fetchall()
                if result:
                  word=0
                for record in result:
                   cv=round(record[0],3)  
                   
   
                today = datetime.today()
                xc=float(R)
                bage=cv-xc
                query = "INSERT INTO byanrserfns (ID_user, mblgsrf,DateSrf,byansrf,raseedhale,raseedbadsrv) VALUES ('"+str(s)+"','"+self.mblgsrf.text+"','"+str(today)+"','"+self.byansrf.text+"','"+str(cv)+"','"+str(bage)+"')"
                print(query)
                print("sccc")
   
                c.execute(query)
                c.commit()

                re_text="تمت الاضافة بنجاح"
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.msg.text =ressh_sen[::-1]
                self.ids.msg.font_name="arial.ttf"
            else:
                self.on_enter(self)  
                sql3 = "SELECT count(*) as xc FROM raseednhaee WHERE ID_user = '" + str(s) + "'"
                #sql = "SELECT username FROM ali_users "
                print("222")
                print(sql3)
                c.execute(sql3)
                result = c.fetchone()
                word=0
                for record in result:
                   #cv=round(record[0],3)  
                   word=record[0]
                if (word)==0:
                #if result :    
                    bage2=cv-bage   
                    query2 = "INSERT INTO raseednhaee (ID_user, rassedhalee,rseedmtbge) VALUES ('"+str(s)+"', '"+cv+"','"+str(bage2)+"')"
                
                    
   
                    c.execute(query2)
                    c.commit()
                
   
                    re_text="تمت الاضافة بنجاح"
                    ressh_sen=arabic_reshaper.reshape(re_text)
                    self.ids.msg.text =ressh_sen[::-1]
                    self.ids.msg.font_name="arial.ttf"
                    self.on_enter(self) 
                else:
                    query2 = "update  raseednhaee set  rassedhalee=%s,rseedmtbge=%s WHERE ID_user = '" + str(s) + "'"
                    bage2=cv-bage   
                    values2 = (cv,bage2)
                    c.execute(query2, values2)
                    conn.commit()
                    re_text="تمت الاضافة بنجاح"
                    ressh_sen=arabic_reshaper.reshape(re_text)
                    self.ids.msg.text =ressh_sen[::-1]
                    self.ids.msg.font_name="arial.ttf"
                    self.on_enter(self) 
    
    def srfshow(self,*arg): 
        screen_manager.transition.direction = 'right'
        screen_manager.transition.duration = 1
        screen_manager.current = "msrofat"  
                          
        pass
    def on_enter(self, *args):
       
        print(screen_manager.get_screen("loginin").user.text)
   
        s=screen_manager.get_screen("home").iduser.text    
   
        sql = "SELECT rassedhalee,rseedmtbge FROM raseednhaee WHERE ID_user = '" + str(s) + "'"
   
        print(sql)
        print("66")
        c = conn.cursor()  
        print(sql)
        print("cc")
        c.execute(sql)
        result = c.fetchall()
        if result:
           print (result)
        #a='welcome:'
        word=0
        for record in result:
            word =f'{word}\n{record[0]}'
            cv=round(record[0],3)  
            #self.ids.raseed.text=f'{cv}'
            self.ids.raseedLhale.text=f'{cv}'

            print("sss{cv}")
        self.ids.datesrf.text =str(datetime.now())
        return result
    
class raseedstartScreen(Screen):
    nav_drawer3:ObjectProperty(None)
    raseed:ObjectProperty(None)
    raseed2:ObjectProperty(None)
    msg:ObjectProperty(None)
    maillabel:ObjectProperty(None)
    def addrassed(self):
            s=screen_manager.get_screen("home").iduser.text    
            R= self.raseed2.text
            f=0
   
            c = conn.cursor()    

            if  (R) == "" :
                f=1
                re_text="ادخل رقماً  "
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.msg.text =ressh_sen[::-1]
                self.ids.msg.font_name="arial.ttf"
            else:
                f=0     
            if (f)==0:
             
   
                today = datetime.today()

                query = "INSERT INTO raseed (ID_user, RAssedRS,Date_in) VALUES ('"+str(s)+"', '"+self.raseed2.text+"',N'"+str(today)+"')"
   
                c.execute(query)
                conn.commit()
   
                re_text="تمت الاضافة بنجاح"
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.msg.text =ressh_sen[::-1]
                self.ids.msg.font_name="arial.ttf"
                self.on_enter(self)
    def raseedstart(self,*arg): 
        screen_manager.current = "raseedstart" 
    def on_enter(self, *args):
       
        print(screen_manager.get_screen("loginin").user.text)
   
        s=screen_manager.get_screen("home").iduser.text    
   
        sql = "SELECT sum(RAssedRS) as xc FROM raseed WHERE ID_user = '" + str(s) + "'"
        #sql = "SELECT username FROM ali_users "
        c = conn.cursor()  
        c.execute(sql)
        result = c.fetchall()
        print (result)
   
        word=0
        if result:
            for record in result:
               word =f'{word}\n{record[0]}'
   
               self.ids.raseed.text=f'{record[0]}'
   
        return result
        return super().on_enter(*args)
                     
        
        pass
    def usreid(user):
        sql = "SELECT id FROM AllUser WHERE UserName = '" + user + "'"
        c = conn.cursor()  
        c.execute(sql)
        result = c.fetchone()
        return result

        pass  
@app.route('/home')     
class homeScreen(Screen):
    nav_drawer3:ObjectProperty(None)
    maillabel:ObjectProperty(None)
    iduser:ObjectProperty(None)
    def home(self,*arg): 
        screen_manager.current = "home" 
    def on_enter(self, *args):
        print(screen_manager.get_screen("loginin").user.text)
        s=screen_manager.get_screen("loginin").user.text
        sql = "SELECT * FROM AllUser WHERE UserName = N'" + s + "'"
        #sql = "SELECT username FROM ali_users "
        c = conn.cursor()  
        c.execute(sql)
        result = c.fetchall()
        print (result)
        #a='welcome:'
        word=''
        us=''
        for record in result:
                word =f'{word}\n{record[5]}'
                
                #self.ids.msg.text =ressh_sen[::-1
                 
                
               
                us =record[0]
                
                self.ids.iduser.text=f'{us}'
                self.ids.maillabel.text=f'{word}'
                         
                te='مرحبا بك:'
                tea=arabic_reshaper.reshape(te)
                #te=tea[::-1]
                print(tea[::-1])
                name =f'{tea[::-1]}\n{record[5]}'
                self.ids.w1.text=f'{name}'


                
   
        return result
        return super().on_enter(*args)
   
@app.route('/login', methods=['GET', 'POST'])

class logininScreen(Screen):
    user = ObjectProperty(None)
    passw = ObjectProperty(None)
    def login_button_action(self):
   
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=alialshhry.com;DATABASE=alyalshhry_shhry;UID=alyalshhry_ali1391;PWD=0et&S74l8') 
   
        c = conn.cursor()  

     
        sql = "SELECT count(*)as count,(select Id FROM AllUser where (UserName =N'"+self.user.text+"' or Email =N'"+self.user.text+"' or Mobile =N'"+self.user.text+"') and  Password=N'"+self.passw.text+"' and active=1) as id,(select UserName FROM AllUser where UserName =N'"+self.user.text+"')as user1 FROM AllUser where (UserName =N'"+self.user.text+"' or Email =N'"+self.user.text+"' or Mobile =N'"+self.user.text+"') and  Password=N'"+self.passw.text+"' and active=1 "
        c.execute(sql) 
        rows = c.fetchall() 
        print(sql)
        iduserV=0
        name1=""
        for x in rows:
            r=x[0]
            
            if (r) ==1 :
         
                print("9")
                iduserV=x[1]
                name1=x[2]
                
                print(iduserV)   
                print("bgbg")   
                print("9")
                homeScreen.home(self)
             

            else:  
                toast('Verify the login information!') 

   
    def raseedstart(self):
            
            pass

    def loginin(self,*arg):
       
        pass
    
    def home(self,*arg): 
        screen_manager.current = "home"  
    
    def raseedstart(self,*arg): 
        screen_manager.current = "raseedstart"      
class profileScreen(Screen):
    nav_drawer3:ObjectProperty(None)
    cbor:ObjectProperty(None)
    pic:ObjectProperty(None)
    usernameInput: ObjectProperty(None)
    emailInput: ObjectProperty(None)
    passwordInput: ObjectProperty(None)
    nav_drawer2:ObjectProperty(None)
    mobilenumInput: ObjectProperty(None)
    selection = ListProperty([])
    numser=ObjectProperty(None)
    lablek=ObjectProperty(None)
    def valpass(selef,passs):
            if  (passs) !="" and len(passs) < 6 :
                return False
            else:
                return True
            
    def valPhone(selef,number):
    
            if  len(number)==12:
                #return number[0] =="0" and number[1]=="5" and number.isdigit()
                return  number.isdigit()
            else:
               return False
        
    def updateuser(self):
        mobile = self.ids.mobilenumInput.text
        passw = self.ids.passwordInput.text
        s=screen_manager.get_screen("home").iduser.text   
        i=0
        j=0
        pass_chis=self.valpass(passw)
        mobile_chis=self.valPhone(mobile)
        

        if pass_chis :
            i=1
                 
        else:
            i=5

        if mobile_chis: 
            j=1
                 
        else:
            j=6


        if (j)==1 and (i)==1 :  
            
            query2 = "update  AllUser set  Mobile='"+mobile+"',Password='"+passw+"',imageuser='"+self.ids.lablek.text+"' WHERE ID = '" + str(s) + "'"
       
            #values2 = (mobile,passw)
            c = conn.cursor()  
            c.execute(query2)
            conn.commit()
            re_text="تمت الحفظ بنجاح"
            ressh_sen=arabic_reshaper.reshape(re_text)
            self.ids.mylabel.text =ressh_sen[::-1]
            self.ids.mylabel.font_name="arial.ttf"
            #self.on_enter(self) 
            print("yes")
        else:
            if (i)==5:
                re_text='كلمة المرور    أقل من ستة خانات'
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.mylabel.text =ressh_sen[::-1]
                self.ids.mylabel.font_name="arial.ttf"
            elif (j)==6:
                re_text='     رقم الجوال يجب أن يكون 12 رقم   '
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.mylabel.text =ressh_sen[::-1]
                self.ids.mylabel.font_name="arial.ttf"
    def check_username(self):
          
            s=screen_manager.get_screen("home").iduser.text  
          
            print(s)
            sql = "SELECT * FROM AllUser WHERE ID = N'" + s + "'"
            print(sql)
            c = conn.cursor()  
            c.execute(sql)
            result = c.fetchone()
          
            word=''
            num=''
            for record in result:
                word =f'{word}\n{record[0]}'
                num =f'{word}\n{record[1]}'
           
                Screen.ids.usernameInput.text=f'{word}'
             
                return result
          
    
    
    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection
        self.ids.pic.source= str(selection[0])

        path=str(selection[0])
        

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
      
        self.ids.pic.source= str(self.selection)
        file_name = os.path.basename(str(self.selection[0]))
        #file = self.selection.filename
        self.ids.lablek.text= file_name
        
        # Copy image to specified path
        filepath = str(self.selection[0])
        print(filepath)
        
        current_dir = os.getcwd()
        print(current_dir) 
        project_path = os.path.abspath(current_dir)
        print(project_path)
        #pathVar =os.StringProperty('images')

        #يعمل هذا الكود
        src_path = filepath
        dst_path = 'images'
        print(dst_path)
      
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False    
    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True
        print("files")
    def select_path(self, path):

        self.exit_manager()
        print(path)
        if os.path.isfile(path)==True:
            Clock.schedule_once(lambda x:self.chpic(path),1)
        #toast(path) #here the location for the image file will be returned
        return path


    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    
    maillabel:ObjectProperty(None)
    

    def on_enter(self, *args):   
        print(screen_manager.get_screen("loginin").user.text)
        s=screen_manager.get_screen("loginin").user.text
           
        sql = "SELECT * FROM AllUser WHERE username = '"+ str(s)+"'"
       
        c = conn.cursor()  
        c.execute(sql)
        result = c.fetchall()
        print (result)
        #a='welcome:'
        word=''
        for record in result:
          
            self.ids.numser.text=f'{record[0]}'
            self.ids.passwordInput.text=f'{record[2]}'
            self.ids.usernameInput.text=f'{record[1]}'
            self.ids.emailInput.text=f'{record[5]}'
            self.ids.mobilenumInput.text=f'{record[6]}'
            im="images/"
            self.ids.lablek.text= f'{record[10]}'
        
            self.ids.pic.source=f'{im}{record[10]}'

            print("sss{cv}")
        
        return result
   
        pass
class regScreen(Screen):
        
        
        usernameInput = ObjectProperty(None)
        emailInput = ObjectProperty(None)
        passwordInput = ObjectProperty(None)
        mylabel= ObjectProperty(None)
        mobilenumInput=ObjectProperty(None)
        labelmsg=ObjectProperty(None)
        global convertToBinary
        global flag

        def insert(self) :
            U= self.usernameInput.text
            E=self.emailInput.text
            p=self.passwordInput.text
            M=self.mobilenumInput.text
            V=''
        def convertToBinary(filename):
            with open (filename,'rb') as file:
                bd=file.read()
            return bd    
            
        def addInfoToDB(self):
            U= self.usernameInput.text
            E=self.emailInput.text
            p=self.passwordInput.text
            M=self.mobilenumInput.text
            V=''
            i=0
            re_text=''

            conn = pyodbc.connect('DRIVER={SQL Server};SERVER=alialshhry.com;DATABASE=alyalshhry_shhry;UID=alyalshhry_ali1391;PWD=0et&S74l8') 
          


            c = conn.cursor()    

            
            sql = "SELECT count(*)as count FROM AllUser where UserName ='"+self.usernameInput.text+"' or mobile='"+self.mobilenumInput.text+"' "
            #adr = (self.usernameInput.text,self.mobilenumInput.text)
            c.execute(sql)
  
            myresult = c.fetchone()

            for x in myresult:
             print(x)
             print(myresult)
            if (x) ==0 :
                flag=0
                i=i+1
            else:  
                flag=1
                
          
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.mylabel.text =ressh_sen[::-1] 
                #return False 
            chiic_email= self.checkemail(E)
            mobile_chis=self.valPhone(M)
            if chiic_email and mobile_chis:    
                flag=0
                i=i+1
            else:
                flag=1
                
            
          
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.mylabel.text =ressh_sen[::-1]
            #valpass    
            
            pass_chis=self.valpass(p)
            if pass_chis :    
                flag=0
                i=i+1
            else:
                flag=1
            
            match i:
                case 1:
                    re_text="اسم المستخدم موجود أو البريد الالكتروني  "
                case 2:
                    re_text="رقم الجوال \البريد الالكتروني خاطيء"
                case 3:
                    re_text="كلمة المرور يجب ان تكون اكثر من 6 حروف او ارقام"    
                
                
            
            
                
            ressh_sen=arabic_reshaper.reshape(re_text)
            self.ids.mylabel.text =ressh_sen[::-1]

            if  (U) == "" or (E) == "" or (p) == "" :
                print("no")
               
                re_text="هناك حقول فارغة"
              
                ressh_sen=arabic_reshaper.reshape(re_text)
                self.ids.mylabel.text =ressh_sen[::-1]
              
    
              
                flag=1
                
              

            else:
                print(flag)
                print(i)
                if (flag)==0 and i==3:
                    
                    query = "INSERT INTO AllUser (UserName, Email, Password,Mobile,fullname,level) VALUES ('"+self.usernameInput.text+"', '"+self.emailInput.text+"', '"+self.passwordInput.text+"', '"+self.mobilenumInput.text+"','"+self.usernameInput.text+"','0')"
                 
                    values = (self.usernameInput.text, self.emailInput.text, self.passwordInput.text,self.mobilenumInput.text,self.usernameInput.text,'0')
                    
                    c.execute(query)
                    conn.commit()
                   
                    tokens="DECLARE @EmployeeID uniqueidentifier SET @EmployeeID = NEWID()  BEGIN   UPDATE AllUser   SET token=@EmployeeID   WHERE email ='"+self.emailInput.text+"'    END"
                    c = conn.cursor()  
                    c.execute(tokens)
                    conn.commit()


                    re_text="تمت الستجيل بنجاح - يجب الدخول على بريدك والضغط على رابط التفعيل"
                    ressh_sen=arabic_reshaper.reshape(re_text)
                    #ressh_sen1=arabic_reshaper.reshape(re_text1)
                    self.ids.mylabel.text =ressh_sen[::-1]+ self.emailInput.text
                    self.ids.mylabel.font_name="arial.ttf"
                    c = conn.cursor()  
                    c.close()
                    conn.close()
                 
                    sender_email = 'pythonshehri@gmail.com'
                    sender_password = 'vbyuioulpnsntovn'
                    recipient_email = self.emailInput.text

                  
                    msg = MIMEText(f'شكرا لتسجيلك! فضلا اضغط على الرابط لتفعيل تسجيلك: http://alialshhry.com/LoginF/show2?email={self.emailInput.text}')
                    msg['Subject'] = 'Activate Your Account'
                    msg['From'] = sender_email
                    msg['To'] = recipient_email

                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.starttls()
                        smtp.login(sender_email, sender_password)
                        smtp.send_message(msg)

                        # Show success message and switch to login screen
                        success_label = Label(text='Registration successful! Please check your email to activate your account')
               
                else  :    
                    
                    #ressh_sen=arabic_reshaper.reshape(re_text2)
                    pass
                    #self.ids.mylabel.text =ressh_sen[::-1]
                return True
        def show_toast(self, instance):
            toast = toast(text='This is a toast message!', font_size=30, font_name='Arial')
            toast.show()    
        def openSnackbar(self):
            sb = toast(text="This is a snackbar!")
            sb.ids.text_bar.font_name = 'arial.ttf'
            sb.open()    
        def valpass(selef,passs):
            if  (passs) !="" and len(passs) < 6 :
                return False
            else:
                return True
    
        def check_Email(email):
            #conn = pyodbc.connect('DRIVER={SQL Server};SERVER=alialshhry.com;DATABASE=alyalshhry_shhry;UID=alyalshhry_ali1391;PWD=0et&S74l8') 
            sql = "SELECT * FROM AllUser WHERE Email = '" + email + "'"
            c = conn.cursor()  
            c.execute(sql)
            result = c.fetchone()
            print(email)
            return result
            cursor.close()
            db.close()
            pass
            
 
# Define a function for
# for validating an Email
        def checkemail(selef,email):
            #email = selef.ids.emailInput.text
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
            if(re.fullmatch(regex, email)):
                #print("Valid Email")
                return True
            else:
                #print("Invalid Email")
                return False
 
        def check_mobile(mobile):
            sql = "SELECT * FROM AllUser WHERE Mobile = '" + mobile + "'"
            c = conn.cursor()  
            c.execute(sql)
            result = c.fetchone()
            return result
             
        def register_user(username,email, password, mobile):
            if  regScreen.check_Email(email) is None and regScreen.check_mobile(mobile) is None:
                password = encodings.encrypt_password(password)
                #NewG="SELECT NEWID() GO  'C14D84F3-1AC6-4A8B-BA1A-3B4CAB06EDD1' DECLARE @EmployeeID uniqueidentifier SET @EmployeeID = NEWID()"
                query = "INSERT INTO AllUser (UserName, Email, Password,Mobile,fullname,level) VALUES ('"+username+"', '"+email+"', '"+password+"', '"+mobile+"','"+username+"','0')"
                values = (username, email, password,mobile,username,'0')
                c = conn.cursor()  
                c.execute(query)
                conn.commit()

                tokens="DECLARE @EmployeeID uniqueidentifier SET @EmployeeID = NEWID()  BEGIN   UPDATE AllUser   SET token=@EmployeeID   WHERE email = email    END"
                c = conn.cursor()  
                c.execute(tokens)
                conn.commit()


                if c.rowcount > 0:
                    return True
                else:
                    return False
            else:
                    return False
            
        def show_example_snackbar(self, snack_type):
            def callback(instance):
                toast(instance.text)    
        def on_text_validate(self):
             #usernameInput = self.ids['usernameInput'].text
             #self.ids['usernameInput'].text = ''
             usernameInput= self.root.ids.usernameInput
             #my_label=self.root.ids.my_label
             my_label=self.root.ids['my_label']
             my_label.text = usernameInput.text
             pass
        def sent(self):
            #email_list = ["alyalshhry@gmail.com"]
            email_list=[self.ids.emailInput.text]

            #sendmail.send_emails(email_list)
        def valPhone(selef,number):
    
            if  len(number)==12:
                #return number[0] =="0" and number[1]=="5" and number.isdigit()
                return  number.isdigit()
            else:
               return False
        
            
class LoginApp(MDApp,Screen):
    user = ObjectProperty(None)
    passw = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager1 = Builder.load_file('regster.kv')
        city = 'Tokyo'
        self.get_text(city)
           
        #self.screen_manager = Builder.load_file('regster.kv')
    def update_label(self):
       
        print(self.user.text )    
   
    
    def d(self):
        #    E =object.id.emailInput
        emailInput = self.root.ids.emailInput
        re_text="رقم الجوال: "
        ressh_sen=arabic_reshaper.reshape(re_text)
        mylabel = self.root.ids.mylabel
        emailInput.text =ressh_sen[::-1]
        #    emailInput = ObjectProperty(None)
    def get_text(self, city_name):
        #self.screen_manager.ids.emailInput.text = +city_name    
        pass
    def buildv(self):
     #self.screen_manager.ids.reg.ids.usernameInput.hint_text='sdd'
     return self.screen_manager
    def build(self,**kwargs):
        self.icon="images/logoali.ico"
        text3 = ("مسجد الخير")
        reshaped_texts3 = arabic_reshaper.reshape(text3)
        res3 = bidi.algorithm.get_display(reshaped_texts3)
        print (res3)            
        #return self.manager
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("per_splash.kv"))
        #screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(regScreen(name='reg'))
        screen_manager.add_widget(logininScreen(name='loginin'))
        screen_manager.add_widget(logininScreen(name='screenhome'))
        screen_manager.add_widget(homeScreen(name='home'))
        screen_manager.add_widget(raseedstartScreen(name='raseedstart'))
        screen_manager.add_widget(msrofatScreen(name='msrofat'))
        screen_manager.add_widget(tsgeelScreen(name='tsgeel'))
        screen_manager.add_widget(profileScreen(name='profile'))
        screen_manager.add_widget(profileScreen(name='fileshow'))
        
        emailInput = ObjectProperty(None)
       
        return screen_manager
    
    
    def openscreen(self):
     
        screen_manager.current = "reg"
    
    def openprofile(self):
      
        screen_manager.current = "profile"
      
    def callback_1(self):
       #screen_manager.current = "main"
       print("1000000")
       self.close()
    def callback_close(self):
        self.stop()
    def on_start(self):
       #return Builder.load_string(KV)
       Clock.schedule_once(self.mainscrenn,5)
       
    def on_enter(self):
           #usernameInput = ObjectProperty()
           #print('User pressed enter in', instance)
           print (self.root.ids.usernameInput.text)
           #textinput = usernameInput(text='Hello world', multiline=False)
           #textinput.bind(on_text_validate= on_enter )
        #print(usernameInput)
    
    def arab(self):
        re_text=arabic_reshaper.reshape('علي')
        bidi_text = bidi.algorithm.get_display(re_text)
        return Label (text=bidi_text,
                      color= (0,0,1,1),
                      font_size=40,
                      font_name="arial.ttf"
                      )
   
        
    def login(self,*arg):
          
        screen_manager.current = "loginin"      
    def loginin(self,*arg):
        
        screen_manager.current = "loginin"          
        # MainscApp().build()
    def mains(self,*arg):
       
        screen_manager.current = "scr1"
    def raseedstart(self,*arg):
       
        screen_manager.current = "raseedstart" 
    def srfshow(self,*arg):
        
        screen_manager.current = "msrofat"     
    def tsgeelshow(self,*arg):
        screen_manager.current = "tsgeel"     
        pass
    def addR(self,*arg):
        screen_manager.current = "tsgeel"     
        pass


    def toto(self,*arg):
          
        main.kv.nav_drawer.set_state("open")
    def mainscrenn(self,*arg):
       
        screen_manager.current = "main"
       
        #cnxn.commit()
        #cnxn.close()
    
class registerScreen(Screen) :
        
   
    def valMobile(usernameInput):
        if  (usernameInput) !="" and len(usernameInput) < 6 :
           print ("yes")
           return False
          
        else:
            print ("no")
            
        print ("yes")
    #valMobile(usernameInput)     
        
if __name__ == '__main__' :
   LoginApp().run()


