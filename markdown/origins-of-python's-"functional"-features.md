

* * *

##### Tuesday, April 21, 2009

###  Origins of Python's "Functional" Features

I have never considered Python to be heavily influenced by functional
languages, no matter what people say or think. I was much more familiar with
imperative languages such as C and Algol 68 and although I had made functions
first-class objects, I didn't view Python as a functional programming
language. However, earlier on, it was clear that users wanted to do much more
with lists and functions.  
  
A common operation on lists was that of mapping a function to each of the
elements of a list and creating a new list. For example:  

>

>     def square(x):

>         return x*x

>  
>     vals = [1, 2, 3, 4]

>     newvals = []

>     for v in vals:

>         newvals.append(square(v))

  
In functional languages such as Lisp and Scheme, operations such as this were
provided as built-in functions of the language. Thus, early users familiar
with such languages found themselves implementing comparable functionality in
Python. For example:  

>

>     def map(f, s):

>         result = []

>         for x in s:

>                 result.append(f(x))

>         return result

>  
>     def square(x):

>         return x*x

>  
>     vals = [1, 2, 3, 4]

>     newvals = map(square,vals)

  
A subtle aspect of the above code is that many people didn't like the fact
that you to define the operation that you were applying to the list elements
as a completely separate function. Languages such as Lisp allowed functions to
simply be defined "on-the-fly" when making the map function call. For example,
in Scheme you can create anonymous functions and perform mapping operations in
a single expression using lambda, like this:  

>

>     (map (lambda (x) (* x x)) '(1 2 3 4))  

  
Although Python made functions first-class objects, it didn't have any similar
mechanism for creating anonymous functions.  
  
In late 1993, users had been throwing around various ideas for creating
anonymous functions as well as various list manipulation functions such as
map(), filter(), and reduce(). For example, Mark Lutz (author of "Programming
Python") posted some code for a function that created functions using exec:  

>

>     def genfunc(args, expr):

>         exec('def f(' + args + '): return ' + expr)

>         return eval('f')

>  
>     # Sample usage

>     vals = [1, 2, 3, 4]

>     newvals = map(genfunc('x', 'x*x'), vals)

  
Tim Peters then followed up with a solution that simplified the syntax
somewhat, allowing users to type the following:  

>

>     vals = [1, 2, 3, 4]

>     newvals = map(func('x: x*x'), vals)

  
It was clear that there was a demand for such functionality. However, at the
same time, it seemed pretty "hacky" to be specifying anonymous functions as
code strings that you had to manually process through exec. Thus, in January,
1994, the map(), filter(), and reduce() functions were added to the standard
library. In addition, the lambda operator was introduced for creating
anonymous functions (as expressions) in a more straightforward syntax. For
example:  

>

>     vals = [1, 2, 3, 4]

>     newvals = map(lambda x:x*x, vals)

  
These additions represented a significant, early chunk of contributed code.
Unfortunately I don't recall the author, and the SVN logs don't record this.
If it's yours, leave a comment! **UPDATE:** As is clear from Misc/HISTORY in
the repo these were contributed by Amrit Prem, a prolific early contributor.  
  
I was never all that happy with the use of the "lambda" terminology, but for
lack of a better and obvious alternative, it was adopted for Python. After
all, it was the choice of the now anonymous contributor, and at the time big
changes required much less discussion than nowadays, [for
better](http://www.python.org/dev/peps/pep-0001/) and [for
worse](http://yellow.bikeshed.com/).  
  
Lambda was really only intended to be a syntactic tool for defining anonymous
functions. However, the choice of terminology had many unintended
consequences. For instance, users familiar with functional languages expected
the semantics of lambda to match that of other languages. As a result, they
found Python’s implementation to be sorely lacking in advanced features. For
example, a subtle problem with lambda is that the expression supplied couldn't
refer to variables in the surrounding scope. For example, if you had this
code, the map() function would break because the lambda function would run
with an undefined reference to the variable 'a'.  

>

>     def spam(s):

>         a = 4

>         r = map(lambda x: a*x, s)

  
There were workarounds to this problem, but they counter-intuitively involved
setting default arguments and passing hidden arguments into the lambda
expression. For example:  

>

>     def spam(s):

>         a = 4

>         r = map(lambda x, a=a: a*x, s)

  
The "correct" solution to this problem was for inner functions to implicitly
carry references to all of the local variables in the surrounding scope that
are referenced by the function. This is known as a "closure" and is an
essential aspect of functional languages. However, this capability was not
introduced in Python until the release of version 2.2 (though it could be
imported "from the future" in Python 2.1).  
  
Curiously, the map, filter, and reduce functions that originally motivated the
introduction of lambda and other functional features have to a large extent
been superseded by list comprehensions and generator expressions. In fact, the
reduce function was removed from list of builtin functions in Python 3.0.
(However, it's not necessary to send in complaints about the removal of
lambda, map or filter: they are staying. :-)  
  
It is also worth nothing that even though I didn't envision Python as a
functional language, the introduction of closures has been useful in the
development of many other advanced programming features. For example, certain
aspects of new-style classes, decorators, and other modern features rely upon
this capability.  
  
Lastly, even though a number of functional programming features have been
introduced over the years, Python still lacks certain features found in “real”
functional programming languages. For instance, Python does not perform
certain kinds of optimizations (e.g., tail recursion). In general, because
Python's extremely dynamic nature, it is impossible to do the kind of compile-
time optimization known from functional languages like Haskell or ML. And
[that's fine](http://hugunin.net/story_of_jython.html).

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[11:05 AM](http://python-history.blogspot.ca/2009/04/origins-of-pythons-
functional-features.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=5909934651334026902&from=pencil "Edit
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
  *[11:05 AM]: 2009-04-21T11:05:00-07:00

