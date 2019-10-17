# coding=gb18030
# by cyx at 2019/10/17 19:25
import attr
import common_class
from typing import *


@attr.s(auto_attribs=True)
class ObjParser(object):
	vertexs: List[common_class.Float4D] = attr.Factory(list)
	faces: List[List[int]] = attr.Factory(list)

	def open_obj_file(self, filename):
		self.vertexs.clear()
		self.faces.clear()
		with open(filename) as f:
			for line in f:
				if line.startswith('v '):
					items = line.split(' ')
					self.vertexs.append(common_class.Float4D(float(items[1]), float(items[2]), float(items[3]), ))
				elif line.startswith('f '):
					tri = []
					items = line.split(' ')
					for item in items[1:]:
						nums = item.split('/')
						tri.append(int(nums[0]) - 1)
					self.faces.append(tri)
		i = 1
