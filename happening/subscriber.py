#!/usr/bin/env python
from abc import abstractmethod, ABC

from happening.event import Event


class Subscriber(ABC):

    @abstractmethod
    def handle(self, event: Event):
        raise NotImplementedError('You must implement `handle` on {self.__class__.__name__}')
