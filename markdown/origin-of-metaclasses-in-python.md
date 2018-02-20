

* * *

##### Thursday, October 24, 2013

###  Origin of metaclasses in Python

There was some speculation on python-ideas today on whether Python's metaclass
design came from Ruby. It did not. And as long as we are speculating about the
origins of language features, I feel the need to set the record straight.

  
I was not inspired by Ruby at that point (or ever :-). Ruby was in fact
inspired by Python. Mats once told me that his inspiration was 20% Python, 80%
Perl, and that Larry Wall is his hero.  

I wrote about metaclasses in Python in 1998:
[http://www.python.org/doc/essays/metaclasses/](http://www.python.org/doc/essays/metaclasses/).

New-style classes were just the second or third iteration of the idea.

I was inspired to implement new-style classes by a very specific book,
"Putting Metaclasses to Work" by Ira Forman and Scott Danforth
([http://www.amazon.com/Putting-Metaclasses-Work-Ira-
Forman/dp/0201433052](http://www.amazon.com/Putting-Metaclasses-Work-Ira-
Forman/dp/0201433052)).  

But even Python's original design (in 1990, published in 1991) had the notion
that 'type' was itself an object. The type pointer in any object has always
been a pointer to a special object, whose "data" was a bunch of C function
pointers implementing the behavior of other objects, similar to a C++ vtable.
The type of a type was always a special type object, which you could call a
meta-type, to be recognized because it was its own type.  

I was only vaguely aware of Smalltalk at the time; I remember being surprised
by its use of metaclasses (which is quite different from that in Python or
Ruby!) when I read about them much later. Smalltalk's bytecode was a bigger
influence of Python's bytecode though. I'd read about it in a book by Adele
Goldberg and others, I believe "Smalltalk-80: The Language and its
Implementation" ([http://www.amazon.com/Smalltalk-80-The-Language-its-
Implementation/dp/0201113716](http://www.amazon.com/Smalltalk-80-The-Language-
its-Implementation/dp/0201113716)).

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[9:58 AM](http://python-history.blogspot.ca/2013/10/origin-of-metaclasses-in-
python.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=3146444532158366150&from=pencil "Edit
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
  *[10:41 AM]: 2010-06-23T10:41:00-07:00
  *[8:39 AM]: 2010-06-29T08:39:00-07:00
  *[9:49 AM]: 2010-08-24T09:49:00-07:00
  *[4:13 PM]: 2011-07-08T16:13:00-07:00
  *[9:58 AM]: 2013-10-24T09:58:00-07:00

