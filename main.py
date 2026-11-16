import time
from ddgs import DDGS

def run_researcher(topic):
    print(f"🕵️‍♂️ Агент-ресерчер запущен. Тема: '{topic}'\n")
    print("Ищу информацию в сети...")
    
    try:
        # Используем DuckDuckGo для анонимного поиска без API-ключей
        results = DDGS().text(topic, max_results=5)
        
        print("\n=== РЕЗУЛЬТАТЫ ИССЛЕДОВАНИЯ ===")
        for i, res in enumerate(results, 1):
            print(f"\n{i}. {res.get('title')}")
            print(f"🔗 Ссылка: {res.get('href')}")
            print(f"📝 Описание: {res.get('body')}")
        print("\n===============================")
        
    except Exception as e:
        print(f"❌ Ошибка во время поиска: {e}")

if __name__ == "__main__":
    # Запускаем агента с тестовой темой (учитывая, что сейчас 2026 год)
    run_researcher("AI agents frameworks trends 2026")
    
    print("\nИсследование завершено. Агент переходит в фоновый режим ожидания...")
    
    # Бесконечный цикл, чтобы uagents8 не считал завершение скрипта ошибкой (Startup Failed)
    while True:
        time.sleep(60)