from collections import namedtuple
from yeelight import discover_bulbs, Bulb 
from flask import Flask, render_template, redirect, url_for, request
from PIL import ImageColor
bulbs = discover_bulbs()
print(bulbs)
bulb = Bulb(bulbs[0]['ip'])
print(bulb) 
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        hex = request.form['color']
        r_color=ImageColor.getcolor(hex, "RGB")[0]
        g_color=ImageColor.getcolor(hex, "RGB")[1]
        b_color=ImageColor.getcolor(hex, "RGB")[2]
        print("HEX цвет:", hex)
        print("RGB цвет:",r_color,g_color,b_color)
        if r_color==0 and g_color==0 and b_color==0:
            r_color=1
            g_color=1
            b_color=1
            print("Кто-то решил поставить черный цвет :)")
        bulb.set_rgb(r_color,g_color,b_color)
        brightness = abs(int(request.form['brightness']))
        bulb.set_brightness(brightness) 
        print('Яркость:',brightness)
        if request.form.get('action1') == 'Вкл':
            pass
            print("Лампа включена")
            bulb.turn_on()
        elif  request.form.get('action2') == 'Выкл':
            pass 
            print("Лампа выключена")
            bulb.turn_off()
    return render_template('index.html', message=error)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')