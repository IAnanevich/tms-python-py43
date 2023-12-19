import requests
import telebot
from telebot import types

BOT_TOKEN = ''
WEATHER_KEY = ''

bot = telebot.TeleBot(BOT_TOKEN)


def create_start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Поздороваться')
    markup.add(btn1)
    return markup


def create_main_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Факт о кошках')
    btn2 = types.KeyboardButton('Случайное действие')
    btn3 = types.KeyboardButton('Случайное изображение собаки')
    btn4 = types.KeyboardButton('Получить свой IP-адрес')
    btn5 = types.KeyboardButton('Погода')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup


def parse_api(url):
    result = requests.get(url)
    return result.json()


def get_weather(message):
    city = message.text
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_KEY}'
    result = parse_api(weather_url)

    if 'main' in result:
        temperature = result['main']['temp']
        description = result['weather'][0]['description']
        response_text = f'Погода в городе {city}: \nТемпература: {temperature}°C \nОписание: {description}'
    else:
        response_text = f'Не удалось найти информацию о погоде для города {city}'

    bot.send_message(message.from_user.id, response_text)


@bot.message_handler(commands=['start'])
def start(message):
    markup = create_start_markup()
    bot.send_message(message.from_user.id, 'Привет, я твой бот.', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Поздороваться':
        markup = create_main_markup()
        bot.send_message(message.from_user.id, 'Задай свой вопрос', reply_markup=markup)
    elif message.text == 'Факт о кошках':
        result = parse_api(url='https://catfact.ninja/fact')
        bot.send_message(message.from_user.id, result['fact'], parse_mode='Markdown')
    elif message.text == 'Случайное действие':
        result = parse_api(url='https://www.boredapi.com/api/activity')
        bot.send_message(message.from_user.id, result['activity'], parse_mode='Markdown')
    elif message.text == 'Случайное изображение собаки':
        result = parse_api(url='https://dog.ceo/api/breeds/image/random')
        bot.send_photo(message.from_user.id, result['message'])
    elif message.text == 'Получить свой IP-адрес':
        result = parse_api(url='https://api.ipify.org?format=json')
        bot.send_message(message.from_user.id, result['ip'], parse_mode='Markdown')
    elif message.text == 'Погода':
        bot.send_message(message.from_user.id, 'Введите название города: ', parse_mode='Markdown')
        bot.register_next_step_handler(message, get_weather)



if __name__ == '__main__':
    bot.polling(none_stop=True)
