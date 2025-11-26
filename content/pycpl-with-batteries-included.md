Title: Pycpl With Batteries Included
Slug: pycpl-with-batteries-included
Date: 2025-11-26
Status: draft
Tags: AI, tech

Last week, on whim, I gave 
[Claude Code](https://code.claude.com/docs/en/overview) (CC)
a task that turned out to be both possible and highly useful,
because it removed a common annoyance for some collegues and
myself.

See, there is this C-library called CPL that [ESO](https://eso.org) uses
for data reduction pipelines. 

[Session 1]({static}ai/pycpl-initrepo)
[Session 2]({static}ai/pycpl-integrate)
[Session 3]({static}ai/pycpl-itworks)
[Session 4]({static}ai/pycpl-wheels)

```bash
    (uv) pip install pycpl --extra-index-url https://ivh.github.io/pycpl/simple/
```

Or

```bash
    uv run --with pycpl --extra-index-url https://ivh.github.io/pycpl/simple/ python -c "import cpl;"
```

```bash
    uv add --script main.py --index https://ivh.github.io/pycpl/simple/  pycpl
```


