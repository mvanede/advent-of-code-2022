from abc import abstractmethod
import os
from config import ROOT_DIR


class BaseSolution:
    use_test_input = True

    def __init__(self, use_test_input):
        self.use_test_input = use_test_input
        self.parse_input()

    @abstractmethod
    def solve(*args, **kwargs):
        raise NotImplementedError

    # @abstractmethod
    # def path_to_input(*args, **kwargs):
    #     raise NotImplementedError

    def path_to_input(*args, **kwargs):
        return os.path.dirname(__file__)

    def read_input(self):
        input_file = self._test_input if self.use_test_input else self._input
        f = open(os.path.join(ROOT_DIR, input_file), "r")
        input = f.read()
        f.close()
        return input
