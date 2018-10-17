from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.widgets import Box, Frame, TextArea
from prompt_toolkit.key_binding import KeyBindings

class Client(object):

    __slots__ = ["_app", "_layout", "_root_container", "_keybindings"]
    _app: Application

    _layout: Layout
    _root_container: Box
    _keybindings: KeyBindings

    def __init__(self):
        self._root_container = Box(Frame(TextArea(text="This is a test", width=40, height=3)))
        self._layout = Layout(container=self._root_container)
        self._keybindings = KeyBindings()

        @self._keybindings.add("c-c")
        def _(event):
            event.app.exit()

        self._app = Application(layout=self._layout, full_screen=True, key_bindings=self._keybindings)
        self._app.run()