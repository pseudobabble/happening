#!/usr/bin/env python
from typing import Dict

from .event import Event
from .subscriber import Subscriber


class EventBus:

    subscriptions: Dict[str, Subscriber] = {}

    @classmethod
    def issue_synchronous(cls, event: Event) -> None:
        handler_class = cls.subscriptions[event.identifier]()
        if not hasattr(handler_class, 'handle'):
            raise AttributeError("'handle' method not defined on {}".format(handler_class.__class__.__name__))

        handler_class.handle(event)

    @classmethod
    def issue_asynchronous(cls, event: Event) -> None:
        # Implement message queue integration here
        pass
