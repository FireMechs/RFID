from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder

Builder.load_file("bios.kv")
Builder.load_file("verfs.kv")

class Display(AnchorLayout):
    pass

class DisplayApp(App):
    def build(self):
        return Display()

if __name__ == "__main__":
    DisplayApp().run()