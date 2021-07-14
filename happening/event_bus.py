#!/usr/bin/env python
from typing import Dict, List

from .event import Event
from .subscriber import Subscriber


class EventBus:

    subscriptions: Dict[str, List[Subscriber]] = {}

    @classmethod
    def issue_synchronous(cls, event: Event) -> None:
        subscribers = cls.subscriptions[event.identifier]
        for subscriber_class in subscribers:
            if not hasattr(subscriber_class, 'handle'):
                raise AttributeError("'handle' method not defined on {}".format(subscriber_class.__class__.__name__))

            subscriber = subscriber_class()
            subscriber.handle(event)

    @classmethod
    def issue_asynchronous(cls, event: Event) -> None:
        # Implement message queue integration here
        pass
