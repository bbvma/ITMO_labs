#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
from lxml import etree
from math import sqrt

def MyKoha(x,y,l):
 s='M'+str(x)+','+str(y-l)+'L'+str(x+l/sqrt(12))+','+str(y-l/2)+'L'+str(x+l*sqrt(3)/2)+','+str(y-l/2)+'L'+str(x+l*sqrt(3)/3)+','+str(y)+'L'+str(x+l*sqrt(3)/2)+','+str(y+l/2)+'L'+str(x+l/sqrt(12))+','+str(y+l/2)+'L'+str(x)+','+str(y+l)+'L'+str(x-l/sqrt(12))+','+str(y+l/2)+'L'+str(x-l*sqrt(3)/2)+','+str(y+l/2)+'L'+str(x-l*sqrt(3)/3)+','+str(y)+'L'+str(x-l*sqrt(3)/2)+','+str(y-l/2)+'L'+str(x-l/sqrt(12))+','+str(y-l/2)+'z'
 if (l>10):
  s=s+MyKoha(x,y-l*2/3,l/3)
  s=s+MyKoha(x+l*sqrt(3)/3,y-l/3,l/3)
  s=s+MyKoha(x+l*sqrt(3)/3,y+l/3,l/3)
  s=s+MyKoha(x,y+l*2/3,l/3)
  s=s+MyKoha(x-l*sqrt(3)/3,y+l/3,l/3)
  s=s+MyKoha(x-l*sqrt(3)/3,y-l/3,l/3)
 return s

def draw_SVG_MyKoha(x,y,l,cur):
    style = {'stroke': 'black', 'stroke-width': '0.5', 'fill': 'black'}
    elem = cur.add(inkex.PathElement())
    elem.update(**{
        'style': style,
        'inkscape:label': 'MyKOHA',
        'd': MyKoha(x,y,l)})
    return elem

class MyKOHA(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--s_l", type=int, default=100, help="Side Length")
        pars.add_argument("--c_x", type=float, default=10, help="x (px)")
        pars.add_argument("--c_y", type=float, default=40, help="y (px)")
    def effect(self):
        cur = self.svg.get_current_layer()
        x = self.svg.unittouu(str(self.options.c_x) + 'px')
        y = self.svg.unittouu(str(self.options.c_y) + 'px')
        l = self.svg.unittouu(str(self.options.s_l) + 'px')
        draw_SVG_MyKoha(x,y,l,cur)
if __name__ == '__main__':
    MyKOHA().run()