

* * *

##### Friday, July 8, 2011

###  Karin Dewar, Indentation and the Colon

In a [recent post on my other
blog](http://neopythonic.blogspot.com/2011/06/depth-and-breadth-of-
python.html) I mentioned a second-hand story about how Python's indentation
was invented by the wife of Robert Dewar. I added that I wasn't very sure of
the details, and I'm glad I did, because the truth was quite different. I
received a long email from Lambert Meertens with the real story. I am going to
quote it almost completely here, except for some part which he requested not
to be quoted. In summary: Karin Dewar provided the inspiration for the use of
the colon in ABC (and hence in Python) leading up to the indentation, not for
indentation itself. Here is Lambert's email:  
  

> The Dewar story is not about indentation, but about the invention of the
colon.  
>  
> First about indentation in _B_. Already _B_ 0, the first iteration in the
_B_ 0, _B_ 1, _B_ 2, ... sequence of designs leading to ABC, had non-optional
indentation for grouping, supplemented by enclosing the group between `BEGIN`
and `END` delimiters. This can be seen in [GM76], section 4.1 ( _Layout_ ).
The indentation was supposed to be added, like pretty printing, by a dedicated
_B_ editor, and the user had no control over this; they were not supposed to
be able to turn this off or otherwise modify the indentation regime.  
>  
>  Given the mandatory indentation, separate `BEGIN` and `END` delimiters are
of course superfluous; in  _B_ 1 we had no `BEGIN`, but only `END IF`, `END
FOR`, and so on, and then the latter delimiters were also dropped in  _B_ 2,
leaving pure indentation as the sole indicator of grouping. See [ME81],
Section 4 (STATEMENT SYNTAX).  
>  
> The origin of indentation in ABC is thus simply the desire to have the
program text look neat and be suggestive of the meaning, codifying what was
already common practice but not enforced. The decision to remove the noise of
`BEGIN` ... `END` may have been influenced by [PL75], which actually advocated
using pure indentation for grouping. Since occam came later (1983), the
feature can't have been copied from that language. Same for Miranda (1985). As
far as I am aware, _B_ was the first actually published (and implemented)
language to use indentation for grouping.  
>  
>  Now the Dewar story, which is how I got the idea of the colon, as I wrote
it down in a memoir of the ABC design rationale:

  
And here I will paraphrase, at Lambert's request.  
  
In 1978, in a design session in a mansion in Jabłonna (Poland), Robert Dewar,
Peter King, Jack Schwartz and Lambert were comparing various alternative
proposed syntaxes for B, by comparing (buggy) bubble sort implementations
written down in each alternative. Since they couldn't agree, Robert Dewar's
wife was called from her room and asked for her opinion, like a modern-day
Paris asked to compare the beauty of Hera, Athena, and Aphrodite. But after
the first version was explained to her, she remarked: "You mean, in the line
where it says: 'FOR i ... ', that it has to be done for the lines that follow;
not just for that line?!" And here the scientists realized that the
misunderstanding would have been avoided if there had been a colon at the end
of that line.  
  
Lambert also included the following useful references:  
  

> [PL75] P. J. Plauger. [Signal and noise in programming
language](http://portal.acm.org/citation.cfm?id=800181.810322). In J. D.
White, editor, _Proc. ACM Annual Conference 1975_ , page 216. ACM, 1975.  
>  
> [GM76] Leo Geurts and Lambert Meertens. [Designing a beginners' programming
language](http://www.kestrel.edu/home/people/meertens/publications/papers/Designing_a_beginners_programming_language.pdf).
In S.A. Schuman, editor, _New Directions in Algorithmic Languages 1975_ ,
pages 1–18. IRIA, Rocquencourt, 1976.  
>  
> [ME81] Lambert Meertens. [Issues in the design of a beginners' programming
language](http://www.kestrel.edu/home/people/meertens/publications/papers/Issues_in_the_design_of_a_beginners_programming_language.pdf).
In J.W. de Bakker and J.C. van Vliet, editors, _Algorithmic Languages_ , pages
167–184. North-Holland Publishing Company, Amsterdam, 1981.

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[4:13 PM](http://python-history.blogspot.ca/2011/07/karin-dewar-indentation-
and-colon.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=3379377789727695529&from=pencil "Edit
Post")

Labels: [abc](http://python-history.blogspot.ca/search/label/abc),
[colon](http://python-history.blogspot.ca/search/label/colon),
[indentation](http://python-history.blogspot.ca/search/label/indentation),
[python](http://python-history.blogspot.ca/search/label/python)

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

