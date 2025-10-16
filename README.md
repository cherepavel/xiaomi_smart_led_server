# xiaomi_smart_led_server

Веб-сервер для управления умной лампочкой Xiaomi.

---

## Как пользоваться

1.  Через официальное приложение Mi Home добавьте умное устройство.

2. Удалите официальное Mi Home

3. Установите модифицированное приложение [Mi Home от vevs](https://www.vevs.me/2017/11/mi-home.html)

   * В приложении получите **токен устройства**.
   * (По желанию) заблокируйте обновление умных устройств.

4. Установите Python и зависимости

   ```bash
   pip install -r requirements.txt
   ```

5. Проверьте подключение к лампочке
   Выполните команду:

   ```bash
   miiocli yeelight --ip "IP_лампочки" --token "ТОКЕН" status
   ```

   Вы должны получить примерно такой вывод:

   ```
   Name:
   Update default on change: True
   Delay in minute before off: 0
      Power: True
      Brightness: 100
      Color mode: ColorTemperature
      Temperature: 4000
      Color flowing mode: False
   ```

6. Активируйте режим разработчика

   ```bash
   miiocli yeelight --ip "IP_лампочки" --token "ТОКЕН" set_developer_mode 1
   ```

   Если появится `['ok']`, значит режим успешно включен.

7. Запустите сервер управления

   ```bash
   python3 led_control.py
   ```

8. Управление лампочкой через веб-интерфейс
   Перейдите в браузере по адресу:

   ```
   http://IP_компьютера:5000
   ```

---

## Демонстрация

![test](https://user-images.githubusercontent.com/24592649/148617416-9396ef82-8cee-40ff-a5a3-8c26112ece27.gif)

