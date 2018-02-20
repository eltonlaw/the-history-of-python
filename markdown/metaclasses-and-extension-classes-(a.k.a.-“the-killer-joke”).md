

* * *

##### Friday, April 24, 2009

###  Metaclasses and Extension Classes (a.k.a. “The Killer Joke”)

In Python’s original implementation, classes were first class objects that
could be manipulated just like any other object. However, the process of
creating a class object was something that was set in stone. Specifically,
when you defined a class such as this  

>

>     class ClassName(BaseClass, ...):  
>     >      ...method definitions...

The body of the class would be executed in its own local dictionary. The name
of the class, a tuple of base classes, and this local dictionary would then be
passed to an internal class creation function that was responsible for
creating the class object. Since all of this machinery was hidden away behind
the scenes, it was an implementation detail that users didn’t need to worry
about.  
  
Don Beaudry was the first to point out that this was a missed opportunity for
expert users. Specifically, if classes were simply special kinds of objects,
why couldn’t you create new kinds of classes that could be customized to
behave in different ways? He then suggested a very slight modification to the
interpreter that would allow new kinds of class objects to be created by C
code extension modules. This modification, first introduced in 1995, has long
been known as the “Don Beaudry hook” or “Don Beaudry hack”, where the
ambiguity about the name was an intentional joke. Jim Fulton later generalized
the modification where it remained a part of the language (albeit under-
documented) until it was replaced by true support for metaclasses through the
introduction of new-style classes in Python 2.2 (see below).  
  
The basic idea behind the Don Beaudry hook is that expert users would be able
to create custom class objects if there was some way to supply a user-supplied
function in the final step of class creation. Specifically, if the class name,
base classes, and local dictionary could be passed to a different construction
function, then that function could do whatever it wanted with the information
to create a class object. The only catch was that I didn't want to make any
changes to the class syntax which had already been well-established.  
  
To do this, the hook required you to create a new type object in C that was
callable. Then, when an instance of such a callable type was used as a base
class in a class statement, the class creation code would magically call that
type object instead of creating a standard class object. The behavior of
classes created this way (and their instances) was completely up to the
extension module providing the callable type object.  
  
To modern Python users it may sound strange that this was considered such a
hack. But at the time, type objects were not callable -- e.g. 'int' was not a
built-in type but a built-in function that returned an instance of the int
object, and the int type was neither easily accessible nor callable. User-
defined classes were of course callable, but this was originally special-cased
by the CALL instruction, as these were implemented in a completely different
way than built-in types. Don Beaudry is eventually responsible for planting
the insight in my head that led first to metaclasses and later to new-style
classes and the eventual death of classic classes.  
  
Originally, Don Beaudry’s own set of Python extensions named MESS was the only
user of this feature. However, by the end of 1996, Jim Fulton had developed a
very popular third-party package called Extension Classes, which used the Don
Beaudry hook. The Extension Classes package eventually became unnecessary
after Python 2.2 introduced metaclasses as a standard part of the object
machinery.  
  
In Python 1.5, I removed the requirement to write a C extension in order to
use the Don Beaudry hook. In addition to check for a callable base class type,
the class creation code now also checked for an attribute named “__class__” on
the base class, and would call this if present. I wrote an essay about this
feature that was the first introduction to the idea of metaclasses for many
Python users. Due to the head-exploding nature of the ideas presented therein,
the essay was soon nicknamed “The Killer Joke” (a Monty Python reference).  
  
Perhaps the most lasting contribution of the Don Beaudry hook is the API for
the class creation function, which was carried over to the new metaclass
machinery in Python 2.2. As described earlier, the class creation function is
called with three arguments: a string giving the class name, a tuple giving
the base classes (possibly empty or a singleton), and a dictionary giving the
contents of the namespace in which the indented block with method definitions
(and other class-level code) has been executed. The return value of the class
creation function is assigned to a variable whose name is the class name.  
  
Originally, this was simply the internal API for creating classes. The Don
Beaudry hook used the same call signature and hence it became a public API.
The most important aspect of this API is that the block containing the method
definitions is executed before the class creation function is called. This
places certain restrictions on the effectiveness of metaclasses, since a
metaclass cannot influence the initial contents of the namespace in which the
method definitions are executed.  
  
This was changed in Python 3000, so that now a metaclass can provide an
alternative mapping object in which the class body is executed. In order to
support this, the syntax for specifying an explicit metaclass is also changed:
it uses keyword argument syntax in the list of base classes, which was
introduced for this purpose.  
  
In the next episode I'll write more about how the idea of metaclasses led to
the introduction of new-style classes in 2.2 (and the eventual demise of
classic classes in 3.0).

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[9:14 AM](http://python-history.blogspot.ca/2009/04/metaclasses-and-extension-
classes-aka.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=8375160878003324033&from=pencil "Edit
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

