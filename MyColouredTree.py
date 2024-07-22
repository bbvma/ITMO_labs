#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
from lxml import etree
import math 
import random
from inkex import Circle

def draw_SVG_tree(x,y,l,a,a0,n):
    result = inkex.Group()
    wood0 = inkex.PathElement()
    style = {'stroke': '#39352a', 'stroke-width': str(l*0.15)}
    wood0.update(**{
        'style': style,
        'inkscape:label': 'MyTree',
        'd': 'M' +str(x) + ',' + str(y) + 'L' + str(x)+','+str(y+l)})
    
    result.add(wood0)
    result.add(tree(x,y,l,a,a0))
    return result
def tree(x,y,l,a,a0):
    res = inkex.Group()
    a1 = a0 + a/random.randint(2,4) 
    a2 = a0 - a/random.randint(2,3)
    x1 = x + l*math.cos(a1)
    y1 = y - l*math.sin(a1)
    x2 = x + l*math.cos(a2)
    y2 = y - l*math.sin(a2)
    x3 = x 
    y3 = y - l 
    if(l > 2):
        if(random.randint(0,100) > 15):
            res.add(tree(x1,y1,l*random.randint(2,3)/4,a,a1))
        if(random.randint(0,100) > 15):
            res.add(tree(x2,y2,l*random.randint(2,3)/4,a,a2))
        if(random.randint(0,100) > 15):
            res.add(tree(x3,y3,l*random.randint(2,3)/4,a,a0)) 
        style_1 = {'stroke': '#39352a', 'stroke-width': str(l*0.1)}
        
        wood = inkex.PathElement()
        wood.update(**{
            'style':style_1,
            'inkscape:label': 'MyTree',
            'd':'M'+str(x)+','+str(y)+'L'+str(x1)+','+str(y1)+'M'+str(x)+','+str(y)+'L'+str(x2)+','+str(y2)+'M'+str(x)+','+str(y)+'L'+str(x3)+','+str(y3)})
        
        
        list1 = inkex.Circle()
        list1.update(**{
            'style': {'fill': '#6dae81', 'stroke': 'none','stroke-width': 0.47, 'stroke': '#027500'},
            'cx': x3, 'cy': y3, 'r': l*0.27})
            
        list2 = inkex.Circle()
        list2.update(**{
            'style': {'fill': '#4f7942', 'stroke': 'none','stroke-width': 0.47, 'stroke': '#027500'},
            'cx': x2, 'cy': y2, 'r': l*0.34})
            
        list3 = inkex.Circle()
        list3.update(**{
            'style': {'fill': '#21421e', 'stroke': 'none','stroke-width': 0.47, 'stroke': '#027500'},
            'cx': x1, 'cy': y1, 'r': l*0.51})
        
        
        
        res.add(wood)
        res.add(list1)
        res.add(list2)
        res.add(list3)
        
    return res
class MyTree(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--s_l", type=float, default=100.0, help="Side Length")
        pars.add_argument("--c_x", type=float, default=0.0, help="X coord.")
        pars.add_argument("--c_y", type=float, default=0.0, help="Y coord.")
        pars.add_argument("--a", type=int, default=1, help="Angle")
        pars.add_argument("--n", type=int, default=3, help="Рекурсия")
    def effect(self):
        cur = self.svg.get_current_layer()
        l = self.svg.unittouu(str(self.options.s_l) + 'px')
        x = self.svg.unittouu(str(self.options.c_x) + 'px')
        y = self.svg.unittouu(str(self.options.c_y) + 'px')
        a = self.options.a
        n = self.options.n
        if (n>1):
            cur.add(draw_SVG_tree(x,y,l,2*a*3.14/180,3.14/2,n))
            n=n-1
if __name__ == '__main__':
    MyTree().run()
