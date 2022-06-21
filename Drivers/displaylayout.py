from argparse import ArgumentError
import dataclasses

class DisplayLayout():
    def __init__(self, clustersize : int, *args : list):
        first_width = None
        for line in args:
            if first_width == None:
                first_width = len(line)
            else:
                if first_width != len(line):
                    raise ValueError("All Lines in DisplayLayout need to be of same length.")
            if type(line) != list:
                raise ArgumentError(message="All Arguments of DisplayLayout.__init__ must be of type list.")
        matrix = args
        self.width = clustersize * len(args[0])
        self.height = clustersize * len(args)
        