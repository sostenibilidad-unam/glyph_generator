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


def addArcs(dwg, current_group, radius, center, data, labels=False):
    """ Adds as many as categories arcs given radius and center """
    values = []
    categories = len(data["categories"])
    for category in data["categories"]:
        values.append(category["value"])

    cortesAngulares = np.linspace(0,360,categories+1)
    delta = (7/120)*cortesAngulares[1]
    size = int(12*radius/100)
    text = dwg.add(svgwrite.text.Text("",style = "font-size:"+str(size)+"px; font-family:Arial; font-weight:bold"))
    for i in range(1,categories+1):
        r = radius-((radius*0.15)*(1.0-values[i-1]))
        width = radius * .3 * values[i-1]
        addArc(dwg, current_group, p0=angle2xy(center[0],center[1],r,cortesAngulares[i]-delta), p1=angle2xy(center[0],center[1],r,cortesAngulares[i-1]+delta), radius=r, width=width)

        ###addLabels
        if labels:
            middle_angle = (cortesAngulares[i]+cortesAngulares[i-1])/2
            if middle_angle < 90 or middle_angle > 270:
                rt = r*1.17
                alverez = "1"
                pt1=angle2xy(center[0],center[1],rt,cortesAngulares[i]-delta)
                pt0=angle2xy(center[0],center[1],rt,cortesAngulares[i-1]+delta)
            else:
                rt = r*1.25
                alverez = "0"
                pt0=angle2xy(center[0],center[1],rt,cortesAngulares[i]-delta)
                pt1=angle2xy(center[0],center[1],rt,cortesAngulares[i-1]+delta)

            args = {'x0':pt0[0],
                'y0':pt0[1],
                'xradius':rt,
                'yradius':rt,
                'ellipseRotation':0, #has no effect for circles
                'x1':(pt1[0]-pt0[0]),
                'y1':(pt1[1]-pt0[1]),
                'alverez':alverez}
            color = 'green'
            w = dwg.path(d="M %(x0)f,%(y0)f a %(xradius)f,%(yradius)f %(ellipseRotation)f 0,%(alverez)s %(x1)f,%(y1)f"%args,
                     fill="none",
                     stroke=color, stroke_width=0
                    )
            current_group.add(w)
            name = data["categories"][i-1]["name"]

            text.add(svgwrite.text.TextPath(path=w, text=name, startOffset="33%", method='align', spacing='exact'))


def addCircle(dwg, current_group,radius,center,data,labels=False):
    total = data["total"]["value"]
    dwg.add(dwg.circle(center=(center[0],center[1]),
                       r=radius*0.6*total, #aqui talvez que un total de 0 no de un radio 0 si no un radio minimo?
                       stroke='none',#svgwrite.rgb(15, 15, 15, '%'),
                       fill='green')
    )

    ###addLabels
    if labels:
        size = int(14*radius/100)
        text_central = dwg.add(svgwrite.text.Text("",style = "font-size:"+str(size)+"px; font-family:Arial; font-weight:bold"))
        rt = radius*0.62
        pt0=angle2xy(center[0],center[1],rt,300)
        pt1=angle2xy(center[0],center[1],rt,60)
        args = {'x0':pt0[0],
            'y0':pt0[1],
            'xradius':rt,
            'yradius':rt,
            'ellipseRotation':0, #has no effect for circles
            'x1':(pt1[0]-pt0[0]),
            'y1':(pt1[1]-pt0[1])}
        w = dwg.path(d="M %(x0)f,%(y0)f a %(xradius)f,%(yradius)f %(ellipseRotation)f 0,1 %(x1)f,%(y1)f"%args,
                 fill="none",
                 stroke_width=0
                )
        current_group.add(w)
        name = data["total"]["name"]

        text_central.add(svgwrite.text.TextPath(path=w, text=name, startOffset="15%", method='align', spacing='exact'))


def addDots(dwg, current_group,radius,center,data,labels=False):
    n_categories = len(data["categories"])
    cortesAngulares = np.linspace(0,360,n_categories+1)

    cual_category = -1
    size = int(10*radius/100)
    text_sub = dwg.add(svgwrite.text.Text("",style = "font-size:"+str(size)+"px; font-family:Arial; font-weight:bold"))
    for category in data["categories"]:
        cual_category += 1
        n_subcategories = len(category["subcategories"])
        dots_angles = np.linspace(cortesAngulares[cual_category],cortesAngulares[cual_category+1],n_subcategories+2)[1:-1]
        dots_xys = [angle2xy(center[0],center[1],radius*1.4,dots_angle) for dots_angle in dots_angles]
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

            #add Labels
            if labels:

                if dots_angles[cual_subcategory] > 180:
                    text0_xys = [angle2xy(center[0],center[1],radius*1.4,dots_angle-1) for dots_angle in dots_angles]
                    text1_xys = [angle2xy(center[0],center[1],radius*2.5,dots_angle-1) for dots_angle in dots_angles]
                    args = {'x1':text0_xys[cual_subcategory][0],
                        'y1':text0_xys[cual_subcategory][1],
                        'x0':text1_xys[cual_subcategory][0],
                        'y0':text1_xys[cual_subcategory][1]}
                else:
                    text0_xys = [angle2xy(center[0],center[1],radius*1.4,dots_angle+1) for dots_angle in dots_angles]
                    text1_xys = [angle2xy(center[0],center[1],radius*2.5,dots_angle+1) for dots_angle in dots_angles]
                    args = {'x0':text0_xys[cual_subcategory][0],
                        'y0':text0_xys[cual_subcategory][1],
                        'x1':text1_xys[cual_subcategory][0],
                        'y1':text1_xys[cual_subcategory][1]}

                l = dwg.path(d="M %(x0)f %(y0)f %(x1)f %(y1)f"%args,
                         fill="none",
                         stroke_width=0
                        )
                current_group.add(l)
                name = subcategory["name"]

                text_sub.add(svgwrite.text.TextPath(path=l, text=name, startOffset="13%", method='align', spacing='exact'))


def makeGlyph(dwg, current_group,radius,center,data,labels=False):
    addCircle(dwg, current_group,radius,center,data,labels)
    addArcs(dwg, current_group,radius,center,data,labels)
    addDots(dwg, current_group,radius,center,data,labels)



data = { "total": {"name" : "Vulnerabilidad",
                 "value": 0.5},
         "categories":[{"name":"Exposición",
                        "value":0.6,
                        "subcategories":[{"name":"Expocisión A","value":0.2},
                                         {"name":"Expocisión B","value":0.4},
                                         {"name":"Expocisión C","value":0.8},
                                         #{"name":"e4","value":0.5}
                                         ]},
                      {"name":"Resiliencia",
                       "value":0.9,
                       "subcategories":[{"name":"Resiliencia A","value":1.0},
                                      {"name":"Resiliencia B","value":0.9},
                                      {"name":"Resiliencia C","value":0.8},
                                      {"name":"Resiliencia D","value":1.0},
                                      {"name":"Resiliencia E","value":0.8}
                                      ]},
                       {"name":"Susceptibilidad",
                        "value":0.4,
                        "subcategories":[{"name":"Susceptibilidad A","value":0.5},
                                         {"name":"Susceptibilidad B","value":0.6},
                                         {"name":"Susceptibilidad C","value":0.2},
                                         {"name":"Susceptibilidad D","value":0.3}
                                         ]},


                    ]}

data5 = { "total": {"name" : "Vulnerabilidad",
                 "value": 0.9},
         "categories":[{"name":"Exposición",
                        "value":0.7,
                        "subcategories":[{"name":"Expocisión A","value":0.6},
                                         {"name":"Expocisión B","value":0.8},
                                         {"name":"Expocisión C","value":0.7},
                                         #{"name":"e4","value":1}
                                         ]},
                      {"name":"Resiliencia",
                       "value":0.3,
                       "subcategories":[{"name":"Resiliencia A","value":0.3},
                                      {"name":"Resiliencia B","value":0.2},
                                      {"name":"Resiliencia C","value":0.4},
                                      {"name":"Resiliencia D","value":0.2},
                                      {"name":"Resiliencia E","value":0.4}
                                      ]},
                       {"name":"Susceptibilidad",
                        "value":0.8,
                        "subcategories":[{"name":"Susceptibilidad A","value":0.7},
                                         {"name":"Susceptibilidad B","value":0.9},
                                         {"name":"Susceptibilidad C","value":0.6},
                                         {"name":"Susceptibilidad D","value":1}
                                         ]},


                    ]}

data2 = { "total": {"name" : "Vulnerabilidad",
                 "value": 1.0},
         "categories":[{"name":"Exposición",
                        "value":1,
                        "subcategories":[{"name":"Expocisión A","value":1},
                                         {"name":"Expocisión B","value":1},
                                         {"name":"Expocisión C","value":1},
                                         #{"name":"e4","value":1}
                                         ]},
                      {"name":"Resiliencia",
                       "value":1,
                       "subcategories":[{"name":"Resiliencia A","value":1.0},
                                      {"name":"Resiliencia B","value":1},
                                      {"name":"Resiliencia C","value":1},
                                      {"name":"Resiliencia D","value":1},
                                      {"name":"Resiliencia E","value":1}
                                      ]},
                       {"name":"Susceptibilidad",
                        "value":1,
                        "subcategories":[{"name":"Susceptibilidad A","value":1},
                                         {"name":"Susceptibilidad B","value":1},
                                         {"name":"Susceptibilidad C","value":1},
                                         {"name":"Susceptibilidad D","value":1}
                                         ]},


                    ]}




data3 = { "total": {"name" : "Sostenibilidad",
                 "value": 0.7},
         "categories":[{"name":"Social",
                        "value":1.0,
                        "subcategories":[{"name":"Social 1","value":1.0},
                                         {"name":"Social 2","value":1.0},
                                         {"name":"Social 3","value":1.0},
                                         {"name":"Social 4","value":1.0}
                                         ]},
                       {"name":"Económica",
                        "value":0.5,
                        "subcategories":[{"name":"Económica 1","value":0.3},
                                         {"name":"Económica 2","value":0.5},
                                         {"name":"Económica 3","value":0.7},
                                         #{"name":"Económica 4","value":0.5}
                                         ]},
                       {"name":"Ambiental",
                        "value":0.8,
                        "subcategories":[{"name":"Ambiental 1","value":0.6},
                                         {"name":"Ambiental 2","value":0.7},
                                         {"name":"Ambiental 3","value":0.8},
                                         {"name":"Ambiental 4","value":0.9},
                                         {"name":"Ambiental 5","value":1}
                                         ]},
                        {"name":"Gobernanza",
                         "value":0.6,
                         "subcategories":[{"name":"Gobernanza 1","value":0.2},
                                          {"name":"Gobernanza 2","value":1},
                                          {"name":"Gobernanza 3","value":0.5},
                                          {"name":"Gobernanza 4","value":0.7},
                                          {"name":"Gobernanza 5","value":0.6}
                                          ]}

                    ]}

data4 = { "total": {"name" : "Sostenibilidad",
                 "value": 1},
         "categories":[{"name":"Social",
                        "value":1.0,
                        "subcategories":[{"name":"Social 1","value":1.0},
                                         {"name":"Social 2","value":1.0},
                                         {"name":"Social 3","value":1.0},
                                         {"name":"Social 4","value":1.0}
                                         ]},
                       {"name":"Económica",
                        "value":1,
                        "subcategories":[{"name":"Económica 1","value":1},
                                         {"name":"Económica 2","value":1},
                                         {"name":"Económica 3","value":1},
                                         #{"name":"Económica 4","value":1}
                                         ]},
                       {"name":"Ambiental",
                        "value":1,
                        "subcategories":[{"name":"Ambiental 1","value":1},
                                         {"name":"Ambiental 2","value":1},
                                         {"name":"Ambiental 3","value":1},
                                         {"name":"Ambiental 4","value":1},
                                         {"name":"Ambiental 5","value":1}
                                         ]},
                        {"name":"Gobernanza",
                         "value":1,
                         "subcategories":[{"name":"Gobernanza 1","value":1},
                                          {"name":"Gobernanza 2","value":1},
                                          {"name":"Gobernanza 3","value":1},
                                          {"name":"Gobernanza 4","value":1},
                                          {"name":"Gobernanza 5","value":1}
                                          ]}

                    ]}




dwg = svgwrite.Drawing(filename="test3.svg", debug=True, size=(1500,800))
current_group = dwg.add(dwg.g(id='uno', fill='none', fill_opacity=0 ))

centro1 = [300,200]
makeGlyph(dwg, current_group,80,centro1,data,True)

centro2 = [750,200]
makeGlyph(dwg, current_group,80,centro2,data5,True)

centro3 = [500,600]
makeGlyph(dwg, current_group,80,centro3,data3,True)

centro4 = [900,600]
makeGlyph(dwg, current_group,80,centro4,data4)

centro5 = [1200,200]
makeGlyph(dwg, current_group,80,centro5,data2)


dwg.save()
