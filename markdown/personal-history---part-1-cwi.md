

* * *

##### Tuesday, January 20, 2009

###  Personal History - part 1, CWI

Python’s early development started at a research institute in Amsterdam called
[CWI](http://www.cwi.nl/), which is a Dutch acronym for a phrase that
translates into English as Centre for Mathematics and Computer Science. CWI is
an interesting place; funded by the Dutch government’s Department of Education
and other research grants, it conducts academic-level research into computer
science and mathematics. At any given time there are plenty of Ph.D. students
wandering about and old-timers in the profession may still remember its
original name, the Mathematical Centre. Under this name, it was perhaps most
famous for the invention of [Algol 68](http://en.wikipedia.org/wiki/ALGOL_68).  
  
I started working at CWI in late 1982, fresh out of university, as a
programmer in the
[ABC](http://en.wikipedia.org/wiki/ABC_%28programming_language%29) group led
by [Lambert Meertens](http://en.wikipedia.org/wiki/Lambert_Meertens) and
[Steven Pemberton](http://en.wikipedia.org/wiki/Steven_Pemberton). After 4 or
5 years the ABC project was terminated due to the lack of obvious success and
I moved to CWI’s
[Amoeba](http://en.wikipedia.org/wiki/Amoeba_distributed_operating_system)
group led by [Sape Mullender](http://www.huygens.org/sape/). Amoeba was a
micro-kernel-based distributed system being jointly developed by CWI and the
[Vrije Universiteit of
Amsterdam](http://en.wikipedia.org/wiki/Vrije_Universiteit), under leadership
of [Andrew Tanenbaum](http://en.wikipedia.org/wiki/Andrew_S._Tanenbaum). In
1991 Sape left CWI for a professorship at the [University of
Twente](http://en.wikipedia.org/wiki/University_of_Twente) and I ended up in
the newly formed CWI multimedia group led by [Dick
Bulterman](http://homepages.cwi.nl/%7Edcab/).  
  
Python is a direct product of my experience at CWI. As I explain later, ABC
gave me the key inspiration for Python, Amoeba the immediate motivation, and
the multimedia group fostered its growth. However, so far as I know, no funds
at CWI were ever officially earmarked for its development. Instead, it merely
evolved as an important tool for use in both the Amoeba and multimedia groups.  
  
My original motivation for creating Python was the perceived need for a higher
level language in the Amoeba project. I realized that the development of
system administration utilities in C was taking too long. Moreover, doing
these in the Bourne shell wouldn’t work for a variety of reasons. The most
important one was that as a distributed micro-kernel system with a radically
new design, Amoeba’s primitive operations were very different (and finer-
grain) than the traditional primitive operations available in the Bourne
shell. So there was a need for a language that would “bridge the gap between C
and the shell.” For a long time, this was Python’s main catchphrase.  
  
At this point, you might ask "why not port an existing language?" In my view,
there weren’t a lot of suitable languages around at that time. I was familiar
with Perl 3, but it was even more tied to Unix than the Bourne shell. I also
didn’t like Perl’s syntax--my tastes in programming language syntax were
strongly influenced by languages like [Algol
60](http://en.wikipedia.org/wiki/ALGOL), Pascal, Algol 68 (all of which I had
learned early on), and last but not least, ABC, on which I’d spent four years
of my life. So, I decided to design a language of my own which would borrow
everything I liked from ABC while at the same time fixing all its problems (as
I perceived them).  
  
The first problem I decided to fix was the name! As it happened, the ABC team
had some trouble picking a name for its language. The original name for the
language, B, had to be abandoned because of confusion with another language
named B, that was older and better known. In any case, B was meant as a
working title only (the joke was that B was the name of the variable
containing the name of the language--hence the italics). The team had a public
contest to come up with a new name, but none of the submissions made the cut,
and in the end, the internal back up candidate prevailed. The name was meant
to convey the idea that the language made programming “as simple as ABC”, but
it never convinced me all that much.  
  
So, rather than over-analyzing the naming problem, I decided to under-analyze
it. I picked the first thing that came to mind, which happened to be [Monty
Python’s Flying
Circus](http://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus), one of
my favorite comedy troupes. The reference felt suitably irreverent for what
was essentially a “[skunkworks
project](http://en.wikipedia.org/wiki/Skunkworks_project)”. The word “Python”
was also catchy, a bit edgy, and at the same time, it fit in the tradition of
naming languages after famous people, like Pascal, Ada, and Eiffel. The Monty
Python team may not be famous for their advancement of science or technology,
but they are certainly a geek favorite. It also fit in with a tradition in the
CWI Amoeba group to name programs after TV shows.  
  
For many years I resisted attempts to associate the language with snakes. I
finally gave up when O’Reilly wanted to put a snake on the front of their
first Python book "Programming Python". It was an O’Reilly tradition to use
animal pictures, and if it had to be an animal, it might as well be a snake.  
  
With the naming issue settled, I started working on Python in late December
1989, and had a working version in the first months of 1990. I didn’t keep
notes, but I remember vividly that the first piece of code I wrote for
Python’s implementation was a simple LL(1) parser generator I called “pgen."
This parser generator is still part of the Python source distribution and
probably the least changed of all the code. This early version of Python was
used by a number of people at CWI, mostly, but not exclusively in the Amoeba
group during 1990. Key developers besides myself were my officemates,
programmers [Sjoerd Mullender](http://homepages.cwi.nl/%7Esjoerd/) (Sape’s
younger brother) and [Jack Jansen](http://homepages.cwi.nl/%7Ejack/) (who
remained one of the lead developers of the Macintosh port for many years after
I left CWI).  
  
On February 20, 1991, I first released Python to the world in the
[alt.sources](http://www.faqs.org/faqs/alt-sources-intro/) newsgroup (as 21
[uuencoded](http://en.wikipedia.org/wiki/Uuencode) parts that had to be joined
together and uudecoded to form a compressed tar file). This version was
labeled 0.9.0, and released under a license that was an almost verbatim copy
of the MIT license used by the X11 project at the time, substituting
“Stichting Mathematisch Centrum”, CWI’s parent organization, as the
responsible legal entity. So, like almost everything I’ve written, Python was
open source before the term was even invented by [Eric
Raymond](http://en.wikipedia.org/wiki/Eric_S._Raymond) and [Bruce
Perens](http://en.wikipedia.org/wiki/Bruce_Perens) in late 1997.  
  
There was immediately a lot of feedback and with this encouragement I kept a
steady stream of releases coming for the next few years. I started to use
[CVS](http://en.wikipedia.org/wiki/Concurrent_Versions_System) to track
changes and to allow easier sharing of coding responsibilities with Sjoerd and
Jack (Coincidentally, CVS was originally developed as a set of shell scripts
by [Dick Grune](http://en.wikipedia.org/wiki/Dick_Grune), who was an early
member of the ABC group). I wrote a FAQ, which was regularly posted to some
newsgroup, as was customary for FAQs in those days before the web, started a
mailing list, and in March 1993 the
[comp.lang.python](http://groups.google.com/group/comp.lang.python/topics)
newsgroup was created with my encouragement but without my direct involvement.
The newsgroup and mailing list were joined via a bidirectional gateway that
still exists, although it is now implemented as a feature of mailman – the
dominant open source mailing list manager, itself written in Python.  
  
In the summer of 1994, the newsgroup was buzzing with a thread titled “[If
Guido was hit by a
bus?](http://legacy.python.org/search/hypermail/python-1994q2/1040.html)”
about the dependency of the growing Python community on my personal
contributions. This culminated in an invitation from Michael McLay for me to
spend two months as a guest researcher at [NIST](http://www.nist.gov/), the US
National Institute for Standards and Technology, formerly the National Bureau
of Standards, in Gaithersburg, Maryland. Michael had a number of “customers”
at NIST who were interested in using Python for a variety of standards-related
projects and the budget for my stay there was motivated by the need to help
them improve their Python skills, as well as possibly improving Python for
their needs.  
  
The [first Python
workshop](http://legacy.python.org/workshops/1994-11/attendees.pics.html) was
held while I was there in November 1994, with NIST programmer [Ken
Manheimer](http://en.wikipedia.org/wiki/Ken_Manheimer) providing important
assistance and encouragement. Of the approximately 20 attendees, about half
are still active participants in the Python community and a few have become
major open source project leaders themselves ([Jim
Fulton](http://www.zope.com/about_us/management/james_fulton.html) of
[Zope](http://www.zope.org/) and [Barry Warsaw](http://barry.warsaw.us/) of
[GNU mailman](http://en.wikipedia.org/wiki/GNU_Mailman)). With NIST’s support
I also gave a keynote for about 400 people at the Usenix Little Languages
conference in Santa Fe, organized by [Tom
Christiansen](http://en.wikipedia.org/wiki/Tom_Christiansen), an open-minded
Perl advocate who introduced me to Perl creator [Larry
Wall](http://en.wikipedia.org/wiki/Larry_Wall) and Tcl/Tk author [John
Ousterhout](http://home.pacbell.net/ouster/).  
  
Next installment: how I got a job in the US...

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[3:19 PM](http://python-history.blogspot.ca/2009/01/personal-history-
part-1-cwi.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=3977478274237365514&from=pencil "Edit
Post")

  *[9:29 AM]: 2009-01-13T09:29:00-08:00
  *[9:17 AM]: 2009-01-13T09:17:00-08:00
  *[3:19 PM]: 2009-01-20T15:19:00-08:00

