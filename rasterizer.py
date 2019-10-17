# coding=gb18030
# by cyx at 2019/10/17 13:04

from PIL import Image
from typing import *
import common_class
import math


def line(x0: int, y0: int, x1: int, y1: int, image: Image.Image, color: common_class.Color):
	dx = abs(x0 - x1)
	dy = abs(y0 - y1)
	if dx < dy:
		x0, y0 = y0, x0
		x1, y1 = y1, x1
	if x0 > x1:
		x0, x1 = x1, x0
		y0, y1 = y1, y0
	t = color.as_rgba_tuple()
	tmp = (y1 - y0) / (x1 - x0)
	for x in range(x0, x1, 1):
		y = int((x - x0) * tmp + y0 + 0.5)
		if dx < dy:  # has swapped xy
			x, y = y, x
		image.putpixel((x, y), t)
