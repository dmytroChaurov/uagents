import time
import requests

def run_hacker_news_agent():
    print("🕵️‍♂️ Агент-ресерчер запущен. Ищу свежие ИТ-новости (Hacker News)...\n")
    
    try:
        # Получаем ID лучших статей
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(top_stories_url, timeout=10)
        
        if response.status_code != 200:
            print("❌ Ошибка доступа к API Hacker News")
            return
            
        story_ids = response.json()[:5]  # Берем топ-5 новостей
        
        print("=== ТОП-5 НОВОСТЕЙ НА HACKER NEWS ===")
        for i, story_id in enumerate(story_ids, 1):
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story_data = requests.get(story_url, timeout=10).json()
            
            title = story_data.get("title", "Без заголовка")
            url = story_data.get("url", "Нет ссылки (только текст)")
            
            print(f"\n{i}. {title}")
            print(f"🔗 Ссылка: {url}")
        print("\n=====================================")
        
    except Exception as e:
        print(f"❌ Ошибка во время получения данных: {e}")

if __name__ == "__main__":
    run_hacker_news_agent()
    
    print("\nСбор новостей завершен. Агент переходит в фоновый режим ожидания...")
    while True:
        time.sleep(60)