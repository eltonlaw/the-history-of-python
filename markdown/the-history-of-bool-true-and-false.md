

* * *

##### Monday, November 11, 2013

###  The history of bool, True and False

Writing up the reasons why True and False, when introduced, weren't reserved
words, I realized there's another interesting lesson in the history of
Python's bool type. It was formally introduced in Python 2.3, as a new type
with two constants, and the type was introduced in [PEP
285](http://www.python.org/dev/peps/pep-0285/) ("Adding a bool type").  
  
But bool, True and False were also introduced in Python 2.2.1 (a bugfix
release!). The Misc/NEWS file said:  

> What's New in Python 2.2.1 final?

>

> Release date: 10-Apr-2002

>

> =================================

>

>  
>

>

> Core and builtins

>

>  
>

>

> \- Added new builtin function bool() and new builtin constants True and

>

> False to ease backporting of code developed for Python 2.3. In 2.2,

>

> bool() returns 1 or 0, True == 1, and False == 0.

  
This was the last (and the most criticized) time we added a new feature in a
bugfix release -- we'd never do that these days. Also note that
bool/True/False in 2.2.1 were different from 2.3: in 2.3, bool is a new type;
in 2.2.1, bool() is a built-in function and the constants are just ints.  
  
The chronology is also interesting: the proper new bool type was introduced in
2.3a1, released on Dec 31 2002, well after the above-mentioned 2.2.1 release.
And the final 2.3 release didn't come out until July 29 2003. And yet, the
above comment talks about backporting from 2.3 to 2.2.1. PEP 285 was created
on March 8, 2002, accepted on April 3, and declared final on April 11 (i.e.
after Python 2.2.1 was released). I'm assuming that by then the proper bool
implementation had landed in the 2.3 branch. That's a breakneck pace compared
to how we do things a decade later!

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[4:29 PM](http://python-history.blogspot.ca/2013/11/the-history-of-bool-true-
and-false.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=6096682169298430956&from=pencil "Edit
Post")

Labels: [bool](http://python-history.blogspot.ca/search/label/bool),
[False](http://python-history.blogspot.ca/search/label/False),
[python](http://python-history.blogspot.ca/search/label/python), [python
history](http://python-history.blogspot.ca/search/label/python%20history),
[True](http://python-history.blogspot.ca/search/label/True)

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
  *[8:44 AM]: 2013-10-24T08:44:00-07:00
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
  *[2:40 PM]: 2013-11-10T14:40:00-08:00
  *[4:29 PM]: 2013-11-11T16:29:00-08:00

