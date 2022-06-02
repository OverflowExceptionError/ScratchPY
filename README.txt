PyJava
A attempt at a Python implementation of Java. (of course it uses Python syntax)
The purpose of PyJava's 'importer' library is so that it can fix:
1. Imports (for example just trying to import com.pyjava.interface won't work because PyJava expands it's applets to the 'applet' directory - use importer.require([LIBRARY]) to import it)
2. Fixing filepaths (same reason imports dont work)
PJAR can NOT be used to extract pjar archives.
The reasons are as follows:
Why would you need to when I just gave you the source files for the PJar format?
Tresspassing on code (PyJava Source Code Specifiacton rule 1)

Just run:
Windows: 
py -m pip install pygame,requests
Mac and Linux:
python3 -m pip install pygame,requests

Commands:
Windows:
py pyjava.py none com.pyjava.help noargs
py pyjava.py none com.pyjava.help debug (Debugger for PyJava)
py pyjava.py demos com.examplecorp.pjframeDemo noargs
py pyjava.py demos com.examplecorp.pjframeDemo debug (Debugger for PyJava)
py pyjava.py demos com.examplecorp.httprequestDemo [URL]
py pyjava.py demos com.examplecorp.httprequestDemo debug;[URL] (Debugger for PyJava)
py pyjava.py none com.pyjava.demo noargs
py pyjava.py none com.pyjava.demo debug (Debugger for PyJava)
Mac and Linux:
python3 pyjava.py none com.pyjava.help noargs
python3 pyjava.py none com.pyjava.help debug (Debugger for PyJava)
python3 pyjava.py demos com.examplecorp.pjframeDemo noargs
python3 pyjava.py demos com.examplecorp.pjframeDemo debug (Debugger for PyJava)
python3 pyjava.py demos com.examplecorp.httprequestDemo [URL]
python3 pyjava.py demos com.examplecorp.httprequestDemo debug;[URL] (Debugger for PyJava)
python3 pyjava.py none com.pyjava.demo noargs
python3 pyjava.py none com.pyjava.demo debug (Debugger for PyJava)
Required files:
pyjava.py
pjar.py
importer.py
libs/components.pjar