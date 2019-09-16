#!/usr/bin/env python3
# ==================================================================
# File:     generate_html_flashcards.py
# Author:   Erik Johannes Husom
# Created:  2019-09-04
# ------------------------------------------------------------------
# Description:
# Generate HTML flashcards from Markdown files, and produce JavaScript files
# with updated arrays with filenames.
# ==================================================================
import numpy as np
import os


def get_categories(dir_name):
    '''Get list of categories.'''
    return os.listdir(dir_name)


def generate_html_flashcards(dir_name):
    '''Generate HTML flashcards from Markdown with Pandoc.'''

    js_file = open('random-flashcard.js', 'w')

    categories = get_categories(dir_name)

    for category in categories:
        category_path = os.path.join(dir_name, category)

        md_files = os.listdir(category_path)

        js_file.write('var ' + category + ' = new Array(')

        html_main_filename = 'main-' + category
        html_main_filename_ext = html_main_filename + '.html'
        html_main_file = open(html_main_filename_ext, 'w')

        for md_file in md_files:
            md_path = os.path.join(category_path, md_file)
            html_file = os.path.splitext(md_file)[0] + '.html'
            

            os.system('pandoc -t dzslides -s ' + md_path + ' -o flashcards/' +
                    html_file)

            js_file.write('"' + html_file + '",')

        category_html = category + '.html'
        os.system('pandoc -t dzslides -s ' + category_path + '/*.md' + 
            ' -o flashcards/' + category_html)

        js_file.write('"' + category + '.html");\n')


        html_text = f"""
        
<!DOCTYPE html>
<html>

  <head>
    <title>Flashcards - Erik Johannes Husom</title>
    <link rel='stylesheet' href='../minimalistWhite.css'>

    <script type='text/javascript' src='random-flashcard.js'></script>

    <meta name='viewport' content='width=device-width, initial-scale=1'>
  </head>

  <body>
    <header>
      <a href='../index.html' class='ghost'>
        <h1>Erik Johannes Husom</h1>
      </a>
      <h2>::</h2>
      <h2><a href="flashcards.html">Flashcards </a></h2>
      <h2>::</h2>
      <h2>{category}</h2>
    </header>

    <h2><a href="{html_main_filename_ext}">Random flashcard</a></h2>
    <br>
    <h2><a href="flashcards/{category_html}">View all flashcards in fixed order</a></h2>

    <script type="text/javascript">
        document.write(random_flashcard({category}));
    </script>


    <footer>
      Copyright 2019 by Erik Johannes Husom. All rights reserved.
    </footer>
  </body>

</html>


        """

        html_main_file.write(html_text)
        html_main_file.close()

    js_function = """function random_flashcard(flashcards) {
    var path = '<iframe src=\"flashcards/';
    var random_index = Math.floor(Math.random()*flashcards.length);
    path += flashcards[random_index];
    path += '\" width=\"95%\"></iframe>';
    return path;
    }"""

    js_file.write(js_function)
    js_file.close()


    flashcards_html = open('flashcards.html', 'w')


    flashcards_text1 = """
<!DOCTYPE html>
<html>

  <head>
    <title>Flashcards - Erik Johannes Husom</title>
    <link rel='stylesheet' href='../minimalistWhite.css'>


    <meta name='viewport' content='width=device-width, initial-scale=1'>
  </head>


  <body>
    <header>
      <a href='../index.html' class='ghost'>
        <h1>Erik Johannes Husom</h1>
      </a>
      <h2>::</h2>
      <h2><a href="flashcards.html">Flashcards </a></h2>
    </header>

    This page is under development.


    <nav>
      <ul>"""




    flashcards_text2 = """
        </ul>
    </nav>


    <footer>
      Copyright 2019 by Erik Johannes Husom. All rights reserved.
    </footer>
  </body>

</html>
    """
    
    flashcards_html.write(flashcards_text1)

    for category in categories:
        flashcards_html.write('<li><a href="main-' + category + '.html">' +
                category + '</a></li>\n')

    flashcards_html.write(flashcards_text2)


    flashcards_html.close()
        



generate_html_flashcards('markdown')
