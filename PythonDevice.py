# coding=gb18030
# by cyx at 2019/10/24 20:

import attr
import numpy
import common_class
from typing import *


@attr.s
class PythonDevice(object):
	curRt = attr.ib(default=numpy.zeros(1))
	indexBuf = attr.ib(default=[])
	vertexBuf: List[common_class.Vertex] = attr.ib(default=[])
	vertexShader = attr.ib(default=lambda: None)
	pixelShader = attr.ib(default=lambda: None)

	def draw_line(self):
		curIdx = 0
		while curIdx < len(self.indexBuf):
			point0 = self.vertexBuf[curIdx]
			point1 = self.vertexBuf[curIdx+1]
			curIdx += 2
