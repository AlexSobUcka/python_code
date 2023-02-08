import telebot

API_KEY = '999290654:AAF-w0l8XHUW_S7osjzXiq7YkeoEm68Byog'

# Create a bot instance
bot = telebot.TeleBot(API_KEY)

# Global variable to store the secret number
secret = None
count_of_guess = None


# Function to count the number of bulls and cows
def count_bulls_and_cows(secret, guess):
    secret = str(secret)
    guess = str(guess)
    if len(secret) != 4 or len(guess) != 4:
        return 0, 0, "Both numbers must have 4 digits"
    for digit in secret:
        if not digit.isdigit() or int(digit) < 1 or int(digit) > 9:
            return 0, 0, "Both numbers can only contain digits from 1 to 9"
    for digit in guess:
        if not digit.isdigit() or int(digit) < 1 or int(digit) > 9:
            return 0, 0, "Both numbers can only contain digits from 1 to 9"
    if len(set(secret)) != 4 or len(set(guess)) != 4:
        return 0, 0, "Both numbers can't have repeated digits"
    bulls = 0
    cows = 0
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1
        elif secret[i] in guess:
            cows += 1
    return bulls, cows, ""


# Handle the /start command
@bot.message_handler(commands=['start'])
def start_game(message):
    global secret
    global count_of_guess
    count_of_guess = 1
    secret = message.text.split()[1] if len(message.text.split()) > 1 else None
    if secret and len(secret) == 4 and secret.isdigit() and len(set(secret)) == 4:
        bot.reply_to(message, "Game started! Please ask another user to guess the number.")
    else:
        bot.reply_to(message, "Invalid secret number. Please provide a 4-digit integer with no repeating digits.")


# Handle messages from users
@bot.message_handler(func=lambda message: True)
def guess_number(message):
    global secret
    global count_of_guess
    if not secret:
        bot.reply_to(message, "Please start the game first by using the /start command.")
        return
    guess = message.text
    bulls, cows, error = count_bulls_and_cows(secret, guess)
    if error:
        bot.reply_to(message, error)
        return
    if bulls == 4:
        bot.reply_to(message,
                     f"Congratulations! You guessed the number correctly. Number of attempts: {count_of_guess}")
        secret = None
    else:
        count_of_guess += 1
        bot.reply_to(message, f"{bulls} bull(s) and {cows} cow(s)")


# Start the bot
bot.polling()
