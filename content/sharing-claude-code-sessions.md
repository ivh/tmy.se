Title: Sharing Claude Code Sessions
Slug: sharing-claude-code-sessions
Date: 2025-11-24 08:30
Status: published
Tags: AI, tech

I've been using Claude Code (CC) quite extensively in recent weeks, and apart
from a few fails it's been a blast. I want to write about a few of the things I
got it to do successfully, but in order to do that I need to be able to share
the session logs.

Unfortunately, there is no straight-forward way to do this. The logs
are saved as `.jsonl` files in
`$HOME/.claude/projects/-path-to-your-work-directory/` and when using the
[online version of CC](https://claude.ai/code/), all one to do is use the _Open
in CLI_ button and continue locally, then the `.jsonl` with the whole session
will show up in the project folder.

These file are a bit unweildy. For example, they contain the whole content of files that CC reads and a
buch of distracting metadata. I tried [Simon Willison](https://simonwillison.net/)'s
[claude_to_markdown.py](https://github.com/simonw/tools/blob/main/python/claude_to_markdown.py)
but that was not quite what I wanted, which is a static HTML file with embedded
JavaScript (JS) to hide the long reads and outputs by default, but make them
expandable if needed.

What better way to achieve this than just let CC do it? Very meta, I know.  So
I donwloaded the JS from `https://claude.ai/code/` (after all, they have solved
the same task there already) and put it into a fresh repo with an example
session log. This is the outline I wrote and added to the repo:

```
# main goal
a script, python or other, that takes session logs from Claude Code (CC)
and converts them into HTML.

## example data
- a06171f9-5f33-4258-84e1-4dc70e84c6dd.jsonl an example session log. all
  input files will have this format.
- Screenshot, two example screenshots of how it looks on CC web.
- CCweb_example.html and CCweb_example_files/ , the saved web page of CC
  that should contain useful routines to render the session. Ignore the 
  left half of the page and session management, only the session part 
  itself is needed.

## requirements
- the output should be a single html-file, named like the input but ending
  .jsonl exchanged to .html
- all javascript should be inlined.
- the script does not need to be self-contained, can e.g. read js files or
  templates to make the output.
- the html should look similar to the screenshots, i.e. compact with 
  unnecessary information skipped, file reads hiden, and long diffs
  shortened but expandable.
```

Then all that was let do do was to point CC to the repository and tell it to get crackin'. 

[*This is how it went*]({static}ai/claudecode-to-html).

I wasn't a perfect one-shot success, as you can see. But with just a little
prodding CC figured it out. I then continued in a new short session to have it
sum up the elapsed working time and put that on top of the HTML.  Not bad at
all, I would say.
