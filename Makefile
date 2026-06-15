INPUT ?= main.md
OUTPUT ?= index.html

.PHONY: build watch clean toc

build: toc
	marp $(INPUT).tmp -o $(OUTPUT)

toc:
	cp $(INPUT) $(INPUT).tmp
	markdown-toc -i --bullets="-" --maxdepth=3 $(INPUT).tmp

watch:
	marp $(INPUT).tmp -o $(OUTPUT) --watch

clean:
	rm -f $(OUTPUT) $(INPUT).tmp
