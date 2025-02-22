from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.img = Image(source="catcry.webp", pos=(300, 500), size=(100, 100))
        self.add_widget(self.img)

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == "__main__":
    app = MyApp()
    app.run()
    
    