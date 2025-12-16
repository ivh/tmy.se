Title: Vibe On
Slug: vibe-on
Date: 2025-12-16
Status: published
Tags: photo, tech, AI
image: {photo}vibe-on.png

[![vibe-on]({photo}vibe-on.png "vibe-on")]({static}/pic/vibe-on.png)

Here's another example for the kind of task that I no longer do myself but
rather hand off to the AI, because it does it so well. My

> Let's implement a new option --fib_eff that gets a single value or a range,
> like 0.9 or 0.7-0.9 , in order to set the fiber efficiencies in the simulation.
> see fiber_efficiency.md how to do that. set the eff after loading the HDF file,
> dont modify it. Ranges like 0.7-0.9 are to be interpreted as a random value
> within that range, uniformly distributed. ask if this was unclear, othweise get
> crackin and iterate.  example command: uv run andes-sim flat-field --band H
> --subslit slitA --wl-min 1600 --wl-max 1602 --fib_eff 0.5-0.95

As expected, [Claude had no problem figuring this out]({static}/ai/andesim-fibeff). [This the resulting
commit](https://github.com/ivh/ANDES_simulator/commit/cbb51d00f8a0210f71121ee1194b43b89d95431e#diff-6167f0249d8f9eecf8ce832c3d8fb8a8693c18c9c59d5aee29e70204dac19857). The image above is the ouput of that example command.

I did not have to to type anything else than the prompt above. And in doing that, I
needed to get clear for myself what I actually wanted, which is always a good
thing to do first. The rest is just typing.

The [whole project](https://github.com/ivh/ANDES_simulator), a CLI to make
simulated spectra, was "vibe-coded" this way, me caring little about the actual
code that Claude produced, only taking the occasional glance at it. It is
therefore probably not great for a long-term maintained code-base, but it
already does what I need it to and I have no intention to take this much
further.
