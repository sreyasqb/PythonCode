import Teacher_app as Ta
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import ObjectProperty
from kivy.app import App
kv=Builder.load_file("my.kv")
# class MyGrid(GridLayout):
#     def __init__(self,**kwargs):
#         super(MyGrid,self).__init__(**kwargs)
#         self.cols=1
#         self.add_widget(Label(text="Name :"))
#         self.name=TextInput(multiline=False)
no_of_questions=ObjectProperty(None)
class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
screen_manager=ScreenManager()

screen_manager.add_widget(MainWindow(name="main"))
screen_manager.add_widget(SecondWindow(name="second"))

class MyApp(App):
    def build(self):
        return screen_manager


    #MyGrid()
MyApp().run()
