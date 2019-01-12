import svgwrite
import math
import numpy as np

def angle2xy(centerX, centerY, radius, angleInDegrees):
  """ Calculates [x,y] from angle and radius """
  angleInRadians = (angleInDegrees-90) * math.pi / 180.0
  x= centerX + (radius * math.cos(angleInRadians))
  y= centerY + (radius * math.sin(angleInRadians))
  return [x,y]



def addArc(dwg, current_group, p0, p1, radius, width):
    """ Adds an arc that cirles to the right as it moves from p0 to p1 """
    args = {'x0':p0[0],
        'y0':p0[1],
        'xradius':radius,
        'yradius':radius,
        'ellipseRotation':0, #has no effect for circles
        'x1':(p1[0]-p0[0]),
        'y1':(p1[1]-p0[1])}
    color = 'green' #aqui hay que usar una rampa de color que dependa del value

    current_group.add(dwg.path(d="M %(x0)f,%(y0)f a %(xradius)f,%(yradius)f %(ellipseRotation)f 0,0 %(x1)f,%(y1)f"%args,
             fill="none",
             stroke=color, stroke_width=width
            ))


def addArcs(dwg, current_group, categories, radius, center, data):
    """ Adds as many as categories arcs given radius and center """
    values = []
    #se deberia deducir el categories de los datos en vez de que sea otro parametro
    for category in data["categories"]:
        values.append(category["value"])

    cortesAngulares = np.linspace(0,360,categories+1)
    delta = (7/120)*cortesAngulares[1]
    for i in range(1,categories+1):
        r = radius-((radius*0.15)*(1.0-values[i-1]))
        width = radius * .3 * values[i-1]
        addArc(dwg, current_group, p0=angle2xy(center[0],center[1],r,cortesAngulares[i]-delta), p1=angle2xy(center[0],center[1],r,cortesAngulares[i-1]+delta), radius=r, width=width)

def addCircle(dwg, current_group,radius,center,total):
    dwg.add(dwg.circle(center=(center[0],center[1]),
                       r=radius*0.6*total, #aqui talvez que un total de 0 no de un radio 0 si no un radio minimo?
                       stroke=svgwrite.rgb(15, 15, 15, '%'),
                       fill='green')
    )


def addDots(dwg, current_group,radius,center,data):
    n_categories = len(data["categories"])
    cortesAngulares = np.linspace(0,360,n_categories+1)

    cual_category = -1
    for category in data["categories"]:
        cual_category += 1
        n_subcategories = len(category["subcategories"])
        dots_angles = np.linspace(cortesAngulares[cual_category],cortesAngulares[cual_category+1],n_subcategories+2)[1:-1]
        dots_xys = [angle2xy(center[0],center[1],radius*1.3,dots_angle) for dots_angle in dots_angles]
        cual_subcategory = -1
        for subcategory in category["subcategories"]:
            cual_subcategory += 1
            x = dots_xys[cual_subcategory][0]
            y = dots_xys[cual_subcategory][1]
            dwg.add(dwg.circle(center=(x,y),
                               r=radius*0.1*subcategory["value"], #aqui talvez que un total de 0 no de un radio 0 si no un radio minimo?
                               stroke='none',
                               fill='green')
            )


data = { "total": {"name" : "Vulnerabilidad",
                 "value": 0.8},
         "categories":[{"name":"Exposicion",
                        "value":0.6,
                        "subcategories":[{"name":"e1","value":0.2},
                                         {"name":"e2","value":0.4},
                                         {"name":"e3","value":0.8},
                                         {"name":"e4","value":0.5}
                                         ]},
                       {"name":"Susceptibilidad",
                        "value":0.4,
                        "subcategories":[{"name":"s1","value":0.5},
                                         {"name":"s2","value":0.6},
                                         {"name":"s3","value":0.2},
                                         {"name":"s4","value":0.3}
                                         ]},
                       {"name":"Resiliencia",
                        "value":0.9,
                        "subcategories":[{"name":"r1","value":1.0},
                                         {"name":"r2","value":0.9},
                                         {"name":"r3","value":0.8},
                                         {"name":"r4","value":1.0},
                                         {"name":"r5","value":0.8}
                                         ]}

                    ]}




dwg = svgwrite.Drawing(filename="test.svg", debug=True, size=(1500,800))
current_group = dwg.add(dwg.g(id='uno', fill='none', fill_opacity=0 ))
centro1 = [200,200]
addCircle(dwg, current_group,50,centro1,data["total"]["value"])
addArcs(dwg, current_group,3,50,centro1,data)
addDots(dwg, current_group,50,centro1,data)

dwg.save()
