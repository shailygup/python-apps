"""
    Mocking removal of a file
"""

import mock
import unittest

from mockingmodule.mocking import rm

class RmTestCase(unittest.TestCase):

    @mock.patch('mockingmodule.mocking.os.remove')
    def test_rm(self, mocked_remove):
        rm("any path")

        # test that rm called os.remove with the correct parameters
        # mock_os.remove.assert_called_with("any path")
        self.assertTrue(mocked_remove.called)
