---
title: "Optimizing images for the web"
date: 2021-12-11
type: ["posts"]
draft: false
tags:
categories:
---

When you're crafting your own website without any website builder or tools like Wordpress, it can be a bit challenging to know how to optimize images.
JPG-files from a digital camera is usually a few MBs in size. 
For example, an image from my Gopro, with a resolution of 4032x3024, generally amounts to at least 2 MB.
If you're uploading such files, you're wasting bandwith, since most screens and monitors won't show the images in their full resolution anyway.
I have found it suprisingly difficult to find "best practices" for optimizing images for the web using simple tools, but after a bit of research, I've managed to put together a script that combines three different command line tools to reduce image size without loosing to much quality.

The three command line tools are:

- [`exiftool`](https://www.exiftool.org/): Edits EXIF-information. Used to remove metadata from the image, such as geolocation, which I don't want to share on the web.
- [`jpegoptim`](https://github.com/tjko/jpegoptim): Optimizes JPG-files.
- [`imagemagick`](https://imagemagick.org/): Used to reduce resolution of image.

Here's the bash script, which takes files as input:

```bash
#!/bin/bash

for i in "$@"; do
    # Reduce all metadata, but keep orientation of image:
    exiftool -all:all= -tagsFromFile @ -exif:Orientation "$i"

    # Optimize image to a size of 500 kB:
    jpegoptim --size=500k "$i"

    # Reduce resolution so the width is maximum 1500 pixels 
    # (mogrify is a part of imagemagick)
    mogrify -resize 1500 "$i"
done
```

I am by no means an expert on this, but I've found a routine that works fine. If you have any comments or better solutions, [let me know](mailto:erikjohannes@protonmail.com).
