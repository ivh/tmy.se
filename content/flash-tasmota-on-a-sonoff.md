Title: Flash Tasmota On A Sonoff
Slug: flash-tasmota-on-a-sonoff
Date: 2020-09-27 9:14
Status: published
Tags: photo
image: {photo}flash-tasmota-on-a-sonoff.jpg

[![flash-tasmota-on-a-sonoff]({photo}flash-tasmota-on-a-sonoff.jpg "flash-tasmota-on-a-sonoff")]({static}/pic/flash-tasmota-on-a-sonoff.jpg)


Ok, that title takes some unpacking: A _Sonoff_ is a microcontroller that connects to Wifi and can switch some other electrical device
on and off, pictured on the right. It is basically a remote switch that can be used for all kinds of purposes, from a manually triggered remote to some fancy
home automation.
To _flash_ in this context means putting a new operating system (firmware) onto the microcontroller and [_Tasmota_](https://tasmota.github.io/docs/About/)
is the open-source firmware that everyone seems to love and recommend.

I have had two of these switches for quite a while, but never got around to converting them to Tasmota. Earlier today I finally did, following
[this guide for using a RaspberryPi](https://tasmota.github.io/docs/Flash-Sonoff-using-Raspberry-Pi/). The Sonoff provides an old-school
serial port and wants 3.3V power internally. The only thing I had available that can do both was my Pi Zero (left in picture), and I am happy to say that
it worked without much fiddling around. The most tricky part was to physically hold the Sonoff button and cables in place while turning on the 
Pi, then waiting for it to start up to trigger the software transfer whithout losing the connection on the cables.

Not I have to decide what to do with the switches. Probably I will go back to installing [Home Assistant](https://www.home-assistant.io/) for
central control. I have tried several years ago but I expect it to have improved much since. 
