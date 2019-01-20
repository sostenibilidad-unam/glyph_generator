# Hier-'o-glyph!

Visualize hierarchical indexes with a nice glyph.

![](tests/plots/test2.svg)

### With labels

![](tests/plots/conlabels.png)

### Bars in the outmost track

![](tests/plots/conbarras.png)



## Usage

    gw.makeBarGlyph("glyph1.svg", 400, data1, True, True)

![](tests/plots/glyph1.png)


    gw.makeBarGlyph("glyph2.svg", 400, data2, True, True)

![](tests/plots/glyph2.png)

    gw.makeBarGlyph("glyph3.svg", 400, data3, True, True)

![](tests/plots/glyph3.png)

    gw.makeGlyph("glyph4.svg", 400, data1, True, True)

![](tests/plots/glyph4.png)

    gw.makeGlyph("glyph5.svg", 400, data2, True, True)

![](tests/plots/glyph5.png)

    gw.makeGlyph("glyph6.svg", 400, data3, True, True)

![](tests/plots/glyph6.png)

    gw.makeLabels("labels.svg", 400, data1)

![](tests/plots/labels.png)

    gw.makeGlyph("glyph7.svg", 400, data1, False, True)

![](tests/plots/glyph7.png)
