import svgwrite
import math
import numpy as np
import pandas as pd

"""
g = Glyph('Vulnerability', 0.2)

resilience = Arc('Resilience', 0.3)
resilience.dots.append(Dot('res A', 0.1))
resilience.dots.append(Dot('res B', 0.3, pallete=rainbow))

icon_dot = Dot('res C', 0.2)
icon_dot.svg.add_group(some_svg_icon)

resilience.dots.append(icon_dot)

g.add_arc(resilience)


g.add_arc(Arc('Susceptibility', 0.1))
g.arcs['Susceptibility'].add_dot('sus A', 0.1)

with open('glyph.svg', 'w') as f:
    f.write(g.render())
    
"""



"""
An experiment with pandas dataframe

data = [{'E': 0.1, 'E1': 0.2},
        {'R': 0.3, 'R1': 0.2, 'R2': 0.3},
        {'S': 0.2, 'S1': 0.3, 'S2': 0.4, 'S3': 0.6}]

df = pd.DataFrame(data=data, index=['E', 'R', 'S'])

df.set_index(['E', 'R', 'S'])

g = Glyph(df, bars=True)

"""



class Glyph:

    def __init__(self, label, value):
        self.label = label
        self.value = value
    

class Arc:

    def __init__(self, label, value, dots=[]):
        self.label = label
        self.value = value
        self.dots = dots

    def to_svg(self):
        pass
    

    def add_dot(dot):
        """
        Add a peripheral dot to arc
        """


class Dot:

    def __init__(self, label, value):
        self.label = label
        self.value = value
