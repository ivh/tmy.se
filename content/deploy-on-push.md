Title: Deploy on Push
Slug: deploy-on-push
Date: 2016-11-23 09:20
Status: published
Tags: tech, python, git

I disabled some of my social media accounts and want to use this blog some more instead.
To that end it was about time to stream-line my pusblishing process here, lowering the
mental threshold. After writing a new entry, I would up to now [build the
site]({filename}new-site.md) locally and then sync the output to the server. The commit to
the git-repository was optional.

Now, I commit and push with git, directly to the server which updates the repo, rebuilds
and syncs locally to the place where the webserver expects its files. There are many ways
people do this, the following is what I found the simplest for now.

Have a git repository on the server that you push into. Let this be a standard repo, not a
bare one. Set the option `git config --local receive.denyCurrentBranch updateInstead`
inside of it. This will update the current branch working files instead of refusing to
receive the push. Since we never edit files here, the tree will always be clean, so it can
be updated.

Then add a script at `.git/hooks/post-receive` which is a hook that gets executed after the
repository received the push. Mine looks like this:

    #!/bin/sh
    cd ..
    pelican -q -s publishconf.py && rsync -a output/* ../tmy.se

This builds the static html files with Pelican and then syncs them to the place where the
webserver expects them.One could point the webserver directly to `output/`, in principle.
But the built process takes half a minute for me during which the main index file is
missing and the website would be offline.

Also note the `cd ..` in the script above, which is there because the working directory
that the scripts gets run in seems to be the `.git/` subdirectory. This is contrary to the
git docs which claim that hooks get started in the root directory for non-bare repos.
