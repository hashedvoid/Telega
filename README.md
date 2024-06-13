# <p align="center">Telega

<p align="center">A simple python module for writing telegram bots.</p>

# <p align="center">Installation
```
pip install git+https://github.com/hashedvoid/Telega
```
# <p align="center">Writing the first bot
```python
from Telega import Bot
import time

bot = Bot.newExistence('TOKEN')

if __name__ == '__main__':
    update_id = bot.getUpdates()[-1]['update_id']
    while True:
        time.sleep(2)
        messages = bot.getUpdates(update_id)
        for message in messages:
            if update_id < message['update_id']:
                update_id = message['update_id']
                if message['message']['text'] == '/start':
                	bot.sendMessage(message['message']['chat']['id'], f"Hello, world!")
```
# <p align="center">Simple echo bot
```python
from Telega import Bot
import time

bot = Bot.newExistence('TOKEN')

if __name__ == '__main__':
    update_id = bot.getUpdates()[-1]['update_id']
    while True:
        time.sleep(2)
        messages = bot.getUpdates(update_id)
        for message in messages:
            if update_id < message['update_id']:
                update_id = message['update_id']
                bot.sendMessage(message['message']['chat']['id'], message['message']['text'])
```
# <p align="center">Keyboard usage
```python
from Telega import Bot, Keyboard
import time

bot = Bot.newExistence('TOKEN')

kb = Keyboard()
kb.add_button(text="Wow, this is button!")

if __name__ == '__main__':
    update_id = bot.getUpdates()[-1]['update_id']
    while True:
        time.sleep(2)
        messages = bot.getUpdates(update_id)
        for message in messages:
            if update_id < message['update_id']:
                update_id = message['update_id']
                if message['message']['text'] == '/start':
                	bot.sendMessage(message['message']['chat']['id'], f"Hello, world!", reply_markup=kb.compile())
```
