from tkinter import Scale
from pinout import config
from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows, Panel
from pinout.components.pinlabel import PinLabelGroup
from pinout.components.annotation import AnnotationLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend

import data

#diagram = Diagram(1200, 675, "diagram")
diagram = Diagram_2Rows(1024, 576, 440, "diagram")
#diagram.add_stylesheet("styles_auto.css", True)
diagram.add_stylesheet("styles.css", embed=True)
# content = diagram.add(Panel(width=1200, height=675, tag="panel__content"))

# panel_graphic = content.add(
#     Panel(
#         width=860,
#         height=300,
#         tag="panel__graphic",
#     )
# )

graphic = diagram.panel_01.add(Group(400, 100))

hardware = graphic.add(Image("10-pin-keyed.svg", dpi=72, width=2.4, height=6.4, embed=True))

hardware.add_coord("p1",  x=110, y=110)
hardware.add_coord("p2",  x=210, y=110)
hardware.add_coord("p3",  x=0.12, y=0.22)
hardware.add_coord("p4",  x=0.22, y=0.22)
hardware.add_coord("p5",  x=0.12, y=0.32)
hardware.add_coord("p6",  x=0.22, y=0.32)
hardware.add_coord("p7",  x=0.12, y=0.42)
hardware.add_coord("p8",  x=0.22, y=0.42)
hardware.add_coord("p9",  x=0.12, y=0.52)
hardware.add_coord("p10", x=0.22, y=0.52)
hardware.add_coord("pin_pitch_v", x=0, y=100)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("p1").x,
        y=hardware.coord("p1").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, 30),
        scale=(-1, 1),
        labels=data.left_header,
    )
)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("p2").x,
        y=hardware.coord("p2").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, 30),
        labels=data.right_header,
    )
)

# Create a title and description text-blocks
title_block = diagram.panel_02.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)
diagram.panel_02.add(
    TextBlock(
        data.description,
        x=20,
        y=60,
        width=title_block.width,
        height=diagram.panel_02.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)


# Create a legend
legend = diagram.panel_02.add(
    Legend(
        data.legend,
        x=700,
        y=8,
        max_height=132,
    )
)
