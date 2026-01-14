print("Привет. Сейчас мы с тобой сыграем в игру. Тебе нужно будет угадать число. У тебя есть на это 5 попыток.")
number = int(input("Угадай число от 1 до 10: "))
attempt = 1
max_attempts = 5
import random
secret = random.randint(1, 10)
while number != secret and attempt < max_attempts:
    if number > secret:
        print("Неправильно, попробуй еще раз. Твое число больше.")
        number = int(input("Угадай число от 1 до 10: "))
    elif number < secret:
        print("Неправильно, попробуй еще раз. Твое число меньше.")
        number = int(input("Угадай число от 1 до 10: "))
    attempt += 1
if number == secret:
    print("Правильно. Ты угадал за" , attempt , "попыток")
else:
    print("Ты проиграл.Колличество попыток окончено.Загаданное число было" , secret)
