import requests
import os
import time

def run_agent():
    print("Инициализация тестового агента...")
    
    # Правильный вызов requests
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1") 
    
    if response.status_code == 200:
        data = response.json()
        print(f"API ответ: {data.get('title')}")
    
    test_secret = os.environ.get("TEST_SECRET_KEY", "Ключ не передан")
    print(f"Переменные окружения: {test_secret}")

if __name__ == "__main__":
    run_agent()
    
    print("Агент выполнил задачу. Переход в режим ожидания (чтобы процесс не считался упавшим)...")
    
    # Искусственно поддерживаем жизнь процесса
    while True:
        time.sleep(60)