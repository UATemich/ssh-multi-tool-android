from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import paramiko


class SSHClientUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.host = TextInput(hint_text="Host", multiline=False)
        self.user = TextInput(hint_text="Username", multiline=False)
        self.password = TextInput(hint_text="Password", multiline=False, password=True)

        self.output = Label(text="Output...")

        btn = Button(text="Connect")
        btn.bind(on_press=self.connect)

        self.add_widget(self.host)
        self.add_widget(self.user)
        self.add_widget(self.password)
        self.add_widget(btn)
        self.add_widget(self.output)

    def connect(self, instance):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(
                hostname=self.host.text,
                username=self.user.text,
                password=self.password.text,
                timeout=5
            )

            stdin, stdout, stderr = client.exec_command("whoami && uname -a")
            result = stdout.read().decode()

            self.output.text = result

            client.close()

        except Exception as e:
            self.output.text = str(e)


class SSHTool(App):
    def build(self):
        return SSHClientUI()


SSHTool().run()
