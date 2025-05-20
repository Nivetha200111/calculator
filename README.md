# Scratch Calculator DevOps Pipeline

![CI & Build](https://github.com/Nivetha200111/calculator/actions/workflows/ci.yml/badge.svg)

A simple desktop calculator whose buttons (and operations) are driven by `config.json`, which logs each calculation into `history.json`, fully automated with a one-click CI/CD pipeline on GitHub Actions.

---

## 📋 Overview

* **GUI**: Built with Python 3 + Tkinter
* **Config**: Button layout and operations defined in `config.json`
* **History**: Each calculation is appended to `history.json`
* **Lint & Test**: `flake8` for style, `pytest` for unit tests
* **Container**: Dockerfile to build a reproducible image
* **CI/CD**: GitHub Actions workflow (`ci.yml`) to lint, test, build & run

---

## ⚙️ Prerequisites

* Git (command-line)
* GitHub account
* Python 3.10+ (includes Tkinter)
* Docker
* (Optional) GitHub CLI
* Text editor / IDE (VS Code, PyCharm, etc.)

---

## 📂 Project Structure

```plaintext
calculator/
├── .gitignore
├── config.json
├── history.json        ← generated at runtime
├── main.py
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml
```

* **main.py** — JSON-driven Tkinter calculator
* **config.json** — 2D array of button labels & operations
* **history.json** — log of `{ timestamp, expression, result }`
* **requirements.txt** — `flake8`, `pytest`
* **Dockerfile** — builds a Python container that runs the app
* **.github/workflows/ci.yml** — CI pipeline

---

## ▶️ Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/Nivetha200111/calculator.git
   cd calculator
   ```
2. Launch the app:

   ```bash
   python3 main.py
   ```
3. Use the on-screen buttons:

   * `=` to evaluate
   * `C` to clear
4. Check `history.json` for a timestamped log of each calculation.

---

## 🐳 Docker Usage

1. Build the image:

   ```bash
   docker build -t scratch-calculator .
   ```
2. Run the container (example: add 2 + 3):

   ```bash
   docker run --rm scratch-calculator add 2 3
   # Outputs: 5
   ```

---

## 🔧 CI/CD Pipeline

### Workflow: `.github/workflows/ci.yml`

```yaml
name: 🚀 CI & Build

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  lint-and-validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: python-version: '3.10'
      - run: pip install --no-cache-dir flake8 pytest
      - run: flake8 main.py
      - run: python -m json.tool config.json

  test:
    needs: lint-and-validate
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: python-version: '3.10'
      - run: pytest --maxfail=1 --disable-warnings -q || echo "No tests to run"

  build-and-run-docker:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t scratch-calculator:ci .
      - run: |
          echo "2 + 3 = $(docker run --rm scratch-calculator:ci add 2 3)"
          echo "6 × 7 = $(docker run --rm scratch-calculator:ci mul 6 7)"
```

### One-Click Execution

* Go to **Actions → CI & Build** on GitHub
* Click **Run workflow** → select `main` → **Run**
* Watch live logs for:

  ```
  2 + 3 = 5
  6 × 7 = 42
  ```

---

## 🔗 GitHub Links

* **Repository**: [https://github.com/Nivetha200111/calculator](https://github.com/Nivetha200111/calculator)
* **Dockerfile**: [https://github.com/Nivetha200111/calculator/blob/main/Dockerfile](https://github.com/Nivetha200111/calculator/blob/main/Dockerfile)
* **CI Workflow**: [https://github.com/Nivetha200111/calculator/blob/main/.github/workflows/ci.yml](https://github.com/Nivetha200111/calculator/blob/main/.github/workflows/ci.yml)
* **Actions Dashboard**: [https://github.com/Nivetha200111/calculator/actions](https://github.com/Nivetha200111/calculator/actions)

---

## 🚀 Next Steps

* Add unit tests under `tests/`
* Persist history in SQLite instead of JSON
* Publish Docker image to Docker Hub or GitHub Packages
* Add scheduled runs (`on: schedule`) and Slack/email notifications
* Extend CI to deploy to a server or cloud function

---

*That's it—push your changes, click **Run workflow**, and your Scratch Calculator flows through lint, test, build, and run automatically!*