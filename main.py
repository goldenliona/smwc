import requests
from icq import bot
import datetime
global message_text
global current_time
# Replace with your ICQ bot API token
ICQ_BOT_TOKEN = "001.3280755794.0514846345:1010959428"


def send_message(chat_id, text):
    url = f'https://api.icq.net/bot/v1/messages/sendText?token={ICQ_BOT_TOKEN}'
    payload = {
        'chatId': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.status_code


def message_handler(bot1, event1):
    sender_id = event1.data['from']['firstName']

    response_text = f"Hello! You said: {message_text}"
    bot1.send_text(sender_id, response_text)
    response_text1 = f"Hello! You said: {message_text}"
    bot1.send_text(sender_id, response_text1)
    response_text = f"Hello! You said: {message_text}"
    bot.send_text(sender_id, response_text)


def main(sender_id=None):

    global current_time
    chat_id = 'sender_id'

    message_to_send = "Hello, this is your ICQ bot!"
    send_message(chat_id, message_to_send)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    response_text = f"The current time is: {current_time}"
    bot.send_text(sender_id, response_text)

    user_input = input("")

    # Check if user input matches "/break" and provide a response
    if user_input == "break":
        print("\nTIME: ", current_date, "\n\nUser ID:", chat_id, "\nRESPONSE: ", user_input, "\nTIME: ", current_time)

    elif user_input == "sm":
        print("\nTIME: ", current_date, "\n\nUser ID:", chat_id, "\nRESPONSE: ", user_input, "\nTIME: ", current_time)

    elif user_input == "wc":
        print("\nTIME: ", current_date, "\n\nUser ID:", chat_id, "\nRESPONSE: ", user_input, "\nTIME: ", current_time)

    elif user_input == "back":
        print("\nTIME: ", current_date, "\nUser ID:", chat_id, "\nRESPONSE: ", user_input, "\nTIME: ")

    else:

        print("User ID:", chat_id, "Invalid Key in:", user_input)


if __name__ == '__main__':
    main()
