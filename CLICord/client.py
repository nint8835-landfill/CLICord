import disco.types
from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window, WindowAlign
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import TextArea, Frame


class Client(object):
    _app: Application
    _keybindings: KeyBindings

    _root_container: HSplit
    _message_text_area: TextArea
    _message_input: TextArea

    _current_channel: disco.types.Channel

    def __init__(self):
        self._current_channel = None

        self._message_text_area = TextArea(read_only=True, focusable=False)

        self._message_input = TextArea(height=3, multiline=False)
        self._message_input.accept_handler = self._handle_message_entered

        self._root_container = HSplit([
            Frame(Window(height=1,
                         content=FormattedTextControl(lambda: [("class:title", self.get_title())]),
                         align=WindowAlign.CENTER)),
            self._message_text_area,
            Frame(self._message_input)
        ])

        self._keybindings = KeyBindings()

        @self._keybindings.add("c-c")
        def _(event):
            event.app.exit()

        self._app = Application(layout=Layout(self._root_container), full_screen=True, key_bindings=self._keybindings)
        self._app.run()

    def _handle_message_entered(self, buffer: Buffer):
        self.send_message(buffer.text)
        buffer.text = ""

    def send_message(self, text):
        self._message_text_area.text += f"{text}\n"

    def get_title(self):
        if not self._current_channel:
            return "No channel selected"
        else:
            return f"{self._current_channel.guild.name} > {self._current_channel.name}"
