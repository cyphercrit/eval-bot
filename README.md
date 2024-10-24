# Eval Bot

A Discord bot designed to execute Python code snippets directly from Discord messages. This bot is primarily focused on providing an eval command that allows the bot owner to run arbitrary Python code and see the output in real-time.

## Features
- **Eval Command**: Execute Python code snippets and get the output directly in Discord, with markdown support.
- **Echo Command**: Simple command to echo back messages.
- **Sync Command**: Sync application commands globally or to a specific guild.

## Demonstration Image

![Demo Image](https://i.imgur.com/DV08NnQ.png)

## :warning: Warning :warning:

The `eval` command executes arbitrary Python code, which can be dangerous. Only the bot owner should have access to this command. Misuse of this command can lead to security vulnerabilities, data loss, or other unintended consequences. Use with caution.

For more information regarding arbitrary code execution, please refer [here](https://www.geeksforgeeks.org/what-is-arbitrary-code-execution/).

## Setup

### Prerequisites

- Python 3.8+
- `pip` (Python package installer)
- A Discord bot token

### Installation

#### 1. Clone the repository:
```sh
git clone https://github.com/cyphercrit/eval-bot
cd eval-bot
```

#### 2. Create a virtual environment and activate it:
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

#### 3. Install the required packages:
```sh
pip install -r requirements.txt
```

#### 4. Create a `.env` file in root directory and add your Discord bot token:
```sh
DISCORD_TOKEN=your_discord_bot_token
```

#### 5. Start the bot:
```sh
python bot.py
```

## Commands

#### Eval Command
The eval command allows the bot owner to execute Python code snippets. This command is restricted to the bot owner for security reasons. (See warning above)

Usage:
```sh
e.eval <code>
```
Example:
````py
e.eval ```py
print("Hello, World!")
```
````
**or**
```sh
e.eval print("Hello, World")
```
Output:
```
Hello, World!
```

#### Echo Command _(Slash)_
The `echo` command sends back a message provided by the user. This command utilizes [Discord Interactions](https://discord.com/developers/docs/interactions/receiving-and-responding), which means that this bot can be used to maintain a [active developer badge](https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge)!

Usage:
```sh
/echo <message>
```

Example:
```
/echo Hello There!
```
Output:
```
Hello There!
```

#### Sync Command
The `sync` command syncs application commands globally or to a specific guild. This command is also restricted to the owner to avoid API misuse. _Note: global syncing of application commands may take longer than syncing for a specific guild, which is typically instant_

Usage:
```sh
e.sync
```
Output:
```
Global Application Commands Synced!
```
**or**

Usage:
```sh
e.sync <guild_id>
```
Output:
```
Application Commands Synced to Guild ID <guild_id>!
```
## License
This project is licensed under the MIT License
