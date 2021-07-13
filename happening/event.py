#!/usr/bin/env python
from abc import abstractmethod, ABC
from typing import Any


class Event():

    def __init__(self, payload: Any) -> None:
        self._payload = payload

    @property
    @abstractmethod
    def identifier(self) -> str:
        raise NotImplementedError(f'You must implement `identifier` on {self.__class__.__name__}')

    @property
    def payload(self) -> Any:
        return self._payload
