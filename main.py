2.1
a=input("Введите пароль:")
if len(a)<8:
    print("Слишком короткий пароль")
else:
    print("Пароль принят")
2.2
a=input("Введите статус сервера(online or offline):")
if a=="online":
    print("Связь установлена")
else:
    print("Связь потеряна")
2.3
a=int(input("Введите уровень угрозы(от 1 до 100):"))
if 1<=a<=30:
    print("Низкий уровень угрозы")
elif 31<=a<=70:
    print("Средний уровень угрозы")
elif 71<=a<=100:
    print("Критический уровень угрозы")
else:
    print("Ошибка ввода")
2.4
checksum_original=int(input("Введите оригинальный контрольный чек:"))
checksum_current=int(input("Введите текущий контрольный чек:"))
status="Файл не изменён" if checksum_original==checksum_current else "Файл повреждён"
print(status)
2.5
event_code=input("Введите событие(ERR,WRN,INF):")
match event_code:
    case "ERR":
        print("Ошибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Неизвестный код события")