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
        ("10", "pin"),
        ("nRst", "rst"),
        ("nRst", "rst"),
    ],
    [
        ("8", "pin"),
        ("NC", "nc"),
        ("TDI", "jtag"),
    ],
    [
        ("6", "pin"),
        ("TRACESWO", "swd"),
        ("TDO", "jtag"),
    ],
    [
        ("4", "pin"),
        ("SWDCLK", "swd"),
        ("TCK", "jtag"),
    ],
    [
        ("2", "pin"),
        ("SWDIO", "swd"),
        ("TMS", "jtag"),
    ],
]

right_header = [
    [
        ("9", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("7", "pin"),
        ("Key", "nc"),
    ],
    [
        ("5", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("3", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("1", "pin"),
        ("vRef", "pwr")
    ],
]

# Text

title = "<tspan class='h1'>ARM Cortex JTAG/SWD Debug Connector Pinout</tspan>"

description = """This is the standard ARM Cortex JTAG/SWD Debug connector 
used on Black Magic Probe as well as many targets. 

NOTE: The header is HALF PITCH! This means it is 0.05 inch (1.27 mm) pitch pin header.
"""
