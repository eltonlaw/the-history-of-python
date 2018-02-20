

* * *

##### Wednesday, June 23, 2010

###  Method Resolution Order

In languages that use multiple inheritance, the order in which base classes
are searched when looking for a method is often called the Method Resolution
Order, or MRO. (In Python this also applies to other attributes.) For
languages that support single inheritance only, the MRO is uninteresting; but
when multiple inheritance comes into play, the choice of an MRO algorithm can
be remarkably subtle. Python has known at least three different MRO
algorithms: classic, Python 2.2 new-style, and Python 2.3 new-style (a.k.a.
C3). Only the latter survives in Python 3.  
  
Classic classes used a simple MRO scheme: when looking up a method, base
classes were searched using a simple depth-first left-to-right scheme. The
first matching object found during this search would be returned. For example,
consider these classes:  

>

>     class A:  
>     >   def save(self): pass  
>     >  
>     > class B(A): pass  
>     >  
>     > class C:  
>     >   def save(self): pass  
>     >  
>     > class D(B, C): pass

If we created an instance x of class D, the classic method resolution order
would order the classes as D, B, A, C. Thus, a search for the method x.save()
would produce A.save() (and not C.save()). This scheme works fine for simple
cases, but has problems that become apparent when one considers more
complicated uses of multiple inheritance. One problem concerns method lookup
under "diamond inheritance." For example:  

>

>     class A:  
>     >   def save(self): pass  
>     >  
>     > class B(A): pass  
>     >  
>     > class C(A):  
>     >   def save(self): pass  
>     >  
>     > class D(B, C): pass

Here, class D inherits from B and C, both of which inherit from class A. Using
the classic MRO, methods would be found by searching the classes in the order
D, B, A, C, A. Thus, a reference to x.save() will call A.save() as before.
However, this is unlikely what you want in this case! Since both B and C
inherit from A, one can argue that the redefined method C.save() is actually
the method that you want to call, since it can be viewed as being "more
specialized" than the method in A (in fact, it probably calls A.save()
anyways). For instance, if the save() method is being used to save the state
of an object, not calling C.save() would break the program since the state of
C would be ignored.  
  
Although this kind of multiple inheritance was rare in existing code, new-
style classes would make it commonplace. This is because all new-style classes
were defined by inheriting from a base class object. Thus, any use of multiple
inheritance in new-style classes would always create the diamond relationship
described above. For example:  

>

>     class B(object): pass  
>     >  
>     > class C(object):  
>     >   def __setattr__(self, name, value): pass  
>     >  
>     > class D(B, C): pass

Moreover, since object defined a number of methods that are sometimes extended
by subtypes (e.g., __setattr__()), the resolution order becomes critical. For
example, in the above code, the method C.__setattr__ should apply to instances
of class D.  
  
To fix the method resolution order for new-style classes in Python 2.2, I
adopted a scheme where the MRO would be pre-computed when a class was defined
and stored as an attribute of each class object. The computation of the MRO
was officially documented as using a depth-first left-to-right traversal of
the classes as before. If any class was duplicated in this search, all but the
last occurrence would be deleted from the MRO list. So, for our earlier
example, the search order would be D, B, C, A (as opposed to D, B, A, C, A
with classic classes).  
  
In reality, the computation of the MRO was more complex than this. I
discovered a few cases where this new MRO algorithm didn't seem to work. Thus,
there was a special case to deal with a situation when two bases classes
occurred in a different order in the inheritance list of two different derived
classes, and both of those classes are inherited by yet another class. For
example:  

>

>     class A(object): pass  
>     > class B(object): pass  
>     > class X(A, B): pass  
>     > class Y(B, A): pass  
>     > class Z(X, Y): pass

Using the tentative new MRO algorithm, the MRO for these classes would be Z,
X, Y, B, A, object. (Here 'object' is the universal base class.) However, I
didn't like the fact that B and A were in reversed order. Thus, the real MRO
would interchange their order to produce Z, X, Y, A, B, object. Intuitively,
this algorithm tried to preserve the order of classes for bases that appeared
first in the search process. For instance, on class Z, the base class X would
be checked first because it was first in the inheritance list. Since X
inherited from A and B, the MRO algorithm would try to preserve that ordering.
This is what I implemented for Python 2.2, but I documented the earlier
algorithm (naïvely thinking it didn't matter much).  
  
However, shortly after the introduction of new-style classes in Python 2.2,
Samuele Pedroni discovered an inconsistency between the documented MRO
algorithm and the results that were actually observed in real-code. Moreover,
inconsistencies were occurring even in code that did not fall under the
special case observed above. After much discussion, it was decided that the
MRO adopted for Python 2.2 was broken and that Python should adopt the C3
Linearization algorithm described in the paper "A Monotonic Superclass
Linearization for Dylan" (K. Barrett, et al, presented at OOPSLA'96).  
  
Essentially, the main problem in the Python 2.2 MRO algorithm concerned the
issue of monotonicity. In a complex inheritance hierarchy, each inheritance
relationship defines a simple set of rules concerning the order in which
classes should be checked. Specifically, if a class A inherits from class B,
then the MRO should obviously check A before B. Likewise, if a class B uses
multiple inheritance to inherit from C and D, then B should be checked before
C and C should be checked before D.  
  
Within a complex inheritance hierarchy, you want to be able to satisfy all of
these possible rules in a way that is monotonic. That is, if you have already
determined that class A should be checked before class B, then you should
never encounter a situation that requires class B to be checked before class A
(otherwise, the result is undefined and the inheritance hierarchy should be
rejected). This is where the original MRO got it wrong and where the C3
algorithm comes into play. Basically, the idea behind C3 is that if you write
down all of the ordering rules imposed by inheritance relationships in a
complex class hierarchy, the algorithm will determine a monotonic ordering of
the classes that satisfies all of them. If such an ordering can not be
determined, the algorithm will fail.  
  
Thus, in Python 2.3, we abandoned my home-grown 2.2 MRO algorithm in favor of
the academically vetted C3 algorithm. One outcome of this is that Python will
now reject any inheritance hierarchy that has an inconsistent ordering of base
classes. For instance, in the previous example, there is an ordering conflict
between class X and Y. For class X, there is a rule that says class A should
be checked before class B. However, for class Y, the rule says that class B
should be checked before A. In isolation, this discrepancy is fine, but if X
and Y are ever combined together in the same inheritance hierarchy for another
class (such as in the definition of class Z), that class will be rejected by
the C3 algorithm. This, of course, matches the Zen of Python's "errors should
never pass silently" rule.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[10:41 AM](http://python-history.blogspot.ca/2010/06/method-resolution-
order.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=9080535281798722395&from=pencil "Edit
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

