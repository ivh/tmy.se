Title: Pycpl With Batteries Included
Slug: pycpl-with-batteries-included
Date: 2025-11-26
Status: published
Tags: AI, tech

Last week, on a whim, I gave 
[Claude Code](https://code.claude.com/docs/en/overview) (CC)
a task that turned out to be both possible and highly useful,
because it removed a common annoyance for some colleagues and
myself.

See, there is this C-library called CPL that [ESO](https://eso.org) uses for
processing of astronomical data. There also is a Python-wrapper for it,
*pycpl*, that allows to use the library from Python, which is great because
it's the language that astronomers and data scientists mostly use nowadays.

However, *pycpl* does not come with CPL, but instead requires it to be
installed beforehand, which often implies compiling it oneself because not all
operating systems package the right version, if at all. This is not a big hurdle
for developers, but if one wants to share a half-finished pipeline with some
prospective users, it easily becomes one. Containers and such can help with this
but are always a crutch that I would rather avoid.

Claude to the rescue. The off-handed remark in a telecon, that we should just make
a *pycpl* package that comes with CPL (and its dependency libs) included, took hold
with me long enough to ask CC to just do it!

I started by downloading the latest CPL source code, and the three libs it
needs. Then I asked CC to [initialize the git
repository]({static}ai/pycpl-initrepo) and sort out which files to add and
which to ignore.

After pushing to Github, I could switch to the [online version of
CC](https://claude.ai/code) where I had free credits to burn, so no harm done
if this endeavour would turn into failure. Then I just quickly told it what to
do like this, typos and all:

> pycpl is a python wrapper for C-lib CPL. But it is packaged without the
> C-lib, so the overall goal is to upgrade the pycpl package to include the
> build of CPL and its depencencies (which are also present here).
> start by looking at the build system of pycpl and how to include the other
> lobraries to it. then move the libs to appropriate places inside pycpl and try
> the build.


[This session log]({static}ai/pycpl-integrate) and [this
follow-up]({static}ai/pycpl-itworks) basically show how CC figured it all out.
I only skimmed through it at the time and could not tell you what exactly it
did. At some point I realized it needed some of the files that were omitted
earlier, so I added those back. In the end, I had a package that installed
locally -- a success already.

But what would make this *really* useful would be a Python "wheel", i.e. a
package bundle that is pre-compiled for different platforms and Python version.
This way, users would be able to install instantly, without any compiling
happening at all. So I naturally [asked CC about it]({static}ai/pycpl-wheels),
and how to set it up such that GitHub Actions do the compiling.  This was the
most tedious bit. CC needed many iterations to get this right and compiling on
GitHub is not fast. So I let it work in the background over an evening, only
checking in occasionally. Claude figured it out in the end! The package
installs and works nicely for myself and several colleagues.

Initially, the plan was to also upload to PyPI, because ESO does not actually
do that. But I was not able to put claim to the name "pycpl" there, and without
that it would not work. Plus I did not want to step on people's toes too much
by publishing work that is not my own. Even though, in principle, it should be
fine with GPL-licensed code.

Thus, for now, one has to provide an "extra index URL" to install this *pycpl*
package. Use [*uv*](https://docs.astral.sh/uv/), for example like this:


```bash
    (uv) pip install pycpl --extra-index-url https://ivh.github.io/pycpl/simple/
```

Or try if it works without having anything prepared:

```bash
    uv run --with pycpl --extra-index-url https://ivh.github.io/pycpl/simple/ python -c "import cpl;"
```

Or add it to the header of a script file like this:

```bash
    uv add --script main.py --index https://ivh.github.io/pycpl/simple/  pycpl
```

One can also add the index URL to one's `pyproject.toml`, together with ESO index URL that provides tools like *pyesorex* and *edps*, which seem to play nicely with my *pycpl* instead of ESO's own. For how to do that, see the README in the [GitHub repo](https://github.com/ivh/pycpl/).
