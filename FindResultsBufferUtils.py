
# A Sublime Text plugin to focus or close the Find Results buffer.
#
# Author:      mattst - https://github.com/mattst/
# Requires:    Sublime Text version 2 or 3
# ST Command:  find_results_buffer (args: "focus" or "close")

import sublime, sublime_plugin

SUBLIME_TEXT_VERSION             = int(sublime.version())
VIEW_CLOSE_ADDED_VERSION         = 3024
FIND_RESULTS_BUFFER_NAME         = "Find Results"
FIND_RESULTS_BUFFER_ACTION_FOCUS = "focus"
FIND_RESULTS_BUFFER_ACTION_CLOSE = "close"
FIND_RESULTS_BUFFER_CONTEXT_KEY  = "is_find_results_buffer_open"
MSG_FIND_RESULTS_BUFFER_CLOSED   = "Closed the Find Results buffer"
MSG_FIND_RESULTS_BUFFER_FOCUSED  = "Focused the Find Results buffer"
MSG_FIND_RESULTS_BUFFER_NOT_OPEN = "The Find Results buffer is not open"


class FindResultsBufferCommand(sublime_plugin.WindowCommand):
    """ A ST plugin to focus or close the Find Results buffer. """

    def run(self, action):
        """ Called by Sublime Text when the plugin is run. """

        active_buffer = self.window.active_view()
        find_results_buffer = self.get_find_results_buffer()

        if not find_results_buffer:
            sublime.status_message(MSG_FIND_RESULTS_BUFFER_NOT_OPEN)

        elif action == FIND_RESULTS_BUFFER_ACTION_FOCUS:
            self.focus_find_results_buffer(active_buffer, find_results_buffer)

        elif action == FIND_RESULTS_BUFFER_ACTION_CLOSE:
            self.close_find_results_buffer(active_buffer, find_results_buffer)


    def get_find_results_buffer(self):
        """ Returns the View object of the Find Results buffer or None. """

        for view in self.window.views():
            if view.name() == FIND_RESULTS_BUFFER_NAME:
                return view

        return None


    def focus_find_results_buffer(self, active_buffer, find_results_buffer):
        """ Sets the focus to the Find Results buffer. """

        is_already_focused = find_results_buffer.id() == active_buffer.id()

        if is_already_focused:
            return

        self.window.focus_view(find_results_buffer)
        sublime.status_message(MSG_FIND_RESULTS_BUFFER_FOCUSED)


    def close_find_results_buffer(self, active_buffer, find_results_buffer):
        """ Closes the Find Results buffer. """

        restore_focus = active_buffer.id() != find_results_buffer.id()

        if SUBLIME_TEXT_VERSION >= VIEW_CLOSE_ADDED_VERSION:
            find_results_buffer.close()
        else:
            self.window.focus_view(find_results_buffer)
            self.window.run_command("close")

        # Even if view.close() is used there are still some
        # circumstances when the focus is not auto-restored
        # to the correct buffer, e.g. if the groups differ.

        if restore_focus:
            self.window.focus_view(active_buffer)

        sublime.status_message(MSG_FIND_RESULTS_BUFFER_CLOSED)


class iOpenerEventListener(sublime_plugin.EventListener):
    """ A class to listen for events triggered by ST. """

    def on_query_context(self, view, key, operator, operand, match_all):
        """
        The on_query_context() event is triggered by ST to determine whether
        key bindings, that contain a context key, should be activated or not.
        """

        if key == FIND_RESULTS_BUFFER_CONTEXT_KEY:

            is_find_results_buffer_open = False

            for view in sublime.active_window().views():
                if view.name() == FIND_RESULTS_BUFFER_NAME:
                    is_find_results_buffer_open = True
                    break

            if operator == sublime.OP_EQUAL:
                return is_find_results_buffer_open == operand
            elif operator == sublime.OP_NOT_EQUAL:
                return is_find_results_buffer_open != operand

        return None
