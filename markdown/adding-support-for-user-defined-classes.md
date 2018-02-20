

* * *

##### Wednesday, February 18, 2009

###  Adding Support for User-defined Classes

Believe it or not, classes were added late during Python’s first year of
development at CWI, though well before the first public release. However, to
understand how classes were added, it first helps to know a little bit about
how Python is implemented.  
  
Python is implemented in C as a classic stack-based byte code interpreter or
“virtual machine” along with a collection of primitive types also implemented
in C. The underlying architecture uses “objects” throughout, but since C has
no direct support for objects, they are implemented using structures and
function pointers. The Python virtual machine defines several dozen standard
operations that every object type may or must implement (for example, “get
attribute”, “add” and “call”). An object type is then represented by a
statically allocated structure containing a series of function pointers, one
for each standard operation. These function pointers are typically initialized
with references to static functions. However, some operations are optional,
and the object type may leave the function pointer NULL if it chooses not to
implement that operation. In this case, the virtual machine either generates a
run-time error or, in some cases, provides a default implementation of the
operation. The type structure also contains various data fields, one of which
is a reference to a list of additional methods that are unique to this type,
represented as an array of structures containing a string (the method name)
and a function pointer (its implementation) each. Python’s unique approach to
introspection comes from its ability to make the type structure itself
available at run-time as an object like all others.  
  
An important aspect of this implementation is that it is completely C-centric.
In fact, all of the standard operations and methods are implemented by C
functions. Originally the byte code interpreter only supported calling pure
Python functions and functions or methods implemented in C. I believe my
colleague Siebren van der Zee was the first to suggest that Python should
allow class definitions similar to those in C++ so that objects could also be
implemented in Python.  
  
To implement user-defined objects, I settled on the simplest possible design;
a scheme where objects were represented by a new kind of built-in object that
stored a class reference pointing to a "class object" shared by all instances
of the same class, and a dictionary, dubbed the "instance dictionary", that
contained the instance variables.  
  
In this implementation, the instance dictionary would contain the instance
variables of each individual object whereas the class object would contain
stuff shared between all instances of the same class--in particular, methods.
In implementing class objects, I again chose the simplest possible design; the
set of methods of a class were stored in a dictionary whose keys are the
method names. This, I dubbed the class dictionary. To support inheritance,
class objects would additionally store a reference to the class objects
corresponding to the base classes. At the time, I was fairly naïve about
classes, but I knew about multiple inheritance, which had recently been added
to C++. I decided that as long as I was going to support inheritance, I might
as well support a simple-minded version of multiple inheritance. Thus, every
class object could have one or more base classes.  
  
In this implementation, the underlying mechanics of working with objects are
actually very simple. Whenever changes are made to instance or class
variables, those changes are simply reflected in the underlying dictionary
object. For example, setting an instance variable on an instance updates its
local instance dictionary. Likewise, when looking up the value of a instance
variable of an object, one merely checks its instance dictionary for the
existence of that variable. If the variable is not found there, things become
a little more interesting. In that case, lookups are performed in the class
dictionary and then in the class dictionaries of each of the base classes.  
  
The process of looking up attributes in the class object and base classes is
most commonly associated with locating methods. As previously mentioned,
methods are stored in the dictionary of a class object which is shared by all
instances of the same class. Thus, when a method is requested, you naturally
won't find it in the instance dictionary of each individual object. Instead,
you have to look it up in the class dictionary, and then ask each of the base
classes in turn, stopping when a hit is found. Each of the base classes then
implements the same algorithm recursively. This is commonly referred to as the
depth-first, left-to-right rule, and has been the default method resolution
order (MRO) used in most versions of Python. More modern releases have adapted
a more sophisticated MRO, but that will be discussed in a later blog.  
  
In implementing classes, one of my goals was to keep things simple. Thus,
Python performs no advanced error checking or conformance checking when
locating methods. For example, if a class overrides a method defined in a base
class, no checks are performed to make sure that the redefined method has the
same number of arguments or that it can be called in the same way as the
original base-class method. The above method resolution algorithm merely
returns the first method found and calls it with whatever arguments the user
has supplied.  
  
A number of other features also fall out of this design. For instance, even
though the class dictionary was initially envisioned as a place to put
methods, there was no inherent reason why other kinds of objects couldn't be
placed there as well. Thus, if objects such as integers or strings are stored
in the class dictionary, they become what are known as class variables---
variables shared by all instances of a given class instead of being stored
inside each instance.  
  
Although the implementation of classes is simple, it also provides a
surprisingly degree of flexibility. For instance, the implementation not only
makes classes “first-class objects”, which are easily introspected at run
time, it also makes it possible to modify a class dynamically. For example,
methods can be added or modified by simply updating the class dictionary after
a class object has already been created! (*) The dynamic nature of Python
means that these changes have an immediate effect on all instances of that
class or of any of its subclasses. Likewise, individual objects can be
modified dynamically by adding, modifying, and deleting instance variables (a
feature that I later learned made Python's implementation of objects more
permissive than that found in Smalltalk which restricts the set of attributes
to those specified at the time of object creation).  
  
Development of the class Syntax  
  
Having designed the run-time representations for user-defined classes and
instances, my next task was to design the syntax for class definitions, and in
particular for the method definitions contained therein. A major design
constraint was that I didn’t want to add syntax for methods that differed from
the syntax for functions. Refactoring the grammar and the byte code generator
to handle such similar cases differently felt like a huge task. However, even
if I was successful in keeping the grammar the same, I still had to figure out
some way to deal with instance variables. Initially, I had hoped to emulate
implicit instance variables as seen in C++. For example, in C++, classes are
defined by code like this:  

    
    
      
    class A {  
    public:  
       int x;  
       void spam(int y) {  
            printf("%d %d\n", x, y);  
       }  
    };  
    

  
In this class, an instance variable x has been declared. In methods,
references to x implicitly refer to the corresponding instance variable. For
example, in the method spam(), the variable x is not declared as either
function parameter or as local variable However, since the class has declared
an instance variable with that name, references to x simply refer to that
variable. Although I had hoped to provide something similar in Python, it
quickly became clear that such an approach would be impossible because there
was no way to elegantly distinguish instance variables from local variables in
a language without variable declarations.  
  
In theory, getting the value of instance variables would be easy enough.
Python already had a search order for unqualified variable names: locals,
globals, and built-ins. Each of these were represented as a dictionary mapping
variable names to values. Thus, for each variable reference, a series of
dictionaries would be searched until a hit was found. For example, when
executing a function with a local variable p, and a global variable q, a
statement like “print p, q” would look up p in the first dictionary in the
search order, the dictionary containing local variables, and find a match.
Next it would look up q in the first dictionary, find no match, then look it
up in the second dictionary, the global variables, and find a match.  
  
It would have been easy to add the current object’s instance dictionary in
front of this search list when executing a method. Then, in a method of an
object with an instance variable x and local variable y, a statement like
“print x, y” would find x in the instance dictionary (the first dictionary on
the search path) and y in the local variable dictionary (the second
dictionary).  
  
The problem with this strategy is that it falls apart for setting instance
variables. Python’s assignment doesn’t search for the variable name in the
dictionaries, but simply adds or replaces the variable in the first dictionary
in the search order, normally the local variables. This has the effect that
variables are always created in the local scope by default (although it should
be noted that there is a “global declaration” to override this on a per-
function, per-variable basis.)  
  
Without changing this simple-minded approach to assignment, making the
instance dictionary the first item in the search order would make it
impossible to assign to local variables in a method. For example, if you had a
method like this  

    
    
      
    def spam(y):  
        x = 1         
        y = 2         
    

  
The assignments to x and y would overwrite the instance variable x and create
a new instance variable y that shadowed the local variable y. Swapping
instance variables and local variables in the search order would merely
reverse the problem, making it impossible to assign to instance variables.  
  
Changing the semantics of assignment to assign to an instance variable if one
already existed and to a local otherwise wouldn’t work either, since this
would create a bootstrap problem: how does an instance variable get created
initially? A possible solution might have been to require explicit declaration
of instance variables as was the case for global variables, but I really
didn’t want to add a feature like that given that that I had gotten this far
without any variable declarations at all. Plus, the extra specification
required for indicating a global variable was more of a special case that was
used sparingly in most code. Requiring a special specification for instance
variables, on the other hand, would have to be used almost everywhere in a
class. Another possible solution would have been to make instance variables
lexically distinct. For example, having instance variables start with a
special character such as @ (an approach taken by Ruby) or by having some kind
of special naming convention involving prefixes or capitalization. Neither of
these appealed to me (and they still don't).  
  
Instead, I decided to give up on the idea of implicit references to instance
variables. Languages like C++ let you write this->foo to explicitly reference
the instance variable foo (in case there’s a separate local variable foo).
Thus, I decided to make such explicit references the only way to reference
instance variables. In addition, I decided that rather than making the current
object ("this") a special keyword, I would simply make "this" (or its
equivalent) the first named argument to a method. Instance variables would
just always be referenced as attributes of that argument.  
  
With explicit references, there is no need to have a special syntax for method
definitions nor do you have to worry about complicated semantics concerning
variable lookup. Instead, one simply defines a function whose first argument
corresponds to the instance, which by convention is named "self." For example:  

    
    
      
    def spam(self,y):  
        print self.x, y  
    

  
This approach resembles something I had seen in Modula-3, which had already
provided me with the syntax for import and exception handling. Modula-3
doesn’t have classes, but it lets you create record types containing fully
typed function pointer members that are initialized by default to functions
defined nearby, and adds syntactic sugar so that if x is such a record
variable, and m is a function pointer member of that record, initialized to
function f, then calling x.m(args) is equivalent to calling f(x, args). This
matches the typical implementation of objects and methods, and makes it
possible to equate instance variables with attributes of the first argument.  
  
The remaining details of Python’s class syntax follow from this design or from
the constraints imposed by the rest of the implementation. Keeping with my
desire for simplicity, I envisioned a class statement as a series of method
definitions, which are syntactically identical to function definitions even
though by convention, they are required to have a first argument named "self".
In addition, rather than devising a new syntax for special kinds of class
methods (such as initializers and destructors), I decided that these features
could be handled by simply requiring the user to implement methods with
special names such as __init__, __del__, and so forth. This naming convention
was taken from C where identifiers starting with underscores are reserved by
the compiler and often have special meaning (e.g., macros such as __FILE__ in
the C preprocessor).  
  
Thus, I envisioned that a class would be defined by code that looked like
this:  

    
    
      
    class A:  
         def __init__(self,x):  
             self.x = x  
         def spam(self,y):  
            print self.x, y  
    

  
Again, I wanted to reuse as much of my earlier code as possible. Normally, a
function definition is an executable statement that simply sets a variable in
the current namespace referencing the function object (the variable name is
the function name). Thus, rather than coming up with an entirely different
approach for handling classes, it made sense to me to simply interpret the
class body as a series of statements that were executed in a new namespace.
The dictionary of this namespace would then be captured and used to initialize
the class dictionary and create a class object. Underneath the covers, the
specific approach taken is to turn the class body into an anonymous function
that executes all of the statements in the class body and then returns the
resulting dictionary of local variables. This dictionary is then passed to a
helper function that creates a class object. Finally, this class object is
then stored in a variable in the surrounding scope, whose name is the class
name. Users are often surprised to learn that any sequence of valid Python
statements can appear in a class body. This capability was really just a
straightforward extension of my desire to keep the syntax simple as well as
not artificially limiting what might possibly be useful.  
  
A final detail is the class instantiation (instance creation) syntax. Many
languages, like C++ and Java, use a special operator, “new”, to create new
class instances. In C++ this may be defensible since class names have a rather
special status in the parser, but in Python this is not the case. I quickly
realized that, since Python’s parser doesn’t care what kind of object you
call, making the class object itself callable was the right, “minimal”
solution, requiring no new syntax. I may have been ahead of my time here---
today, factory functions are often the preferred pattern for instance
creation, and what I had done was simply to turn each class into its own
factory.  
  
Special Methods  
  
As briefly mentioned in the last section, one of my main goals was to keep the
implementation of classes simple. In most object oriented languages, there are
a variety of special operators and methods that only apply to classes. For
example, in C++, there is a special syntax for defining constructors and
destructors that is different than the normal syntax used to define ordinary
function and methods.  
  
I really didn't want to introduce additional syntax to handle special
operations for objects. So instead, I handled this by simply mapping special
operators to a predefined set of "special method" names such as __init__ and
__del__. By defining methods with these names, users could supply code related
to the construction and destruction of objects.  
  
I also used this technique to allow user classes to redefine the behavior of
Python's operators. As previously noted, Python is implemented in C and uses
tables of function pointers to implement various capabilities of built-in
objects (e.g., “get attribute”, “add” and “call”). To allow these capabilities
to be defined in user-defined classes, I mapped the various function pointers
to special method names such as __getattr__, __add__, and __call__. There is a
direct correspondence between these names and the tables of function pointers
one has to define when implementing new Python objects in C.  
  
__________  
(*) Eventually, new-style classes made it necessary to control changes to the
class __dict__; you can still dynamically modify a class, but you must use
attribute assignment rather than using the class __dict__ directly.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[11:25 AM](http://python-history.blogspot.ca/2009/02/adding-support-for-user-
defined-classes.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=1132767206472588337&from=pencil "Edit
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

