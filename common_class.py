# coding=gb18030
# by cyx at 2019/10/17 13:05

import attr
from typing import *
import numpy
from PIL import Image


@attr.s
class RenderTarget(object):
	w = attr.ib(default=0)
	h = attr.ib(default=0)
	data = attr.ib(factory=lambda: numpy.array([]))
	zBuffer = attr.ib(factory=lambda: numpy.array([]))

	@classmethod
	def from_w_h(cls, w, h, color, withZBuffer=False):
		assert len(color) == 4
		c = cls(w, h)
		d = numpy.tile(numpy.array(color, dtype=numpy.dtype('uint8')), w * h)
		d.resize(h, w, 4)
		c.data = d
		if withZBuffer:
			c.zBuffer = numpy.ones((h, w), dtype=float) * -999999
		return c

	def as_image(self) -> Image.Image:
		m = Image.fromarray(self.data)
		return m

	@property
	def size(self):
		return self.w, self.h


@attr.s
class Color(object):
	data = attr.ib(factory=lambda: numpy.array([]))
	maxColor = 255.999999

	def as_rgba_tuple(self):
		tmp = self.data * self.maxColor
		tmp = tmp.astype(numpy.dtype('uint8'))
		return tuple(tmp.tolist())

	@property
	def r(self):
		return self.data[0]

	@property
	def g(self):
		return self.data[1]

	@property
	def b(self):
		return self.data[2]

	@property
	def a(self):
		return self.data[3]


@attr.s
class Vector(object):
	data = attr.ib(factory=lambda: numpy.array([]))
	length = attr.ib(default=0)
	@classmethod
	def from_size(cls, w):
		c = cls()
		c.length = w
		c.data = numpy.zeros(w, dtype=float)
		return c

	def normalize(self):
		n = numpy.linalg.norm(self.data)
		if n > 0:
			self.data = self.data / n


@attr.s
class Vertex(object):
	xyzw = attr.ib(factory=lambda: numpy.array([]))
	uv = attr.ib(default=[])

	@property
	def x(self):
		return self.xyzw[0]

	@property
	def y(self):
		return self.xyzw[1]

	@property
	def z(self):
		return self.xyzw[2]
