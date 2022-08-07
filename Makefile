all:
	for i in */Makefile ; do \
		$(MAKE) -C `dirname $$i`; \
	done;

clean:
	for i in */Makefile ; do \
		$(MAKE) -C `dirname $$i` clean; \
	done;

.PHONY: clean