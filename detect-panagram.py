import string
import unittest
from unittest import TestCase


def is_pangram(s):

    alphabet = set(string.ascii_lowercase)

    if (set(s.lower()) >= alphabet):
        return True
    else:
        return False
  
if __name__ == "__main__":
    pass


    s = "The quick, brown fox jumps over the lazy cat!"
    is_pangram(s)

    ### Tests
    # self.assertEqual(is_pangram(s), True)
    assert is_pangram(s) == True