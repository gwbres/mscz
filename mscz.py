from lxml import etree
class Mscz:
    Clefs = ["G", "F"]
    def __init__ (self, fp):
        self.root = etree.parse(fp)
    
    def __handle (self, tag, r=None):
        """ 
        Returns handle pointer to child matching given tag
        """
        if r is None:
            r = self.root
        for child in r.iter():
            if child.tag == tag:
                return child
        return None

    def score (self):
        """ 
        Returns handle to Score marker 
        """
        return self.__handle("Score")
    
    def part (self):
        return self.__handle("Part", r=self.score())

    def style (self):
        """ 
        Returns handle to Style marker 
        """
        return self.__handle("Style", r=self.score())
    
    def page_layout (self):
        """ 
        Returns handle to page layout 
        """
        return self.__handle("page-layout", r=self.style())
    
    def page_geometry (self):
        """ 
        Returns Page geometry as (Height, Width) tuple 
        """
        (h,w) = (None,None)
        for c in self.page_layout():
            if c.tag == "page-height":
                h = float(c.text)
            elif c.tag == "page-width":
                w = float(c.text)
        return (h,w)

    def page_geometry_advanced (self):
        """ 
        Returns Page geometry as complex dict, with margins 
        """
        (h, w) = self.page_geometry()
        for child in self.__handle("page-margins", r=self.page_layout()):
            print(child.tag) #TODO

    def __len__ (self):
        """ 
        Returns number of staffs contained in self 
        """
        i = 0
        for child in self.part():
            if child.tag == "Staff":
                i += 1
        return i

    def staff (self, id):
        """ 
        Returns handle to desired track 
        """
        for child in self.part():
            if child.tag == "Staff":
                if "id" in child.attribute:
                    if child.attribute["id"] == id:
                        return child

    def total_measures (self):
        """
        Returns total number of measures
        """
        m = 0
        for c in self.score().iter():
            if c.tag == "Measure":
                m += 1
        return m // len(self) #TODO a revoir
