import xml.sax
from xml.dom import minidom

class AlbumHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.author = ""
        self.genere = ""
        self.year = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "album":
            print("-----------------------------------------------------------")
            title = attributes["title"]
            print(f"Album title: {title}")

    def endElement(self, tag):
        if self.CurrentData == "author":
            print(f"Author: {self.author}")
        elif self.CurrentData == "genere":
            print(f"Genere: {self.genere}")
        elif self.CurrentData == "year":
            print(f"Year: {self.year}")
        elif self.CurrentData == "description":
            print(f"Description: {self.description}")
        self.CurrentData = ""


    def characters(self, content):
        if self.CurrentData == "album":
            self.album = content
        elif self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "genere":
            self.genere = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "description":
            self.description = content


def main():
    parser_xml = xml.sax.make_parser()
    sax_handler = AlbumHandler()
    parser_xml.setContentHandler(sax_handler)
    parser_xml.parse(r'C:\Users\karol\Desktop\Python_zajecia\zad_17_xml.xml')
    parser_dom = minidom.parse(r'C:\Users\karol\Desktop\Python_zajecia\zad_17_xml.xml')

    collection = parser_dom.documentElement

    albums = collection.getElementsByTagName("album")

    for album in albums:
        author = album.getElementsByTagName('author')[0]
        description = album.getElementsByTagName('description')[0]
        if author.childNodes[0].data == "Marina":
            print("Current description: ", description.childNodes[0].data)
            desc_marina = description.childNodes[0].data
            new_desc = desc_marina + " Her previous name was Marina and The Diamonds."
            print("New description: ", new_desc)
            description.childNodes[0].data = new_desc

    with open (r'C:\Users\karol\Desktop\Python_zajecia\_modified_zad_17_xml.xml', 'w+') as file:
        file.write(parser_dom.toxml())

if __name__ == "__main__":
    main()


