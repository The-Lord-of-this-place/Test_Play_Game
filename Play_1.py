import numpy as np

def script_revolition(number: int = 1) -> int:
    """Сначала устанавливаем любое случайное число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. По умолчанию 1.

    Returns:
        int: Число попыток
    """
    count = 0  # Количество попыток
    min_num = 0  # Минимум диапазона
    max_num = 100  # Максимум диапазона

    while True:
        predict = np.random.randint(min_num, max_num) 
        count += 1
        
        if predict == number:
            break
        elif predict > number:
            max_num = predict
        elif predict < number:
            min_num = predict
            
    return f"Число попыток - {count},\nЗагаданное число {number}"
 
 # RUN
if __name__ == '__main__':
    number = np.random.randint(1, 101) # Рандомное значение задаваемое компьютером
    print(script_revolition(number))
    