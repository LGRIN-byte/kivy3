import os
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
import kivy.properties as kyprops
from kivy.clock import mainthread
from kivy.lang import Builder
from datetime import date, timedelta
from kivy.uix.checkbox import CheckBox 
from kivy.uix.label import Label 
from kivy.uix.widget import Widget 
from kivy.uix.gridlayout import GridLayout
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.slider import Slider

Window.clearcolor = (1, 1, 1, 1)


LabelBase.register(name="main", 
fn_regular="NanumBarunGothic.ttf"
)

gui = '''
#:import utils kivy.utils


MyScreenManager

    LoginScreen
        name: 'login'
        
    HomeScreen
        name: 'home'
    UserGroup
        name: 'info'
    InfoScreen2
        name: 'info2'
    EndScreen:
        name: 'end'
        
<Label>:
    
	color: 0,0,0,1
    font_name: 'main'
<QLabel@Label>:
    text: "도서 예약"
                
    font_size: 50
    size_hint: (1, 0.5)
        
	color: 1,1,1,1
    canvas.before:
        Color:
            rgba: 0.2, 0.23, 0.50, 1    
        Rectangle:
            pos: self.pos
            size: self.size
                
<Button>:
    font_size: 40
	size: 170,75
	color: 1,1,1,1
    size_hint: (1, 0.7)
<LoginScreen>
    entered_email_address:entered_email_address
    email_address:entered_email_address.text
    entered_password:entered_password
    password: entered_password.text
    
    

    BoxLayout:
    
        GridLayout:
            cols:1
            canvas:
                
            QLabel:
                id: main_title1

         #       text: "도서 예약"
                font_name: 'main'
                
                
                        
            
            Label:
                text: ''
                size_hint: (1, 0.3)
                
                
            BoxLayout:
                
            
                Image:
                    id: main_image
                    source: "logo.png"
                    
            BoxLayout:
                orientation: "vertical"
                
                

                Label:
                    id: main_title


                    text: "학번과 이름을 입력해주세요"
                    font_name: 'main'
                    halign: 'center'
                    valign: "top"
                    
                    font_size: 40
                    size_hint: (1, 0.3)
                
                Label:
                    text: '정보를 잘못 입력할 시 책임지지 않습니다.'
                    font_name: 'main'
                    font_size: 20
                    
#                    size_hint: (1, 0.2)


                
   
            GridLayout:
                    
                cols: 2
                spacing: 10, 10
                padding: 10, 10

    
                Label:
                    text: '이름'
                    font_name: 'main'
                            
                    halign: 'center'
                    font_size: 30
                   
                    
                    height: 60
                    size_hint_x: 60
                                        
                TextInput:
 
                    id: entered_email_address
                    font_name: 'main'

                    
                    multiline: False
                    size_hint: 1, None
                    
                    height: 60
                    
                    size_hint_x: 120
                    
                Label:
                    text: '학번'
                    font_name: 'main'
                    
                    halign: 'center'
                    font_size: 30
                   
                    size_hint_x: 60
                    height: 60
                    
                    
                TextInput:
                    id: entered_password
                    multiline: False
                    size_hint: 1, None  
                    hint_text: "only number"
                    input_filter: "float" 
                    height: 60
                    size_hint_x: 120
            
                
            Label:
                text: ''
                size_hint: (1, 0.4)

            Button:
            
                id: btn_login
       
                text: '로그인'
                font_name: 'main'
                   
                size_hint: (1, 0.7)
                    #    height: 40  
                    #    width: 50
                on_press:
                    if root.email_address== "" or root.password=="" : root.manager.current = 'login' 
                    else:root.manager.current = 'home'

<HomeScreen>
    BoxLayout:
        BoxLayout:
            BoxLayout:
                orientation: "vertical"
                canvas:
                
                QLabel:
                    id: main_title1

                    text: "자리 예약"
                    font_name: 'main'
                Label:
                
                    text: ""
                    size_hint_y: 0.2
                BoxLayout:
                
            
                    Image:
                        id: main_image
                        source: "bb.png"
                        
                BoxLayout:
                    
                    Label:
                        
                        text: "이름과 학번을 확인해주세요"
                        font_name: 'main'
                        halign: 'center'
                        valign: "top"
            
                        font_size: 40
                        size_hint: (1, 0.3)
                        canvas.before:
                            Color:
                                rgba: 1, 0.2, 0, 0    # red
                            Rectangle:
                                pos: self.pos
                                size: self.size
                          

                BoxLayout:
                    orientation: "vertical"
                              
                   
                        
                        
                    Label:
                        text: "이름:" +root.email_address
                        font_name: 'main'
                        font_size: 40
                        size_hint_y: 0.3
                        
                    Label:
                        text: " 학번:" + root.password
                        
                        font_size: 40
                        size_hint_y: 0.3
                BoxLayout:
                    orientation: "vertical"
                    BoxLayout:
                                
                        Button:
                            text: '정보 다시 입력하기'
                            font_name: 'main'
                       
                            on_press: root.manager.current = 'login'
                        Button:
                            text: '장소 정하기'
                            font_name: 'main'
                            on_press: root.manager.current = 'info'

<MCQCheckBox@CheckBox>:
    color:  0, 0, 0, 1  
    size_hint: 0.15, 1                             
    
<CustomLabel@Label>:
   
    valign: "middle"
    
    padding_x: 5



<GreenButton@Button>:
    background_color: 1, 1, 1, 1
    size_hint: (1, 0.7)



<UserGroup>

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
     
    BoxLayout:        
        BoxLayout:  
            orientation: 'vertical'
            
            QLabel:
                id: main_title1

                text: "자리 예약"
                font_name: 'main'
           
                          
            BoxLayout:  
                orientation: 'vertical'
            
                Label:
                    
                    text: "위치를 정해주세요"
                    font_name: 'main'
                    font_size: 50
                    
                    color: 0,0,0,1
                            



            GridLayout:
                cols: 2
                padding : 30,30
                spacing: 20, 20
                row_default_height: '30dp'
                

                Label:
                    text: '중앙도서관 열람실'
                    font_name: 'main'
                   
                   
                    valign: 'middle'
                    font_size: 40
                    color: 0,0,0,1
                    size_hint: (1, 0.2)
                    

                MCQCheckBox:
                    group: 'check'
                    id : chk
                    halign: 'center'
                
                    text: "중앙도서관 열람실"
                    size_hint: (1, 0.2)
                    
                    on_active:
                        root.pla = self.text


                Label:
                    text: '중앙도서관 레퍼런스룸'
                    font_name: 'main'
                   
  
                    valign: 'middle'
                    font_size: 40
                    
                    
                    color: 0,0,0,1
                MCQCheckBox:
                    group: 'check'
                    id : chk
                    text: "중앙도서관 레퍼런스룸"
                    
                    
                    on_active:
                        root.pla = self.text
                Label:
                    text: '미래 열람실'
                    font_name: 'main'
                    font_size: 40
                   
                    valign: 'middle'

                    color: 0,0,0,1
                MCQCheckBox:
                    group: 'check'
                    text: "미래 열람실"
                    size_hint: (1, 0.2)
                    
                    on_active:
                        root.pla = self.text
                Label:
                    text: '미래 레퍼런스룸'
                    font_name: 'main'
                    font_size: 40
                   
                    valign: 'middle'
                    color: 0,0,0,1
                MCQCheckBox:
                    group: 'check'
                    text: "미래 레퍼런스룸"
                    size_hint: (1, 0.2)
                    
                    on_active:
                        root.pla = self.text

    
            BoxLayout:
                orientation: "horizontal"

                GreenButton:
                    text: '로그아웃'
                    font_name: 'main'
                    
                    on_press: root.manager.current = 'login'
            
                        
                GreenButton:
                    text: '이전'
                    font_name: 'main'
                    
                    on_press: root.manager.current = 'home'
    
                        
                GreenButton:
                    text: '선택'
                    font_name: 'main'
                    
                    on_press:  
                        if root.pla== ""  : root.manager.current = 'info' 
                        else:root.manager.current = 'info2'

                        
                GreenButton:
                    text: '종료'
                    font_name: 'main'
                    
                    on_press: app.stop()

                    

<InfoScreen2>

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
    BoxLayout:        
        BoxLayout:  
            orientation: 'vertical'
            
            QLabel:
                id: main_title1

                text: "자리 선택"
                font_name: 'main'
           
                          
            BoxLayout:  
                orientation: 'vertical'
            
                Label:
                    
                    text: "자리 번호를 정해주세요"
                    font_name: 'main'
                    font_size: 50
                    
                    color: 0,0,0,1
                Label:
                    text: root.pla + "의" + str(slider.value)+"번 자리입니다."
                    font_size: 40
                            
     
            BoxLayout: 
                Slider:
                    id: slider
                    min: 1
                    max: 30
                    step: 1
                    orientation: 'horizontal'
                
 
            BoxLayout:
                BoxLayout: 
                    orientation: "horizontal"

                    GreenButton:
                        text: '로그아웃'
                        font_name: 'main'
                            
                        on_press: root.manager.current = 'login'
                    
                                
                    GreenButton:
                        text: '이전'
                        font_name: 'main'
                            
                        on_press: root.manager.current = 'home'
            
                                
                    GreenButton:
                        text: '선택'
                        font_name: 'main'
                            
                        on_press:  
                            root.num= str(slider.value)
                        on_release:
                            root.manager.current = 'end'
                                
                    GreenButton:
                        text: '종료'
                        font_name: 'main'
                            
                        on_press: app.stop()


<EndScreen>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
    BoxLayout:        
        BoxLayout:
            BoxLayout:  
                orientation: 'vertical'
                
                QLabel:
                    id: main_title1

                    text: "자리 선택"
                    font_name: 'main'
            
                    
                        
                Label:
                    text: root.password+" "+root.email_address+"님"
                    font_size: 40
                Label:
                    text: root.pla + "의 " + root.num+"번 자리예약"
                    font_size: 40
                Image:
                    id: main_image
                    source: "cc.gif"
                    
                    
                BoxLayout: 
                    orientation: "horizontal"
                    GreenButton:
                        text: '로그아웃'
                        font_name: 'main'
                                        
                        on_press: root.manager.current = 'login'
                                    
                                                
                    GreenButton:
                        text: '이전'
                        font_name: 'main'
                                        
                        on_press:  
                            root.num= str(slider.value)
                        on_release:
                            root.manager.current = 'end'
                                            
                    GreenButton:
                        text: '종료'
                        font_name: 'main'
                                            
                        on_press: app.stop()


                
'''


class LoginScreen(Screen):
    entered_email_address = kyprops.ObjectProperty("")
    entered_password = kyprops.ObjectProperty(None)
    email_address = kyprops.StringProperty("")
    password = kyprops.StringProperty("")

class HomeScreen(Screen):
    email_address = kyprops.StringProperty("")
    password = kyprops.StringProperty("")


class UserGroup(Screen):
    pla =kyprops.StringProperty("")

class InfoScreen2(Screen):

    pla =kyprops.StringProperty("")
    num =kyprops.StringProperty("")
class EndScreen(Screen):
    email_address = kyprops.StringProperty("")
    password = kyprops.StringProperty("")

    pla =kyprops.StringProperty("")
    num =kyprops.StringProperty("")


class MyScreenManager(ScreenManager):

    def __init__(self, *args, **kwargs):
        
        super(MyScreenManager, self).__init__(*args, **kwargs)

        @mainthread
        
        def delayed():
            home_screen = self.get_screen('home')
            login_screen = self.get_screen('login')
            UserGroup = self.get_screen('info')
            Info_screen2 = self.get_screen('info2')
            end_screen=self.get_screen('end')
            login_screen.bind(email_address=home_screen.setter('email_address'))
            login_screen.bind(password=home_screen.setter('password'))
            
            UserGroup.bind(pla=Info_screen2.setter('pla'))
            login_screen.bind(email_address=end_screen.setter('email_address'))
            login_screen.bind(password=end_screen.setter('password'))
            UserGroup.bind(pla=end_screen.setter('pla'))
            
            Info_screen2.bind(num=end_screen.setter('num'))
                
        delayed()


class Test(App):

    def build(self):
        
        return Builder.load_string(gui)

Test().run()