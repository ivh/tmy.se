Title: Site Update
Slug: site-update
Date: 2020-01-23 12:28
Status: published
Tags: tech, webdev, sweden

This site no longer runs on a small virtual server in some data center, but just moved home. Literally,
that is, it runs from my old RaspberryPi3 that sits on top of my fridge at home. This became possible
because we got fast internet into our cottage in the middle of the Swedish forest.

With government subsidies and spreading costs over the local association, getting connected cost us
1800 EUR, which is a steal because they had to dig an extra kilometer just to get to us. Yes, there
is an acutal glass fiber running all the way into our kitchen and I could get 1GBit/s up and down, if
I had the use for it.

I was shortly considering switching back to Wordpress, but decided against it, even though there did
not seem to be a performance problem on the RasPi. I might still do it for the comments and easier
posting from mobile, but I would have to write a script to insert the posts that I made in the 
meantime from the markdown files into the database, since the RSS-import of WP fails.

[https://caddyserver.com/](Caddy) is no longer just a proxy for nginx to get automatic
LetsEncrypt certificates, but it serves the files itself now and interfaces with fastcgi, among other things for my
instance of [https://tt-rss.org/](TT-RSS) that I use as my main news and blog aggregator.
