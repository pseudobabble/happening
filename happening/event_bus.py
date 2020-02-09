#!/usr/bin/env python

from .event import Event


class EventBus:

    subscriptions: dict = NotImplemented  # {}

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
