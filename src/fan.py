# src/fan.py
from .observer import Observer

class Fan(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, match_name: str, event_type: str, event_data: str):
        print(f"Notification for {self.name}: {match_name} - {event_type} - {event_data}")
