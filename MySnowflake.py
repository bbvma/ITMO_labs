#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
from math import sin, cos, pi
from lxml import etree
def MySnow_string(x,y,l,n):
	if n==0:
		return ""

	s=f"M {x} {y} L {x+l*cos(pi/3)} {y+l*sin(pi/3)} "
	s=s+MySnow_string(x+l*cos(pi/3), y+l*sin(pi/3), l*0.3,n-1)
	s=s+f"M {x} {y} L {x+l*cos(2*pi/3)} {y+l*sin(2*pi/3)} "
	s=s+MySnow_string(x+l*cos(2*pi/3), y+l*sin(2*pi/3), l*0.3,n-1)
	s=s+f"M {x} {y} L {x+l*cos(4*pi/3)} {y+l*sin(4*pi/3)} "
	s=s+MySnow_string(x+l*cos(4*pi/3), y+l*sin(4*pi/3), l*0.3,n-1)
	s=s+f"M {x} {y} L {x+l*cos(5*pi/3)} {y+l*sin(5*pi/3)} "
	s=s+MySnow_string(x+l*cos(5*pi/3), y+l*sin(5*pi/3), l*0.3,n-1)
	s=s+f"M {x} {y} L {x+l*cos(0)} {y+l*sin(0)} "
	s=s+MySnow_string(x+l*cos(0), y+l*sin(0), l*0.3,n-1)
	s=s+f"M {x} {y} L {x+l*cos(pi)} {y+l*sin(pi)} "
	s=s+MySnow_string(x+l*cos(pi), y+l*sin(pi), l*0.3,n-1)
	return s

def draw_SVG_MySnow(x,y,l,n):
	style = {'stroke': 'blue', 'stroke-width': '2', 'fill': 'none'}
	elem = inkex.PathElement()
	elem.update(**{
		'style': style,
		'inkscape:label': 'MySnow',
		'd': MySnow_string(x,y,l,n)
		})
	return elem
class MySnow(inkex.EffectExtension):
	def add_arguments(self, pars):
		pars.add_argument("--s_l", type=int, default=100.0, help="Side Length")
		pars.add_argument("--c_x", type=float, default=10, help="x (px)")
		pars.add_argument("--c_y", type=float, default=40, help="y (px)")
		pars.add_argument("--n", type=int, default=0, help="Глубина рекурсии")
	def effect(self):
		cur = self.svg.get_current_layer()
		l = self.options.s_l
		x = self.svg.unittouu(str(self.options.c_x) + 'px')
		y = self.svg.unittouu(str(self.options.c_y) + 'px')
		n = self.options.n
		cur.add(draw_SVG_MySnow(x,y,l,n))
 
if __name__ == '__main__':
    MySnow().run()
