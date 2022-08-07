DIAGRAM = unified
MODEL = 10-pin-keyed

%-legend.svg: data.py pinout_diagram.py ../models/${MODEL}.svg
	python -m pinout.manager --overwrite --export pinout_diagram.py $@


%-legend.png: data.py pinout_diagram.py ../models/${MODEL}.svg
	python -m pinout.manager --overwrite --export pinout_diagram.py $@

all: ${DIAGRAM}-legend.svg ${DIAGRAM}-legend.png

clean:
	rm -f ${DIAGRAM}-legend.svg ${DIAGRAM}-legend.png

.PHONY: clean
