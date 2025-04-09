from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]  # daftar nama (strings)

    def build(self):
        root = BoxLayout(orientation='vertical')
        for name in self.names:
            label = Label(text=name)
            root.add_widget(label)
        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()

