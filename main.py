import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from plyer import tts


class SayThis(BoxLayout):
    saywhat_text = ObjectProperty(None)

    def say_something(self, text):
        try:
            tts.speak(text)
        except NotImplementedError:
            popup = Popup(title= "TTS Not Implimented",
                            content = Label(text="Sorry. TTS is not available"),
                            size_hint=(None, None),
                            size=(300, 300))
            popup.open()
    def clear(self):
        self.saywhat_text.text = ""
        self.saywhat_text.focus = True

class SayThisApp(App):
    def build(self):
        return SayThis()

if __name__ == "__main__":
    SayThisApp().run()