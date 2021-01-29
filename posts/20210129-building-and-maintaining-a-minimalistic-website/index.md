---
title: "Building and maintaining a minimalistic website"
date: 2021-01-29
---

When I first started making my own website, I wrote everything manually, from
scratch. This type of approach is very fun and instructional, and probably the
best way if one wants to learn how a website functions.

After a while though, this approach gets quite tedious, because the total
number of pages piles up (mostly blog posts) and it gets hard to manually
update all of them when you want to make changes. This is one of the perfect
use cases for a Static Site Generator, which is a tool that uses templates to
build the static HTML pages for you. You are able to define the "rules" and
layouts for how the page should look independently of the content, and gives
you a lot of flexibility with regards to what you want to automate and what you
want to do manually.

I resisted the temptation of using an SSG for a while, since I enjoyed writing
everything from scratch and having a minimalistic approach. But, when I wanted
to add an RSS feed to my site, I figured that I couldn't be bothered with
writing an `feed.xml` file manually. I chose to try out
[Hugo](https://gohugo.io/), since I didn't really need to install anything, I
could just have a binary executable in the folder where I edit my website, and
then build it there. There was a lot of syntax to learn in order to get
everything working as I wanted, but it was also nice to have RSS feed, tags on
blog posts and blog feed being built automatically.

Even though Hugo worked fine, I felt like it was to bloated and complex for
what I wanted. I can certainly recommend Hugo in general, but I want a workflow
that has as few dependencies as possible, and is sustainable for a long, long
time, with very little maintainance. Keeping it purely HTML+CSS, without a
complex build process, would be preferable. I read an article called [Why I
Built My Own Shitty Static Site
Generator](https://erikwinter.nl/articles/2020/why-i-built-my-own-shitty-static-site-generator/),
which expressed some of the same thoughts I was having, and I was inspired to
stop using Hugo, and restructure this website. I could still use most of what I
had written from before, but I wrote my own small script for adding head,
header and footer (the elements that are the same on every page) and building
the blog feed. After that, the only thing missing was generating an RSS feed.
This is probably the most complex part of my build script, but I made it work
in the end.

There are some people who are even more hardcore (check out
[My stack will outlive
yours](https://blog.steren.fr/2020/my-stack-will-outlive-yours/)), who avoids
having a build step at all. I would like to eliminate the need for a build
script, just to keep things even simpler, but I appreciate having the option of
easily changing some elements in a template-file rather than on every page.
It's also very convinient to write blog posts in Markdown instead of HTML (my
build script does this conversion as well). The build script is still quite
small and I know exactly what it does and does not, and I prefer that over a
more complex SSG for my use case.

After further delving into the world of minimalistic web development, I
discovered the [512k.club](https://512kb.club/), the
[250kb.club](https://250kb.club/) and the [10kclub.com](https://10kbclub.com/).
Those are collections of websites that have a size below a certain (quite
small) threshold. I think the goal is just to make a point of how (often
needlessly) enormous many websites are, and that it's perfectly possible to
make good-looking websites without many MBs of data.

My own main page has a size of 1.6 kB at the time of writing, but of course,
there's not much there. Some of the blog posts contain a lot of images, and
those pages are certainly bigger in size, but the point is that it's totally fine
accessing the website on old browsers and with slow internet speed. I wish that
were the case for most websites.

Finally, I see this website as my online "profile page", in the same way that
many people have a Facebook-profile as an online presence. Maintaining a
website is a little bit harder than making a Facebook-profile, but it gives you
much more control and flexibility.

To round off, here are some minimalistic websites that I find interesting
(regarding design, content or both):

- [slashdev.space](https://slashdev.space/)
- [simbly.me](https://simbly.me/)
- [drewdevault.com](https://drewdevault.com/)
- [cri.dev](https://cri.dev/)
- [lawzava.com](https://lawzava.com/)
- [tokiesan.github.io](https://tokiesan.github.io/index.html)
