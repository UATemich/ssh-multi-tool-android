from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

import paramiko
import threading


class SSHApp(MDApp):

    def build(self):
        self.screen = Screen()

        self.login = MDTextField(
            hint_text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            size_hint=(0.8, None)
        )

        self.password = MDTextField(
            hint_text="Password",
            password=True,
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            size_hint=(0.8, None)
        )

        self.host = MDTextField(
            hint_text="Host (a2469-m1)",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            size_hint=(0.8, None)
        )

        self.output = MDLabel(
            text="",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            halign="center"
        )

        btn_version = MDRaisedButton(
            text="CHECK VERSION",
            pos_hint={"center_x": 0.5, "center_y": 0.45}
        )
        btn_version.bind(on_press=self.check_version)

        self.screen.add_widget(self.login)
        self.screen.add_widget(self.password)
        self.screen.add_widget(self.host)
        self.screen.add_widget(btn_version)
        self.screen.add_widget(self.output)

        return self.screen

    def ssh_connect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(
            hostname=self.host.text,
            username=self.login.text,
            password=self.password.text,
            timeout=10
        )
        return client

    def check_version(self, instance):
        threading.Thread(target=self._check_version, daemon=True).start()

    def _check_version(self):
        try:
            client = self.ssh_connect()
            stdin, stdout, _ = client.exec_command("uname -r")
            result = stdout.read().decode().strip()

            self.output.text = f"Kernel: {result}"

            client.close()

        except Exception as e:
            self.output.text = str(e)


SSHApp().run()
