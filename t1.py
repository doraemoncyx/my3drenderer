# coding=gb18030
# by cyx at 2019/10/17 13:01

from PIL import Image, ImageOps
import common_class
import rasterizer
import model
import random
import numpy


def test1():  # draw wireframe
	rt = common_class.RenderTarget.from_w_h(500, 500)
	mod = model.ObjParser()
	mod.open_obj_file('res/obj/african_head.obj')
	c = common_class.Color(numpy.array([0, 0, 1, 1.0]))

	sx, sy = rt.size

	for face in mod.faces:
		for idx in range(3):
			p0 = mod.vertexs[face[idx]]
			p1 = mod.vertexs[face[(idx + 1) % 3]]
			rasterizer.line(p0, p1, rt, c)

	m = ImageOps.flip(rt.as_image())
	m.save('out.png')


def test2():  # draw triangle
	rt = common_class.RenderTarget.from_w_h(500, 500)
	mod = model.ObjParser()
	mod.open_obj_file('res/obj/african_head.obj')

	lightDir = common_class.Vector.from_size(3)
	lightDir.data[0] = 0.0
	lightDir.data[1] = 0
	lightDir.data[2] = -11
	lightDir.normalize()
	for face in mod.faces:
		p0 = mod.vertexs[face[0]]
		p1 = mod.vertexs[face[1]]
		p2 = mod.vertexs[face[2]]
		intensity = 1
		n = numpy.cross(p2.xyzw - p0.xyzw, p1.xyzw - p0.xyzw)
		n = n / numpy.linalg.norm(n)
		intensity = numpy.dot(lightDir.data, n)
		if intensity < 0:
			continue
		c = common_class.Color(numpy.array([intensity, intensity, intensity, 1]))
		c.data[3] = 1
		rasterizer.triangle(p0, p1, p2, rt, c)

	m = ImageOps.flip(rt.as_image())
	m.save('out.png')


def triangle_test():
	rt = common_class.RenderTarget.from_w_h(500, 500)
	c = common_class.Color(numpy.array([0, 0, 1, 1.0]))
	v0 = common_class.Vertex(numpy.array([0, 0.05, 0]))
	v1 = common_class.Vertex(numpy.array([1, 0, 0]))
	v2 = common_class.Vertex(numpy.array([0, 0.1, 0]))
	rasterizer.triangle(v0, v1, v2, rt, c)
	m = ImageOps.flip(rt.as_image())
	m.save('out.png')


if __name__ == '__main__':
	test2()
