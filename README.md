# KeyUI.py
A keyboard user interface framework for python

### What's a "keyboard user interface"?
I was working on a project that does something when `\\<something>\<something>\\` is typed (anywhere, eg. in a text document). I wrote this simple class as a part of that; as it could have more general uses, I called it "KeyUI.py" for keyboard user iterface (because I couldn't think of anything else) and put it here.

### Usage
download the keyUI.py file

```python
from keyUI import KeyUI
```


#### from the KeyUI class:
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



### License
GNU GPLv3