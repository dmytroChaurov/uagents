import time
import requests
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

def run_hacker_news_agent():
    print("🕵️‍♂️ Агент-ресерчер запущен. Ищу свежие ИТ-новости (Hacker News)...\n")
    try:
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10)
        if response.status_code != 200:
            print("❌ Ошибка доступа к API")
            return
            
        story_ids = response.json()[:5]
        print("=== ТОП-5 НОВОСТЕЙ НА HACKER NEWS ===")
        for i, story_id in enumerate(story_ids, 1):
            story_data = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", timeout=10).json()
            print(f"\n{i}. {story_data.get('title', 'Без заголовка')}")
            print(f"🔗 Ссылка: {story_data.get('url', 'Нет ссылки')}")
        print("\n=====================================")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

# Заглушка для веб-сервера, чтобы uagents8 видел HTTP-активность
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Agent is active and running!")
        
    def log_message(self, format, *args):
        pass # Отключаем лишний спам в логи от сервера

if __name__ == "__main__":
    # Запускаем сбор новостей
    run_hacker_news_agent()
    
    print("\nСбор новостей завершен. Запуск HTTP-сервера для платформы uagents8 на порту 8000...")
    
    # Запускаем сервер на порту 8000
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    httpd.serve_forever()