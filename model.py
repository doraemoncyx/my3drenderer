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
	
	def open_obj_file(self, filename):
		self.vertexs.clear()
		self.faces.clear()
		with open(filename) as f:
			for line in f:
				if line.startswith('v '):
					items = line.split(' ')
					tmp = common_class.Vertex()
					tmp.xyzw = numpy.zeros(4, dtype=float)
					d = tmp.xyzw
					d[0] = items[1]
					d[1] = items[2]
					d[2] = items[3]
					self.vertexs.append(tmp)
				elif line.startswith('f '):
					tri = []
					items = line.split(' ')
					for item in items[1:]:
						nums = item.split('/')
						tri.append(int(nums[0]) - 1)
					self.faces.append(tri)
		i = 1
