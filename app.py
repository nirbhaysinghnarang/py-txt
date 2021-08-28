from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.codeinput import CodeInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from pygments.lexers import CythonLexer
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.graphics import Rectangle, Color
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os
from load_dialog import LoadDialog
from save_dialog import SaveDialog

class PyTxt(App):
    def build(self):
        root = BoxLayout(orientation="horizontal")
        topBar = BoxLayout(orientation="horizontal",
                           size=(50,50),
                           size_hint=(None,None))
        layout = BoxLayout(orientation='vertical',
                        size=(200,200),
                        size_hint=(None, None))
        btn1 = Button(text='Save',
                    size=(layout.width,100),
                    size_hint=(None, None),
                    pos=(0,layout.height),
                    background_color="#26367D")
        btn2 = Button(text='Open',
                    size=(layout.width,100),
                    size_hint=(None, None),
                    pos=(0,layout.height),
                    background_color="#26367D")
        btn1.bind(on_press = self.save_file)
        btn2.bind(on_press=self.show_load)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        self.code_input = CodeInput(lexer=CythonLexer())
        root.add_widget(layout)
        root.add_widget(self.code_input)
        return root
    def save_file(self,i):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,size_hint=(0.9, 0.9))
        self._popup.open()
    def show_load(self,i):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        print(content)
        self._popup = Popup(title="Load file", content=content,size_hint=(0.9, 0.9))
        self._popup.open()
    def dismiss_popup(self):
        self._popup.dismiss()
    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.code_input.text)
        self.dismiss_popup()
    def load(self, path, filename,):
        with open(os.path.join(path, filename[0])) as stream:
            self.code_input.text = stream.read()
        self.dismiss_popup()
