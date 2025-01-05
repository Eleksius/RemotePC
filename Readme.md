# Remote PC bot

## Ru (на русском)

Этот бот создан для управления вашим пк через телеграм.

### Установка зависимостей

```shell
pip install pyTelegramBotAPI==4.20.0 comtypes==1.4.8 pycaw==20240210 screen_brightness_control==0.24.1
```

Или используйте `pip install -r requirements.txt`

### Настройка

Все, что нужно сделать - вставить свой токен бота, полученного от BotFather.

#### Как получить токен?

- Перейти к [BotFather](https://t.me/BotFather)
- Ввести команду /newbot, и, следуя инструкциям, назанчить имя и юзейрнейм боту
- После создания бота, BotFather пришлет вам его токен в формате: `6373337774:AAEthdBHfwloSB-YoG1t6ILqpH4QKa8lhMk`, скопирйте его

Теперь идем в config и вставляем свой токен в константу TOKEN.

### Запуск

Запустите файл `main.py`

Теперь напишите своему боту команду /start, бот должен прислать вам основное меню, через которое вы сможете управлять своим пк

---

## EN (in English)

This bot is designed to control your PC via telegram.

## Installing dependencies

```shell
pip install pyTelegramBotAPI==4.20.0 comtypes==1.4.8 pycaw==20240210 screen_brightness_control==0.24.1
```

Or use `pip install -r requirements.txt`

## Setting up

All you need to do is insert your bot token received from BotFather.

### How do I get a token?

- Go to [BotFather](https://t.me/BotFather )
- Enter the /newbot command, and, following the instructions, give the name and username to the bot
- After creating the bot, BotFather will send you its token in the format: `6373337774:AAEthdBHfwloSB-YoG1t6ILqpH4QKa8lhMk`, copy it

Now go to config and insert your token into the TOKEN constant.

## Launch

Run the file `main.py`

Now write the /start command to your bot, the bot should send you the main menu through which you can control your PC.
