from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from sandbox import SandBox
from verfs import Verfs

class Bios(GridLayout):
    def __init__(self, **kwargs):
        self.data = []
        Clock.schedule_interval(self.on_detected, 0.5)
        super(Bios, self).__init__(**kwargs)
    def on_detected(self, dt):
        sd = SandBox()
        vf = Verfs()
        self.data = sd.handle_data()
        if self.data[0] == sd.No_data:
            vf.setText(sd.No_data)
        else:
            self.ids.reg_no.text = self.data[0]
            self.ids.serial_no.text = self.data[1]
            self.ids.phone_no.text = str(self.data[2])