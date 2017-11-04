.PHONY: all check clean

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(patsubst %/,%,$(dir $(mkfile_path)))
parent_dir := $(patsubst %/,%,$(dir $(current_dir)))
setup = $(parent_dir)/setup.py
objects = $(wildcard *.in)
outputs := base.txt $(objects:.in=.txt)

all: $(outputs)

something:
	@echo $(mkfile_path)
	@echo $(current_dir)

base.txt: $(setup)
	cd $(parent_dir) && pip-compile --output-file $(current_dir)/$@ $<

%.txt: %.in
	pip-compile --output-file $@ $<

test.txt: base.txt

dev.txt: test.txt

check:
	@which pip-compile > /dev/null

clean: check
	- rm *.txt

sync: base.txt test.txt dev.txt
	pip-sync base.txt test.txt dev.txt
