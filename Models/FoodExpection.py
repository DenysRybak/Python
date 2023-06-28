import logging

class FoodUnavailableException(Exception):
    pass

class NotEnoughFoodException(Exception):
    pass
# визначення декоратора logged для обробки виключень
def logged(exception, mode):
    def decorator(func):  # повернення обгортки
        def wrapper(*args, **kwargs): # визначення wrapper() та обробляє обгортку func
            try:
                return func(*args, **kwargs)
            except exception as e:  # перехоплення якщо є викляючення і присвоєння е
                logging.basicConfig(level=logging.ERROR, filename='log.txt', format='%(asctime)s - %(levelname)s - %(message)s')
                if mode == 'console':
                    logging.error(f'Exception occurred: {e}', exc_info=True)
                elif mode == 'file':
                    logging.error(f'Exception occurred: {e}')
                else:
                    logging.error(f'Invalid mode: {mode}')
                raise e
        return wrapper
    return decorator