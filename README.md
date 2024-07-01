# python version project test

**Compatibility: 3.6 only**

### Details

This project contains a piece of code compatible with 3.6 only.

Creating a piece of Python code that is compatible with Python 3.6 but not with Python 3.8 is a bit unusual, as typically, the goal is to write code that is forward-compatible with newer versions of Python. However, to test package manager this is required.

One such feature is the `time.clock()` function, which was deprecated since Python 3.3 and removed in Python 3.8. This function can be used in Python 3.6 but will result in an AttributeError in Python 3.8 because it no longer exists.


### How to

Using a compatible python version, just run

```shell
pip install -e .
mycommand
```

