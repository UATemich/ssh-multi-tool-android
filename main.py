from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

import paramiko
import threading


class SSHApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.login = TextInput(hint_text="Login", multiline=False)
        self.password = TextInput(hint_text="Password", password=True, multiline=False)
        self.host = TextInput(hint_text="Host", multiline=False)

        self.output = Label(text="Result will appear here")

        btn = Button(text="CHECK VERSION")
        btn.bind(on_press=self.check_version)

        layout.add_widget(self.login)
        layout.add_widget(self.password)
        layout.add_widget(self.host)
        layout.add_widget(btn)
        layout.add_widget(self.output)

        return layout

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
        threading.Thread(target=self._run).start()

    def _run(self):
        try:
            client = self.ssh_connect()
            _, stdout, _ = client.exec_command("uname -r")
            result = stdout.read().decode().strip()
            self.output.text = f"Kernel: {result}"
            client.close()
        except Exception as e:
            self.output.text = str(e)


SSHApp().run()
