#!/usr/bin/python3

class Restaurant(object):
    def __init__(self, name=None, weight=None):
        if name!=None:
            self.name = name
        if weight!=None:
            self.weight = weight
