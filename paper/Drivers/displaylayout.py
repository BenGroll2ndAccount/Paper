from argparse import ArgumentError

class DisplayLayout():
    def __init__(self, width : int = None, height : int = None, startwidget = None, clustersize : int = None, clusterlayout : list = None, widgetlayout : list = None):
        if width != None and height != None and startwidget != None:
            # Run Code for Simple Fullscreen application.
            self.width = width
            self.height = height
            self.startwidget = startwidget

        elif clustersize != None and clusterlayout != None and widgetlayout != None:
            # Run Code for Complex Multi-Display application
            first_width = None
            for line in clusterlayout:
                if first_width == None:
                    first_width = len(line)
                else:
                    if first_width != len(line):
                        raise ValueError("All Lines in DisplayLayout need to be of same length.")
                if type(line) != list:
                    raise ValueError(message="All Arguments of DisplayLayout.__init__ must be of type list.")
            matrix = clusterlayout
            self.width = clustersize * len(clusterlayout[0])
            self.height = clustersize * len(clusterlayout)
        else:
            return ValueError(message="Either ( width, height and startwidget ) or ( clustersize, clusterlayout and widgetlayout ), all have to be anything else but None.")

    @classmethod
    def simple(cls, width : int, height : int, startwidget = None):
        return cls(width = width, height = height, startwidget = startwidget)

    @classmethod
    def complex(cls, clustersize : int, clusterlayout : list, widgetlayout : list):
        return cls(clustersize = clustersize, clusterlayout = clusterlayout, widgetlayout = widgetlayout)

        