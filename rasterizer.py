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
	if x0 == x1:
		return
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


def triangle(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, image: Image.Image, color: common_class.Color):
	minx = min(x1, x2, x3)
	maxx = max(x1, x2, x3)
	miny = min(y1, y2, y3)
	maxy = max(y1, y2, y3)
	t = color.as_rgba_tuple()
	clockOrder = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) > 0
	if not clockOrder:
		x2, y2, x3, y3 = x3, y3, x2, y2
	for px in range(minx, maxx + 1):
		s1 = (px - x1) * (y2 - y1) - (miny - y1) * (x2 - x1)
		d1 = x2 - x1
		s2 = (px - x2) * (y3 - y2) - (miny - y2) * (x3 - x2)
		d2 = x3 - x2
		s3 = (px - x3) * (y1 - y3) - (miny - y3) * (x1 - x3)
		d3 = x1 - x3
		# if y2 < y1 or (y2 == y1 and x2 < x1):
		# 	s1 += 1
		# if y3 < y2 or (y3 == y2 and x3 < x2):
		# 	s2 += 1
		# if y1 < y3 or (y1 == y3 and x1 < x3):
		# 	s3 += 1
		for py in range(miny, maxy + 1):
			if s1 >= 0 and s2 >= 0 and s3 >= 0:
				image.putpixel((px, py), t)
			s1 -= d1
			s2 -= d2
			s3 -= d3
