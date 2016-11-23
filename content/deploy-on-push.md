Title: Deploy on Push
Slug: vdeploy-on-push
Date: 2016-11-23 09:20
Status: published
Tags: tech, python, git

I disabled some of my social media accounts and want to use this blog some more instead. To that end it was about time to stream-line
my pusblishing process here, lowering the mental threshold. After writing a new entry, I would up to now [build the site]({filename}new-site.md) locally
and then sync the output to the server. The commit to the git-repository was optional.

Now, I commit and push with git, directly to the server which updates the repo, rebuilds and syncs locally to the place where the webserver
expects its files. There are many ways people do this, this is what I found the simplest for now:

