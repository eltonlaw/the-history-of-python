

* * *

##### Friday, February 27, 2009

###  First-class Everything

[Folks, please don't use the comments section of this blog to ask questions.
If you want to suggest a topic for a future blog entry, send me email. (Use
Google to find my home page, which has my email address.) If you want to
propose a change or discuss the merits of alternative designs, use the python-
ideas mailing list at python.org.]  
  
One of my goals for Python was to make it so that all objects were "first
class." By this, I meant that I wanted all objects that could be named in the
language (e.g., integers, strings, functions, classes, modules, methods, etc.)
to have equal status. That is, they can be assigned to variables, placed in
lists, stored in dictionaries, passed as arguments, and so forth.  
  
The internal implementation of Python made this simple to do. All of Python's
objects were based on a common C data structure that was used everywhere in
the interpreter. Variables, lists, functions, and everything else just used
variations of this one data structure---it just didn't matter if the structure
happened to represent a simple object such as an integer or something more
complicated such as a class.  
  
Although the idea of having "first-class everything" is conceptually simple,
there was still one subtle aspect of classes that I still needed to address---
namely, the problem of making methods first class objects.  
  
Consider this simple Python class (copied from last week's blog post):  

    
    
    class A:  
         def __init__(self,x):  
             self.x = x  
         def spam(self,y):  
            print self.x, y

If methods are going to be first-class objects, then they can be assigned to
other variables and used just like other objects in Python. For example,
someone could write a Python statement such as "s = A.spam". In this case, the
variable "s" refers to a method of a class, which is really just a function.
However, a method is not quite the same as ordinary function. Specifically,
the first argument of a method is supposed to be an instance of the class in
which a method was defined.  
  
To deal with this, I created a type of callable object known as an "unbound
method." An unbound method was really just a thin wrapper around the function
object that implemented a method, but it enforced a restriction that the first
argument had to be an instance of the class in which the method was defined.
Thus, if someone wanted to call an unbound method "s" as a function, they
would have to pass an instance of class "A" as the first argument. For
example, "a = A(); s(a)". (*)  
  
A related problem occurs if someone writes a Python statement that refers to a
method on a specific instance of an object. For example, someone might create
an instance using "a = A()" and then later write a statement such as "s =
a.spam". Here, the variable "s" again refers to a method of a class, but the
reference to that method was obtained through an instance "a" . To handle this
situation, a different callable object known as a "bound method." is used.
This object is also a thin wrapper around the function object for the method.
However, this wrapper implicitly stores the original instance that was used to
obtain the method. Thus, a later statement such as "s()" will call the method
with the instance "a" implicitly set as the first argument.  
  
In reality, the same internal object type is used to represent bound and
unbound methods. One of the attributes of this object contains a reference to
an instance. If set to None, the method is unbound. Otherwise, the method is
bound.  
  
Although bound and unbound methods might seem like an unimportant detail, they
a critical part of how classes work underneath the covers. Whenever a
statement such as "a.spam()" appears in a program, the execution of that
statement actually occurs in two steps. First, a lookup of "a.spam" occurs.
This returns a bound method--a callable object. Next, a function call
operation "()" is applied to that object to invoke the method with user
supplied arguments.  
  
__________  
(*) In Python 3000, the concept of unbound methods has been removed, and the
expression "A.spam" returns a plain function object. It turned out that the
restriction that the first argument had to be an instance of A was rarely
helpful in diagnosing problems, and frequently an obstacle to advanced usages
--- some have called it "duck typing self" which seems an appropriate name.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[11:59 AM](http://python-history.blogspot.ca/2009/02/first-class-
everything.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=8289611853646702775&from=pencil "Edit
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

