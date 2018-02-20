

* * *

##### Tuesday, March 3, 2009

###  How Everything Became an Executable Statement

New users to Python are sometimes surprised to find out that every part of the
language is an executable statement, including function and class definitions.
That means that any statement can appear anywhere in a program. For instance,
a function definition could appear inside an "if" statement if you wanted.  
  
In a very early version of Python’s grammar, this was not the case: grammar
elements that had a “declarative flavor”, like import statements and function
definitions, were allowed only at the top level in a module or script (where
they were being executed in order to become effective). However, at the time I
was adding support for classes, I decided that this was too restrictive.  
  
My reasoning went roughly as follows. Rather than defining the class body as a
series of function declarations only, it seemed to make sense to also allow
regular variable assignments there. However, if I was going to allow that, why
not go one step further and allow arbitrary executable code? Or, taking this
even further, why not allow function declarations inside an “if” statement,
for example? It quickly became clear that this enabled a simplification of the
grammar, since now all uses of statements (whether indented or not) could
share the same grammar rule, and hence the compiler could use the same byte
code generation function for all of them.  
  
Although this reasoning allowed me to simplify the grammar and allowed users
to place Python statements anywhere, this feature did not necessarily enable
certain styles of programming. For example, the Python grammar technically
allowed users to write things such as nested functions even though the
underlying semantics of Python didn't support nested scopes. Therefore, code
such as that would often operate in ways that were unexpected or "broken"
compared to languages that were actually designed with such features in mind.
Over time, many of these "broken" features have been fixed. For example,
nested function definitions only began to work more sanely in Python 2.1.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[12:02 PM](http://python-history.blogspot.ca/2009/03/how-everything-became-
executable.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=5249285308816481989&from=pencil "Edit
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

