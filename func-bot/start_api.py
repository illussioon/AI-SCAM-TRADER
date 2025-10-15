import asyncio
import threading
import uvicorn
import sys
import os


def start_api_server():
    """Запуск API сервера в отдельном потоке"""
    
    # Добавляем путь к API серверу
    api_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "api-server")
    sys.path.append(api_path)
    
    try:
        # Импортируем приложение FastAPI
        from main import app
        
        # Запускаем сервер
        uvicorn.run(
            app, 
            host="127.0.0.1", 
            port=8000, 
            log_level="info"
        )
        
    except Exception as e:
        print(f"Ошибка запуска API сервера: {e}")


def start_api_in_thread():
    """Запуск API сервера в отдельном потоке (для совместной работы с ботом)"""
    
    def run_server():
        # Полный путь к API серверу
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        api_path = os.path.join(project_root, "api-server")
        
        print(f"📁 Путь к API серверу: {api_path}")
        
        # Проверяем существование директории
        if not os.path.exists(api_path):
            print(f"❌ Директория API сервера не найдена: {api_path}")
            return
            
        # Проверяем main.py
        main_py_path = os.path.join(api_path, "main.py")
        if not os.path.exists(main_py_path):
            print(f"❌ Файл main.py не найден: {main_py_path}")
            return
            
        # Добавляем путь в sys.path
        if api_path not in sys.path:
            sys.path.insert(0, api_path)
        
        print(f"📝 Пути в sys.path: {sys.path[:3]}...")
        
        try:
            # Меняем рабочую директорию на API сервер
            old_cwd = os.getcwd()
            os.chdir(api_path)
            print(f"📂 Изменена рабочая директория на: {os.getcwd()}")
            
            # Импортируем приложение
            from main import app
            print("✅ Приложение FastAPI успешно импортировано")
            
            # Запускаем сервер
            print("🚀 Запуск uvicorn сервера...")
            uvicorn.run(
                app, 
                host="0.0.0.0",  # Слушаем на всех интерфейсах
                port=8000, 
                log_level="info",
                access_log=True
            )
            
        except ImportError as e:
            print(f"❌ Ошибка импорта: {e}")
        except Exception as e:
            print(f"❌ Ошибка API сервера: {e}")
        finally:
            # Восстанавливаем рабочую директорию
            try:
                os.chdir(old_cwd)
            except:
                pass
    
    # Создаем и запускаем поток
    api_thread = threading.Thread(target=run_server, daemon=True)
    api_thread.start()
    print("🌐 API сервер запущен на http://127.0.0.1:8000")
    
    return api_thread


if __name__ == "__main__":
    print("🚀 Запуск API сервера...")
    start_api_server()
