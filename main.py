from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.screen import MDScreen


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return (
            MDScreen(
                MDFloatingActionButtonSpeedDial(
                    id="speed_dial",
                    hint_animation=True,
                    root_button_anim=True,
                )
            )
        )

    def on_start(self):
        data = {
            "Python": "language-python",
            "JS": [
                "language-javascript",
                "on_press", lambda x: print("pressed JS"),
                "on_release", lambda x: print(
                    "stack_buttons",
                    self.root.ids.speed_dial.stack_buttons
                )
            ],
            "PHP": [
                "language-php",
                "on_press", lambda x: print("pressed PHP"),
                "on_release", self.callback
            ],
            "C++": [
                "language-cpp",
                "on_press", lambda x: print("pressed C++"),
                "on_release", lambda x: self.callback()
            ],
        }
        self.root.ids.speed_dial.data = data

    def callback(self, *args):
        print(args)


Example().run()