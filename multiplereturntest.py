import unittest
import threading

from multiplereturn import *


class TestMultipleReturnFunctions(unittest.TestCase):
    def setUp(self):
        self.divide = multiplereturn(lambda x, y: (x // y, x % y))

    def test_all_results_use_before_multiple_return_function_invocation(self):
        try:
            _ = values(0)
        except ValueError:
            pass
        else:
            self.fail()

    def test_all_results_use_twice_after_multiple_return_function_invocation(self):

        _ = values(self.divide(4, 2))

        try:
            _ = values(0)
        except ValueError:
            pass
        else:
            self.fail()

    def test_all_results_use_in_different_threads(self):
        threading.Thread(target=self.divide, args=(4, 2)).run()

        try:
            _ = values(0)
        except ValueError:
            pass
        else:
            self.fail()

    def test_all_results_use_on_a_non_multiple_return_function(self):
        _ = self.divide(5, 3)
        try:
            _ = values(lambda: (0, 0))
        except ValueError:
            pass
        else:
            self.fail()