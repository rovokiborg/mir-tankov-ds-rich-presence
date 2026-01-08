import time
import psutil
import os
from pypresence import Presence

CLIENT_ID = 'xxx'  
POSSIBLE_PROCESSES = ["tanki.exe", "worldoftanks.exe", "wot.exe"]
IMAGE_KEY = "tank" 

def get_active_process():
    for proc in psutil.process_iter(['name']):
        try:
            process_name = proc.info['name'].lower()
            if process_name in POSSIBLE_PROCESSES:
                return proc.info['name']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return None

def main():
  
    rpc = Presence(CLIENT_ID)
    is_connected = False
    start_time = None

    while True:
        current_process = get_active_process()

        if current_process:
            if not is_connected:
                try:
                    print(f"Найдена игра: {current_process}. Подключаюсь к Discord...")
                    rpc.connect()
                    is_connected = True
                    start_time = time.time()  
                    print("Успешно подключено!")
                except Exception as e:
                    print(f"Ошибка подключения к Discord: {e}")
                    time.sleep(10)
                    continue

            try:
                rpc.update(
                    state="На поле боя",
                    details="Играет в Мир Танков",
                    start=start_time,
                    large_image=IMAGE_KEY,
                    large_text="Мир Танков"
                )
            except Exception as e:
                print(f"Ошибка обновления статуса: {e}")
                is_connected = False
        else:
            if is_connected:
                print("Игра закрыта. Убираю статус...")
                try:
                    rpc.clear()
                    rpc.close()
                except:
                    pass
                is_connected = False
                start_time = None
                print("Ожидание запуска игры...")

        time.sleep(15)  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nСкрипт остановлен пользователем.")