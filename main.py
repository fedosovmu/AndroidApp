from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 2
        self.spinner = Spinner(
            text='Hello world',
            values=('Hello world!', 'Привет мир!', 'I am android app', 'Test Test')
        )
        self.add_widget(self.spinner)
        self.button = Button(text='Изменить надпись')
        def button_press(button):
            self.lable.text = self.spinner.text
        self.button.bind(on_press=button_press)
        self.add_widget(self.button)
        self.lable = Label(text='Lable text', height=100)
        self.add_widget(self.lable)


class MyApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()