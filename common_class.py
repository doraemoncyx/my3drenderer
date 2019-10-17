# coding=gb18030
# by cyx at 2019/10/17 13:05

import attr
from typing import *


@attr.s
class Color(object):
	r = attr.ib(default=0.0)
	g = attr.ib(default=0.0)
	b = attr.ib(default=0.0)
	a = attr.ib(default=0.0)
	maxColor = 255.999999
	
	def as_rgba_tuple(self):
		return (int(self.r * self.maxColor), int(self.g * self.maxColor), int(self.b * self.maxColor),
		        int(self.a * self.maxColor),)


@attr.s
class Float3D(object):
	x = attr.ib(default=0.0)
	y = attr.ib(default=0.0)
	z = attr.ib(default=0.0)
	
	def crossproduct(self, other):
		"""

		:type other: Float3D
		"""
		a1, a2, a3 = self.x, self.y, self.z
		b1, b2, b3 = other.x, other.y, other.z
		return Float3D(a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1)
	
	def normalize(self):
		s = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5;
		self.x /= s
		self.y /= s
		self.z /= s
		return self
	
	def __sub__(self, other):
		"""

		:type other: Float3D
		"""
		return Float3D(self.x - other.x, self.y - other.y, self.z - other.z)
	
	def __mul__(self, other):
		"""

		:type other: Float3D
		:rtype: float
		"""
		return sum((self.x * other.x, self.y * other.y, self.z * other.z))


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
	
	def __sub__(self, other):
		"""

		:type other: Float4D
		"""
		return Float4D(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
	
	def as_float3d(self) -> Float3D:
		return Float3D(self.x, self.y, self.z)
