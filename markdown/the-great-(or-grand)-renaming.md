

* * *

##### Tuesday, March 31, 2009

###  The Great (or Grand) Renaming

When Python was first created, I always envisioned it as a stand-alone
program, occasionally linking in third-party libraries. The source code
therefore freely defined global names (in the C/linker sense) like ‘object’,
‘getlistitem’, ‘INCREF’ and so on. As Python’s popularity grew, people started
to ask for an “embedded” version of Python, which would itself be a library
that could be linked into other applications – not unlike the way that Emacs
incorporates a Lisp interpreter.  
  
Unfortunately, this embedding was complicated by name clashes between Python’s
global names and those defined by the embedding application – the name
'object’ was especially popular. To deal with this problem, a naming
convention was chosen, whereby all Python globals would have a name starting
with “Py” or “_Py” (for internal names that had to be global for technical
reasons) or “PY” (for macros).  
  
For backwards compatibility reasons (there were already many third party
extension modules) and to ease the transition for core developers (who had the
old names engrained in their brain) there were two phases. In phase one the
linker saw the old names, but the source code used the new names, which were
translated to the old names using a large number of C preprocessor macros. In
phase two the linker saw the new names, but for the benefit of some laggard
extension modules that hadn’t been ported yet, another set of macros now
translated the old names to the new names. In both phases, the code could mix
old and new names and work correctly.  
  
I researched the history of these renamings a bit in our [Subversion
logs](http://svn.python.org/view/python/trunk/). I found
[r4583](http://svn.python.org/view?view=rev&revision=4583) from January 12,
1995, which signalled phase two of the great renaming was started by
introducing the new names to all header files. But in December 1996 the
renaming of .c source files was still going on. Around this time the renaming
seems to have been renamed, and checkin comments often refer to the "Grand
Renaming". The backwards compatibility macros were finally removed in May
2000, as part of the Python 1.6 release effort. The check-in comment for
[r15313](http://svn.python.org/view?view=rev&revision=15313) celebrates this
event.  
  
Much credit goes to Barry Warsaw and Roger Masse, who participated in the
unthankful task of renaming the contentes of file after file after file
(albeit with the help of a script). They also helped with the equally tedious
task of adding unit tests for much of the standard library.  
  
Wikipedia has a reference to an earlier Great Renaming event, which apparently
involved renaming USENET groups. I probably unconsciously remenbered that
event when I named Python's Great Renaming. I also found some references to a
later Grand Renaming in Sphinx, the package used for generating Python's
documentation. Zope also seems to have had a Grand Renaming, and some recent
Py3k discussions also used the term for the PyString -> PyBytes renaming
(although this is a minor one compared to the others).  
  
Great or Grand Renamings are often traumatic events for software developer
communities, since they requires the programmers' brains to be rewired,
documentation to be rewritten, and complicate the integration of patches
created before the renaming but applied after. (This is especially problematic
when unrenamed branches exist.)

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[8:44 AM](http://python-history.blogspot.ca/2009/03/great-or-grand-
renaming.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=8812005943596964114&from=pencil "Edit
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
  *[8:44 AM]: 2009-03-31T08:44:00-07:00

