import threading
import time


class MapGenerator:
    def __init__(self):
        self.generator_thread = None
        self.running = False
        self.current_map_state = []

    def generate_map(self):
        """Эта функция отвечает за генерацию карты каждую секунду."""
        while self.running:
            # Генерация карты и обновление current_map_state
            cur_time = time.time()
            self.current_map_state.append(self.create_new_map_state())
            print(f"Генерация карты: {self.current_map_state}")
            time.sleep(1 - time.time()+cur_time)

    def create_new_map_state(self):
        """Функция, которая симулирует создание нового состояния карты."""
        # Здесь можно добавить логику генерации карты
        return {"time": time.time()}  # Пример карты с текущим временем

    def start_generator(self):
        """Запуск генератора, если он ещё не запущен."""
        if self.generator_thread is None or not self.running:
            print("Запуск генератора...")
            self.running = True
            self.generator_thread = threading.Thread(target=self.generate_map)
            self.generator_thread.start()
        else:
            print("Генератор уже запущен.")

    def stop_generator(self):
        """Остановка генератора, сохраняя текущее состояние."""
        if self.running:
            print("Остановка генератора...")
            self.running = False
            self.generator_thread.join()
            self.generator_thread = None
        else:
            print("Генератор уже остановлен.")

    def restart_generator(self):
        """Перезапуск генератора с созданием новой карты."""
        print("Перезапуск генератора...")
        self.stop_generator()
        # Логика для создания нового файла карты
        self.current_map_state = {}  # Обновляем карту
        print("Создан новый файл карты.")
        self.start_generator()


# Пример использования
if __name__ == "__main__":
    generator = MapGenerator()

    # Запуск генератора
    generator.start_generator()

    # Ожидание 5 секунд
    time.sleep(5)

    # Остановка генератора
    generator.stop_generator()

    # Перезапуск генератора
    generator.restart_generator()

    # Ожидание 5 секунд
    time.sleep(5)

    # Остановка генератора
    generator.stop_generator()
