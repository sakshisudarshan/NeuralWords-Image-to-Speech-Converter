import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.filechooser import FileChooserListView
from kivy.clock import Clock
from gtts import gTTS
import requests
import os

kivy.require('2.0.0')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.popup = None
        self.build_ui()

    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        top_bar = BoxLayout(size_hint=(1, 0.1), padding=[5, 5])
        back_button = Button(text="Back", size_hint=(0.1, 1), background_color=(0.8, 0.3, 0.3, 1))
        back_button.bind(on_press=self.on_back)
        title_label = Label(text="NEURAL WORDS", size_hint=(0.95, 1), font_size='24sp', bold=True,
                            color=(0.2, 0.4, 0.6, 1))
        top_bar.add_widget(back_button)
        top_bar.add_widget(title_label)
        layout.add_widget(top_bar)

        self.image_display = Image(source='', size_hint=(1, 0.6), allow_stretch=True, color=(1, 1, 1, 1))
        self.image_display.bind(on_touch_down=self.on_image_click)
        layout.add_widget(self.image_display)

        layout.add_widget(BoxLayout(size_hint=(1, 0.05)))

        play_button = Button(text="Replay", size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5},
                             background_color=(0.3, 0.5, 0.8, 1), font_size='18sp')
        play_button.bind(on_press=self.on_play)
        layout.add_widget(play_button)

        self.result_label = Label(size_hint=(1, 0.2), halign='center', valign='middle', text_size=(self.width, None),
                                  color=(0.1, 0.1, 0.1, 1))
        layout.add_widget(self.result_label)

        self.add_widget(layout)

    def on_image_click(self, instance, touch):
        if self.image_display.collide_point(*touch.pos):
            self.open_file_chooser()

    def open_file_chooser(self):
        file_chooser = FileChooserListView(path='/Users/sakshisudarshan/IMAGES')
        file_chooser.bind(on_submit=self.load_image)
        self.popup = Popup(title='Select an image', content=file_chooser, size_hint=(0.9, 0.9))
        self.popup.open()

    def load_image(self, instance, path, *args):
        if path:
            self.image_display.source = path[0]
            if self.popup:
                self.popup.dismiss()
            Clock.schedule_once(lambda dt: self.process_image(self.image_display.source),
                                2)

    def on_play(self, instance):
        if self.image_display.source:
            self.process_image(self.image_display.source)

    def process_image(self, image_path):
        url = 'http://127.0.0.1:5000/process_image'
        files = {'file': open(image_path, 'rb')}
        try:
            response = requests.post(url, files=files)
            if response.status_code == 200:
                result = response.json()
                extracted_text = result.get('text_result', '').strip()
                caption = result.get('caption_result', 'No caption found')

                if extracted_text:
                    self.text_to_speech(f"Extracted Text: {extracted_text}. Caption: {caption}")
                else:
                    self.text_to_speech(f"Caption: {caption}")

            else:
                self.result_label.text = "Error processing image"
                print("Error processing image:", response.text)
        except requests.exceptions.RequestException as e:
            self.result_label.text = "Error processing image"
            print("Error processing image:", e)

    def text_to_speech(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('output.mp3')
        os.system("open output.mp3")

    def on_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'previous_screen_name'


class NeuralWordsApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm


if __name__ == '__main__':
    NeuralWordsApp().run()