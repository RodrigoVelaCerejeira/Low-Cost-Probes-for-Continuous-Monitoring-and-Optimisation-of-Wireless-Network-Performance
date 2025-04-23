REM -----------------------------------------------------------------
REM Compilation on TeXworks
REM
REM script to be used only when the glossary or nomenclature are modified
REM otherwise, command "texify" inside TeXworks does the job better
REM
REM the defaul is the optimized full compilation option
REM uncommented other command options as desired
REM
REM -----------------------------------------------------------------

REM -----------------------------------------------------------------
REM Optimized full compilation

@echo off

echo. &
texify --pdf Thesis.tex
echo. &
makeglossaries Thesis
echo. &
makeindex Thesis.nlo -s nomencl.ist -o Thesis.nls
echo. &
texify --pdf Thesis.tex


REM -----------------------------------------------------------------
REM Glossary and nomenclature only
REM 
REM @echo off
REM 
REM echo. &
REM makeglossaries Thesis
REM echo. &
REM makeindex Thesis.nlo -s nomencl.ist -o Thesis.nls


REM -----------------------------------------------------------------
REM Full compilation
REM 
REM pdflatex Thesis
REM makeglossaries Thesis
REM makeindex Thesis.nlo -s nomencl.ist -o Thesis.nls
REM bibtex Thesis
REM pdflatex Thesis
REM pdflatex Thesis


REM -----------------------------------------------------------------

