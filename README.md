# Lepo Bot

> This is the official Python version of Lepo Bot, designed with modular command structures and asynchronous tasks.

⚠️ **Status:** Currently updating this project. Features and architecture are subject to active modification.

---

## Features Breakdown

*   **Modular Architecture:** Utilizing `discord.ext.commands` for clean, grouped command handling within the `cmds/` directory.
*   **Dual-Format Configurations:** Supports parsing complex setup formats dynamically through `config.json` and structured environment rules via `config.yml`.
*   **Persistent Data Handling:** Tracks operational statistics, local logs, and custom dynamic databases cleanly in real-time.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd Lepo
   ```

2. **Configure Settings:**
   Fill out your sensitive variables inside `settings/config.yml` or `data/config.json`.

3. **Launch the Bot:**
   ```bash
   python lepo.py
   ```
