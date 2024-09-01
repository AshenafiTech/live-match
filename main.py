# main.py
import time
import random
import threading
from src.match_manager import MatchManager
from src.fan import Fan

def simulate_match_events(match_name: str, match_manager: MatchManager):
    teams = {"Manchester United vs Arsenal": ["Manchester United", "Arsenal"],
             "Liverpool vs Manchester City": ["Liverpool", "Manchester City"]}
    events = ["Goal", "Penalty", "Substitution", "Yellow Card", "Red Card"]
    
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # End the simulation after 60 seconds
        if elapsed_time > 60:
            match_manager.notify_final_score(match_name)
            print(f"\n--- End of simulation for {match_name} ---\n")
            break
        
        event_type = random.choice(events)
        team = random.choice(teams[match_name])
        player = f"Player {random.randint(1, 11)}"
        event_data = f"{team} - {event_type}: {player}"
        match_manager.notify_observers(match_name, event_type, event_data)
        
        if event_type == "Goal":
            match_manager.update_score(match_name, team)
        
        time.sleep(random.randint(3, 10))  # Random delay between events

if __name__ == "__main__":
    match_manager = MatchManager()
    
    # Fans for Manchester United vs Arsenal
    alice = Fan("Alice")
    bob = Fan("Bob")
    
    # Fans for Liverpool vs Manchester City
    tom = Fan("Tom")
    sam = Fan("Sam")
    
    # Register observers
    match_manager.register_observer("Manchester United vs Arsenal", "Goal", alice)
    match_manager.register_observer("Manchester United vs Arsenal", "Goal", bob)
    match_manager.register_observer("Liverpool vs Manchester City", "Goal", tom)
    match_manager.register_observer("Liverpool vs Manchester City", "Goal", sam)
    
    match_manager.register_observer("Manchester United vs Arsenal", "Penalty", alice)
    match_manager.register_observer("Manchester United vs Arsenal", "Penalty", bob)
    match_manager.register_observer("Liverpool vs Manchester City", "Substitution", tom)
    match_manager.register_observer("Liverpool vs Manchester City", "Substitution", sam)
    
    # Simulate events for both matches concurrently
    threading.Thread(target=simulate_match_events, args=("Manchester United vs Arsenal", match_manager)).start()
    threading.Thread(target=simulate_match_events, args=("Liverpool vs Manchester City", match_manager)).start()
