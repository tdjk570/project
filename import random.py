import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Твой вариант: "))
            attempts += 1
            
            if guess < secret_number:
                print("Слишком мало! Попробуй еще раз.")
            elif guess > secret_number:
                print("Слишком много! Попробуй еще раз.")
            else:
                print(f"Поздравляю! Ты угадал число за {attempts} попыток!")
                break
        except ValueError:
            print("Пожалуйста, вводи только числа!")

    print("Спасибо за игру!")

# Запуск игры
guess_the_number()