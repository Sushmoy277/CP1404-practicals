from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKm(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Convert miles to kilometres and update the output label."""
        miles = self.get_miles()
        kilometres = miles * MILES_TO_KM
        self.output_km = f"{kilometres:.3f}"

    def handle_increment(self, change):
        """Up/Down the miles value and update the TextInput."""
        miles = self.get_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)

    def get_miles(self):
        """Get miles value from TextInput, or 0.0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesToKm().run()
