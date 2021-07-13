#!/usr/bin/env python3
import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from happening.event import Event
from happening.event_bus import EventBus
from happening.subscriber import Subscriber


class RecorderSubscriber(Subscriber):
    """
    The RecorderSubscriber should be callable, so that we can access the
    instance state after it has been called inside the EventBus,
    otherwise the instance is created inside the EventBus and we
    never get access to it in the test scope.
    """

    def __init__(self, argument_1='fake', argument_2='fake'):
        self.argument_1 = argument_1
        self.argument_2 = argument_2
        self.handled_events = []

    def __call__(self):
        return self

    def handle(self, event: Event):
        self.handled_events.append(event)



class TestEvent(Event):
    @property
    def identifier(self) -> str:
        return '1'


class TestEventBus(TestCase):

    def test__handler_matching_event_identifier_is_called_with_event(self):
        mock_handler_1 = RecorderSubscriber()
        mock_handler_2 = RecorderSubscriber()

        class TestEventBus(EventBus):
            subscriptions = {'1': mock_handler_1, '2': mock_handler_2}

        test_event_bus = TestEventBus()
        event = TestEvent('relevant')
        test_event_bus.issue_synchronous(event)

        assert mock_handler_1.handled_events[0] == 'relevant'
        assert not mock_handler_2.handled_events




if __name__ == "__main__":
    unittest.main()
