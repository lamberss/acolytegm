#   Copyright 2017 Steven E. Lamberson, Jr. <steven.lamberson@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import logging



class Command(object):
    """Maps a string (the command) to a function that should be called
    when the string is present.
    """

    def __init__(self, string=None, function=None):
        """Creates the Command object."""
        self.function = None
        self.string = ''
        self.subcommands = {}
        if function is not None:
            self.function = function
        if string is not None:
            self.string = string


    def add_subcommands(self, subcommands, function):
        """Create subcommands for this command."""
        this_subcommand = subcommands[0]
        if len(subcommands) == 1:
            self.subcommands[this_subcommand] = Command(this_subcommand,
                                                        function)
        else:
            new_subcommands = subcommands[1:]
            self.subcommands[this_subcommand] = Command(this_subcommand)
            self.subcommands[this_subcommand].add_subcommands(new_subcommands,
                                                              function)



class Interpreter(object):
    """Interprets a string as a command with possible subcommands."""

    def __init__(self):
        """Creates the Interpreter object."""
        self._log = logging.getLogger('__name__')
