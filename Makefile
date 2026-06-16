INPUT       ?= main.md
OUTPUT      ?= index.html
TOC         ?= python3 toc.py
TOC_FLAGS   := --maxdepth 3

.PHONY: build watch clean

%.toc: %
	$(TOC) $< $(TOC_FLAGS) > $@

build: $(INPUT).toc
	marp $(INPUT).toc -o $(OUTPUT)

watch:
	marp $(INPUT).toc -o $(OUTPUT) --watch

clean:
	rm -f $(OUTPUT) $(INPUT).toc
