#!/usr/bin/env python
from typing import Dict, List

from .event import Event
from .subscriber import Subscriber


class EventBus:

    subscriptions: Dict[str, List[Subscriber]] = {}

    def issue_synchronous(self, event: Event) -> None:
        for subscriber_class in self.subscriptions[event.identifier]:
            if not hasattr(subscriber_class, 'handle'):
                raise AttributeError("'handle' method not defined on {}".format(subscriber_class.__class__.__name__))

            subscriber = subscriber_class()
            subscriber.handle(event)

    def issue_asynchronous(cls, event: Event) -> None:
        # Implement message queue integration here
        pass
