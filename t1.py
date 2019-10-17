# coding=gb18030
# by cyx at 2019/10/17 13:01

from PIL import Image, ImageOps
import common_class
import rasterizer
import model
import random


def test1():  # draw wireframe
	m = Image.new('RGBA', (500, 500), (0, 0, 0, 255))
	mod = model.ObjParser()
	mod.open_obj_file('res/obj/african_head.obj')
	c = common_class.Color(1.0, 1.0, 0, 1.0)

	sx, sy = m.size

	def get_coord(v, size):
		return int((v + 1.0) / 2 * (size - 0.0001))

	for face in mod.faces:
		for idx in range(3):
			p0 = mod.vertexs[face[idx]]
			p1 = mod.vertexs[face[(idx + 1) % 3]]
			rasterizer.line(get_coord(p0.x, sx), get_coord(p0.y, sy), get_coord(p1.x, sx), get_coord(p1.y, sy), m, c)

	m = ImageOps.flip(m)
	m.save('out.png')


def test2():  # draw triangle
	m = Image.new('RGBA', (500, 500), (0, 0, 0, 255))
	mod = model.ObjParser()
	mod.open_obj_file('res/obj/african_head.obj')
	c = common_class.Color(1.0, 1.0, 0, 1.0)

	sx, sy = m.size

	def get_coord(v, size):
		return int((v + 1.0) / 2 * (size - 0.0001))

	for face in mod.faces:
		c = common_class.Color(random.random(), random.random(), random.random(), 1.0)
		for idx in range(3):
			p0 = mod.vertexs[face[0]]
			p1 = mod.vertexs[face[1]]
			p2 = mod.vertexs[face[2]]
			rasterizer.triangle(get_coord(p0.x, sx), get_coord(p0.y, sy), get_coord(p1.x, sx), get_coord(p1.y, sy), get_coord(p2.x, sx), get_coord(p2.y, sy), m, c)

	m = ImageOps.flip(m)
	m.save('out.png')


if __name__ == '__main__':
	test2()
