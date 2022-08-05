legend = [
    ("SWD", "swd"),
    ("JTAG", "jtag"),
    ("Ground", "gnd"),
    ("Pin", "pin"),
    ("Power", "pwr"),
    ("Not Connected", "nc"),
    ("Reset", "rst"),
]

left_header = [
    [
        ("1", "pin"),
        ("vRef", "pwr")
    ],
    [
        ("3", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("5", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("7", "pin"),
        ("Key", "nc"),
    ],
    [
        ("9", "pin"),
        ("GND", "gnd"),
    ],
]

right_header = [
    [
        ("2", "pin"),
        ("SWDIO", "swd"),
        ("TMS", "jtag"),
    ],
    [
        ("4", "pin"),
        ("SWDCLK", "swd"),
        ("TCK", "jtag"),
    ],
    [
        ("6", "pin"),
        ("TRACESWO", "swd"),
        ("TDO", "jtag"),
    ],
    [
        ("8", "pin"),
        ("NC", "nc"),
        ("TDI", "jtag"),
    ],
    [
        ("10", "pin"),
        ("nRst", "rst")
    ],
]

# Text

title = "<tspan class='h1'>ARM Cortex JTAG/SWD Debug Connector Pinout</tspan>"

description = """This is the standard ARM Cortex JTAG/SWD Debug connector 
used on Black Magic Probe as well as many targets. 

NOTE: The header is HALF PITCH! This means it is 0.05 inch (1.27 mm) pitch pin header.
"""
