import datetime

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.clock import Clock


# class LoginScreen(GridLayout):
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)


class MyApp(App):
    now_ja = StringProperty("hello world")

    def update(self,*args):
        self.now_ja = str(datetime.datetime.now())

    def build(self):
        Clock.schedule_interval(self.update, 1)
        return Label(text=self.now_ja)


if __name__ == '__main__':
    MyApp().run()
