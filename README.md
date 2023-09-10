Fuke
====

**An emulator of [Foundry’s Nuke][1] API.**

Ever wanted to manipulate a Nuke script from entirely outside Nuke? Then this Python package is for you.


Installation
------------

Fuke parses Nuke scripts using [Lark][2]:

```sh
pip install lark
```


Usage
-----

It’s self-explanatory really:

```python
import fuke

nuke = fuke.Fuke() # This emulates Nuke being launched-- you can have multiple "sessions" running.
nuke.scriptOpen('/path/to/my/nuke_script.nk')
for node in nuke.allNodes('Read'):
    print(node['file'].value())
```


Limitations
-----------

Currently, Fuke is in **pre-alpha** stage— it’s been developed to respond to very particular needs ([3DEqualizer4][3]’s lens nodes if you must know), because I was tired of writing limited parsers over and over. Hopefully this is a solid skeleton to grow from. Here’s what Fuke can emulate:

* `nuke.allNodes()`: Only the 1st optional argument (`filter`) is implemented. Returns a list of `fuke.Node`s.
* `nuke.scriptOpen()`.

For the classes below, their constructors might not behave like in Nuke. This will be addressed in the future.


### `fuke.Node` properties

No notion of user knob definitions (`addUserKnob`); likely to fail if the node contains these.

* `[...]`: Returns a `fuke.Knob`.
* `Class()`.
* `allKnobs()`: No concept of nameless knobs.
* `knob()`: Same as `[...]`. 1st argument (`p`) must be the knob name (no index support). `follow_link` optional argument not implemented.
* `knobs()`.


### `fuke.Knob` properties

No notion of the knob type. No notion of expressions; they probably get evaluated as strings starting with `{expr`. It can only handle single floating point or string values. No channel/index/view selection is implemented.

* `animation()`: Returns a `fuke.AnimationCurve`.
* `getValue()`: `time` not implemented either (not sure what it does).
* `getValueAt()`: Only when there’s a keyframe at the queried time.
* `isAnimated()`.
* `value()`: Same as `getValue()`.
* `valueAt()` Same as `getValueAt()`.


### `fuke.AnimationCurve` properties

* `evaluate()`: Only when there’s a keyframe at the queried time.
* `keys()`: Returns a list of `fuke.AnimationKey`s.


### `fuke.AnimationKey` properties

* `x`.
* `y`.


[1]: https://foundry.com/products/nuke-family 'Nuke Family | Foundry'
[2]: https://pypi.org/project/lark 'lark · PyPI'
[3]: https://3dequalizer.com '3DEqualizer4 - Enterprise Matchmove Software'
