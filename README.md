# Live-Match

**Live-Match** is a Python application that simulates live sports match updates using the Observer pattern. It provides real-time notifications about different events during two concurrent football matches and displays the final score.

## Features

- Simulate live events in football matches.
- Notify subscribers of various match events such as goals, penalties, and substitutions.
- Display real-time notifications for multiple matches in a console-based interface.
- Show final scores at the end of the simulation.

## Project Structure

- `match_manager.py`: Contains the `MatchManager` class responsible for managing match events, scores, and observers.
- `observer.py`: Defines the `Observer` interface and the `Fan` class implementing it.
- `main.py`: Contains the `simulate_match_events` function to simulate match events.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ashyea/live-match.git
   cd live-match

2. **Run**
    
    ```python main.py``` from the root directory of the project
