import os
import time
import random
import requests
import json
from datetime import datetime
from fake_useragent import UserAgent
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

def load_config(filename):
    """Загружает файл конфигурации и проверяет его существование."""
    if not os.path.exists(filename):
        log(f"Configuration file '{filename}' not found.", level="ERROR")
        return None
    
    with open(filename, 'r') as config_file:
        config = json.load(config_file)
    
    # Проверка на наличие обязательных параметров
    if not config.get('user_id') or not config.get('api_key'):
        log("Configuration error: 'user_id' and 'api_key' must not be empty.", level="ERROR")
        return None
    
    return config

def log(message, level="INFO"):
    """Функция для вывода логов с метками времени и уровнем важности"""
    timestamp = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    
    if level == "INFO":
        level_str = f"{Fore.LIGHTGREEN_EX}INFO {Fore.LIGHTWHITE_EX}"
    elif level == "ERROR":
        level_str = f"{Fore.LIGHTRED_EX}ERROR{Fore.LIGHTWHITE_EX}"
    elif level == "DEBUG":
        level_str = f"{Fore.LIGHTBLUE_EX}DEBUG{Fore.LIGHTWHITE_EX}"
    elif level == "WARNING":
        level_str = f"{Fore.LIGHTYELLOW_EX}WARN {Fore.LIGHTWHITE_EX}"
    
    print(f"{Fore.LIGHTWHITE_EX}{timestamp} | {level_str:<7} | {message}")

def safe_request(url, headers):
    """Функция для отправки запросов"""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Вызывает исключение для кодов ошибок HTTP
        return response
    except requests.exceptions.HTTPError as http_err:
        log(f"HTTP error occurred: {http_err}", level="ERROR")
    except requests.exceptions.ConnectionError as conn_err:
        log(f"Connection error occurred: {conn_err}", level="ERROR")
    except requests.exceptions.Timeout as timeout_err:
        log(f"Timeout error occurred: {timeout_err}", level="ERROR")
    except requests.exceptions.RequestException as req_err:
        log(f"Request error occurred: {req_err}", level="ERROR")
    return None

# Загрузка конфигурации
config = load_config('config.json')
if not config:
    log("Terminating program due to configuration errors.", level="ERROR")
    exit(1)

user_id = config['user_id']
api_key = config['api_key']
delay_range = config['delay_range']
click_count_range = config['click_count_range']
energy_delay_range = config['energy_delay_range']

base_headers = {
    'Authorization': f'Api-Key {api_key}',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru;q=0.6',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://savemoney.alfabank.ru',
    'Referer': 'https://savemoney.alfabank.ru/',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'User-Agent': UserAgent(os="android").random  # Случайный User-Agent
}

# 1. Авторизация и получение данных
auth_url = 'https://back.palindrome.media/api/screens/alfa_combat/data.json'
response = safe_request(auth_url, headers=base_headers)
if response and response.status_code == 200:
    log("Authorization successful!")
else:
    log("Authorization failed!", level="ERROR")

# 2. Бесконечный цикл кликов
while True:
    try:
        # Случайное количество кликов
        click_count = random.randint(*click_count_range)
        
        sync_url = f'https://back.palindrome.media/api/hampter/sync/{user_id}/{click_count}'
        response = safe_request(sync_url, headers=base_headers)
        
        if response and response.status_code == 200:
            data = response.json()
            coins = f"{data.get('coins', 0):,}"
            energy = data.get('energy', 0)

            log(f"Successful tapped! | Balance: {Fore.LIGHTBLUE_EX}{coins}{Fore.LIGHTWHITE_EX} ({Fore.LIGHTGREEN_EX}+{click_count:,}{Fore.LIGHTWHITE_EX})", level="INFO")

            # Проверка энергии и игрового статуса
            if energy <= 0 or data.get('is_game_over'):
                log(f"Minimum energy reached: {energy}", level="WARNING")
                delay = random.randint(*energy_delay_range)
                log(f"Sleep {delay}s", level="DEBUG")
                time.sleep(delay)
                continue
        else:
            log("Synchronization error. Continuing operation.", level="ERROR")
    except Exception as e:
        log(f"Error during synchronization: {e}", level="ERROR")

    # Случайная задержка между запросами
    delay = random.randint(*delay_range)
    log(f"Sleep {delay}s", level="DEBUG")
    time.sleep(delay)
