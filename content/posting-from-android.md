Title: Posting Images from Android to a Static Site
Slug: posting-from-android
Date: 2020-02-24 13:47
Status: published
Tags: photo, meta, tech
image: {photo}posting-from-android.jpg

[![posting-from-android]({photo}posting-from-android.jpg "posting-from-android")]({static}/pic/posting-from-android.jpg)

I didn't post this picture because it is
in any way interesting in itself, but because
I can! From my phone, that is!

Let me back up and tell you why I find that exciting.
This site is [statically generated]({filename}/new-site.md)
and a new blog post is added via a markdown file,
re-compiling and uploading.
This means firing up the text editor and some quick command-line
actions after finishing the writing. This fits me perfectly fine,
most of the time.

But when it comes to images, I found always it cumbersome to 
first download them to my laptop for processing and
inclusion in a post. Which is why I finally got around to
figuring out how to post them directly from the phone that
takes the image. 

The centerpice for making this work is [Termux](https://termux.com/)
which gives you a full Linux-environment on Android devices; it's
really really good and can do much more than I describe here.
Termux supports the "Share with..." mechanism and allows me to execute a script
with the shared file as argument. So I adapted my 
[script](https://github.com/ivh/tmy.se/blob/master/termux-file-editor)
that prepares the markdown file and resizes the image for this 
purpose.

Now when I share an image from my phone with Termux, the following steps
happen:

* The image is saved in Termux.
* My script is called with the image location.
* It asks me to enter a title which is used as the post title, the URL-slug and the filenames.
* The Markdown template with this information, the image link and date/time is prepared, and saved.
* A text editor is fired up to verify and/or write an extra line in the mardown-file.
* The image gets resized and renamed accordingly.
* The files get added and committed to the repository, and pushed to GitHub.
* Finally, [Pelican](https://getpelican.com) is told to re-compile the site into HTML, make the smaller inline-version of the image, and upload everything with rsync to my RaspberryPi-server.

Done.
