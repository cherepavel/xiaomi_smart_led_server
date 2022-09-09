# xiaomi_smart_led_server readme
Веб-сервер для управления умной лампочкой xiaomi

# Как пользоваться 
1. Добавляем умную лампочку на наш xiaomi аккаунт через официальное приложение Mi Home
2. Удаляем его
3. Ставим модифицированное приложение mi home vens. В нем узнаем токен и блокируем обновление умных устройств (по желанию)
4. Устанавливаем python3 и делаем pip install miiocli-python
5. Вводим miiocli yeelight --ip "ip лампочки" --token "токен из пункта 3" status и получаем что-то типа:
Name:
Update default on change: True
Delay in minute before off: 0
   Power: True
   Brightness: 100
   Color mode: ColorTemperature
   Temperature: 4000
   Color flowing mode: False
6. Пробуем активировать режим разработчика miiocli yeelight --ip "ip лампочки" --token "токен из пункта 3" set_developer_mode 1
7. Если появилась надпись ['ok'], то запускаем led_control.py
8. Если не запустилась, ставим зависимости Pillow, flask и yeelight
9. Переходим по ссылке ipкомпьютеранакоторомзапущенвебсервер:5000 и управляем лампочкой
# GIF
![test](https://user-images.githubusercontent.com/24592649/148617416-9396ef82-8cee-40ff-a5a3-8c26112ece27.gif)
