import time
from datetime import datetime


def bot_logger(filepath):
    """Декоратор для логирования работы бота"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                result = func(*args, **kwargs)
                exec_time = time.time() - start_time

                log_entry = (
                    f"[{timestamp}] {func.__name__} - УСПЕХ\n"
                    f"Аргументы: args={args[:2]}..., kwargs={kwargs}\n"
                    f"Время выполнения: {exec_time:.4f} сек\n"
                    f"{'-' * 50}\n"
                )

                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(log_entry)

                return result

            except Exception as e:
                error_entry = (
                    f"[{timestamp}] {func.__name__} - ОШИБКА\n"
                    f"Аргументы: args={args[:2]}..., kwargs={kwargs}\n"
                    f"Тип ошибки: {type(e).__name__}\n"
                    f"Сообщение: {str(e)}\n"
                    f"{'-' * 50}\n"
                )

                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(error_entry)

                raise

        return wrapper

    return decorator

