INPUT ?= main.md
OUTPUT ?= index.html
THEME ?= my-theme.css

.PHONY: build watch clean toc

build: toc
	marp --theme-set $(THEME) --theme my-theme --html $(INPUT).tmp -o $(OUTPUT)

toc:
	cp $(INPUT) $(INPUT).tmp
	markdown-toc -i --bullets="-" --maxdepth=3 $(INPUT).tmp

watch:
	marp --theme-set $(THEME) --theme my-theme --html $(INPUT).tmp -o $(OUTPUT) --watch

clean:
	rm -f $(OUTPUT) $(INPUT).tmp
