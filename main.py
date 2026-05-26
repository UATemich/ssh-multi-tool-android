from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

import requests


class SSHApp(MDApp):

    def build(self):
        self.screen = Screen()

        self.host = MDTextField(
            hint_text="Server URL (http://...)",
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            size_hint=(0.8, None)
        )

        self.output = MDLabel(
            text="Result...",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            halign="center"
        )

        btn = MDRaisedButton(
            text="CHECK SERVER",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        btn.bind(on_press=self.check)

        self.screen.add_widget(self.host)
        self.screen.add_widget(btn)
        self.screen.add_widget(self.output)

        return self.screen

    def check(self, instance):
        try:
            url = self.host.text.strip()

            r = requests.get(url, timeout=5)

            self.output.text = f"OK: {r.status_code}"

        except Exception as e:
            self.output.text = str(e)


SSHApp().run()
