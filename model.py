# coding=gb18030
# by cyx at 2019/10/17 19:25
import attr
import common_class
from typing import *
import numpy


@attr.s(auto_attribs=True)
class ObjParser(object):
	vertexs: List[common_class.Vertex] = attr.Factory(list)
	faces: List[List[int]] = attr.Factory(list)
	facesTex: List[List[int]] = attr.Factory(list)
	textureCoords: List = attr.ib(default=[])

	def open_obj_file(self, filename):
		self.vertexs.clear()
		self.faces.clear()
		with open(filename) as f:
			for line in f:
				if line.startswith('v '):
					items = line.split(' ')
					tmp = common_class.Vertex()
					tmp.xyzw = numpy.zeros(3, dtype=float)
					d = tmp.xyzw
					d[0] = items[1]
					d[1] = items[2]
					d[2] = items[3]
					self.vertexs.append(tmp)
				elif line.startswith('f '):
					tri = []
					texIdx = []
					items = line.split(' ')
					for item in items[1:]:
						nums = item.split('/')
						tri.append(int(nums[0]) - 1)
						texIdx.append(int(nums[1]) - 1)
					self.faces.append(tri)
					self.facesTex.append(texIdx)
				elif line.startswith('vt '):
					items = line.split(' ')
					d = items[2:4]

					d = [float(c) for c in d]
					self.textureCoords.append(d)
		i = 1
