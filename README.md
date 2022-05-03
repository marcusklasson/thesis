# thesis

I am using Texstudio as my editor for writing, which I installed from the website ```https://www.texstudio.org/```. 
Check for the right Ubuntu version and install the .deb and then just click on the file, very easy and nice.

When I tried compiling the KTH Latex template, I got some errors that I had no idea to fix.

First one was "File `utf8x.def' not found. \endinput" that I fixed with running this in the terminal
```
sudo apt-get install texlive-latex-extra
```

I don't entirely know what ```texlive``` is, but it seems to be some platform where you can download Tex programs like packages, macros, and fonts.
I had to install some more things from texlive because the compiler was complaining about

"Package babel Error: Unknown option `swedish'."
```
sudo apt-get install texlive-lang-european 
```

"File `algorithm.sty' not found." (and many other files if \usepackage{algorithm} was commented out)
```
sudo apt-get install texlive-science 
```

The command ```sudo apt-get install texlive-full``` also exists, but I tried it and it took quite some time to install everything, so I decided to cancel installing everything.

But the KTH template compiled after I had installed those things from texlive!


### Error eps file
If you get this error "Package pdftex.def Error: File `KTHLogo-eps-converted-to.pdf' not found: using draft setting.", it's becuase package epstopdf isnot installed. So you can fix it by executing:
```
sudo apt install texlive-font-utils
```

## Using separate References using multibib package 
I had many issues with fixing using separate references in each chapter.

Now I have to remove all .aux files in order to get the references to work. 
Maybe all this is works out fine in Overleaf? It seemed to do so for Taras.

I think also that I should contribute to RPL with an overleaf template of this solution 
if I can make it work with Ioanna's files and the multibib package.

