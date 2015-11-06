# hobbysite_project

This project A Django app for helping people manage their club's or other organizations' web site. The idea is that most of these organizations need a mostly static site, but with a little bit of time sensitive info (upcomming events, club offices, a picture page, an online newsletter, links to resources). The idea is that people could take this site and customize it to their organizations needs by addding some static pages and content on the few dynamic areas like the calendar or newsletter archive.

My Story
--------

A while back I took over managing my Son's scout troop website. It was originally hosted on geocities.com with a few pictures, but quickly became a pain to manage. So someone actually registered a domain name got a hosting service and FTP'd an index.html up there.  I came along and added some more content and converted it to an open source CMS. That quickly  got out of hand too. Info was dated and maintaining it became a second job. Instead of an assitant scoutmaster, I became a full time webmaster.

This happed again with our local clubs model airplane site. One of the members registerd the domain, and created tables of pictures (he is a pretty good amateur photographer) that he rendered as html on his mac, and pushed up there. I got asked to help him run the site and others quickly began sending me pictures. The expectation was that these would be put up on the site within a day or two after every event. It's easy enough to do on flickr, so how hard can it be? Once again it quickly became a full time job. Instead of building and flying model planes, I was looking at all the neat photos of others doing that. The final straw was when the newsletter editor asked how we can make a members only page to display 30 year back issues. It was an important problem for us to solve because paper copies of these were being mailed all over the world and that was getting expensive. It cost a lot and many people have really bad mail service in their countries, but they do have internet.

I tried several attempts at creating site based on various CMS systems. Most were all about the blog or the photo gallery. A blog was something that none of the organizations I was involved with really needed. These sites were mostly static with a few tings that changed on a monthly or yearly basis. The photo galleries are there, but they mostly demand that you get familiar with a bunch of CSS just to do the simplest things. Many required a DB to be setup and lots of software installed on the server side.

Goals
-----

My concept it to let the poor guy got sucked into this job do his work on his local PC with tools commonly available and minimal configuration on the server side. The work being done is the initial site setup with all it branding and links and then be able to maintain it. Since most of this is static, why not just upload the changes once a month for the members to see? The idea being that if this changes monthly or yearly, there's no need for a fully real time content managed system. We're not talking about changing the sale item on our ecommerce site at 10AM on 'Black Friday' or pushing patches out for tax software on April 14th. Rather, this is about posting some picture from last week's white water rafting trip, model plane contest results or the new contact info for the club officers. However, there are some things that need to be changed on a timely basis. The hope is that will a little training, the club officers could be added to the list of site managers and take care or routine updates throught the Django admin interface

Thanks for looking!
