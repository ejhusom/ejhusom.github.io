---
title: Dark mode on a website
date: 2021-01-30
---

I just discovered that it is quite easy to make a website adjust the style to
whether the client is using dark mode or not. Take a look at a snippet of my
CSS for this website:

```css
* {
    --txc: #393838;
    --lc: #1183b9;
    --bgc: #fff;
    --hlc: #70b4d5;
}

@media (prefers-color-scheme: dark) {
    * {
        --txc: #f5f5f5;
        --lc: #70b4d5;
        --bgc: #212121;
        --hlc: #1183b10;
    }
}
```

The first block defines the default values for two text colors, the background
and a highlight color. With the second block, those variables are redefined if
the user is using a dark system theme.

This might be common knowledge for a lot of people, but have not seen this
functionality much "in the wild". Maybe some people prefer to keep the same
colors anyway, but I think it is very comfortable that websites dynamically
adapt to the system theme, especially when there are lots of articles.
