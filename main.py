from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout

from sound_kit_service import SoundKitService
from track import TrackWidget

Builder.load_file("track.kv")

class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.sound_kit_service = SoundKitService()

    # Used because cannot edit Widget before it is initialised.
    def on_parent(self, widget, parent):
        for i in range(self.sound_kit_service.get_nb_tracks()):
            sound = self.sound_kit_service.get_sound_at(i)
            self.tracks_layout.add_widget(TrackWidget(sound))

class MrBeatApp(App):
    pass

if __name__ == "__main__":
    MrBeatApp().run()