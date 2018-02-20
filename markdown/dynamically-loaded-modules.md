

* * *

##### Tuesday, March 17, 2009

###  Dynamically Loaded Modules

Python’s implementation architecture made it easy to write extension modules
written in C right from the start. However, in the early days, dynamic loading
technology was obscure enough that such extensions had to be statically linked
into Python interpreter at build time. To do this, C extension modules had to
be added to a shell script that was used to generate the Makefile for Python
and all of its extension modules.  
  
Although this approach worked for small projects, the Python community started
producing new extension modules at an unanticipated rate, and demanded that
extension modules could be compiled and loaded separately. Shortly thereafter,
code interfacing to the platform-specific dynamic linking API was contributed
which allowed the import statement to go out to disk looking for a shared
library as well as a “.py” file. The first mention of dynamic loading in the
CVS logs stems from January 1992 and most major platforms were supported by
the end of 1994.  
  
The dynamic linking support proved to be very useful, but also introduced a
maintenance nightmare. Each platform used a different API and some platforms
had additional constraints. In January 1995, the dynamic linking support was
restructured so that all the dynamic linking code was concentrated in a single
source file. However, the approach resulted in a large file cluttered with
conditional compilation directives (#ifdef). In December 1999, it was
restructured again with the help of Greg Stein so that the platform-specific
code for each platform was placed in a file specific to that platform (or
family of platforms).  
  
Even though Python supported dynamically loadable modules, the procedure for
building such modules often remained a mystery to many users. An increasingly
large number of users were building modules--especially with the introduction
of extension building tools such as SWIG. However, a user wishing to
distribute an extension module faced major hurdles getting the module to
compile on all possible combinations of platforms, compilers, and linkers. In
a worst-case scenario, a user would have to write their own Makefile and
configuration script for setting the right compiler and linker flags.
Alternatively, a user could also add their extension module to Python's own
Makefile and perform a partial Python rebuild to have the module compiled with
the right options. However, this required end users to have a Python source
distribution on-hand.  
  
Eventually, a Python extension building tool called distutils was invented
that allowed building and installing extension modules from anywhere. The
necessary compiler and linker options were written by Python’s makefile to a
data file, which was then consulted by distutils when building extension
modules. Largely written by Greg Ward, the first versions of distutils were
distributed separately, to support older Python versions. Starting with Python
1.6 it was integrated into Python distributions as a standard library module.  
  
It is worth noting that distutils does far more than simply building extension
modules from C source code. It can also install pure Python modules and
packages, create Windows installer executables, and run third party tools such
as SWIG. Alas, its complexity has caused many folks to curse it, and it has
not received the maintenance attention it deserved. As a result, in recent
times, 3rd party alternatives (especially ez_install, a.k.a. "eggs") have
become popular, unfortunately causing fragmentation in the development
community, as well as complaints whenever it doesn't work. It seems that the
problem in its full generality is just inherently difficult.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[1:07 PM](http://python-history.blogspot.ca/2009/03/dynamically-loaded-
modules.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=1769026926729045356&from=pencil "Edit
Post")

  *[9:29 AM]: 2009-01-13T09:29:00-08:00
  *[9:17 AM]: 2009-01-13T09:17:00-08:00
  *[3:19 PM]: 2009-01-20T15:19:00-08:00
  *[2:05 PM]: 2009-01-20T14:05:00-08:00
  *[2:01 PM]: 2009-01-27T14:01:00-08:00
  *[6:40 AM]: 2009-01-28T06:40:00-08:00
  *[10:53 AM]: 2009-02-03T10:53:00-08:00
  *[11:27 AM]: 2009-02-10T11:27:00-08:00
  *[11:25 AM]: 2009-02-18T11:25:00-08:00
  *[11:59 AM]: 2009-02-27T11:59:00-08:00
  *[12:02 PM]: 2009-03-03T12:02:00-08:00
  *[9:26 AM]: 2009-03-06T09:26:00-08:00
  *[1:31 PM]: 2009-03-10T13:31:00-07:00
  *[1:07 PM]: 2009-03-17T13:07:00-07:00

