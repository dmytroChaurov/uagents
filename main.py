import requests
import os

def run_agent():
    print("Инициализация тестового агента...")
    
    # Намеренная ошибка для краш-теста: опечатка в вызове библиотеки (reqests вместо requests)
    response = reqests.get("https://jsonplaceholder.typicode.com/todos/1") 
    
    if response.status_code == 200:
        data = response.json()
        print(f"API ответ: {data.get('title')}")
    
    # Тестирование защищенного хранилища ключей
    test_secret = os.environ.get("TEST_SECRET_KEY", "Ключ не передан")
    print(f"Переменные окружения: {test_secret}")

if __name__ == "__main__":
    run_agent()