PAPER=slides.tex
COMPILER=xelatex
BUILDDIR=build
FLAGS=-shell-escape \
      -interaction nonstopmode \
      -halt-on-error \
      -file-line-error \
      -output-directory=$(BUILDDIR)

all:
	mkdir -p $(BUILDDIR)
	$(COMPILER) $(FLAGS) $(PAPER)
	mv $(BUILDDIR)/*.pdf .

clean:
	rm -rf $(BUILDDIR) _minted-slides/ indent.log

watch:  
	ls $(PAPER) | entr make all
