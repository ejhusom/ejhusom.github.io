---
title: "Reducing the temperature on a Raspberry Pi"
date: 2020-11-10T13:23:21+01:00
type: ["posts"]
draft:
tags:
    - raspberrypi
categories:
    - gear
    - technology
mastodonurl: ""
twitterurl: ""
instagramurl: ""
pixelfedurl: ""
image: "posts/20201110-raspberry-pi-temperature/cluster.jpeg"
---

I have for several months been hosting my own cloud services using
[Nextcloud](https://nextcloud.com/) on a [Raspberry Pi
4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/). At first I
was using a plastic case for the Pi, but I quickly figured out that I had to
use something else, as the temperature was constantly in the range of 70-75
degrees Celsius, which I figured was too high when it is supposed to be an
always-on system.

I purchased an [extra large heat
sink](https://thepihut.com/products/xl-raspberry-pi-4-heatsink) and a [cluster
case with fans](https://thepihut.com/products/cluster-case-for-raspberry-pi) in
order to reduce the temperature, but I was unsure of how much it would help,
and also whether the fan was as quiet as the product description claimed.
The delivery of the items took some weeks, so in the meantime I used a stack of
coins placed on top of the processing unit, which worked remarkably well (at
least compared to my expectations): The temperature was reduced with about
15-20 degrees Celsius.

![Using a coin stack as a heat sink.](posts/20201110-raspberry-pi-temperature/coin-stack.jpeg)
*Using a coin stack as a heat sink.*


After attaching the heat sink to the Pi, and then installing the Pi in the
cluster case and mounting the fan, the temperature of the Pi dropped to the
range of 30-35 degrees Celsius when running a Nextcloud server. This was much
better than I expected, and the fans hardly make any noise at all!

![Two Raspberry Pis installed in a cluster case, with the old plastic case next
to it.](posts/20201110-raspberry-pi-temperature/cluster.jpeg)
*Two Raspberry Pis installed in a cluster case, with the old plastic case next
to it.*

I have also tried a [heatsink
case](https://thepihut.com/products/aluminium-armour-heatsink-case-for-raspberry-pi-4)
for another one of my Pis, and the temperature is reduced by about 20-25
degrees Celsius, so that is not a bad option either.

