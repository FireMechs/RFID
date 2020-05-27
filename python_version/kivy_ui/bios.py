from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

class Bios(GridLayout):
    def __init__(self, **kwargs):
        Clock.schedule_interval(self.on_detected, 0.5)
        super(Bios, self).__init__(**kwargs)
    def on_detected(self, dt):
        self.ids.name.text = 'Eric Kipngeno Koech'
        self.ids.reg_no.text = 'ENM221-0068/2017'
        self.ids.tag_data.text = 'Dummy Text'
        self.ids.serial_no.text = '5CB2032SYK' + str(dt)