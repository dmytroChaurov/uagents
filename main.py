import time
import requests
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Заглушка для платформы
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")
    def log_message(self, format, *args):
        pass

def start_server():
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    httpd.serve_forever()

def run_hacker_news_agent():
    print("🕵️‍♂️ Ищу свежие ИТ-новости...\n")
    try:
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10)
        if response.status_code == 200:
            story_ids = response.json()[:5]
            for i, story_id in enumerate(story_ids, 1):
                story_data = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", timeout=10).json()
                print(f"{i}. {story_data.get('title')}\n🔗 {story_data.get('url', 'Нет ссылки')}\n")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    # 1. Мгновенно запускаем сервер в фоне, чтобы uagents8 был доволен
    threading.Thread(target=start_server, daemon=True).start()
    print("Сервер запущен. Платформа должна подтвердить статус Running.")
    
    # 2. Выполняем нашу основную задачу
    run_hacker_news_agent()
    
    # 3. Держим процесс активным
    while True:
        time.sleep(60)