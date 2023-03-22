import telebot

API_TOKEN = '999290654:AAF-w0l8XHUW_S7osjzXiq7YkeoEm68Byog'

bot = telebot.TeleBot(API_TOKEN)

# A dictionary to store the user information for each message
user_messages = {}


@bot.message_handler(commands=['start'])
def start_handler(message):
    user_id = message.from_user.id
    user_messages[user_id] = []
    bot.send_message(chat_id=message.chat.id, text='Welcome! Please send me a secret digit.')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    user_id = message.from_user.id
    user_messages[user_id].append(message.text)

    # Check if both secret digits have been received from different users
    if len(user_messages) == 2 and len(user_messages[list(user_messages.keys())[0]]) == 1 and len(
            user_messages[list(user_messages.keys())[1]]) == 1:
        secret1 = int(user_messages[list(user_messages.keys())[0]][0])
        secret2 = int(user_messages[list(user_messages.keys())[1]][0])
        full_secret = int(str(secret1) + str(secret2))
        bot.send_message(chat_id=message.chat.id,
                         text='Thanks! Now, please send me two guess digits from two different users.')
    # Check if both guess digits have been received from different users
    elif len(user_messages) == 2 and len(user_messages[list(user_messages.keys())[0]]) == 2 and len(
            user_messages[list(user_messages.keys())[1]]) == 2:
        guess1 = int(user_messages[list(user_messages.keys())[0]][1])
        guess2 = int(user_messages[list(user_messages.keys())[1]][1])
        full_guess = int(str(guess1) + str(guess2))
        bulls, cows, error = count_bulls_and_cows(full_secret, full_guess)
        bot.send_message(chat_id=message.chat.id, text='Bulls: {}, Cows: {}'.format(bulls, cows))


if __name__ == '__main__':
    bot.polling()
