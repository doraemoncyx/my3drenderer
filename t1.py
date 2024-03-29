# coding=gb18030
# by cyx at 2019/10/17 13:01
from typing import Optional, Any

from PIL import Image, ImageOps
import common_class
import rasterizer
import model
import random
import numpy


def test1():  # draw wireframe
	rt = common_class.RenderTarget.from_w_h(500, 500, (0, 0, 0, 255))
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
	rt = common_class.RenderTarget.from_w_h(500, 500, (255, 0, 0, 255))
	mod = model.ObjParser()
	mod.open_obj_file('res/obj/african_head.obj')

	lightDir = common_class.Vector.from_size(3)
	lightDir.data[0] = 0.0
	lightDir.data[1] = 0
	lightDir.data[2] = -11
	lightDir.normalize()

	for idx, face in enumerate(mod.faces):
		p0 = mod.vertexs[face[0]]
		p1 = mod.vertexs[face[1]]
		p2 = mod.vertexs[face[2]]
		intensity = 1
		n = numpy.cross(p2.xyzw - p0.xyzw, p1.xyzw - p0.xyzw)
		n = n / numpy.linalg.norm(n)
		intensity = numpy.dot(lightDir.data, n)
		if intensity < 0:
			continue
		# intensity = ((idx*10)%256)/255.99
		c = common_class.Color(numpy.array([intensity, intensity, intensity, 1]))
		c.data[3] = 1
		rasterizer.triangle(p0, p1, p2, rt, c)

	m = ImageOps.flip(rt.as_image())
	m.save('out.png')


def test3():  # draw triangle with z buffer
	rt = common_class.RenderTarget.from_w_h(500, 500, (255, 0, 0, 255), withZBuffer=True)
	mod = model.ObjParser()
	mod.open_obj_file('res/obj/african_head.obj')

	lightDir = common_class.Vector.from_size(3)
	lightDir.data[0] = 0
	lightDir.data[1] = 0
	lightDir.data[2] = -1
	lightDir.normalize()

	tex: Image.Image = Image.open('res/texture/african_head_diffuse.tga')
	tex = tex.convert('RGBA')
	for idx, face in enumerate(mod.faces):
		p0 = mod.vertexs[face[0]]
		p1 = mod.vertexs[face[1]]
		p2 = mod.vertexs[face[2]]
		uvIdx = mod.facesTex[idx]
		p0.uv = mod.textureCoords[uvIdx[0]]
		p1.uv = mod.textureCoords[uvIdx[1]]
		p2.uv = mod.textureCoords[uvIdx[2]]
		n = numpy.cross(p2.xyzw - p0.xyzw, p1.xyzw - p0.xyzw)
		n = n / numpy.linalg.norm(n)
		intensity = numpy.dot(lightDir.data, n)
		if intensity < 0:
			continue
		# intensity = ((idx*10)%256)/255.99
		c = common_class.Color(numpy.array([intensity, intensity, intensity, 1]))
		c.data[3] = 1
		rasterizer.triangle(p0, p1, p2, rt, c, tex)

	m = ImageOps.flip(rt.as_image())
	m.save('out.png')

	z = rt.zBuffer
	z = z * 255.99 + 255.99
	z = z.astype(numpy.dtype('uint8'))
	m = ImageOps.flip(Image.fromarray(z))
	m.save('zbuffer.png')


def triangle_test():
	rt = common_class.RenderTarget.from_w_h(500, 500, (0, 0, 0, 255))
	c = common_class.Color(numpy.array([1, 1, 1, 1.0]))
	v0 = common_class.Vertex(numpy.array([0, 0, 0]))
	v1 = common_class.Vertex(numpy.array([0, 1, 0]))
	v2 = common_class.Vertex(numpy.array([0.05, 0, 0]))
	rasterizer.triangle(v0, v1, v2, rt, c)
	c = common_class.Color(numpy.array([0, 1, 1, 1.0]))
	v0 = common_class.Vertex(numpy.array([0.05, 1, 0]))
	v1 = common_class.Vertex(numpy.array([0, 1, 0]))
	v2 = common_class.Vertex(numpy.array([0.05, 0, 0]))
	rasterizer.triangle(v0, v1, v2, rt, c)
	m = ImageOps.flip(rt.as_image())
	m.save('out.png')


def line_test():
	import python_device
	d = python_device.PythonDevice()
	d.curRt = numpy.zeros((500, 500, 4), dtype=numpy.dtype('uint8'))
	d.indexBuf = numpy.array([0, 1])
	v0 = common_class.Vertex()
	v0.xyzw = numpy.array([-1, -1, 0, 0])
	v1 = common_class.Vertex()
	v1.xyzw = numpy.array([1, 1, 0, 0])
	d.vertexBuf = [v0, v1]
	d.vertexShader


if __name__ == '__main__':
	test3()
# triangle_test()
