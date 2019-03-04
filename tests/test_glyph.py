import hieroglyph

simple = {"total": {"name": "main",
                    "value": 0.5},
          "categories": [
              {"name": "A",
               "value": 0.6,
               "subcategories": [
                   {"name": "A.1", "value": 0.2},
                   {"name": "A.2", "value": 0.8}]},
              {"name": "B",
               "value": 0.4,
               "subcategories": [
                   {"name": "B.1", "value": 0.3},
                   {"name": "B.2", "value": 0.7}]},
          ]}


def test_elements():
    g = hieroglyph.Glyph(svg_width=100,
                         data=simple,
                         labels=False,
                         toEnsableLabelsLater=False)

    g.render()

    assert len(g.dwg.elements) == 8
