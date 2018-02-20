

* * *

##### Friday, March 6, 2009

###  How Exceptions Came to be Classes

Early on, I knew I wanted Python to use exceptions for error handling.
However, a critical part of making exceptions work is to come up with some
kind of scheme for identifying different kinds of exceptions. In modern
languages (including modern Python :-), exceptions are defined in terms of
user-defined classes. In early Python however, I chose to identify exceptions
by strings. This was unfortunate, but I had two reasons for taking this
approach. First, I learned about exceptions from Modula-3, where exceptions
are unique tokens. Second, I introduced exceptions before I introduced user-
defined classes.  
  
In theory, I suppose I could have created a new type of built-in object to be
used for exceptions, but as every built-in object type required a considerable
coding effort in C, I decided to reuse an existing built-in type. And, since
exceptions are associated with error messages, it seemed natural to use
strings to represent exceptions.  
  
Unfortunately I chose semantics where different string objects would represent
different exceptions, even if they had the same value (i.e. contained the same
sequence of characters). I chose these semantics because I wanted exceptions
defined in different modules to be independent, even if they happened to have
the same value. The idea was that exceptions would always be referenced by
their name, which would imply object identity, never by their value, which
would require string equality.  
  
This approach was influenced by Modula-3’s exceptions, where each exception
declaration creates a unique “exception token” that can’t be confused with any
other exception token. I think I also wanted to optimize testing for
exceptions by using pointer comparisons instead of string value comparisons in
a misguided attempt to prematurely optimize execution time (a rare one – I
usually optimized for my own coding time!). The main reason however is that I
worried about name clashes between unrelated exceptions defined in different
modules. I intended the usage pattern to strictly adhere to the convention of
defining an exception as a global constant in some module, and then using it
by name in all code raising or catching it. (This was also long before certain
string literals would be automatically be “interned”.)  
  
Alas, in practice things never quite work out as you expect. Early Python
users discovered that within the same module, the byte code compiler would
unify string literals (i.e., create a single shared object for all occurrences
of string literals with the same value). Thus, by accident, users found that
exceptions could either be caught be specifying the exception name or the
string literal containing the error message. Well, at least this seemed to
work most of the time. In reality, it only worked for code defined in the same
module---if one tried to catch exceptions using the exception error message in
a different module, it broke mysteriously. Needless to say, this is the sort
of thing that causes widespread confusion.  
  
In 1997, with Python 1.5, I introduced class exceptions into the language.
Although class exceptions have been the recommended approach ever since,
string exceptions were still supported for use by certain legacy applications
through Python 2.5. They were finally removed in Python 2.6.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[9:26 AM](http://python-history.blogspot.ca/2009/03/how-exceptions-came-to-be-
classes.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=7726273395197230422&from=pencil "Edit
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

