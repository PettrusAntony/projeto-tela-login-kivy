from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config

Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', '1')


class PageApp(App):
   def build(self):
      pg = PageLayout()
      btn1 = Button(text ='Page 1')
      btn2 = Button(text ='Page 2')
      btn3 = Button(text ='Page 3')
      pg.add_widget(btn1)
      pg.add_widget(btn2)
      pg.add_widget(btn3)
      return pg



class PageDemoApp(App):
   def build(self):
      pass

if __name__ == '__main__':
   PageDemoApp().run()