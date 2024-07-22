#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
import math
from lxml import etree
def draw_MyKantor(l, x, y, n):
	sub_grp = inkex.Group()
	if n>1:
		sub_grp.add(draw_MyKantor(l//2, x-l//2, y-l//2, n-1))
		sub_grp.add(draw_MyKantor(l//2, x+l//2, y-l//2, n-1))
		sub_grp.add(draw_MyKantor(l//2, x-l//2, y+l//2, n-1))
		sub_grp.add(draw_MyKantor(l//2, x+l//2, y+l//2, n-1))
	style = {'stroke':'black', 'stroke-width': '1', 'fill' : 'white' }
	elem = inkex.Rectangle()
	elem.update(**{
		'style': style,
		'inkscape:label': 'MyKantor',
		'x': str(x - l//2),
		'y': str(y - l//2),
		'width': str(l),
		'height': str(l) })
	sub_grp.add(elem)
	return sub_grp
class MyKantor(inkex.EffectExtension):
	def add_arguments(self, pars):
		pars.add_argument("--s_l", type=int, default=100.0, help="Side Length")
		pars.add_argument("--c_x", type=float, default=10.0, help="x(px)")
		pars.add_argument("--c_y", type=float, default=40.0, help="y(px)")
		pars.add_argument("--n", type=int, default=4, help="Глубина рекурсии")
	def effect(self):
		cur = self.svg.get_current_layer()
		a = self.svg.unittouu(str(self.options.s_l) + 'px')
		x = self.svg.unittouu(str(self.options.c_x) + 'px')
		y = self.svg.unittouu(str(self.options.c_y) + 'px')
		n = self.options.n
		cur.add(draw_MyKantor(a,x,y,n))
if __name__ == '__main__':
		MyKantor().run()
