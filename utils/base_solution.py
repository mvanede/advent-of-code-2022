from abc import abstractmethod
import os


class BaseSolution:
    @abstractmethod
    def solve(*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def path_to_input(*args, **kwargs):
        raise NotImplementedError

    def read_input(self):
        input_file = self._test_input if self.use_test_input else self._input
        f = open(os.path.join(self.path_to_input(), input_file), "r")
        input = f.read()
        f.close()
        return input
