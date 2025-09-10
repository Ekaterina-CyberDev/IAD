def read_number():
    while True:
        num = input("Введите 10-значное число: ")
        if len(num) == 10 and num.isdigit(): return num
        print("Ошибка! 10 цифр!")

def gcd_eight(num):
    last_digit = num[-1]
    if last_digit in '13579': return '1'
    
    last_three = int(num[-3:])
    if last_three % 8 == 0: return '8'
    
    last_two = int(num[-2:])
    return '4' if last_two % 4 == 0 else '2'

number = read_number()
print(f"НОД(8, {number}) = {gcd_eight(number)}")