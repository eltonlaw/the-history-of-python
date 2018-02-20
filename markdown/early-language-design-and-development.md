

* * *

##### Tuesday, February 3, 2009

###  Early Language Design and Development

From ABC to Python  
  
Python’s first and foremost influence was
[ABC](http://homepages.cwi.nl/%7Esteven/abc/), a language designed in the
early 1980s by Lambert Meertens, Leo Geurts and others at CWI. ABC was meant
to be a teaching language, a replacement for BASIC, and a language and
environment for personal computing. It was designed by first doing a task
analysis of the programming task and then doing several iterations that
included serious user testing. My own role in the ABC group was mainly that of
implementing the language and its integrated editing environment.  
  
Python’s use of indentation comes directly from ABC, but this idea didn’t
originate with ABC--it had already been promoted by Donald Knuth and was a
well-known concept of programming style. (The
[occam](http://en.wikipedia.org/wiki/Occam_programming_language) programming
language also used it.) However, ABC’s authors did invent the use of the colon
that separates the lead-in clause from the indented block. After early user
testing without the colon, it was discovered that the meaning of the
indentation was unclear to beginners being taught the first steps of
programming. The addition of the colon clarified it significantly: the colon
somehow draws attention to what follows and ties the phrases before and after
it together in just the right way.  
  
Python’s major data types also derive from ABC, though with some
modifications. ABC’s lists were really bags or multisets, which were always
kept sorted using a modified B-tree implementation. Its tables were
associative arrays that were similarly kept sorted by key. I found that
neither data type was suitable to represent, for example, the sequence of
lines read from a file, which I anticipated would be a common use case. (In
ABC you'd have to use a table with the line numbers as keys, but that
complicates insertions and deletions.) So I changed the list type into a
flexible array with insert and delete operations, giving users complete
control over the ordering of items in a list. A sort method supported the
occasional need for sorted results.  
  
I also replaced the sorted tables with a hash table implementation. I chose a
hash table because I believed this to be faster and easier to implement than
ABC’s B-tree implementation. The latter was theoretically proven to be
asymptotically optimal in space and time consumption for a wide variety of
operations, but in practice it had turned out to be difficult to implement
correctly due to the complexity of the B-tree algorithms. For the same reason,
the performance was also sub-optimal for small table sizes.  
  
I kept ABC’s immutable tuple data type--Python’s tuple packing and unpacking
operations are taken directly from ABC. Since tuples are internally
represented by arrays, I decided to add array-like indexing and slicing.  
  
One consequence of adding an array-like interface to tuples is that I had to
figure out some way to resolve the edge cases of tuples with length 0 or 1.
One of the rules I took from ABC was that every data type, when printed or
converted to a string, should be represented by an expression that was a valid
input to the language’s parser. So, it followed that I needed to have
notations for 0- and 1-length tuples. At the same time I didn’t want to lose
the distinction between a one-tuple and a bare parenthesized expression, so I
settled for an ugly but pragmatic approach where a trailing comma would turn
an expression into a one-tuple and "()" would represent a zero-tuple. It's
worth nothing that parentheses aren’t normally required by Python’s tuple
syntax, except here--I felt representing the empty tuple by “nothing” could
too easily mask genuine typos.  
  
Python’s strings started with very similar (immutable) semantics as ABC’s
strings, but with a different notation, and 0-based indexing. Since I now had
three indexable types, list, tuples, and strings, I decided to generalize
these to a common concept, the sequence. This generalization made it so
certain core operations such as getting the length (len(s)), indexing (s[i]),
slicing (s[i:j]), and iteration (for i in s) worked the same on any sequence
type.  
  
Numbers are one of the places where I strayed most from ABC. ABC had two types
of numbers at run time; exact numbers which were represented as arbitrary
precision rational numbers and approximate numbers which were represented as
binary floating point with extended exponent range. The rational numbers
didn’t pan out in my view. (Anecdote: I tried to compute my taxes once using
ABC. The program, which seemed fairly straightforward, was taking way too long
to compute a few simple numbers. Upon investigation it turned out that it was
doing arithmetic on numers with thousands of digits of precision, which were
to be rounded to guilders and cents for printing.) For Python I therefore
chose a more traditional model with machine integers and machine binary
floating point. In Python's implementation, these numbers are simply
represented by the C datatypes of long and double respectively.  
  
Feeling that there was still an important use case for unbounded exact
numbers, I added a bignum data type, which I called long. I already had a
bignum implementation that was the result of an unfinished attempt at
improving ABC’s implementation a few years earlier (ABC’s original
implementation, one of my first contributions to ABC, used a decimal
representation internally). Thus, it made sense to me to use this code in
Python.  
  
Although I added bignums to Python, it's important to emphasize that I didn’t
want to use bignums for all integer operations. From profiling Python programs
written by myself and colleagues at CWI, I knew that integer operations
represent a significant fraction of the total program running time of most
programs. By far, the most common use of integers is to index sequences that
fit in memory. Thus, I envisioned machine integers being used for all of the
most-common cases and the extra range of bignums only coming into play when
doing "serious math" or calculating the national debt of the US in pennies.  
  
The Problem With Numbers  
  
The implementation of numbers, especially integers, is one area where I made
several serious design mistakes, but also learned important lessons concerning
Python's design.  
  
Since Python had two different integer types, I needed to figure out some way
to distinguish between the two types in a program. My solution was to require
users to explicitly state when they wanted to use longs by writing numbers
with a trailing L (e.g., 1234L). This is one area where Python violated the
ABC-inspired philosophy of not requiring users to care about a uninteresting
implementation details.  
  
Sadly, this was only a minor detail of much larger problem. A more egregious
error was that my implementation of integers and longs had slightly different
semantics in certain cases! Since the int type was represented as a machine
integer, operations that overflowed would silently clip the result to 32 bits
or whatever the precision of the C long type happened to be. In addition, the
int type, while normally considered signed, was treated as an unsigned number
by bitwise and shift operations and by conversions to/from octal and
hexadecimal representations. Longs, on the other hand, were always considered
signed. Therefore, some operations would produce a different result depending
on whether an argument was represented as an int or a long. For example, given
32-bit arithmetic, 1<<31 (1 shifted left by 31 bits) would produce the largest
negative 32-bit integer, and 1<<32 would produce zero, whereas 1L<<31 (1
represented as long shifted left by 31 bits) would produce a long integer
equal to 2**31, and 1L<<32 would produce 2**32.  
  
To resolve some of these issues I made a simple fix. Rather than having
integer operations silently clip the result, I changed most arithmetic
operations to raise an OverflowError exception when the result didn't fit.
(The only exception to this checking were the "bit-wise" operations mentioned
above, where I assumed that users would expect the behavior of these
operations in C.) Had I not added this check, Python users would have
undoubtedly started writing code that relied on the semantics of signed binary
arithmetic modulo 2**32 (like C users do), and fixing the mistake would have
been a much more painful transition to the community.  
  
Although the inclusion of overflow checking might seem like a minor
implementation detail, a painful debugging experience made me realize that
this was a useful feature. As one of my early programming experiments in
Python, I tried to implement a simple mathematical algorithm, the computation
of “Meertens numbers”, a bit of recreational mathematics invented by Richard
Bird for the occasion of ABC’s primary author’s 25ths anniversary at CWI. The
first few Meertens numbers are small, but when translating the algorithm into
code I hadn’t realized that the intermediate results of the computation are
much larger than 32 bits. It took a long and painful debugging session before
I discovered this, and I decided there and then to address the issue by
checking all integer operations for overflow, and raising an exception
whenever the result could not be represented as a C long. The extra cost of
the overflow check would be dwarfed by the overhead I was already incurring
due to the implementation choice of allocating a new object for the result.  
  
Sadly, I'm sorry to say that raising an overflow exception was not really the
right solution either! At the time, I was stuck on C’s rule “operations on
numeric type T return a result of type T”. This rule was also the reason for
my other big mistake in integer semantics: truncating the result of integer
division, which I will discuss in a later blog post. In hindsight, I should
have made integer operations that overflow promote their result to longs. This
is the way that Python works today, but it took a long time to make this
transition.  
  
Despite the problem with numbers, one very positive thing came out of this
experience. I decided that there should be no undefined result values in
Python – instead, exceptions should always be raised when no correct return
value can be computed. Thus, Python programs would never fail due to undefined
values being silently passed around behind the scenes. This is still an
important principle of the language, both in the language proper and in the
standard library.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[10:53 AM](http://python-history.blogspot.ca/2009/02/early-language-design-
and-development.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=2467627787583063984&from=pencil "Edit
Post")

  *[9:29 AM]: 2009-01-13T09:29:00-08:00
  *[9:17 AM]: 2009-01-13T09:17:00-08:00
  *[3:19 PM]: 2009-01-20T15:19:00-08:00
  *[2:05 PM]: 2009-01-20T14:05:00-08:00
  *[2:01 PM]: 2009-01-27T14:01:00-08:00
  *[6:40 AM]: 2009-01-28T06:40:00-08:00
  *[10:53 AM]: 2009-02-03T10:53:00-08:00

