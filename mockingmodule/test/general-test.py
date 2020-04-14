"""
    Test the removal of a file (general)
"""

import unittest
import os.path
import tempfile

from mockingmodule.mocking import rm


class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "w+") as f:
            f.write("Delete me!")

    def test_rm(self):

        # remove the file
        rm(self.tmpfilepath)

        # test if the file was actually deleted
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file")
