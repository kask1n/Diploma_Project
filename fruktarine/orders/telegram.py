import requests
import logging

TOKEN = "6727424585:AAHqvOXEtmu56O7JdvONa20kl8Gezwl1X_Y"
logger = logging.getLogger(__name__)


def get_update_telegram():
    # Функция проверяет наличие новых сообщений, с помощью неё можно найти id чата
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    print(requests.get(url).json())


def send_by_telegram(message):
    chat_id = "37358423"  #Сообщение Диме
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    try:
        requests.get(url).json()
        logger.debug('Сообщение в телеграм успешно отправлено')
    except ConnectionError:
        logger.error('Сбой отправки сообщения в телеграм!')


if __name__ == '__main__':
    send_by_telegram('тест сообщения7')
