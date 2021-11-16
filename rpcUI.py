from kivy.core.text import Text
from time import time
from pypresence import Presence
from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.textinput import TextInput

Window.size = (400,400)
Window.clearcolor = (42/255, 42/255, 42/255, 1)

class Program(App):
    def __init__(self):
        super().__init__()
        self.rpcid = TextInput(hint_text = "RPC ID: ", size = (4,4), multiline = False, height = 30)
        
        self.state = TextInput(hint_text = "State: ", size = (4,4), multiline = False)
        
        self.details = TextInput(hint_text = "Details: ", size = (4,4), multiline = False)
        
        self.large_text = TextInput(hint_text = "Large Text: ", size = (4,4), multiline = False)
        
        self.labtext = Label(text = "RPC кнопка: ", size = (4,4))
        
        self.labell = TextInput(hint_text = "Имя кнопки: ", size = (4,4), multiline = False)
        self.url = TextInput(hint_text = "Ссылка при нажатии: ", size = (4,4), multiline = False)
        self.li = TextInput(hint_text = "Имейдж: ", size = (4,4), multiline = False)
        
        self.btn = Button(text = "Выполнить", size = (4,4))
        self.btn.bind(on_press = self.on_press)
        
        self.disc = Button(text = "Завершить")
        self.disc.bind(on_press = self.dsc)
    def dsc(self, *args): 
        self.RPC.disconnect()
    def on_press(self, *args): 
        self.RPC = Presence(self.rpcid.text)
        self.RPC.connect()
        btns = [
            {
                "label":self.labell.text if self.labell.text != None else None, 
                "url":self.url.text if self.url.text != None else None
            }
        ]
        self.RPC.update(
            state = self.state.text if self.labell.text != None else None, 
            details = self.details.text if self.details.text != None else None,
            large_text = self.large_text.text if self.large_text.text != None else None,
            buttons = btns if self.url.text and self.labell.text != None else None,
            start= time(),
	        large_image = self.li.text if self.li.text != None else None
        )
        
    def build(self):
        mainLay = BoxLayout(orientation = "vertical", spacing = 2, padding = (40, 40,40,40))
        mainLay.add_widget(self.rpcid)
        mainLay.add_widget(self.state)
        mainLay.add_widget(self.details)
        mainLay.add_widget(self.large_text)

        mainLay.add_widget(self.labtext)
        mainLay.add_widget(self.labell)
        mainLay.add_widget(self.url)
        mainLay.add_widget(self.li)
        mainLay.add_widget(self.btn)
        mainLay.add_widget(self.disc)

        return mainLay



if __name__ == "__main__":
    Program().run()