from kivy.app import App
from kivy.lang.builder import Builder
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
class LoadDialog(FloatLayout):
    Builder.load_file('load_dialog.kv')
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
