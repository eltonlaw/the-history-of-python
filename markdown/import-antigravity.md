

* * *

##### Monday, June 21, 2010

###  import antigravity

The antigravity module, referencing the [XKCD comic mentioning
Python](http://xkcd.com/353/), was added to Python 3 by Skip Montanaro. You
can read more about it here, one of the first spottings that I know of:
<http://sciyoshi.com/blog/2008/dec/30/import-antigravity/>).  
  
But it really originated in Google App Engine! It was a last-minute addition
when we launched App Engine on April 7, 2008. A few weeks before launch, when
most code was already frozen, the App Engine team at Google decided we wanted
an easter egg. After a great many suggestions, some too complex, some too
obscure, some too risky, we chose the "antigravity" module. The App Engine
version is a little more elaborate than the Python 3 version: it defines a
fly() function while can randomly do one of two things: with a probability of
10%, it redirects to the XKCD comic; otherwise, it simply renders the text of
the comic in HTML (with a link to the comic on the last line). To invoke it in
your App Engine app, you'd have to write a little main program, like this:

>

>     import antigravity  
>     >  
>     > def main():  
>     >     antigravity.fly()  
>     >  
>     > if __name__ == '__main__':  
>     >     main()

  
  
 **Update:** The Python 3 stdlib version has an easter egg inside the easter
egg, if you inspect the source code: it defines a function that purports to
implement the [XKCD geohashing algorithm](http://xkcd.com/426/).

Posted by  [ Guido van Rossum
](https://www.blogger.com/profile/12821714508588242516 "author profile") at
[11:31 AM](http://python-history.blogspot.ca/2010/06/import-antigravity.html
"permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=3496810514198811936&from=pencil "Edit
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

