#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator.

Example:

    >>> python3 buildsite.py

TODO:
    - Generate RSS feed.


Author:   
    Erik Johannes Husom

Created:  
    2021-01-27

"""
import datetime
from email import utils
import html
import os
import re


class Website():

    def __init__(self):

        self.baseurl = "https://erikjohannes.no/"
        self.layouts_folder = "layouts"
        self.posts_folder = "posts"
        self.pages_folder = "pages"
        self.standalone_folder = "standalone"
        self.photography_folder = "photography"
        self.posts_folder = "posts"

        self.layout_filenames = ["head.html", "header.html", "footer.html"]
        self.layout_files = []
        self.img_exts = [".jpg", ".png"]


        self.wide_pages = [
                "adventure.html",
                "landscape.html",
                "mans-best-friend.html",
                "plants.html",
                "wildlife.html"
        ]

        # Read the common layouts of each page
        for f in self.layout_filenames:
            with open(self.layouts_folder + "/" + f, "r") as infile:
                self.layout_files.append(infile.read())

    def combine_layouts(self, body):

        page = "<!DOCTYPE html>\n"
        page += "<html>\n"
        page += self.layout_files[0]
        page += "    <body>\n"
        page += self.layout_files[1]
        page += body
        page += self.layout_files[2]
        page += "    </body>\n"
        page += "</html>"

        return page

    def save_page(self, page, name):

        with open(name, "w") as outfile:
            outfile.write(page)

        print("Created", name)

    def build_pages(self):

        for f in os.listdir(self.pages_folder):

            # Check that the page is a .html file
            if os.path.splitext(f)[1] != ".html":
                continue

            # Read the content for this specific page
            with open(self.pages_folder + "/" + f, "r") as infile:
                body = infile.read()

            # Combine the common layouts and the page content
            page = self.combine_layouts(body)

            # Check if the page should have a wide body
            if os.path.basename(f) in self.wide_pages:
                page = page.replace("<body>", "<body class=wide>")

            self.save_page(page, f)



        for f in os.listdir(self.standalone_folder):

            # Check that the page is a .html file
            if os.path.splitext(f)[1] != ".html":
                continue

            # Read the content for this specific page
            with open(self.standalone_folder + "/" + f, "r") as infile:
                body = infile.read()

            self.save_page(body, f)


    def build_blog(self):

        blog_links = []
        blog_titles = []
        blog_dates = []
        blog_rfcdates = []
        blog_contents = []

        for f in os.listdir(self.posts_folder):
            # if os.path.isdir(f) and "index.md" in os.listdir(f):
            if os.path.isdir(self.posts_folder + "/" + f):
                if "index.md" in os.listdir(self.posts_folder + "/" + f):

                    draft = False

                    with open(self.posts_folder + "/" + f + "/" + "index.md",
                            "r") as infile:
                        lines = infile.readlines()

                    title = ""
                    date = ""

                    for line in lines:
                        if line.startswith("title:"):
                            title = line.replace("title: ", "")
                        if line.startswith("date:"):
                            date = line.replace("date: ", "")
                        if line.startswith("draft:"):
                            draft = line.replace("draft: ", "")
                            draft = draft.replace('"', "")
                            draft = draft.strip()

                    if draft == "true":
                        continue

                    title = title.replace('"', "")
                    date = datetime.datetime.strptime(date[:10], "%Y-%m-%d")
                    rfcdate = utils.format_datetime(date)
                    print_date = datetime.datetime.strftime(date, "%d %b %Y")

                    os.system(
                            "pandoc {}/{}/index.md -o {}/{}/index.html".format(
                                self.posts_folder, f, self.posts_folder, f
                    ))
                    
                    # body = "<h2>blog</h2>"
                    # body += "\n"
                    body = "<article>"
                    body += "\n"
                    body += "<h2>" + title + "</h2>"
                    body += "\n"
                    body += "<h3>" + print_date + "</h3>"

                    blog_link = self.posts_folder + "/" + f + "/" + "index.html"

                    with open(blog_link, "r") as infile:
                        content = infile.read()

                    content = content.replace("{{&lt; rawhtml &gt;}}", "")
                    content = content.replace("{{&lt; /rawhtml &gt;}}", "")

                    body += content

                    body += "</article>"
                    body += "\n"


                    page = self.combine_layouts(body)

                    self.save_page(page, blog_link)

                    date = datetime.datetime.strftime(date, "%Y-%m-%d")
                    blog_links.append(blog_link)
                    blog_titles.append(title)
                    blog_dates.append(date)
                    blog_rfcdates.append(rfcdate)
                    blog_contents.append(content)

        body = "<article>"
        body += "<h2>blog</h2>"
        body += "\n"
        body += "\n"
        body += "<ul>"
        body += "\n"

        blog_dates, blog_titles, blog_links, blog_contents, blog_rfcdates = zip(
                *sorted(zip(blog_dates, blog_titles, blog_links, blog_contents,
                    blog_rfcdates))
        )


        blog_dates = list(reversed(list(blog_dates)))
        blog_links = list(reversed(list(blog_links)))
        blog_titles = list(reversed(list(blog_titles)))
        blog_contents = list(reversed(list(blog_contents)))
        blog_rfcdates = list(reversed(list(blog_rfcdates)))


        shortblogfeed = "<h2>Latest posts</h2>"
        shortblogfeed += "<ul>"
        length = 3
        counter = 0

        for l, t, d in zip(blog_links, blog_titles, blog_dates):
            

            if counter < length:
                shortblogfeed += f"<li><span class=date>{d}</span><a href='{l}'>{t}</a></li>"
                counter += 1


            # d = datetime.datetime.strftime(d, "%d %b %Y")
            # d = datetime.datetime.strftime(d, "%Y-%m-%d")
            body += f"<li><span class=date>{d}</span><a href='{l}'>{t}</a></li>"
                    
        body += "</ul>"
        shortblogfeed += "</ul>"

        page = self.combine_layouts(body)
        self.save_page(page, "blog.html")

        self.blog_dates = blog_dates
        self.blog_links = blog_links
        self.blog_titles = blog_titles
        self.blog_contents = blog_contents
        self.blog_rfcdates = blog_rfcdates


        with open("index.html", "r") as f:
            index = f.read()
            index = index.replace("<!--BLOGFEED-->", shortblogfeed)

        with open("index.html", "w") as f:
            f.write(index)

    def generate_rss(self):

        with open("rssfeedtemplate.xml", "r") as f:
            feed = f.read()

        with open("rssitemtemplate.xml", "r") as f:
            item_template = f.read()


        items = ""

        for l, t, d, c in zip(self.blog_links, self.blog_titles, self.blog_rfcdates, self.blog_contents):

            c = re.sub(r"<script(.|\n)+?script>", "", c)
            c = re.sub(r"<link(.)+?>", "", c)
            c = c.replace(
                    'src="posts', 'src="' + self.baseurl + 'posts'
            )
            c = html.escape(c)


            item = item_template.format(
                    t, self.baseurl + l, d, self.baseurl + l, c
            )


            items += item

        date = datetime.datetime.now()
        rfcdate = utils.format_datetime(date)
        feed = feed.format(rfcdate, items)

        self.save_page(feed, "index.xml")



    # def build_galleries(self):

    #     for f in os.listdir(self.photography_folder):
    #         if os.path.isdir(f):

    #             body = "<h1>Erik Johannes Husom's photography</h1>"
    #             body += "\n"
    #             body += "<h2>" + f + "</h2>"
    #             body += "\n"
    #             body += "<section class=gallerymasonry>"

    #             for img in os.listdir(self.photography_folder + "/" + f):
    #                 if os.path.splitext(img)[1].lower() in self.img_exts:
    #                     body += "    <section class=galleryitem>"
    #                     body += 

    #             body += "</section>"

    #             page = self.combine_layouts(body)

    #             self.save_page(page, f + ".html")


if __name__ == '__main__':

    website = Website()
    website.build_pages()
    website.build_blog()
    website.generate_rss()

