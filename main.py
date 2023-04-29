from kivy.app import App
from kivy.uix.label import Label


class TelegramAccountApp(App):
    def build(self):
        return Label(text="hello my account ")


TelegramAccountApp().run()