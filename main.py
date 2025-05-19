#!/usr/bin/env python3
import tkinter as tk
import json
import os
from datetime import datetime

# ─── Paths ────────────────────────────────────────────────────────────────
CONFIG_PATH  = "config.json"
HISTORY_PATH = "history.json"

# ─── Load button layout from JSON ────────────────────────────────────────
def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

# ─── Append one entry to history.json ───────────────────────────────────
def save_history(expr, result):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "expression": expr,
        "result": result
    }
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, "r") as f:
            history = json.load(f)
    else:
        history = []
    history.append(entry)
    with open(HISTORY_PATH, "w") as f:
        json.dump(history, f, indent=2)

# ─── Button click handler ───────────────────────────────────────────────
expression = ""
def on_button_click(value):
    global expression
    if value == "=":
        try:
            result = str(eval(expression))
            display.set(result)
            save_history(expression, result)
            expression = result  # allow chaining
        except Exception:
            display.set("Error")
            expression = ""
    elif value == "C":
        expression = ""
        display.set("")
    else:
        expression += value
        display.set(expression)

# ─── Build the GUI ──────────────────────────────────────────────────────
config = load_config()

root = tk.Tk()
root.title("JSON-Driven Scratch Calculator")

display = tk.StringVar()
entry = tk.Entry(root, textvariable=display, font=("Arial", 24), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# create buttons from config
for r, row in enumerate(config["buttons"], start=1):
    for c, label in enumerate(row):
        btn = tk.Button(root, text=label, font=("Arial", 20),
                        command=lambda v=label: on_button_click(v))
        btn.grid(row=r, column=c, sticky="nsew")

# add a Clear button below
clear_btn = tk.Button(root, text="C", font=("Arial", 20),
                      bg="#f66", fg="white",
                      command=lambda: on_button_click("C"))
clear_btn.grid(row=len(config["buttons"])+1, column=0, columnspan=4, sticky="nsew")

# make rows/columns expand equally
for i in range(len(config["buttons"])+2):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
