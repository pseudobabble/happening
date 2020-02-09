#!/usr/bin/env python
from abc import abstractmethod

from happening.event import Event


class Subscriber:

    @abstractmethod
    def handle(self, event: Event):
        raise NotImplemented
