# src/match_manager.py
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register_observer(self, match_name: str, event_type: str, observer):
        pass
    
    @abstractmethod
    def remove_observer(self, match_name: str, event_type: str, observer):
        pass
    
    @abstractmethod
    def notify_observers(self, match_name: str, event_type: str, event_data: str):
        pass

class MatchManager(Subject):
    def __init__(self):
        self._observers = {}
        self._scores = {}
    
    def register_observer(self, match_name: str, event_type: str, observer):
        if match_name not in self._observers:
            self._observers[match_name] = {}
        if event_type not in self._observers[match_name]:
            self._observers[match_name][event_type] = []
        self._observers[match_name][event_type].append(observer)
    
    def remove_observer(self, match_name: str, event_type: str, observer):
        if match_name in self._observers and event_type in self._observers[match_name]:
            self._observers[match_name][event_type].remove(observer)
    
    def notify_observers(self, match_name: str, event_type: str, event_data: str):
        if match_name in self._observers and event_type in self._observers[match_name]:
            for observer in self._observers[match_name][event_type]:
                observer.update(match_name, event_type, event_data)
    
    def update_score(self, match_name: str, team: str):
        if match_name not in self._scores:
            self._scores[match_name] = {}
        if team not in self._scores[match_name]:
            self._scores[match_name][team] = 0
        self._scores[match_name][team] += 1
    
    def notify_final_score(self, match_name: str):
        scores = self._scores.get(match_name, {})
        teams = {"Manchester United vs Arsenal": ["Manchester United", "Arsenal"],
                 "Liverpool vs Manchester City": ["Liverpool", "Manchester City"]}
        teams_list = teams.get(match_name, ["Team A", "Team B"])
        team1, team2 = teams_list
        score1 = scores.get(team1, 0)
        score2 = scores.get(team2, 0)
        score_message = f"Final Score for {match_name}: {team1} {score1} - {team2} {score2}"
        print()
        print(f"--- {score_message} ---")
        self.notify_observers(match_name, "Final Score", score_message)
