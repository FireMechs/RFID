from kivy.uix.boxlayout import BoxLayout

class Verfs(BoxLayout):
    def __init__(self, **kwargs):
        super(Verfs, self).__init__(**kwargs)

    def setText(self, text):
        self.ids.verfsLabel.text = text