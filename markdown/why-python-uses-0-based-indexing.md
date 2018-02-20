

* * *

##### Thursday, October 24, 2013

###  Why Python uses 0-based indexing

I was asked on Twitter why Python uses 0-based indexing, with a link to a new
(fascinating) post on the subject
(<http://exple.tive.org/blarg/2013/10/22/citation-needed/>). I recall thinking
about it a lot; ABC, one of Python's predecessors, used 1-based indexing,
while C, the other big influence, used 0-based. My first few programming
languages (Algol, Fortran, Pascal) used 1-based or variable-based. I think
that one of the issues that helped me decide was slice notation.  
  
Let's first look at use cases. Probably the most common use cases for slicing
are "get the first n items" and "get the next n items starting at i" (the
first is a special case of that for i == the first index). It would be nice if
both of these could be expressed as without awkward +1 or -1 compensations.  
  
Using 0-based indexing, half-open intervals, and suitable defaults (as Python
ended up having), they are beautiful: a[:n] and a[i:i+n]; the former is long
for a[0:n].  
  
Using 1-based indexing, if you want a[:n] to mean the first n elements, you
either have to use closed intervals or you can use a slice notation that uses
start and length as the slice parameters. Using half-open intervals just isn't
very elegant when combined with 1-based indexing. Using closed intervals,
you'd have to write a[i:i+n-1] for the n items starting at i. So perhaps using
the slice length would be more elegant with 1-based indexing? Then you could
write a[i:n]. And this is in fact what ABC did -- it used a different notation
so you could write a@i|n.(See
[http://homepages.cwi.nl/~steven/abc/qr.html#EXPRESSIONS](http://homepages.cwi.nl/%7Esteven/abc/qr.html#EXPRESSIONS).)  
  
But how does the index:length convention work out for other use cases? TBH
this is where my memory gets fuzzy, but I think I was swayed by the elegance
of half-open intervals. Especially the invariant that when two slices are
adjacent, the first slice's end index is the second slice's start index is
just too beautiful to ignore. For example, suppose you split a string into
three parts at indices i and j -- the parts would be a[:i], a[i:j], and a[j:].  
  
So that's why Python uses 0-based indexing.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[8:44 AM](http://python-history.blogspot.ca/2013/10/why-python-uses-0-based-
indexing.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=8737672053383472671&from=pencil "Edit
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

