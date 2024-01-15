
import simple_draw as sd


sd.resolution = (1200, 720)
point_0 = sd.get_point(100, 500)

x = 250
y = 500

x2 = 300
y2 = 350

while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=50)
    y -= 10
    if y < 50:
        break
    x = x * 1.1

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=50)
    y2 -= 15
    if y2 < 50:
        break
    x2 = x2 * 1.1



    sd.sleep(0.1)
    if sd.user_want_exit():
        break






sd.pause()