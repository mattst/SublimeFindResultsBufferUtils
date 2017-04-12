
# Sublime Text plugins to focus and close the Find Results buffer.
#
# Author:    mattst - https://github.com/mattst/ - 2017-04-12
# Requires:  Sublime Text version 2 or 3
# Commands:  "find_results_buffer_focus", "find_results_buffer_close"

import sublime, sublime_plugin

SUBLIME_TEXT_VERSION      = int(sublime.version())
VIEW_CLOSE_ADDED_VERSION  = 3024

FIND_BUFFER_NAME          = "Find Results"
MSG_FIND_BUFFER_CLOSED    = "Closed the Find Results buffer"
MSG_FIND_BUFFER_FOCUSED   = "Focused the Find Results buffer"
MSG_FIND_BUFFER_NOT_FOUND = "Find Results buffer not found"


class FindResultsBuffer:
    """ Parent of the two Find Results Buffer Command classes. """

    def get_find_buffer(self, window):
        """ Returns the View object of the Find Results buffer or None. """

        for view in window.views():
            if view.name() == FIND_BUFFER_NAME:
                return view

        sublime.status_message(MSG_FIND_BUFFER_NOT_FOUND)

        return None


class FindResultsBufferFocusCommand(FindResultsBuffer,
                            sublime_plugin.WindowCommand):
    """
    A Sublime Text plugin to focus the Find Results buffer.
    Sublime Text command name: "find_results_buffer_focus"
    """

    def run(self):
        """ Called by Sublime Text when the plugin is run. """

        find_buffer = self.get_find_buffer(self.window)

        if not find_buffer:
            return

        self.window.focus_view(find_buffer)
        sublime.status_message(MSG_FIND_BUFFER_FOCUSED)


class FindResultsBufferCloseCommand(FindResultsBuffer,
                            sublime_plugin.WindowCommand):
    """
    A Sublime Text plugin to close the Find Results buffer.
    Sublime Text command name: "find_results_buffer_close"
    """

    def run(self):
        """ Called by Sublime Text when the plugin is run. """

        find_buffer = self.get_find_buffer(self.window)

        if not find_buffer:
            return

        # Ensure that the active buffer keeps the focus. This
        # will not happen automatically if the Find Results
        # buffer is in a different group to the active buffer
        # or if it is necessary to call run_command("close").

        active_buffer = self.window.active_view()
        find_buffer_focused = find_buffer.id() == active_buffer.id()

        if SUBLIME_TEXT_VERSION >= VIEW_CLOSE_ADDED_VERSION:
            find_buffer.close()
        else:
            self.window.focus_view(find_buffer)
            self.window.run_command("close")

        if not find_buffer_focused:
            self.window.focus_view(active_buffer)

        sublime.status_message(MSG_FIND_BUFFER_CLOSED)
