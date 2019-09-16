# Flashdown

Flashdown is a system for using Python, Pandoc, HTML and JavaScript to display
flashcards written in Markdown, and make it easy to use them on both computer
and mobile phones.

The project is under development.

## Using `pandoc` for displaying flashcards

Obtain a HTML slide show by running one of the following commands:

```
pandoc -s --mathml -i -t dzslides flashcards.md -o flashcards.html
pandoc -s --webtex -i -t slidy flashcards -o flashcards.html
pandoc -s --mathjax -i -t revealjs flashcards -o flashcards.html
```

