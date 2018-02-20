

* * *

##### Wednesday, January 28, 2009

###  Microsoft Ships Python Code... in 1996

My thanks go to Guido for allowing me to share my own history of Python!  
  
I'll save my introduction to Python for another post, but the end result was
its introduction into a startup that I co-founded in 1991 with several people.
We were working on a large client/server system to handle Business-to-Consumer
electronic shopping. Custom TCP protocols operating over the old X.25 network,
and all that. Old school.  
  
In 1995, we realized, contrary to our earlier beliefs, that more consumers
actually _were_ on the Internet, and that we needed a system for our customers
(the vendors) to reach Internet-based consumers. I was tasked to figure out
our approach, and selected Python as my prototyping tool.  
  
Our first problem was moving to an entirely browser-based solution. Our custom
client was no longer viable, so we needed a new shopping experience for the
consumer, and server infrastructure to support that. At that time, talking to
a web browser meant writing CGI scripts for the Apache and Netscape HTTP
servers. Using CGI, I connected to our existing server backend to process
orders, maintain the shopping basket, and to fetch product information. These
CGI scripts produced plain, vanilla HTML (no AJAX in 1995!).  
  
This approach was less-than-ideal since each request took time to spin up a
new CGI process. The responsiveness was very poor. Then, in December 1995,
while attending the Python Workshop in Washington, DC, I was introduced to
some Apache and Netscape modules (from Digital Creations, who are best known
for Zope) which ran persistently within the server process. These modules used
an RPC system called ILU to communicate with backend, long-running processes.
With this system in place, the CGI forking overhead disappeared and the
shopping experience was now quite enjoyable! We started to turn the prototype
into real code. The further we went with it, the better it looked and more
people jumped onto the project. Development moved **very** fast over the next
few months (thanks Python!).  
  
In January 1996, Microsoft knocked on our door. Their internal effort at
creating an electronic commerce system was floundering, and they needed people
that knew the industry (we'd been doing electronic commerce for several years
by that point) and somebody who was nimble. We continued to develop the
software during the spring while negotiations occurred, and then the
acquisition finalized in June 1996.  
  
Once we arrived at Microsoft with our small pile of Python code, we had to
figure out how to ship the product on Windows NT. The team we joined had lots
of Windows experience and built an IIS plugin to communicate over named pipes
to the backend servers, which were NT Services with our Python server code
embedded. With a mad sprint starting in July, we shipped Microsoft Merchant
Server 1.0 in October, 1996.  
  
And yes... if you looked under the covers, somewhat hidden, was a Python
interpreter, some extension DLLs, and a bunch of .pyc files. Microsoft
certainly didn't advertise that fact, but it was there if you knew were to
look.

Posted by  [ Greg Stein ](https://plus.google.com/102722482248467575904
"author profile") at  [6:40 AM](http://python-
history.blogspot.ca/2009/01/microsoft-ships-python-code-in-1996.html
"permanent link") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=8699431508730375743&postID=6802923042935141836&from=pencil "Edit
Post")

  *[9:29 AM]: 2009-01-13T09:29:00-08:00
  *[9:17 AM]: 2009-01-13T09:17:00-08:00
  *[3:19 PM]: 2009-01-20T15:19:00-08:00
  *[2:05 PM]: 2009-01-20T14:05:00-08:00
  *[2:01 PM]: 2009-01-27T14:01:00-08:00
  *[6:40 AM]: 2009-01-28T06:40:00-08:00

