#!/usr/bin/env python3
import unittest
from unittest import TestCase

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

    def __init__(self):
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
            subscriptions = {'1': [mock_handler_1], '2': [mock_handler_2]}

        test_event_bus = TestEventBus()
        event = TestEvent('irrelevant')
        test_event_bus.issue_synchronous(event)

        assert mock_handler_1.handled_events[0] == event
        assert not mock_handler_2.handled_events


    def test__all_specified_handlers_are_called_for_event(self):
        mock_handler_1 = RecorderSubscriber()
        mock_handler_2 = RecorderSubscriber()

        class TestEventBus(EventBus):
            subscriptions = {'1': [mock_handler_1, mock_handler_2]}

        test_event_bus = TestEventBus()
        event = TestEvent('irrelevant')
        test_event_bus.issue_synchronous(event)

        assert mock_handler_1.handled_events[0] == event
        assert mock_handler_2.handled_events[0] == event


    def test__handler_without_handle_method_raises_attributeerror(self):
        fake_handler = object()

        class TestEventBus(EventBus):
            subscriptions = {'1': [fake_handler]}

        test_event_bus = TestEventBus()
        event = TestEvent('irrelevant')

        with self.assertRaises(AttributeError):
            test_event_bus.issue_synchronous(event)






if __name__ == "__main__":
    unittest.main()
