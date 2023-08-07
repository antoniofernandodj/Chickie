from abc import ABC, abstractmethod


class CommandInterface(ABC):
    @abstractmethod
    def sql(self):
        raise NotImplementedError

    @abstractmethod
    def event(self):
        raise NotImplementedError
