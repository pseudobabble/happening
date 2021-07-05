#!/usr/bin/env python
from abc import abstractmethod, ABC

from happening.event import Event


class Subscriber(ABC):

    @abstractmethod
    def handle(self, event: Event):
        raise NotImplemented
