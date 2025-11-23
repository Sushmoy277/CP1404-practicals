from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicNamesApp(App):
    """Simple app that displays a list of names using dynamic Labels."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Irfan", "Enab", "Arijit", "Akif", "Masran"]

    def build(self):
        """Build GUI and dynamically add Labels for each name."""
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name, font_size=32)
            self.root.ids.main.add_widget(temp_label)

        return self.root


DynamicNamesApp().run()
