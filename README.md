PyNoelShack
===========

A small Python module for NoelShack API.

Description
-----------

This module can be used as a library from any other Python script, or
as a command-line tool.

Dependencies
------------

* [Requests](http://python-requests.org/)


Installation
------------

To install this script as a command-line tool, do the following, assuming
you got a personal `bin` directory:

```sh
cp pynoelshack.py ~/bin/pynoelshack
chmod +x ~/bin/pynoelshack
```

Examples
--------

### Python

```python
from pynoelshack import NoelShack, NoelShackError

ns = NoelShack()

try:
    print(ns.upload('foo.png'))
except NoelShackError as e:
    print(str(e))
```

### Command

```sh
python pynoelshack.py foo.png
```

Or, assuming you installed it in your `PATH` as `pynoelshack`:

```sh
pynoelshack foo.png
```

Feel free to alias it at your convenience.
