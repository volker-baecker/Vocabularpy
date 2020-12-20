import kivy.app
import kivy.uix.label
import arabic_reshaper
import bidi.algorithm

from kivy.properties import NumericProperty, StringProperty
from kivy.uix.textinput import TextInput


class ArText(TextInput):
    max_chars = NumericProperty(20)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(ArText, self).__init__(**kwargs)

    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str+substring
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(ArText, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape(self.str))

class TestApp(kivy.app.App):
    def build(self):
        reshaped_text = arabic_reshaper.reshape("سضمخک")
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        label = kivy.uix.label.Label(text=bidi_text, font_name="DejaVuSans")
        textInput = ArText(text=bidi_text, font_name="DejaVuSans")
        button = kivy.uix.button.Button(text=bidi_text, font_name="DejaVuSans")

        boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        boxLayout.add_widget(label)
        boxLayout.add_widget(textInput)
        boxLayout.add_widget(button)
        return boxLayout


testApp = TestApp()
testApp.run()