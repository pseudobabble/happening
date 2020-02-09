#!/usr/bin/env python
from abc import abstractmethod
from typing import Union


class Event:

    identifier: str = NotImplemented

    payload: Union[dict, list] = NotImplemented

    @abstractmethod
    def get_payload(self) -> Union[dict, list]:
        return self.payload
