#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
from math import sin, cos, pi, radians
from lxml import etree
def MyTree_string(x,y,l,angle,n,angle2):
	if n==0:
		return ""
	angle2=angle2*0.5
	s=f"M {x} {y} L {x+l*cos(angle)} {y-l*sin(angle)} "
	s=s+MyTree_string(x+l*cos(angle), y-l*sin(angle), l*0.8, angle+angle2,n-1,angle2)
	s=s+f"M {x} {y} L {x+l*cos(angle)} {y-l*sin(angle)} "	
	s=s+MyTree_string(x+l*cos(angle), y-l*sin(angle), l*0.8, angle-angle2,n-1,angle2)
	s=s+f"M {x} {y} L {x+l*cos(angle)} {y-l*sin(angle)} "	
	s=s+MyTree_string(x+l*cos(angle), y-l*sin(angle), l*0.8, angle,n-1,angle2)
	return s

def draw_SVG_MyTree(x,y,l,angle,n,angle2):
	style = {'stroke': 'purple', 'stroke-width': '2', 'fill': 'none'}
	elem = inkex.PathElement()
	elem.update(**{
		'style': style,
		'inkscape:label': 'MyTree',
		'd': MyTree_string(x,y,l,angle,n,angle2)
		})
	return elem
class MyTree(inkex.EffectExtension):
	def add_arguments(self, pars):
		pars.add_argument("--c_x", type=float, default=10, help="x (px)")
		pars.add_argument("--c_y", type=float, default=40, help="y (px)")
		pars.add_argument("--s_l", type=int, default=50, help="Side Length")
		pars.add_argument("--angle", type=int, default=45, help="Угол отклонения")
		pars.add_argument("--n", type=int, default=1, help="Глубина рекурсии")
	def effect(self):
		cur = self.svg.get_current_layer()
		x = self.svg.unittouu(str(self.options.c_x) + 'px')
		y = self.svg.unittouu(str(self.options.c_y) + 'px')
		l = self.options.s_l
		angle = self.options.angle
		n = self.options.n
		cur.add(draw_SVG_MyTree(x,y,l,pi/2,n+1,radians(angle*2)))
 
if __name__ == '__main__':
    MyTree().run()
