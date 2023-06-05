import logging

class FoodUnavailableException(Exception):
    pass

class NotEnoughFoodException(Exception):
    pass

def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
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