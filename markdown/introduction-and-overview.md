

* * *

##### Tuesday, January 13, 2009

###  Introduction and Overview

Introduction  
  
Python is currently one of the most popular dynamic programming languages,
along with Perl, Tcl, PHP, and newcomer Ruby. Although it is often viewed as a
"scripting" language, it is really a general purpose programming language
along the lines of Lisp or Smalltalk (as are the others, by the way). Today,
Python is used for everything from throw-away scripts to large scalable web
servers that provide uninterrupted service 24x7. It is used for GUI and
database programming, client- and server-side web programming, and application
testing. It is used by scientists writing applications for the world's fastest
supercomputers and by children first learning to program.  
In this blog, I will shine the spotlight on Python's history. In particular,
how Python was developed, major influences in its design, mistakes made,
lessons learned, and future directions for the language.  
  
Acknowledgment: I am indebted to [Dave Beazley](http://www.dabeaz.com/) for
many of the better sentences in this blog. (For more on the origins of this
blog, see [my other blog](http://neopythonic.blogspot.com/2009/01/history-of-
python-introduction.html).)  
  
A Bird's Eye View of Python  
  
When one is first exposed to Python, they are often struck by way that Python
code looks, at least on the surface, similar to code written in other
conventional programming languages such as C or Pascal. This is no accident---
the syntax of Python borrows heavily from C. For instance, many of Python's
keywords (if, else, while, for, etc.) are the same as in C, Python identifiers
have the same naming rules as C, and most of the standard operators have the
same meaning as C. Of course, Python is obviously not C and one major area
where it differs is that instead of using braces for statement grouping, it
uses indentation. For example, instead of writing statements in C like this  

    
    
    if (a < b) {  
        max = b;  
    } else {  
        max = a;  
    }

Python just dispenses with the braces altogether (along with the trailing
semicolons for good measure) and uses the following structure  

    
    
    if a < b:  
        max = b  
    else:  
        max = a

The other major area where Python differs from C-like languages is in its use
of dynamic typing. In C, variables must always be explicitly declared and
given a specific type such as int or double. This information is then used to
perform static compile-time checks of the program as well as for allocating
memory locations used for storing the variable’s value. In Python, variables
are simply names that refer to objects. Variables do not need to be declared
before they are assigned and they can even change type in the middle of a
program. Like other dynamic languages, all type-checking is performed at run-
time by an interpreter instead of during a separate compilation step.  
  
Python’s primitive built-in data types include Booleans, numbers (machine
integers, arbitrary-precision integers, and real and complex floating point
numbers), and strings (8-bit and Unicode). These are all immutable types,
meaning that values are represented by objects that cannot be modified after
their creation. Compound built-in data types include tuples (immutable
arrays), lists (resizable arrays) and dictionaries (hash tables).  
  
For organizing programs, Python supports packages (groups of modules and/or
packages), modules (related code grouped together in a single source file),
classes, methods and functions. For flow control, it provides if/else, while,
and a high-level for statement that loops over any “iterable” object. For
error handling, Python uses (non-resumable) exceptions. A raise statement
throws an exception, and try/except/finally statements specify exception
handlers. Built-in operations throw exceptions when error conditions are
encountered.  
  
In Python, all objects that can be named are said to be "first class." This
means that functions, classes, methods, modules, and all other named objects
can be freely passed around, inspected, and placed in various data structures
(e.g., lists or dictionaries) at run-time. And speaking of objects, Python
also has full support for object-oriented programming including user-defined
classes, inheritance, and run-time binding of methods.  
  
Python has an extensive standard library, which is one of the main reasons for
its popularity. The standard library has more than 100 modules and is always
evolving. Some of these modules include regular expression matching, standard
mathematical functions, threads, operating systems interfaces, network
programming, standard internet protocols (HTTP,FTP, SMTP, etc.), email
handling, XML processing, HTML parsing, and a GUI toolkit (Tcl/Tk).  
  
In addition, there is a very large supply of third-party modules and packages,
most of which are also open source. Here one finds web frameworks (too many to
list!), more GUI toolkits, efficient numerical libraries (including wrappers
for many popular Fortran packages), interfaces to relational databases
(Oracle, MySQL, and others), SWIG (a tool for making arbitrary C++ libraries
available as Python modules), and much more.  
  
A major appeal of Python (and other dynamic programming languages for that
matter) is that seemingly complicated tasks can often be expressed with very
little code. As an example, here is a simple Python script that fetches a web
page, scans it looking for URL references, and prints the first 10 of those.  

    
    
    # Scan the web looking for references  
      
    import re  
    import urllib  
      
    regex = re.compile(r'href="([^"]+)"')  
      
    def matcher(url, max=10):  
        "Print the first several URL references in a given url."  
        data = urllib.urlopen(url).read()  
        hits = regex.findall(data)  
        for hit in hits[:max]:  
            print urllib.basejoin(url, hit)  
      
    matcher("http://python.org")

This program can easily be modified to make a web crawler, and indeed Scott
Hassan has told me that he wrote Google’s first web crawler in Python. Today,
Google employs millions of lines of Python code to manage many aspects of its
operations, from build automation to ad management (Disclaimer: I am currently
a Google employee.)  
  
Underneath the covers, Python is typically implemented using a combination of
a bytecode compiler and interpreter. Compilation is implicitly performed as
modules are loaded, and several language primitives require the compiler to be
available at run-time. Although Python’s de-facto standard implementation is
written in C, and available for every imaginable hardware/software platform,
several other implementations have become popular. Jython is a version that
runs on the JVM and has seamless Java integration. IronPython is a version for
the Microsoft .NET platform that has similar integration with other languages
running on .NET. PyPy is an optimizing Python compiler/interpreter written in
Python (still a research project, being undertaken with EU funding). There’s
also Stackless Python, a variant of the C implementation that reduces reliance
on the C stack for function/method calls, to allow co-routines, continuations,
and microthreads.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[9:17 AM](http://python-history.blogspot.ca/2009/01/introduction-and-
overview.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=4303792486631987225&from=pencil "Edit
Post")

  *[9:29 AM]: 2009-01-13T09:29:00-08:00
  *[9:17 AM]: 2009-01-13T09:17:00-08:00

