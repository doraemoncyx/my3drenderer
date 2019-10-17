# coding=gb18030
# by cyx at 2019/10/17 13:01

from PIL import Image
import common_class
import rasterizer

m = Image.new('RGBA', (500, 500), (0, 0, 0, 255))
c = common_class.Color(1.0, 1.0, 0, 1.0)
rasterizer.line(0, 0, 2, 300, m, c)
m.save('out.png')
