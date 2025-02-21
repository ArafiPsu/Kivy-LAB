from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

class ScatterTextWidget(BoxLayout):
    def change_label_color(self, *args):
        # ตรวจสอบว่า TextInput มีข้อความหรือไม่ และยาวเกิน 5 ตัวอักษร
        text = self.ids['my_textinput'].text
        
        if len(text) > 5:  # ถ้ามีข้อความมากกว่า 5 ตัวอักษร
            # เปลี่ยนสีเป็นสุ่ม
            colour = [random.random() for i in range(3)] + [1]
            label = self.ids['my_label']
            label.color = colour
            print("เปลี่ยนสีแล้ว")
        else:
            # ถ้ามีข้อความน้อยกว่าหรือเท่ากับ 5 ตัวอักษร ไม่เปลี่ยนสี
            print("ข้อความต้องยาวมากกว่า 5 ตัวอักษรถึงจะเปลี่ยนสี")

class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    TutorialApp().run()
