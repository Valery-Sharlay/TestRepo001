def decor1(f): #создаем простой декоратор
    def wrapper():
        print('Дополнение 1')
        f()
        print('Дополнение 2')
    return wrapper

@decor1
def sayHi(): print('Hi')

sayHi()