Title: Terminal blogging
Slug: termblog
Date: 2016-11-28 8:50
Status: published
Tags: tech, android
image: {photo}blogterm.png
Attachments: pic/blogterm.png

[![Termux, Git and Pelican]({photo}blogterm.png "Termux, Git and Pelican")](/pic/blogterm.png)

I no longer carry my laptop home most days, just an Android tablet. To be able to
blog with that setup, I installed Termux which provides a nice self-contained
Linux environment with Apt to install more software goodies. The "Hacker Keyboard"
makes vim and the command line more usable on a tablet and now I can quite
comfortably edit blog entries in Markdown, commit and push to the server where Pelican
re-builds the HTML site automatically.

For blogging pictures and URLs, they can be shared to Termux from other Adroid apps, I
just had to drop a small script that writes the URL from the clipboard to a text file.
