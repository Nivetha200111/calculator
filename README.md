# Scratch Calculator

A simple desktop calculator whose buttons (and operations) are driven by `config.json`, and which logs each calculation into `history.json`.

## How to Run

1. Clone/download the repo.
2. Ensure you have Python 3.6+ (Tkinter comes bundled).
3. From the project root:
   ```bash
   python main.py
4.     Use the on-screen buttons. Press = to evaluate; press C to clear.

Arithmetic history is appended to history.json (timestamp, expression, result).