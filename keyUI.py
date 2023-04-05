"""KeyUI.py -- Keyboard User Interface -- GPLv3 -- blobbybilb"""

from pynput.keyboard import Key, Listener, Controller, KeyCode
from typing import Callable, Any


class KeyUI:
    """
    Main KeyUI.py class.

    Usage:
    1. Initialize KeyUI -- `KeyUI()`
    2. Set handler -- `KeyUI().set_handler(handler_func)` where `handler_func` is a function that takes a list of strings as an argument.
    3. Run -- `KeyUI().run()`

    Example:
    ```
    def handler(args: list[str]):
        print(args)

    KeyUI().set_handler(handler).run()
    ```

    ---

    Custom separator and delimiter (Note: not yet supported, may not work):

    set `KeyUI().separator`/`KeyUI().delimiter` to your custom separator/delimiter
    """

    def __init__(self):
        self.state = ""
        self.separator = "\\"  # \ -- separator
        self.delimiter = 2 * self.separator  # \\ -- start
        self.handler: Callable[[list[str]], Any] = lambda _: None

    def __on_press(self, key: Key | KeyCode) -> bool | None:
        try:
            if key.char == self.separator:  # FIXME makes custom delimiter not work
                self.state += key.char
            elif self.state.startswith(self.delimiter):
                self.state += key.char
            else:
                self.state = ""

            if (
                key.char == self.separator
                and self.state.startswith(self.delimiter)
                and len(self.state) >= 4
                and self.state.endswith(self.delimiter)
            ):
                self.handler(self.parse_args(self.state))
                self.backspace_len_state()
                self.state = ""
        except AttributeError:
            if key == Key.esc:
                self.backspace_len_state()
                self.state = ""
            elif key == Key.backspace:
                self.state = self.state[:-1]
            elif key == Key.space:
                self.state += " "
            elif not key in [Key.alt, Key.shift]:
                self.state = ""
        print(self.state)
        return None

    def run(self):
        with Listener(on_press=self.__on_press) as listener:
            listener.join()
        return self

    def set_handler(self, handler: Callable[[list[str]], Any]):
        self.handler = handler
        return self

    def parse_args(self, str) -> list[str]:
        return str[2:-2].split(self.separator)

    def backspace_len_state(self):
        with Controller() as controller:
            for _ in range(len(self.state)):
                controller.press(Key.backspace)
                controller.release(Key.backspace)
