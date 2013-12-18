#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import pickle
import urllib2

from PySide import QtCore, QtGui
from bs4 import BeautifulSoup

from ..helpers.constants import IDE_WIKI_DOCS
from ..helpers.dialogs import Dialogs
from ...frames.wiki_doc_widget import Ui_Form_wiki


########################################################################
class WikiWidget(QtGui.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        super(WikiWidget, self).__init__()
        
        self.main_widget = Ui_Form_wiki()
        self.main_widget.setupUi(self)
        
        self.main = parent
        
        self.to_ignore = ["Examples"]
        
        self.count_lib = 1
        
        self.html_doc = "<html>"
        
        self.build_header()
        self.build_title()
        

        libs = self.get_libraries()
        libs_html = ""
        self.index_html = ""
        for lib in libs:
            libs_html += self.build_library(**lib)
        
        
        self.html_doc += self.index_html + "<hr>"
        self.html_doc += libs_html
        
        
        self.html_doc += "</body></html>"        
    
        #self.main_widget.textEdit_doc.insertHtml(self.html_doc)
        self.main_widget.textBrowser_doc.insertHtml(self.html_doc)
        self.main_widget.textBrowser_doc.moveCursor(QtGui.QTextCursor.Start)
        
        
        self.connect(self.main_widget.textBrowser_doc, QtCore.SIGNAL("sourceChanged(QUrl)"), self.open_tab_doc)
        #self.connect(self.main_widget.textBrowser_doc, QtCore.SIGNAL("anchorClicked(QUrl)"), self.open_tab_doc)
        
    #----------------------------------------------------------------------
    def open_tab_doc(self, url):
        """"""
        url = url.toString()
        if url == "__update__":
            Dialogs.info_message(self.main, "This will take a long time.")
            self.update_from_wiki()
            return
        
        if not "http" in url: return
        
            
        #print url[1:]
        self.main.set_url_wiki_docs(url[1:])
        #self.replace_with_url(url[1:])
        #wiki_widget = WikiWidget(self.main)
        #setattr(wiki_widget, "is_widget", True)
        #self.replace_with_url(url)
        #self.main.tabWidget_files.addTab(wiki_widget, "Docs - Wiki")        
        
        
        
    #----------------------------------------------------------------------
    def replace_with_url(self, url):
        """"""
        html = self.get_html_from_url(url)
        soup = BeautifulSoup(html)
        title = soup.find_all("h1", attrs={"id":"firstHeading"})[0].text
        content = soup.find_all("div", attrs={"id": "content"})[0]
        #content = soup.
        self.main_widget.textBrowser_doc.clear()
        
        
        
        delete = []
        delete.append(content.find("h3",attrs={"id":"siteSub"}).extract())
        delete.append(content.find("div",attrs={"id":"jump-to-nav"}).extract())
        delete.append(content.find("div",attrs={"class":"printfooter"}).extract())
        delete.append(content.find("div",attrs={"id":"catlinks"}).extract())
        
        content = str(content.extract())
        
        content = content.replace('<div id="bodyContent">', '<hr><div id="bodyContent">')
        
        for d in delete:
            content = content.replace("", "")
        
        
        
        html = """
            <html>
            <head>
                %s
            </head>
            <body>
                %s
            </body>
        </html>"""% (self.stylesheet(), content)
        
        self.main_widget.textBrowser_doc.insertHtml(html)
        self.main_widget.textBrowser_doc.moveCursor(QtGui.QTextCursor.Start)
        
        return title
        
        
    #----------------------------------------------------------------------
    def get_libraries(self):
        """"""
        if not os.path.isfile(IDE_WIKI_DOCS):
            libs = self.update_from_wiki()
            pickle.dump(libs, file(IDE_WIKI_DOCS, "w"))
            return libs
            
        else:
            return pickle.load(file(IDE_WIKI_DOCS, "r"))
            
        
    #----------------------------------------------------------------------
    def update_from_wiki(self):
        """"""
        url = "http://wiki.pinguino.cc"
        html = self.get_html_from_url(url+"/index.php/Category:Libraries")
        soup = BeautifulSoup(html)
        if not soup.find_all("table"): return []
        
        table = soup.find_all("table")[1]
        
        libs = []
        for lib in table.find_all("a"):
            description, funtions = self.get_functions(url+lib.get("href"))
            libs.append({
                "href": url+lib.get("href"),
                "name": lib.text,
                "functions": funtions,
                "description": description,
            })
            
        return libs
        
    #----------------------------------------------------------------------
    def get_functions(self, url):
        """"""
        html = self.get_html_from_url(url)
        soup = BeautifulSoup(html)
        
        print "\n" + "*" * 70
        print url
        print "*" * 70 + "\n"  
                
        mw_pages = soup.find_all("div", attrs={"id":"mw-pages"})
        
        if not mw_pages: return "", []
        
        mw_pages = mw_pages[0]
        
        try: description = soup.find_all("table")[0].find_all("tr")[1].text
        except: description = ""
        
        funcs = []
        for func in mw_pages.find_all("a"):
            funcs.append({
                "href": "http://wiki.pinguino.cc"+func.get("href"),
                "name": func.text,
            })
            
        return description, funcs
        
    #----------------------------------------------------------------------
    def get_html_from_url(self, url):
        """"""
        page = urllib2.urlopen(url)
        html = page.readlines()
        page.close()
        return "".join(html)
        
    
    #----------------------------------------------------------------------
    def build_header(self):
        """"""
        html = """
        <head>
        
        <!--styles-->
        <style>
        
        body{
            margin: 10px;
        }
        
        div#title a:link,
        div#title a:visited,
        div#title a:hover{
            color: #3C3CFF;
	    text-decoration: none;
        }
        
        div#title{
            margin: 10px;
            font-size: 25px;
            font-weight: bold;
        }
        p#update a:link,
        p#update a:visited,
        p#update a:hover{
            color: #3C3CFF;
	    text-decoration: underline;
        }
        
        p#update{
            margin: 0px;
            font-size: 12px;
            font-weight: normal;
        }
	
        div.lib{
            font-size: 16px;
            font-weight: bold;
        }
        
        div.lib a:link,
        div.lib a:visited,
        div.lib a:hover{
            color: #3030C7;
            text-decoration: none;
        }
        
        .list a:link,
        .list a:visited,
        .list a:hover,{
            color: #5555ff;
            text-decoration: underline;
            font-size: 13px;
        }
        
        
        div#des{
            color: #3f3f3f;
            float: left;
        }
        
        
        
        
        
        
        </style>
        
            
        </head>
        """
        self.html_doc += html
        
        
    #----------------------------------------------------------------------
    def stylesheet(self):
        """"""
        
                
        return """
        
        <style type="text/css">
        
        
	body{
            margin: 10px;
	   color: #3f3f3f;
        }
        

        h1#firstHeading{
            color: #3C3CFF;
            margin: 10px;
            font-size: 25px;
            font-weight: bold;
        }
        
        h2{
            
        }        
        */
        
        .source-c {line-height: normal;}
        .source-c li, .source-c pre {
                line-height: normal; border: 0px none white;
        }
        /**
         * GeSHi Dynamically Generated Stylesheet
         * --------------------------------------
         * Dynamically generated stylesheet for c
         * CSS class: source-c, CSS id: 
         * GeSHi (C) 2004 - 2007 Nigel McNie, 2007 - 2008 Benny Baumann
         * (http://qbnz.com/highlighter/ and http://geshi.org/)
         * --------------------------------------
         */
        .c.source-c .de1, .c.source-c .de2 {font: normal normal 1em/1.2em monospace; margin:0; padding:0; background:none; vertical-align:top;}
        .c.source-c  {font-family:monospace;}
        .c.source-c .imp {font-weight: bold; color: red;}
        .c.source-c li, .c.source-c .li1 {font-weight: normal; vertical-align:top;}
        .c.source-c .ln {width:1px;text-align:right;margin:0;padding:0 2px;vertical-align:top;}
        .c.source-c .li2 {font-weight: bold; vertical-align:top;}
        .c.source-c .kw1 {color: #b1b100;}
        .c.source-c .kw2 {color: #000000; font-weight: bold;}
        .c.source-c .kw3 {color: #000066;}
        .c.source-c .kw4 {color: #993333;}
        .c.source-c .co1 {color: #666666; font-style: italic;}
        .c.source-c .co2 {color: #339933;}
        .c.source-c .coMULTI {color: #808080; font-style: italic;}
        .c.source-c .es0 {color: #000099; font-weight: bold;}
        .c.source-c .es1 {color: #000099; font-weight: bold;}
        .c.source-c .es2 {color: #660099; font-weight: bold;}
        .c.source-c .es3 {color: #660099; font-weight: bold;}
        .c.source-c .es4 {color: #660099; font-weight: bold;}
        .c.source-c .es5 {color: #006699; font-weight: bold;}
        .c.source-c .br0 {color: #009900;}
        .c.source-c .sy0 {color: #339933;}
        .c.source-c .st0 {color: #ff0000;}
        .c.source-c .nu0 {color: #0000dd;}
        .c.source-c .nu6 {color: #208080;}
        .c.source-c .nu8 {color: #208080;}
        .c.source-c .nu12 {color: #208080;}
        .c.source-c .nu16 {color:#800080;}
        .c.source-c .nu17 {color:#800080;}
        .c.source-c .nu18 {color:#800080;}
        .c.source-c .nu19 {color:#800080;}
        .c.source-c .me1 {color: #202020;}
        .c.source-c .me2 {color: #202020;}
        .c.source-c .ln-xtra, .c.source-c li.ln-xtra, .c.source-c div.ln-xtra {background-color: #ffc;}
        .c.source-c span.xtra { display:block; }
        
        /*]]>*/
        </style>"""    
        
    
    #----------------------------------------------------------------------
    def build_library(self, href, name, description, functions):
        """"""
        if name in self.to_ignore: return ""
        
        name = name.replace("Library", "")
            
    
        html_funcs = self.build_functions(functions, str(self.count_lib))
        

        html = """
        <div class="lib" id="%s">%s. <a href="%s">%s</a></div>
        
        """% (name.replace(" ", "_"), str(self.count_lib), href, name)
        
        self.index_html += """<div class="list">%s. <a href="#%s">%s</div>""" % (str(self.count_lib), name.replace(" ", "_"), name)
        
        if description:
            html += """<div id="des">%s</div>""" % description
           
        
        self.count_lib += 1
        
        return html + html_funcs  # + "<hr>"            
        
    #----------------------------------------------------------------------
    def build_functions(self, functions, number):
        """"""
        
        html = ""
        count = 1
        for func in functions:
            html += """
            <div class="list" id="func">%s.%d <a href="#%s">%s</a></div>
            """% (number, count, func["href"], func["name"])
            count += 1
        
        
        return html + "<br>"
        
    
    #----------------------------------------------------------------------
    def build_title(self):
        """"""
        html = """
        <body>
        <p id="update" align="right"><a href="__update__">Update libraries</a></p>
        <div id="title"><a href="http://wiki.pinguino.cc/">Pinguino Libraries</a></div>
        <hr>
        """
        self.html_doc += html
        
        