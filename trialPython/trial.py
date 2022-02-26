

print("Sign_up")

username = input("Введите свой ник: ")

name = input("Введите свой имя: ")
surname = input("Введите свой фамиля: ")

while True:
    gmail = input("Введите свой gmail: ")
    if gmail[-10:] != "@gmail.com":
        print("Почта должна содержать @gmail.com")
    else:
        break

phone = input("Введите свой номер: ")

while True:
    age = 2022 - int(input("Введите свой год рождение: "))
    if age < 8:
        print("Щегол иди спать!! ")
    else:
        break


while True:
    password = input("Введите свой пароль: ")
    password2 = input("Повторить свой пароль: ")
    if password != password2:
        print("ЭЭЭ нормально пиши !!!!! ")
    else:
        break

user = dict(
    username=username,
    name=name,
    surname=surname,
    gmail=gmail,
    age=age,
    phone=phone,
    password=password,
)

for key , values in user.items():
    print(f"{key}: {values}")


while True:
    username = input("Введите свой ник: ")
    password = input("Повторить свой пароль: ")
    if username != user["username"] or password != user["password"]:
        print("Неверный логин или пароль !!! ")
    else:
        print("Успешная Авторизация <3")
        break







