# ---------------------------------------------------------
# type "make" command in the Linux terminal to create PDF 
#
# by default, runs the first targer (all)
#
# type "make clean" to remove auxiliary files
# type "make veryclean" to clean and delete PDF
# ---------------------------------------------------------

# Main filename
FILE=Thesis

# ---------------------------------------------------------

all:
	pdflatex  ${FILE}
	makeglossaries $(FILE)
	makeindex $(FILE).nlo -s nomencl.ist -o $(FILE).nls
	bibtex ${FILE}
	pdflatex  ${FILE}
	pdflatex  ${FILE}

clean:
	(rm -rf *.acn *.acr *.alg *.aux *.bbl *.blg *.glg *.glo *.gls *.ilg *.ist *.lof *.log *.lot *.nlo *.nls *.out *.toc)

veryclean:
	make clean
	rm -f $(FILE).pdf
