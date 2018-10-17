from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, Window, WindowAlign
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.key_binding import KeyBindings

class Client(object):

    _app: Application
    _keybindings: KeyBindings

    _root_container: HSplit

    title_text: str

    def __init__(self):
        self.title_text = "CLICord - Not connected"
        self._root_container = HSplit([
            Window(height=1,
                   content=FormattedTextControl(lambda: [("class:title", self.title_text)]), 
                   align=WindowAlign.CENTER),
            Window(height=1, char="-", style="class:line")

        ])

        self._keybindings = KeyBindings()

        @self._keybindings.add("c-c")
        def _(event):
            event.app.exit()

        self._app = Application(layout=Layout(self._root_container), full_screen=True, key_bindings=self._keybindings)
        self._app.run()