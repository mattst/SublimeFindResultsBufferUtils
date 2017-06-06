
## Find Results Buffer Utils (Sublime Text Package)

### Overview

*Find Results Buffer Utils* is a Sublime Text package which adds keys allowing users to switch focus to and to close the *Find Results* buffer, and to jump to the first and last of the current results. It should be noted that closing the buffer is performed without the active buffer losing focus.

While these are simple tasks, which do not take much time, I have found the plugin so useful that it has become an integral part of how I use Sublime's powerful *Find in Files (Use Buffer)* feature.

### Requirements

Sublime Text version 2 or 3.

### Installing

Use [Package Control](https://packagecontrol.io/):

- Open the command palette and select: `Package Control: Install Package`
- Wait for the package list to be updated and then select: `FindResultsBufferUtils`

Users can, if they prefer, download the [zip file](https://github.com/mattst/SublimeFindResultsBufferUtils/archive/master.zip) and then [install it manually](http://docs.sublimetext.info/en/latest/extensibility/packages.html); `FindResultsBufferUtils.sublime-package` should be used as the installed package file name or, if unzipping for folder installation, then `FindResultsBufferUtils` should be used as the folder name.

### Key Bindings

The default key bindings are only triggered when a *Find Results* buffer is open (see: *Context Handling* below).

Since `F4` is used for the *Find Results* buffer's show *Next/Previous* result keys, the same keys, prefixed by `ctrl+k`, are used to show the *First/Last* result. Likewise, due to the `F` key's use in initiating *Find in Files*, the same key is used to switch focus to, and to close, the *Find Results* buffer.

Linux / Windows:

- Focus the *Find Results* buffer: `ctrl+k, ctrl+f`
- Close the *Find Results* buffer: `ctrl+k, ctrl+shift+f`
- Show the first result: `ctrl+k, f4`
- Show the last result: `ctrl+k, shift+f4`

OSX:

- Focus the *Find Results* buffer: `super+k, super+f`
- Close the *Find Results* buffer: `super+k, super+shift+f`
- Show the first result: `super+k, f4`
- Show the last result: `super+k, shift+f4`

Context Handling:

The context key `is_find_results_buffer_open` simply checks whether there is a *Find Results* buffer open in the active window or not. The `operator` can be set to either `equal` or `not_equal` and the `operand` to `true/false`.

The default key bindings are only triggered when a *Find Results* buffer is open. If users prefer to make them active all the time, ignoring the *Find Results* buffer's status, then simply remove the `"context": [{"key": "is_find_results_buffer_open"}]` line from each of the key bindings. See the always useful [PackageResourceViewer](https://packagecontrol.io/packages/PackageResourceViewer) plugin.

### License

This package is licensed under The MIT License (MIT).
