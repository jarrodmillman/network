all: clean slides.pdf

clean:
	-rm -f slides.{aux,log,nav,out,pdf,snm,tex,toc}

slides.tex: slides
	pandoc -t beamer slides -o slides.tex -s

slides.pdf: slides.tex
	xelatex slides.tex

