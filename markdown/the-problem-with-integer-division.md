

* * *

##### Tuesday, March 10, 2009

###  The Problem with Integer Division

Python's handling of integer division is an example of early mistake with huge
consequences. As mentioned earlier, when Python was created, I abandoned the
approach to numbers that had been used in ABC. For example, in ABC, when you
divided two integers, the result was an exact rational number representing the
result. In Python however, integer division truncated the result to an
integer.  
  
In my experience, rational numbers didn't pan out as ABC's designers had
hoped. A typical experience would be to write a simple program for some
business application (say, doing one’s taxes), and find that it was running
much slower than expected. After some debugging, the cause would be that
internally the program was using rational numbers with thousands of digits of
precision to represent values that would be truncated to two or three digits
of precision upon printing. This could be easily fixed by starting an addition
with an inexact zero, but this was often non-intuitive and hard to debug for
beginners.  
  
So with Python, I relied on the other numerical model with which I was
familiar, C. C has integers and floating point numbers of various sizes. So, I
chose to represent Python integers by a C long (guaranteeing at least 32 bits
of precision) and floating point numbers by a C double. I then added an
arbitrary precision integer type which I called "long."  
  
The major mistake was that I also borrowed a rule that makes sense in C but
not so much in a very-high-level language. For the standard arithmetic
operations, including division, the result would always be the same type as
the operands. To make matters worse, I initially used another misguided rule
that forbade mixed-mode arithmetic, with the aim of making the type
implementations independent from each other. So, originally you couldn’t add
an int to a float, or even an int to a long. After Python was released
publicly, Tim Peters quickly convinced me that this was a really bad idea, and
I introduced mixed-mode arithmetic with the usual coercion rules. For example,
mixing an int and a long operand would convert the argument of type int to
long and return a long result and mixing either with float would convert the
int or long argument to float and return a float result..  
  
Unfortunately, the damage was done--integer division returned an integer
result. You might be wondering "Why was this so bad?" Was this really just an
ado about nothing? Historically, the proposal to change this has had some
tough opposition from folks who believed that learning about integer division
was one of the more useful "rites of passage" for all programmers. So let me
explain the reasons for considering this a design bug.  
  
When you write a function implementing a numeric algorithm (for example,
calculating the phase of the moon) you typically expect the arguments to be
specified as floating point numbers. However, since Python doesn’t have type
declarations, nothing is there to stop a caller from providing you with
integer arguments. In a statically typed language, like C, the compiler will
coerce the arguments to floats, but Python does no such thing – the algorithm
is run with integer values until the wonders of mixed-mode arithmetic produce
intermediate results that are floats.  
  
For everything except division, integers behave the same as the corresponding
floating point numbers. For example, 1+1 equals 2 just as 1.0+1.0 equals 2.0,
and so on. Therefore one can easily be misled to expect that numeric
algorithms will behave regardless of whether they execute with integer or
floating point arguments. However, when division is involved, and the
possibility exists that both operands are integers, the numeric result is
silently truncated, essentially inserting a potentially large error into the
computation. Although one can write defensive code that coerces all arguments
to floats upon entry, this is tedious, and it doesn’t enhance the readability
or maintainability of the code. Plus, it prevents the same algorithm from
being used with complex arguments (although that may be highly special cases).  
  
Again, all of this is an issue because Python doesn’t coerce arguments
automatically to some declared type. Passing an invalid argument, for example
a string, is generally caught quickly because few operations accept mixed
string/numeric operands (the exception being multiplication). However, passing
an integer can cause an answer that is close to the correct answer but has a
much larger error – which is difficult to debug or even notice. (This recently
happened to me in a program that draws an analog clock – the positions of the
hands were calculated incorrectly due to truncation, but the error was barely
detectable except at certain times of day.)  
  
Fixing integer division was no easy task due to programs that rely on the
behavior of integer truncation. A truncating division operator (//) was added
to the language to provide the same functionality. In addition, a mechanism
("from __future__ import division") was introduced by which the new integer
division semantics could be enabled.Finally , a command line flag (-Qxxx) was
added both to change the behavior and to aid in program conversion.
Fortunately, the correct behavior has become the default behavior in Python
3000.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[1:31 PM](http://python-history.blogspot.ca/2009/03/problem-with-integer-
division.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=7537129625622057460&from=pencil "Edit
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

