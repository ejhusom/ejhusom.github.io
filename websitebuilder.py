#!/usr/bin/env python3
# ============================================================================
# File:     websitebuilder.py
# Author:   Erik Johannes Husom
# Created:  2019-11-04
# ----------------------------------------------------------------------------
# Description:
# Building a website from Markdown files with Python.
# ============================================================================
import os
import sys


class WebsiteBuilder():
    """Building a website from Markdown files.

    Directory structure:

    website/
    | _config.yml
    | _includes/
    | | footer.html
    | | head.html
    | | header.html
    | _layouts/
    | | default.html
    | _posts/
    | _sass/
    | | style.css


    Parameters
    ----------
    parameter : float
      Description.



    Attributes
    ----------
    attribute : float
       Description.

    array[float]
       Description.


    Notes
    -----

    
    References
    ----------


    Example
    -------
    >>>

    """


    def __init__(self):





        self.create_dir(directory='_site')


    def create_dir(self, directory='_site'):

        if not os.path.exists(directory):
            os.makedirs(directory)



    def markdown2html(self, filename):
        """Convert Markdown file to html.

        Parameters
        ----------
        filename : str
            Filename of the Markdown file to be converted.


        Notes
        -----


        Example
        -------
        >>>


        """
                
        if filename.endswith('.md') or filename.endswith('.markdown'):
            os.system()

    
    def assemble_html(self):
        """Oneliner.

        Parameters
        ----------
        parameter : float
          Description.


        Returns
        -------
        array[float]
           Description.


        Notes
        -----


        Example
        -------
        >>>


        """



