# Happening
Event-Subscriber in Python

## How it works:
- Subclass and customise Event, Subscriber, and EventBus
- Define subscriptions in your custom EventBus
- Fire events, and have them handled by listeners
- (Message Queue integration coming soon)

## Example:

``` python
#!/usr/bin/env python

from happening import EventBus, Event, Subscriber

class FakeLogger:

    @staticmethod
    def info(message: str) -> None:
        print(message)


class UserAdded(Event):
    identifier = 'user.added'


class RegistrationConfirmationEmailSender(Subscriber):

    def __init__(self, logger: FakeLogger = FakeLogger) -> None:
        self.logger = logger

    def handle(self, event: UserAdded) -> None:
        user_email = event.payload['email']
        self.send_email(user_email)
        self.logger.info(f'Registration confirmation email sent to {user_email}')

    def send_email(self, user_email: str) -> None:
        pass


class MyEventBus(EventBus):
    subscriptions = {
        UserAdded.identifier: [RegistrationConfirmationEmailSender]
    }


class UserController:

    def __init__(self, event_bus: EventBus = MyEventBus()) -> None:
        self.event_bus: EventBus = event_bus

    def add_user(self, request) -> None:
        user_added_event = UserAdded(request['data'])

        self.event_bus.issue_synchronous(user_added_event)


if __name__ == '__main__':

    fake_request = {'data': {'email': 'a.n.other@nowhere.com'}}

    controller = UserController()
    controller.add_user(fake_request)

```

## Tests

``` bash
python3 -m unittest
```
