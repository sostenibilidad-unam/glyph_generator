import glyph_writer as gw

data1 = { "total": {"name" : "Vulnerabilidad",
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
                        "subcategories":[{"name":"Susceptibilidad A","value":1},
                                         {"name":"Susceptibilidad B","value":1},
                                         {"name":"Susceptibilidad C","value":0.2},
                                         {"name":"Susceptibilidad D","value":0.3}
                                         ]},


                    ]}

data2 = { "total": {"name" : "Vulnerabilidad",
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
                                         {"name":"Económica 4","value":0.5}
                                         ]},
                       {"name":"Ambiental",
                        "value":0.3,
                        "subcategories":[{"name":"Ambiental 1","value":0.5},
                                         {"name":"Ambiental 2","value":0.2},
                                         {"name":"Ambiental 3","value":0.1},
                                         {"name":"Ambiental 4","value":0.3},
                                         {"name":"Ambiental 5","value":0.2}
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









gw.makeBarGlyph("glyph1.svg", 400, data1, True, True)
gw.makeBarGlyph("glyph2.svg", 400, data2, True, True)
gw.makeBarGlyph("glyph3.svg", 400, data3, True, True)
gw.makeGlyph("glyph4.svg", 400, data1, True, True)
gw.makeGlyph("glyph5.svg", 400, data2, True, False)
gw.makeGlyph("glyph6.svg", 400, data3, True, False)
gw.makeLabels("labels.svg", 400, data1)
gw.makeLabels("labels2.svg", 400, data3)
gw.makeGlyph("glyph7.svg", 400, data1, False, True)
