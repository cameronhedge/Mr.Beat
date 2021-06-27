from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

TRACKS_NB_STEPS = 16

class TrackStepButton(ToggleButton):
    pass

class TrackSoundButton(Button):
    pass


class TrackWidget(BoxLayout):
    def __init__(self, sound):
        super().__init__()
        sound_button = TrackSoundButton()
        sound_button.text = sound.displayname
        self.add_widget(sound_button)
        for i in range(TRACKS_NB_STEPS):
            self.add_widget(TrackStepButton())