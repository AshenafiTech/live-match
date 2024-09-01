# src/observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, match_name: str, event_type: str, event_data: str):
        pass
