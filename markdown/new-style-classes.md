

* * *

##### Monday, June 21, 2010

###  New-style Classes

[After a long hiatus, this blog series is back! I will continue where I left
off last year. I'll try to keep the frequency up.]  
  
Earlier, I described how the addition of classes to Python was essentially an
afterthought. The implementation chosen was definitely an example of Python's
"cut corners" philosophy. However, as Python evolved, various problems with
the class implementation became a popular topic of griping from expert Python
users.  
  
One problem with the class implementation was that there was no way to
subclass built-in types. For example, lists, dictionaries, strings, and other
objects were somehow "special" and could not be specialized via subclassing.
This limitation seemed rather odd for a language that claimed to be "object
oriented."  
  
Another problem was that whole type system just seemed to be "wrong" with user
defined classes. For example, if you created two objects a and b, statements
such as type(a) == type(b) would evaluate as True even if a and b were
instances of completely unrelated classes. Needless to say, developers who
were familiar with languages such as C++ and Java found this be rather odd
since in those languages, classes were tightly integrated with the underlying
type system.  
  
In Python 2.2, I finally took the time to reimplement classes and "do it
right." This change was, by far, the most ambitious rewrite of a major Python
subsystem to date and one could certainly accuse me of a certain amount of
"second-system syndrome" in this effort. Not only did I address the immediate
problem of allowing built-in types to be subclassed, I also added support for
true metaclasses, attempted to fix the naïve method resolution order for
multiple inheritance, and added a variety of other features. A major influence
on this work was the book "Putting Metaclasses to Work" by Ira Forman and
Scott Danforth, which provided me with a specific notion of what a metaclass
is, different from a similar concept in Smalltalk.  
  
An interesting aspect of the class rewrite was that new-style classes were
introduced as a new language feature, not as a strict replacement for old-
style classes. In fact, for backwards compatibility, the old class
implementation remains the default class creation protocol in Python 2. To
create a new-style class, you simply have to subclass an existing new-style
class such as object (which is the root for the new-style class hierarchy).
For example:  

>

>     class A(object):  
>     >  statements  
>     >  ...

The change to new-style classes has been a major success. The new metaclasses
have become popular amongst framework writers and explaining classes has
actually become easier since there were fewer exceptions. The fact that
backwards compatibility was maintained meant that old code has continued to
work as new-style classes have evolved. Finally, although the old-style
classes will eventually be removed from the languages, users are getting used
to writing "class MyClass(object)" to declare a class, which isn't so bad.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[11:07 AM](http://python-history.blogspot.ca/2010/06/new-style-classes.html
"permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=5241351918506086414&from=pencil "Edit
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
  *[4:35 PM]: 2009-04-22T16:35:00-07:00
  *[11:01 AM]: 2009-04-23T11:01:00-07:00
  *[9:14 AM]: 2009-04-24T09:14:00-07:00
  *[11:31 AM]: 2010-06-21T11:31:00-07:00
  *[11:26 AM]: 2010-06-21T11:26:00-07:00
  *[11:18 AM]: 2010-06-21T11:18:00-07:00
  *[11:07 AM]: 2010-06-21T11:07:00-07:00

