from drawtool import DrawTool
import math

dt = DrawTool()
dt.set_XY_range(0,120, 0,20000)

x = 8.33
f = 1666.67
dt.draw_point (x, f)

x = 22.22
f = 3666.67
dt.draw_point (x, f)

x = 23.61
f = 4833.33
dt.draw_point (x, f)

x = 30.55
f = 5000
dt.draw_point (x, f)

x = 36.81
f = 5166.67
dt.draw_point (x, f)

x = 47.22
f = 8000
dt.draw_point (x, f)

x = 69.44
f = 11333.33
dt.draw_point (x, f)

x = 105.56
f = 19666.67
dt.draw_point (x, f)

dt.display()