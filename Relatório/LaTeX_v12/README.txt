%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% README %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                      %
%  ---------- Master of Science Dissertation template ----------       %
%                                                                      %
%  Template for the Master Thesis according to the regulations         %
%  published by the Academic Board (Direcção Académica) at IST.        %
%                                                                      %
%  For up-to-date guide, please refer to the offical website           %
%  http://da.tecnico.ulisboa.pt/dissertacao-de-mestrado/               %
%                                                                      %
%       Andre C. Marta                                                 %
%       Area Cientifica de Mecanica Aplicada e Aeroespacial            %
%       Departamento de Engenharia Mecanica                            %
%       Instituto Superior Tecnico                                     %
%       Av. Rovisco Pais                                               %
%       1049-001 Lisboa                                                %
%       Portugal                                                       %
%       Tel: +351 21 841 9469                                          %
%                        3469 (extension)                              %
%       Email: andre.marta@tecnico.ulisboa.pt                          %
%                                                                      %
%  Created:       Jan 20, 2011                                         %
%  Last Modified: Mar  4, 2024                                         %
%                                                                      %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Contents                                                            %
%  1 - Package contents                                                %
%  2 - Running on Linux                                                %
%  3 - Running on Windows                                              %
%  4 - Running on Mac                                                  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PACKAGE CONTENTS                                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

This set of files provide a template for using LaTeX to write a Master
or PhD thesis according to the IST regulations.

The main file is 'Thesis.tex' and it includes all the other .tex files
in the ZIP package:

	Thesis.TeX
		abbrvunsrtnat.bst
		Makefile
		README.txt (this file)
		Thesis_Preamble.tex
		Thesis_FrontCover.tex
		Thesis_Dedication.tex
		Thesis_Declaration.tex
		Thesis_Acknowledgements.tex
		Thesis_Resumo.tex
		Thesis_Abstract.tex
		Thesis_Nomenclature.tex
		Thesis_Glossary.tex
		Thesis_Introduction.tex
		Thesis_Background.tex
		Thesis_Implementation.tex
		Thesis_Results.tex
		Thesis_Conclusions.tex
		Thesis_Bibliography_DB.bib
		Thesis_Appendix_A.tex
		Thesis_Appendix_B.tex
	Figures/Airbus_A320_sharklets.png
	Figures/Airbus_A350.png
	Figures/Bombardier_CRJ200.png
	Figures/IST_A_CMYK_POS.pdf
	Figures/SolarCell_Sunpower_C60.pdf

It is not required that you are familiar with LaTeX since the files
should be quite self-explanatory.
Please be sure you understand the structure, particularly of the main
file "Thesis.tex" before you start editing.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RUNNING ON OVERLEAF                                                  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

This is a (mostly) free online tool, with some advantages:
 - no need to install/maintain software
 - well documented
 - share feature (read or edit) for collaborative environment)
But, also, some disadvantaged
 - requires internet access
 - future availability or support not guaranteed

It is, however, one of the quickest ways to start using LaTeX...

https://www.overleaf.com/

This option requires an account on overleaf.
Create a blank project and upload all the files from this template.

Pressing the "compile" / "re-compile" button should do the trick.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RUNNING ON LINUX                                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Just use the make file 'Makefile' to process the LaTeX code and output
the PDF file.
Under Linux, opening a terminal window, change to the directory where
the main file "Thesis.tex" is located , and typing 'make' at the prompt.

Any Linux distribution (e.g. Ubuntu) already has the basic installation
of Texlive to process the TeX file, but some packages might be missing.
In that case, it is necessary to install additional Texlive packages
(use synaptic).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RUNNING ON WINDOWS                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

To run LaTeX on Windows, it is required to install additional software,
if it has not been done before.

The instructions below are just three possible solutions, but they proved
robust during tests.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
a) Software download

i) compiler:

>>> MiKTeX 24.1 (works fine with older/newer versions as well)
Download from http://miktex.org/download

ii) text editor:

Choose one of the suggested three editors below.
See http://en.wikipedia.org/wiki/Comparison_of_TeX_editors for helping you choose.

>>> Option a) Texmaker 5.1.4 (works fine with older/newer versions)
Download from http://www.xm1math.net/texmaker/download.html

This editor is nice because it allows two windows,
showing both the source code and the compiled pdf, simultaneously.
It also automatically installs and updates any necessary LaTeX package.

>>> Option b) (recommended) TeXstudio 4.7.3 (works fine with older/newer versions)
Download from http://texstudio.sourceforge.net/

this editor also provides modern writing support, such as interactive
spell checking, code folding, and syntax highlighting.
It is an extended version of the previous one with additional features
while keeping its look and feel.

>>> Option c) TeXworks 0.6.9 (works fine with older/newer versions as well)
Download from https://www.tug.org/texworks/

This editor already comes included in the MiKTeX installation.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
b) Installation notes

i) Compiler
------------------------
>>> MiKTeX
First install this compiler. Just follow the on-screen instructions.

Accept the default directory paths so that Texmaker can automatically
find the required executables for compilation (pdflatex, makeindex,
bibtex, etc).

ii) text editor:
------------------------

After the compiler is installed, the TeX editor can then be installed.
Follow the on-screen instructions.

After installation, it is necessary to configure the compilation
commands and, optionally, define shortcuts.

>>> a) Texmaker

Texmaker -> Options (menu bar) -> Configure Texmaker ->
Compile (left menu) -> User

Add the following commands without line breaks
(this replicates the makefile used in Linux):

pdflatex  -synctex=1 -interaction=nonstopmode %.tex | 
makeglossaries % | 
makeindex %.nlo -s nomencl.ist -o %.nls | 
bibtex %.aux | 
pdflatex -synctex=1 -interaction=nonstopmode %.tex | 
pdflatex -synctex=1 -interaction=nonstopmode %.tex

>>> b) TeXstudio

TeXstudio -> Options (menu bar) -> Configure TeXstudio ->
Build (left menu) -> User Commands

Press "+Add"
Rename command from "user0:" to "THESIS"
Add the following commands without line breaks
(this replicates the makefile used in Linux):

pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex | 
makeglossaries % | 
makeindex %.nlo -s nomencl.ist -o %.nls | 
bibtex.exe % | 
pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex | 
pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex

>>> c) TeXworks

Create a script in a plain text file, e.g. "TeXworks_compile.bat",
with the following lines

pdflatex Thesis
makeglossaries Thesis
makeindex Thesis.nlo -s nomencl.ist -o Thesis.nls
bibtex Thesis
pdflatex Thesis
pdflatex Thesis

note: edit included file "TeXworks_compile.bat" as desired.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
c) Compile LaTeX source

>>> a) Texmaker

Open the main file "Thesis.tex" in Texmaker, go to "Options" and
select "Define Current Document as Master Document" (one time only).

To compile, just click on the blue arrow next to "Compile"
(making sure the main TeX source is open).

To compile from any open file, the compilation commands must be edited,
replacing % by the main file name.

>>> b) TeXstudio

To compile, just select Tools (menu bar) -> User -> THESIS:,
making sure the main TeX source is open.

Note: the batch file "TeXworks_compile.bat" also works and
      can be launched directly by double-clicking on it, without TeXstudio

>>> c) TeXworks

To compile, execute the previously created batch script.

Note: the batch file "TeXworks_compile.bat" can be launched directly
      by double-clicking on it, without TeXworks


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
d) Define shortcuts (optional)

It is possible to program shortcuts.
It is advisable to assign the function keys Fx to the "compile", "clean" and "see pdf" functions.

>>> a) Texmaker

>>> b) TeXstudio

TeXstudio -> Options (menu bar) -> Configure TeXstudio ->
Shortcuts (left menu)

Menu -> Tools -> User
1:THESIS
edit Current Shortcut F12

Now to compile the entire document, just press F12

>>> c) TeXworks


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% RUNNING ON MAC                                                       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

To run LaTeX on Mac, it is required to install additional software,
if it has not been done before.

The instructions below are just two possible solutions.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
a) Software download

i) compiler:

>>> Option a) MiKTeX 24.1 (works fine with older/newer versions)
Download from http://miktex.org/download

>>> Option b) MacTex 
Download from https://tug.org/mactex/downloading.html

This version appears to be quite stable. Search for more recent release
if available.


ii) text editor:

>>> Option a) (recommended) TeXstudio 4.7.3 (works fine with older/newer versions)
Download from http://texstudio.sourceforge.net/

this editor also provides modern writing support, such as interactive
spell checking, code folding, and syntax highlighting.
It is an extended version of the previous one with additional features
while keeping its look and feel.

>>> Option b) Texifier
Download from https://www.texifier.com/mac

This editor is nice because it allows two windows,
showing both the source code and the compiled pdf, simultaneously.
It also automatically installs and updates any necessary LaTeX package.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
b) Installation notes

i) Compiler
------------------------
>>> MiKTeX
First install this compiler. Just follow the on-screen instructions.

Accept the default directory paths so that Texmaker can automatically
find the required executables for compilation (pdflatex, makeindex,
bibtex, etc).

>>> MacTex
First install this compiler. Just follow the on-screen instructions.

Accept the default directory paths so that Texpad can automatically
find the required executables for compilation (pdflatex, makeindex,
bibtex, etc).


ii) text editor:
------------------------

After the compiler is installed, the TeX editor can then be installed.
Follow the on-screen instructions.

After installation, it is necessary to configure the compilation
commands and, optionally, define shortcuts.

>>> a) TeXstudio

TeXstudio -> Options (menu bar) -> Configure TeXstudio ->
Build (left menu) -> User Commands

Press "+Add"
Rename command from "user0:" to "THESIS"
Add the following commands without line breaks
(this replicates the makefile used in Linux):

pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex | 
makeglossaries % | 
makeindex %.nlo -s nomencl.ist -o %.nls | 
bibtex.exe % | 
pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex | 
pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex

>>> b) Texifier

Click on the arrow next to “pdfLaTeX | BibTeX | Makeindex”
-> Toggle “Typeset Configuration” to “Manual”

Check “Nomenclature” and “Glossaries”

Restart Texifier


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
c) Compile LaTeX source

>>> a) TeXstudio

To compile, just select Tools (menu bar) -> User -> THESIS:,
making sure the main TeX source is open.

>>> b) Texifier

To compile, just click on “Typeset” on the upper left corner

Optionally, it is possible to activate “Auto-Typeset”
clicking on the arrow mentioned in b)->ii)->a).
Now every change made to the code is automatically compiled.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

