Title: Disk Magic
Slug: disk-magic
Date: 2021-06-18 08:36
Status: draft
Tags: tech

A while back my installation of [HomeAssistant](https://www.home-assistant.io/)
broke down and while that caused minor inconveniences, I only this week looked into
what happened and whether I could recover the setup. The pairing of the lamps
and switches is not something that one wants to repeat unnecessarily.

The most likely cause turned out to be the case: The microSD-card in
the RaspberryPi4 broke. They are known to do that, unfortunately. I bought a new
one and pulled an image from the old one and after a bit of fiddling, I was able
to restore a snapshot that I had taken not long ago. All good.

I bought a

```bash
ssh berr "dd if=/dev/mmcblk0" > berry.img
losetup --find --show -P /home/tom/media/berry.img
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

    dd if=/home/tom/media/berry.img of=/dev/mmcblk0

But this did not work because the new card was slightly smaller
than the old one. Apparently 32GB are not what they used to be.
Annoying!

So I
cfdisk /dev/loop25
cfdisk /dev/mmcblk0
resize2fs /dev/loop25p2 61083647s
losetup --detach /dev/loop25
dd if=/home/tom/media/berry.img of=/dev/mmcblk0 bs=2048
re-insert
fsck.ext4 /dev/mmcblk0p2
make bootable

