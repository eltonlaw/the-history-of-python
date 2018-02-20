

* * *

##### Tuesday, February 10, 2009

###  Python's Use of Dynamic Typing

An important difference between [ABC](http://homepages.cwi.nl/%7Esteven/abc/)
and Python is the general flavor of the type system. ABC is statically typed
which meant that the ABC compiler analyzes the use of types in a program and
decides whether they are used consistently. If not, the program is rejected
and its execution cannot be started. Unlike most statically typed languages of
its days, ABC used type inference (not unlike
[Haskell](http://www.haskell.org/)) instead of explicit type declarations as
you find in languages such as in C. In contrast, Python is dynamically typed.
The Python compiler is blissfully unaware of the types used in a program, and
all type checking is done at run time.  
  
Although this might seem like a large departure from ABC, it is not as
different as you might imagine. Unlike other statically typed languages, ABC
doesn't (didn't? it's pretty much purely historic now :-) exclusively rely on
static type checking to keep the program from crashing, but has a run-time
library that checks the argument types for all operations again each time they
are executed. This was done in part as a sanity check for the compiler’s type-
checking algorithms, which were not fully implemented in the initial prototype
implementation of the language. The runtime library was also useful as a
debugging aid since explicit run time type checking could produce nice error
messages (aimed at the implementation team), instead of the core dumps that
would ensue if the interpreter were to blindly go ahead with an operation
without checking if the arguments make sense.  
  
However, the most important reason why ABC has run time type checking in
addition to static type checking is that it is interactive. In an interactive
session, the user types ABC statements and definitions which are executed as
soon as they are completed. In an interactive session, it is possible to
create a variable as a number, delete it, and then to recreate it (in other
words, create another variable with the same name) as a string. Inside a
single procedure, it would be a static typing error to use the same variable
name first as a number and then as a string, but it would not be reasonable to
enforce such type checking across different statements entered in an
interactive session, as the accidental creation of a variable named x as a
number would forever forbid the creation of a variable x with a different
type! So as a compromise, ABC uses dynamic type checking for global variables,
but static type checking for local variables. To simplify the implementation,
local variables are dynamically type checked as well.  
  
Thus, it is only a small step from ABC’s implementation approach to type
checking to Python’s approach--Python simply drops the compile-time type
checking completely. This is entirely in line with Python’s “corner-cutting”
philosophy as it’s a simplification of the implementation that does not affect
the eventual safety, since all type errors are caught at run time before they
can cause the Python interpreter to malfunction.  
  
However, once you decide on dynamic typing, there is no way to go back. ABC’s
built-in operations were carefully designed so that the type of the arguments
could be deduced from the form of the operation. For example, from the
expression “x^y” the compiler would deduce that variables x and y were
strings, as well as the expression result. In Python, such deductions cannot
generally be made. For example, the expression “x+y” could be a string
concatenation, a numeric addition, or an overloaded operation on user-defined
types.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[11:27 AM](http://python-history.blogspot.ca/2009/02/pythons-use-of-dynamic-
typing.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=2116332114530101341&from=pencil "Edit
Post")

  *[9:29 AM]: 2009-01-13T09:29:00-08:00
  *[9:17 AM]: 2009-01-13T09:17:00-08:00
  *[3:19 PM]: 2009-01-20T15:19:00-08:00
  *[2:05 PM]: 2009-01-20T14:05:00-08:00
  *[2:01 PM]: 2009-01-27T14:01:00-08:00
  *[6:40 AM]: 2009-01-28T06:40:00-08:00
  *[10:53 AM]: 2009-02-03T10:53:00-08:00
  *[11:27 AM]: 2009-02-10T11:27:00-08:00

