---
title: "Plain text calendar"
date: 2022-05-30T21:47:12+02:00
type: ["posts"]
draft: false
tags:
categories:
---

The last years I have been moving towards plain text files for almost any use case where I need to store information digitally, and after reading about [Calendar.txt](https://terokarvinen.com/2021/calendar-txt/) I have started to use a plain text file as my calendar.
I use (almost) the same template as described in the link, but I wrote my own script for generating the calendar template so I can easily make adjustments if needed.
Example of the format with a few example events:

```
2023-01-02 w1
2023-01-02 w1 Mon 
2023-01-03 w1 Tue  12:00 Meeting.
2023-01-04 w1 Wed 
2023-01-05 w1 Thu  18:00 Going for a run.
2023-01-06 w1 Fri 
2023-01-07 w1 Sat 
2023-01-08 w1 Sun 
2023-01-09 w2
2023-01-09 w2 Mon 
2023-01-10 w2 Tue 
2023-01-11 w2 Wed 
2023-01-12 w2 Thu  Seminar.
2023-01-13 w2 Fri 
2023-01-14 w2 Sat 
2023-01-15 w2 Sun 
```

I find it quite nice since it integrates well with the rest of my very plain text-oriented workflow, and it's easily synced and managed with git together with the rest of my plain text files (notes, todos, etc).
It takes some time to adapt to since the "user interface" is quite different than normal calendar applications, but for those who are familiar with quick navigation in text files (for example using Vim), it can be much more efficient to use a plain text calendar.

I also wrote a small bash script for opening the calendar on the current date in Vim:


```sh
today=`date +%Y-%m-%d`

vim /path/to/calendar.txt -c "/$today"
```
