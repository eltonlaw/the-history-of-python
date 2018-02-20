

* * *

##### Tuesday, August 24, 2010

###  Why Python's Integer Division Floors

I was asked (again) today to explain why integer division in Python returns
the floor of the result instead of truncating towards zero like C.

  

For positive numbers, there's no surprise:

  

>>> 5//2

2

  

But if one of the operands is negative, the result is floored, i.e., rounded
away from zero (towards negative infinity):

  

>>> -5//2

-3

>>> 5//-2

-3

  

This disturbs some people, but there is a good mathematical reason. The
integer division operation (//) and its sibling, the modulo operation (%), go
together and satisfy a nice mathematical relationship (all variables are
integers):

  

a/b = q with remainder r

  

such that

  

b*q + r = a and 0 <= r < b  

  

(assuming a and b are >= 0).

  

If you want the relationship to extend for negative a (keeping b positive),
you have two choices: if you truncate q towards zero, r will become negative,
so that the invariant changes to 0 <= abs(r) < otherwise, you can floor q
towards negative infinity, and the invariant remains 0 <= r < b. [update:
fixed this para]  

  

In mathematical number theory, mathematicians always prefer the latter choice
(see e.g. [Wikipedia](http://en.wikipedia.org/wiki/Modulo_operation)). For
Python, I made the same choice because there are some interesting applications
of the modulo operation where the sign of a is uninteresting. Consider taking
a POSIX timestamp (seconds since the start of 1970) and turning it into the
time of day. Since there are 24*3600 = 86400 seconds in a day, this
calculation is simply t % 86400. But if we were to express times before 1970
using negative numbers, the "truncate towards zero" rule would give a
meaningless result! Using the floor rule it all works out fine.

  

Other applications I've thought of are computations of pixel positions in
computer graphics. I'm sure there are more.

  

For negative b, by the way, everything just flips, and the invariant becomes:

  

0 >= r > b.

  

So why doesn't C do it this way? Probably the hardware didn't do this at the
time C was designed. And the hardware probably didn't do it this way because
in the oldest hardware, negative numbers were represented as "sign +
magnitude" rather than the two's complement representation used these days (at
least for integers). My first computer was a Control Data mainframe and it
used one's complement for integers as well as floats. A pattern of 60 ones
meant negative zero!

  

Tim Peters, who knows where all Python's floating point skeletons are buried,
has expressed some worry about my desire to extend these rules to floating
point modulo. He's probably right; the truncate-towards-negative-infinity rule
can cause precision loss for x%1.0 when x is a very small negative number. But
that's not enough for me to break integer modulo, and // is tightly coupled to
that.

  

PS. Note that I am using // instead of / -- this is Python 3 syntax, and also
allowed in Python 2 to emphasize that you know you are invoking integer
division. The / operator in Python 2 is ambiguous, since it returns a
different result for two integer operands than for an int and a float or two
floats. But that's a totally separate story; see [PEP
238](http://www.python.org/dev/peps/pep-0238/).

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[9:49 AM](http://python-history.blogspot.ca/2010/08/why-pythons-integer-
division-floors.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=7023294333989359916&from=pencil "Edit
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

