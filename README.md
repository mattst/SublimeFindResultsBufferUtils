
## Find Results Buffer Utils - Package for Sublime Text

### Overview

*Find Results Buffer Utils* is a Sublime Text package which adds keys allowing users to switch focus to and to close the *Find Results* buffer. It should be noted that closing the buffer is performed without the active buffer losing focus and that both operations are preformed within the active window only.

While these are simple tasks, which do not take much time, I have found the plugin so useful that it has become an integral part of how I use Sublime's powerful *Find in Files (Use Buffer)* feature.

### Requirements

Sublime Text version 2 or 3.

### Installing

Use *Package Control*:

- Open the command palette and select: Package Control: Install Package
- Wait for the package list to be updated and then select: FindResultsBufferUtils
- Note: Submitted but awaiting addition

Of course users can, if they prefer, download the `zip` file and [install it manually](http://docs.sublimetext.info/en/latest/extensibility/packages.html). There are no naming restrictions beyond the `.sublime-package` file extension but `FindResultsBufferUtils.sublime-package` would be a sensible choice.

### Key Bindings

Since `F4` is used for the *Find Results* buffer's *Next/Previous* keys it makes sense to use the same key for focusing and closing it.

Linux / Windows:

- Focus the *Find Results* buffer: `ctrl+k, ctrl+f4`
- Close the *Find Results* buffer: `ctrl+k, ctrl+shift+f4`

OSX:

- Focus the *Find Results* buffer: `super+k, super+f4`
- Close the *Find Results* buffer: `super+k, super+shift+f4`

Context Handling:

Although not used by the default key bindings, this package does implement context handling should users wish to create context aware key bindings.

The context key `is_find_results_buffer_open` simply checks whether there is a *Find Results* buffer open in the active window or not. The `operator` can be set to either `equal` or `not_equal` and the `operand` to `true/false`.

For example, the following key bindings will only activate the plugin if there is a *Find Results* buffer open in the active window.

    [
        {
            "keys": ["ctrl+???"],
            "command": "find_results_buffer",
            "args": {"action": "focus"},
            "context": [{"key": "is_find_results_buffer_open",
                         "operator": "equal", "operand": true}]
        },
        {
            "keys": ["ctrl+shift+???"],
            "command": "find_results_buffer",
            "args": {"action": "close"},
            "context": [{"key": "is_find_results_buffer_open",
                         "operator": "equal", "operand": true}]
        }
    ]

### License

This package is licensed under The MIT License (MIT).
