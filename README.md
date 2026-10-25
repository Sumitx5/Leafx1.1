# Lepo Bot

> This is the official Python version of Lepo Bot, designed with modular command structures and asynchronous tasks.

⚠️ **Status:** Currently updating this project. Features and architecture are subject to active modification.

---

## Features Breakdown

*   **Modular Architecture:** Utilizing `discord.ext.commands` for clean, grouped command handling within the `cmds/` directory.
*   **Dual-Format Configurations:** Supports parsing complex setup formats dynamically through `config.json` and structured environment rules via `config.yml`.
*   **Persistent Data Handling:** Tracks operational statistics, local logs, and custom dynamic databases cleanly in real-time.
*   **Dynamic Presence System:** Features a customizable activity manager using `discord.ext.tasks` that supports toggling between random and static status rotations.

## Configuration (`settings/config.yml`)

The bot's core behavior, credentials, and rich presence activities are fully customizable through the centralized YAML settings sheet.

```yaml
TOKEN: "" # add Your Token Here if You Want to Use Bot
Prefix: "!" # Bots Prefix

# Bots Activity Controller
activity_loop_time: 10       # Supports only Seconds
activity_logs_on_console: True
random_activities: True
activity_type: "playing"  # options(playing, watching, listening) if random activity is false
activities:
  playing:
    name: "with Python"

  listening:
    name: "!help"
    state: "play with me!"

  watching:
    name: "{guilds} Guilds & {members} Members"
```

### Configuration Instructions

*   **`TOKEN`**: Your Discord bot application token. Generate this via the Discord Developer Portal.
*   **`Prefix`**: The designated symbol or text used to invoke chat commands.
*   **`activity_loop_time`**: The delay window measured in seconds before cycling to the next presence activity profile.
*   **`activity_logs_on_console`**: Toggle log notifications inside the terminal output interface whenever a background status shift happens.
*   **`random_activities`**: When enabled (`True`), the engine continuously chooses random structures configured underneath the `activities` scope. If disabled (`False`), it locks exclusively onto the mode specified by `activity_type`.
*   **`activity_type`**: Baseline standard option selected when randomized loops are turned off. Supported inputs include `playing`, `watching`, or `listening`.
*   **`activities`**: Content parameters defining custom strings. Placeholders like `{guilds}` and `{members}` automatically scale inside status text formatting hooks.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sumitx5/lepo_py
   cd lepo_py
   ```

2. **Configure Settings:**
   Open `settings/config.yml` and insert your Discord Bot Token, prefix, and presence settings.

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Bot:**
   ```bash
   python lepo.py
   ```
