Title: Disk Magic
Slug: disk-magic
Date: 2021-06-22 08:36
Status: published
Tags: tech

A while back, my installation of [HomeAssistant](https://www.home-assistant.io/)
broke down and that caused some minor inconveniences, 
like lamp switches no longer working.
Nevertheless, I only this week looked into
what happened and whether I could recover the setup. The pairing of the lamps
and switches is not something that one wants to repeat unnecessarily.

The most likely cause turned out to be it: The microSD-card in
the RaspberryPi4 broke. They are known to do that, unfortunately. So I bought a new
one, pulled an image from the old card and after a bit of fiddling, I was able
to restore a snapshot that I had taken not long ago. All good.

I bought an additional microSD out of concern for the same thing happening
to the other RasPi, the one that runs this very website.

```bash
ssh berr "dd if=/dev/mmcblk0" > berry.img
losetup --find --show -P berry.img
```

I had not known about the option -P before and it is exactly what
I needed in this case: additional device files for the partitions
within the disk image, not just a loop device for the iamge itself.
So I could go on and check the filesystems' integrity:

```bash
fsck.vfat /dev/loop25p1
e2fsck -f /dev/loop25p2
```

Not surprisingly, there were several errors to be fixed in the
main partition. After all, I was pulling the image from
a running system that was continuously writing logs and
stuff to the disk.

Then I tried to write the image to the new microSD-card.

```bash
dd if=berry.img of=/dev/mmcblk0 bs=2048
```

But this did not work because the new card was slightly smaller
than the old one. Apparently 32GB are not what they used to be.
Annoying!

So I had to figure out the number of sectors that
remained on the new card for the Ext4-filesystem.

```bash
cfdisk /dev/loop25
cfdisk /dev/mmcblk0 # compare numbers in cfdisk
resize2fs /dev/loop25p2 61083647s
losetup --detach /dev/loop25
dd if=berry.img of=/dev/mmcblk0 bs=2048
```
Take out the card and re-insert.
```bash
fsck.ext4 /dev/mmcblk0p2 # passes the test now!
cfdisk /dev/mmcblk0 # mark first partition as bootable
```

And that's it. I did not test whether the card actually boots up because
it would cause unnecessary downtime. I am reasonably confident
it will work, should the need arise.

I quite enjoyed this whole small exercise. It had been a while and
one always learns something new in the process.
