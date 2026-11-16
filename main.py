import os
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

class WebParserHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Отправляем платформе и браузеру статус 200 (Всё ОК)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        try:
            # Идем в интернет за случайным фактом о котах (публичный и очень быстрый API)
            api_response = requests.get("https://catfact.ninja/fact", timeout=5)
            
            if api_response.status_code == 200:
                fact = api_response.json().get("fact", "Факт не найден")
            else:
                fact = "Не удалось получить данные с сайта."

            # Формируем HTML-страничку с результатом
            html_content = f"""
            <html>
            <body style="font-family: Arial, sans-serif; padding: 40px; text-align: center;">
                <h2>Привет! Я ваш тестовый ИИ-агент 🤖</h2>
                <p>Я только что сходил в интернет и принес вам случайный факт:</p>
                <div style="background: #f0f0f0; padding: 20px; border-radius: 10px; display: inline-block; max-width: 600px;">
                    <strong>{fact}</strong>
                </div>
                <p><small>Обновите страницу, чтобы я скачал новый факт!</small></p>
            </body>
            </html>
            """
        except Exception as e:
            html_content = f"<h1>Произошла ошибка при походе в интернет: {e}</h1>"
            
        # Отправляем HTML в браузер
        self.wfile.write(html_content.encode('utf-8'))

    def log_message(self, format, *args):
        pass # Отключаем лишний спам в терминале

def run():
    port = int(os.environ.get("PORT", 8000))
    print(f"🚀 Агент запущен на порту {port}. Жду запросов...")
    
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, WebParserHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    run()