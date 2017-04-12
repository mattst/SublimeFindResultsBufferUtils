
import sublime, sublime_plugin


FIND_BUFFER_NAME      = "Find Results"
OPERATION_FOCUS       = "focus"
OPERATION_CLOSE       = "close"
MSG_BUFFER_NOT_FOUND  = "Find Results Buffer Not Found"
MSG_BUFFER_FOCUSED    = "Focused The Find Results Buffer"
MSG_BUFFER_CLOSED     = "Closed The Find Results Buffer"
MSG_INVALID_OPERATION = "Invalid Command Args"


class FindResultsBufferUtilsCommand(sublime_plugin.WindowCommand):
    """
    A Sublime Text plugin to focus or close the Find Results buffer.

    Command:  "find_results_buffer_utils"
    Argument: "operation" must be set to either "focus" or "close".
    """

    def run(self, operation):

        find_buffer_view = None

        for view in self.window.views():
            if view.name() == FIND_BUFFER_NAME:
                find_buffer_view = view
                break

        if not find_buffer_view:
            sublime.status_message(MSG_BUFFER_NOT_FOUND)

        elif operation == OPERATION_FOCUS:
            self.window.focus_view(find_buffer_view)
            sublime.status_message(MSG_BUFFER_FOCUSED)

        elif operation == OPERATION_CLOSE:
            find_buffer_view.close()
            sublime.status_message(MSG_BUFFER_CLOSED)

        else:
            sublime.status_message(MSG_INVALID_OPERATION)
