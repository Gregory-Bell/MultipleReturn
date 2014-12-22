import unittest
import multiplereturn
import threading


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.divide = multiplereturn.multiplereturn(lambda x, y: (x // y, x % y))

    def test_all_results_use_before_multiple_return_function_invocation(self):
        try:
            _ = multiplereturn.all_results(0)
        except ValueError:
            pass
        else:
            self.fail()

    def test_all_results_use_twice_after_multiple_return_function_invocation(self):

        _ = multiplereturn.all_results(self.divide(4, 2))

        try:
            _ = multiplereturn.all_results(0)
        except ValueError:
            pass
        else:
            self.fail()

    def test_all_results_use_in_different_threads(self):
        threading.Thread(target=self.divide, args=(4, 2)).run()

        try:
            _ = multiplereturn.all_results(0)
        except ValueError:
            pass
        else:
            self.fail()