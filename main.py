import telebot
from telebot import types

bot = telebot.TeleBot('6703583171:AAGuarB-Iw3vRYLK8y36thZpJ0f-IuSxee4')

class User:
    def __init__(self):
        self.period = None
        self.country_from = None
        self.country_to = None

users = {}

# Conversation states
SELECT_PERIOD, SELECT_COUNTRY_FROM = range(2)

@bot.message_handler(commands=['start'])
def main_start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}! Я помогу тебе с поиском открыток из прошлого! Давай приступим! Список команд ты можешь посмотреть в меню')

def select_period(message):
    user = users.get(message.chat.id)
    if not user:
        bot.send_message(message.chat.id, 'Что-то пошло не так. Попробуйте еще раз.')
        return
    bot.send_message(message.chat.id, 'Выбери временной промежуток:', reply_markup=get_period_markup())
    bot.register_next_step_handler(message, select_country_from)

@bot.message_handler(commands=['letsgo'])
def on_click(message):
    users[message.chat.id] = User()
    bot.send_message(message.chat.id, 'Выбери временной промежуток:', reply_markup=get_period_markup())
    bot.register_next_step_handler(message, select_period)

@bot.message_handler(commands=['help'])
def main_creator(message):
    bot.send_message(message.chat.id, 'Если у Вас возникли какие-то вопросы или проблема с ботом, пишите сюда https://vk.com/wfeghd5izn')

def get_period_markup():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='1891-1916 гг', callback_data='period_1')
    button2 = types.InlineKeyboardButton(text='1917-1940 гг', callback_data='period_2')
    button3 = types.InlineKeyboardButton(text='1941-1965 гг', callback_data='period_3')
    button4 = types.InlineKeyboardButton(text='1966-1985 гг', callback_data='period_4')
    button5 = types.InlineKeyboardButton(text='1986-1992 гг', callback_data='period_5')
    button6 = types.InlineKeyboardButton(text='1993-2014 гг', callback_data='period_6')
    markup.add(button1, button2, button3, button4, button5, button6)
    return markup

def get_country_markup():
    markup = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text='Великобритания', callback_data='country_UK'),
        types.InlineKeyboardButton(text='Италия', callback_data='country_IT'),
        types.InlineKeyboardButton(text='Германия', callback_data='country_GER'),
        types.InlineKeyboardButton(text='Китай', callback_data='country_CN'),
        types.InlineKeyboardButton(text='Латвия', callback_data='country_LAT'),
        types.InlineKeyboardButton(text='Польша', callback_data='country_PL'),
        types.InlineKeyboardButton(text='Россия| Российская Империя | СССР', callback_data='country_RUS'),
        types.InlineKeyboardButton(text='США', callback_data='country_US'),
        types.InlineKeyboardButton(text='Турция', callback_data='country_TR'),
        types.InlineKeyboardButton(text='Финляндия', callback_data='country_FI'),
        types.InlineKeyboardButton(text='Франция', callback_data='country_FR'),
        types.InlineKeyboardButton(text='Швейцария', callback_data='country_SW'),
    ]
    markup.add(*buttons)
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user = users.get(call.message.chat.id)

    if not user:
        bot.send_message(call.message.chat.id, 'Что-то пошло не так. Попробуйте еще раз.')
        return

    if call.data.startswith('period'):
        user.period = call.data
        bot.send_message(call.message.chat.id, 'Выбери страну отправления:', reply_markup=get_country_markup())
        bot.register_next_step_handler(call.message, select_country_from)
    else:
        user.country_from = call.data  # Исправлено: сохраняем выбранную страну
        display_selected_values(user, call.message.chat.id)

def select_country_from(message):
    user = users.get(message.chat.id)
    if not user:
        bot.send_message(message.chat.id, 'Что-то пошло не так. Попробуйте еще раз.')
        return

    user.country_from = message.text
    display_selected_values(user, message.chat.id)

def display_selected_values(user, chat_id):
    if user:
        result_period = str(user.period)
        result_country = str(user.country_from)
        if result_period == "period_1":
            result_period = "1891"
            if result_country == "country_RUS":
                result_country = "Rus"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_IT":
                result_country = "It"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_GER":
                result_country = "Ger"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_UK":
                result_country = "Uk"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_CN":
                result_country = "Cn"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_LAT":
                result_country = "Lat"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_PL":
                result_country = "Pl"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_US":
                result_country = "Us"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_TR":
                result_country = "Tr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FI":
                result_country = "Fi"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FR":
                result_country = "Fr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_SW":
                result_country = "Sw"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
        if result_period == "period_2":
            result_period = "1891"
            if result_country == "country_RUS":
                result_country = "Rus"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_IT":
                result_country = "It"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_GER":
                result_country = "Ger"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_UK":
                result_country = "Uk"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_CN":
                result_country = "Cn"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_LAT":
                result_country = "Lat"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_PL":
                result_country = "Pl"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_US":
                result_country = "Us"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_TR":
                result_country = "Tr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FI":
                result_country = "Fi"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FR":
                result_country = "Fr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_SW":
                result_country = "Sw"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
        if result_period == "period_3":
            result_period = "1891"
            if result_country == "country_RUS":
                result_country = "Rus"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_IT":
                result_country = "It"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_GER":
                result_country = "Ger"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_UK":
                result_country = "Uk"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_CN":
                result_country = "Cn"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_LAT":
                result_country = "Lat"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_PL":
                result_country = "Pl"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_US":
                result_country = "Us"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_TR":
                result_country = "Tr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FI":
                result_country = "Fi"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FR":
                result_country = "Fr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_SW":
                result_country = "Sw"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
        if result_period == "period_4":
            result_period = "1891"
            if result_country == "country_RUS":
                result_country = "Rus"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_IT":
                result_country = "It"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_GER":
                result_country = "Ger"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_UK":
                result_country = "Uk"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_CN":
                result_country = "Cn"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_LAT":
                result_country = "Lat"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_PL":
                result_country = "Pl"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_US":
                result_country = "Us"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_TR":
                result_country = "Tr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FI":
                result_country = "Fi"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FR":
                result_country = "Fr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_SW":
                result_country = "Sw"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
        if result_period == "period_5":
            result_period = "1891"
            if result_country == "country_RUS":
                result_country = "Rus"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_IT":
                result_country = "It"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_GER":
                result_country = "Ger"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_UK":
                result_country = "Uk"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_CN":
                result_country = "Cn"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_LAT":
                result_country = "Lat"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_PL":
                result_country = "Pl"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_US":
                result_country = "Us"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_TR":
                result_country = "Tr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FI":
                result_country = "Fi"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FR":
                result_country = "Fr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_SW":
                result_country = "Sw"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
        if result_period == "period_6":
            result_period = "1891"
            if result_country == "country_RUS":
                result_country = "Rus"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_IT":
                result_country = "It"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_GER":
                result_country = "Ger"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_UK":
                result_country = "Uk"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_CN":
                result_country = "Cn"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_LAT":
                result_country = "Lat"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_PL":
                result_country = "Pl"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_US":
                result_country = "Us"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_TR":
                result_country = "Tr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FI":
                result_country = "Fi"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_FR":
                result_country = "Fr"
                for i in range (1,4):
                    file = open('./'+result_country+"_"+result_period+"_"+str(i)+".jpg", "rb")
                    bot.send_photo(chat_id, file)
            if result_country == "country_SW":
                result_country = "Sw"
                for i in range(1, 4):
                    file = open('./' + result_country + "_" + result_period + "_" + str(i) + ".jpg", "rb")
                    bot.send_photo(chat_id, file)

if __name__ == '__main__':
    bot.polling(none_stop=True)
