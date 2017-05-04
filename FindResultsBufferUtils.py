
# A Sublime Text plugin to focus or close the Find Results buffer, and
# to show the first or last matches of the buffer's current results.
#
# Author:       mattst - https://github.com/mattst/
# Requires:     Sublime Text version 2 or 3
# ST Command:   find_results_buffer_utils
# Context Key:  is_find_results_buffer_open

import sublime, sublime_plugin

SUBLIME_TEXT_VERSION     = int(sublime.version())
VIEW_CLOSE_ADDED_VERSION = 3024
FIND_RESULTS_BUFFER_NAME = "Find Results"
FIND_RESULTS_CONTEXT_KEY = "is_find_results_buffer_open"
ACTION_FOCUS_BUFFER      = "focus_buffer"
ACTION_CLOSE_BUFFER      = "close_buffer"
ACTION_SHOW_FIRST_RESULT = "show_first_result"
ACTION_SHOW_LAST_RESULT  = "show_last_result"
MSG_BUFFER_NOT_OPEN      = "The Find Results buffer is not open"
MSG_BUFFER_CLOSED        = "Closed the Find Results buffer"


def get_find_results_buffer():
    """
    Returns the View object of the Find Results buffer or None.
    This function gets called from both of the plugin's classes.
    """

    for view in sublime.active_window().views():
        if view.name() == FIND_RESULTS_BUFFER_NAME:
            return view

    return None


class FindResultsBufferUtilsCommand(sublime_plugin.WindowCommand):
    """
    A Sublime Text plugin to focus or close the Find Results buffer, and
    to show the first or last matches of the buffer's current results.
    """

    def run(self, action):
        """ Called by Sublime Text when the plugin is run. """

        results_buffer = get_find_results_buffer()
        active_buffer = self.window.active_view()

        if not results_buffer:
            sublime.status_message(MSG_BUFFER_NOT_OPEN)

        elif action == ACTION_FOCUS_BUFFER:
            self.focus_buffer(results_buffer, active_buffer)

        elif action == ACTION_CLOSE_BUFFER:
            self.close_buffer(results_buffer, active_buffer)

        elif action == ACTION_SHOW_FIRST_RESULT:
            self.show_first_result(results_buffer)

        elif action == ACTION_SHOW_LAST_RESULT:
            self.show_last_result(results_buffer)


    def focus_buffer(self, results_buffer, active_buffer):
        """ Sets the focus to the Find Results buffer. """

        already_focused = active_buffer.id() == results_buffer.id()

        if not already_focused:
            self.window.focus_view(results_buffer)


    def close_buffer(self, results_buffer, active_buffer):
        """ Closes the Find Results buffer. """

        restore_focus = active_buffer.id() != results_buffer.id()

        if SUBLIME_TEXT_VERSION >= VIEW_CLOSE_ADDED_VERSION:
            results_buffer.close()
        else:
            self.window.focus_view(results_buffer)
            self.window.run_command("close")

        # Even if view.close() is used there are still some
        # circumstances when the focus is not auto-restored
        # to the correct buffer, e.g. if the groups differ.

        if restore_focus:
            self.window.focus_view(active_buffer)

        # Show a status message to provide feedback in case
        # the Find Results buffer is not visible (hidden in
        # lots of tab bar tabs or the tab bar toggled off).

        sublime.status_message(MSG_BUFFER_CLOSED)


    def show_first_result(self, results_buffer):
        """ Shows the first result from the Find Results buffer. """

        move_to_args = {"to": "bof", "extend": False}
        results_buffer.run_command("move_to", move_to_args)
        self.window.run_command("next_result")


    def show_last_result(self, results_buffer):
        """ Shows the last result from the Find Results buffer. """

        move_to_args = {"to": "eof", "extend": False}
        results_buffer.run_command("move_to", move_to_args)
        self.window.run_command("prev_result")


class FindResultsBufferUtilsListener(sublime_plugin.EventListener):
    """ A class to listen for Sublime Text events. """

    def on_query_context(self, view, key, operator, operand, match_all):
        """
        Given the plugin's context key, this method determines whether the Find
        Results buffer is open and returns a boolean value appropriate to the
        operator and operand. In the absence of the plugin's key, or the use of
        an invalid operator, then None is returned as per the API requirements.
        """

        if key == FIND_RESULTS_CONTEXT_KEY:

            is_results_buffer_open = get_find_results_buffer() != None

            if operator == sublime.OP_EQUAL:
                return is_results_buffer_open == operand
            elif operator == sublime.OP_NOT_EQUAL:
                return is_results_buffer_open != operand

        return None
