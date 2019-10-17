# coding=gb18030
# by cyx at 2019/10/17 13:05

import attr


@attr.s
class Color(object):
	r = attr.ib(default=0.0)
	g = attr.ib(default=0.0)
	b = attr.ib(default=0.0)
	a = attr.ib(default=0.0)
	maxColor = 255.999999

	def as_rgba_tuple(self):
		return (int(self.r * self.maxColor), int(self.g * self.maxColor), int(self.b * self.maxColor), int(self.a * self.maxColor),)


@attr.s
class Float4D(object):
	x = attr.ib(default=0.0)
	y = attr.ib(default=0.0)
	z = attr.ib(default=0.0)
	w = attr.ib(default=0.0)

	def as_int(self):
		self.x = int(self.x)
		self.y = int(self.y)
		self.z = int(self.z)
		self.w = int(self.w)
