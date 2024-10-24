# Eval Bot

A Discord bot designed to execute Python code snippets directly from Discord messages. This bot is primarily focused on providing an eval command that allows the bot owner to run arbitrary Python code and see the output in real-time.

## Features
- **Eval Command**: Execute Python code snippets and get the output directly in Discord, with markdown support.
- **Echo Command**: Simple command to echo back messages.
- **Sync Command**: Sync application commands globally or to a specific guild.

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

### Commands

#### Eval Command
The eval command allows the bot owner to execute Python code snippets. This command is restricted to the bot owner for security reasons. (See warning above)

Usage:
```
e.eval <code>
```
Example:
````
e.eval ```py
print("Hello, World!")
```
````
**or**
```
e.eval print("Hello, World")
```
Output:
```
Hello, World!
```

wip
