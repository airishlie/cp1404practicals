"""
CP1404/CP5632 Practical
Kivy GUI program to square a number (refactored version)
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward (Refactored)'

class SquareNumberApp(App):
    """Kivy App to square a number with refactoring"""
    def build(self):
        Window.size = (400, 200)
        self.title = "Square Number 2"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, text_value):
        """Handle calculation and display result in output label with error handling"""
        try:
            number = float(text_value)
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

SquareNumberApp().run()

