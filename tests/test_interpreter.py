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

import unittest

from acolytegm import interpreter



class TestCommand(unittest.TestCase):
    """Test the Command class."""

    def test_init(self):
        """Ensure Command(string, function) creates an object."""
        cmd_name = 'sampleCommand'
        def sample_function():
            return 'sampleFunction'
        try:
            cmd = interpreter.Command(string=cmd_name,
                                      function=sample_function)
        except Exception as e:
            msg = 'Command(string, function) raised exception: '
            self.fail(msg + str(e))
        finally:
            self.assertEqual(cmd.string, cmd_name)
            self.assertEqual(cmd.function, sample_function)
            self.assertEqual(cmd.subcommands, {})


    def test_init_empty(self):
        """Ensure Command() creates an object."""
        try:
            cmd = interpreter.Command()
        except Exception as e:
            msg = 'Command() raised exception: {}'.format(e)
            self.fail(msg)
        finally:
            self.assertEqual(cmd.string, '')
            self.assertEqual(cmd.function, None)
            self.assertEqual(cmd.subcommands, {})


    def test_add_subcommands(self):
        """Ensure Command.add_subcommand works as expected."""
        cmd_name = 'sampleCommand'
        def sample_function():
            return 'sampleFunction'
        subcommands = [ 'sub1', 'sub2' ]
        cmd = interpreter.Command(string=cmd_name)
        self.assertEqual(cmd.string, cmd_name)
        self.assertEqual(cmd.function, None)
        self.assertEqual(cmd.subcommands, {})
        for sc in subcommands:
            cmd.add_subcommands(subcommands, sample_function)
        self.assert_('sub1' in cmd.subcommands)
        sub1 = cmd.subcommands['sub1']
        self.assertEqual(sub1.string, 'sub1')
        self.assertEqual(sub1.function, None)
        self.assert_('sub2' in sub1.subcommands)
        sub2 = sub1.subcommands['sub2']
        self.assertEqual(sub2.string, 'sub2')
        self.assertEqual(sub2.function, sample_function)
        self.assertEqual(sub2.subcommands, {})



class TestInterpreter(unittest.TestCase):
    """Test the Interpreter class."""

    def test_init(self):
        """Ensure interpreter.Interpreter() creates an object."""
        try:
            interp = interpreter.Interpreter()
        except Exception as e:
            msg = 'Interpreter() raised exception: {}'.format(e)
            self.fail(msg)



if __name__ == '__main__':
    unittest.main()
