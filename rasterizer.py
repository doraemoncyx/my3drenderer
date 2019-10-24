# coding=gb18030
# by cyx at 2019/10/17 13:04

from PIL import Image
from typing import *
import common_class
import math
import traceback


def get_coord(v, size):
	return int((v + 1.0) / 2 * (size - 0.0001))


def line(v0: common_class.Vertex, v1: common_class.Vertex, image: common_class.RenderTarget, color: common_class.Color):
	size = image.data.shape
	x0, y0 = get_coord(v0.x, size[0]), get_coord(v0.y, size[1])
	x1, y1 = get_coord(v1.x, size[0]), get_coord(v1.y, size[1])
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
	d = image.data
	tmp = (y1 - y0) / (x1 - x0)
	for x in range(x0, x1, 1):
		y = int((x - x0) * tmp + y0 + 0.5)
		if dx < dy:  # has swapped xy
			x, y = y, x
		d[y, x] = t


def interpolate_by_uv(u, v, commonDiv, v0, v1, v2):
	return (u * v1 + v * v2 + (commonDiv - u - v) * v0) / commonDiv


def triangle(v0: common_class.Vertex, v1: common_class.Vertex, v2: common_class.Vertex,
             image: common_class.RenderTarget, color: common_class.Color,
             texture: Image.Image = None):
	# u * v01 +v * v02 = v0p
	size = image.data.shape
	x0, y0 = get_coord(v0.x, size[0]), get_coord(v0.y, size[1])
	x1, y1 = get_coord(v1.x, size[0]), get_coord(v1.y, size[1])
	x2, y2 = get_coord(v2.x, size[0]), get_coord(v2.y, size[1])
	commonDiv = ((x0 - x1) * (-y0 + y2) + (x0 - x2) * (y0 - y1))
	if commonDiv < 0:
		x1, y1, x2, y2 = x2, y2, x1, y1
		commonDiv = -commonDiv
	try:
		uc = ((x0 - x2) * (y0 - 0) + (x0 - 0) * (-y0 + y2))
		uy = (x2 - x0)
		ux = (y0 - y2)
		vc = (-(x0 - x1) * (y0 - 0) + (x0 - 0) * (y0 - y1))
		vx = (y1 - y0)
		vy = (x0 - x1)
		if commonDiv == 0:
			# TODO:  is a line
			return
	except ZeroDivisionError:  # do not form a triangle
		s = traceback.format_exc()
		return
	minx = min(x1, x2, x0)
	maxx = max(x1, x2, x0)
	miny = min(y1, y2, y0)
	maxy = max(y1, y2, y0)
	t = color.as_rgba_tuple()
	d = image.data
	if texture:
		tw, th = texture.size
	for px in range(minx, maxx + 1):
		for py in range(miny, maxy + 1):
			u = ux * px + uy * py + uc
			v = vx * px + vy * py + vc
			if v < 0 and vy < 0:
				break
			if v > commonDiv and vy > commonDiv:
				break
			if 0 <= u <= commonDiv and 0 <= v <= commonDiv and u + v <= commonDiv:
				curColor = t
				if texture:
					curTexU = interpolate_by_uv(u, v, commonDiv, v0.uv[0], v1.uv[0], v2.uv[0])
					curTexV = interpolate_by_uv(u, v, commonDiv, v0.uv[1], v1.uv[1], v2.uv[1])
					p = texture.getpixel((int(curTexU * tw), int((1-curTexV) * th)))
					curColor = p
				if image.zBuffer.size > 0:
					curZ = interpolate_by_uv(u, v, commonDiv, v0.z, v1.z, v2.z)
					if curZ > image.zBuffer[py, px]:
						image.zBuffer[py, px] = curZ
						d[py, px] = curColor
				else:
					d[py, px] = curColor

