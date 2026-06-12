INPUT ?= main.md
OUTPUT ?= output.html
THEME ?= my-theme.css

.PHONY: build watch clean

build:
	marp --theme-set $(THEME) --theme my-theme --html $(INPUT) -o $(OUTPUT)

watch:
	marp --theme-set $(THEME) --theme my-theme --html $(INPUT) -o $(OUTPUT) --watch

clean:
	rm -f $(OUTPUT)
