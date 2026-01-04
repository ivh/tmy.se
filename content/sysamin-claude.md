Title: Sysamin Claude
Slug: sysamin-claude
Date: 2026-01-04
Status: published
Tags: ai, tech

Claude Opus 4.5 is really good as coding agent, and I'm having a blast with it.
It's even more fun in "YOLO-mode", a.k.a. `--dangerously-skip-permissions`.
This way one does not need to approve anything; Claude gets to do whatever it
sees fit to get the job done. This enables longer tasks because it can do trial and error
on its own, and also requires less attention from us users.

Is it safe though? When will Claude mess up and delete important data? 
After all, unrestricted access to the command line is as powerful a tool as they come.
I have no good answer here,
so I recently looked into various ways to prevent the agent from doing damage. As far as I know, these
are the common approaches:

* Using the [online version](https://claude.ai/code) that clones a git repo into its own sandbox
  and has yolo-mode enabled by default. This is great when nothing outside the repo is needed
  for the task, otherwise it becomes a hassle. Also, I just spent ten minutes figuring out why
  a project did not run there while it does just fine locally: It turns out the sandbox runs an old ´uv´
  that did not know about recent python versions, thus a quick `uv self update` resolved it.
  Still annoying.
* Running in a container like Docker. The desktop version for Macs even has a dedicated command for
  this: `docker sandbox run claude`. Ultimately though, I don't like the friction this introduces.
  Suddenly one has to maintain the Dockerfile and what to install there, mounting directories or copy
  data back and forth, etc.
* A separate local user, that lacks admin privileges, is another way to isolate the coding agent.
  Less friction than a container, since all installed software is still available, but still some
  overhead. For example setting up git & GitHub for a separate clone of the repos, since 
  file ownership and permissions otherwise are a problem.
* Then there is the built-in sandbox of Claude Code. I cannot yet judge how much of a difference
  this really makes, especially considering how good Claude is at finding work-arounds when things do not
  go its way.

For now, I take the risk and run yolo-Claude on my laptop without a container
or separate user. All code is under version control and pushed to remote. And I
make sure to have frequent backups, just in case.

What I *dont't* do however, is run Claude with root-access on a remote server. It would most
likely be fine for a while, until it would not. Claude makes a great sysadmin sidekick though:
earlier today, the maintenance interface (iDRAC) of one of our servers hung itself and in 
[this session](https://claude.ai/share/7c84f996-1366-4440-85bf-a88e449267a6) Claude showed
showed me how to reset it remotely, which I did not know before was possible.
