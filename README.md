Twitch Mobile Web Automation – Take-Home Assignment
Overview
This project implements an end-to-end automated test for the Twitch mobile web experience using Python + Selenium.
The goal is to demonstrate clean code, scalable test architecture, and robust handling of real-world UI behavior (dynamic content, overlays, modals).
The test simulates a realistic user journey:
Open Twitch mobile web
Search for a game
Select a streamer from search results
Handle possible blocking overlays
Verify video playback
Tech Stack
Python 3
Selenium WebDriver
Chrome Mobile Emulation (Pixel 7)
Page Object Model (POM)
Project Structure
project/
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── streamer_page.py
│
├── tests/
│   └── test_twitch_e2e.py
│
├── driver/
│   └── driver_factory.py
│
├── assets/
│   └── test_run.gif
│
└── README.md
Key Design Decisions
Page Object Model
Each page encapsulates its own locators and behavior
No test logic inside page objects
Promotes readability and scalability
Explicit Waits Only
No implicit waits are used
Synchronization is handled via explicit, intention-revealing waits
Avoids flaky timing behavior
Defensive Overlay Handling
The framework safely handles blocking UI elements that may or may not appear:
Explicit content warning
Muted audio notice
Other pre-play overlays
All overlay handling is:
Conditional
Non-blocking
Isolated to the StreamerPage
Demo-Friendly Execution
A configurable demo mode allows slightly slowed execution for recording purposes without affecting test correctness or CI behavior.
Test Run Demo
The following GIF shows a complete automated run of the test:
Flow shown:
Search interaction
Search results loading
Streamer selection
Overlay dismissal (if present)
Video player load confirmation