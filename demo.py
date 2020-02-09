#!/usr/bin/env python

from happening import EventBus, Event, Subscriber


class Happening(Event):
    identifier = 'event.happening'

    def __init__(self, payload: dict) -> None:
        self.payload: dict = payload

    def get_payload(self) -> dict:
        return self.payload


class WatcherDependency:

    def inject_foo(self, state: dict) -> None:
        state.update({'foo': 'foo'})


class HappeningWatcher(Subscriber):

    def __init__(self, dependency: WatcherDependency = WatcherDependency) -> None:
        self.dependency: WatcherDependency = dependency()
        self.state = {'a': 'A'}
        print('{} initialised with state {}'.format(self, self.state))

    def handle(self, event: Event) -> None:
        self.state_mutator(event.get_payload())
        print('Handled {}, updated state to {}'.format(event, self.state))

    def state_mutator(self, new_state: dict) -> None:
        self.state.update(new_state)
        self.dependency.inject_foo(self.state)


class MyEventBus(EventBus):
    subscriptions = {
        Happening.identifier: HappeningWatcher
    }


class HappeningCauser:

    def __init__(self, event_bus: EventBus = MyEventBus) -> None:
        self.event_bus: EventBus = event_bus()

    def cause_something(self) -> None:
        something = Happening(
            {
                'location': 'here',
                'what': 'something'
            }
        )

        self.event_bus.issue_synchronous(something)


if __name__ == '__main__':

    causer = HappeningCauser()
    causer.cause_something()
