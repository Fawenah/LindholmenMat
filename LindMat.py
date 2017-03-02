#!/usr/bin/python3
from restaurant import Restaurant
import math
rest_list_path = 'Restaurant_List.INF'

def list_columns(obj, cols=4, columnwise=True, gap=4):
    """
    Print the given list in evenly-spaced columns.

    Parameters
    ----------
    obj : list
        The list to be printed.
    cols : int
        The number of columns in which the list should be printed.
    columnwise : bool, default=True
        If True, the items in the list will be printed column-wise.
        If False the items in the list will be printed row-wise.
    gap : int
        The number of spaces that should separate the longest column
        item/s from the next column. This is the effective spacing
        between columns based on the maximum len() of the list items.
    """

    sobj = [str(item) for item in obj]
    if cols > len(sobj): cols = len(sobj)
    max_len = max([len(item) for item in sobj])
    if columnwise: cols = int(math.ceil(float(len(sobj)) / float(cols)))
    plist = [sobj[i: i+cols] for i in range(0, len(sobj), cols)]
    if columnwise:
        if not len(plist[-1]) == cols:
            plist[-1].extend(['']*(len(sobj) - len(plist[-1])))
        plist = zip(*plist)
    printer = '\n'.join([
        ''.join([c.ljust(max_len + gap) for c in p])
        for p in plist])
    print(printer)

def read_rest(rest_list_path):
    with open(rest_list_path) as f:
        rest_list_raw = f.readlines()
    rest_list_raw = [x.strip() for x in rest_list_raw]
    rest_list = []
    for line in rest_list_raw:
        rest_list.append(Restaurant(name=line, weight=1))
    return rest_list

def main():
    rest_list = read_rest(rest_list_path)
    str_list = []
    for element in rest_list:
        str_list.append(element.name)
    print('\nList of Restaurants at Lindholmen:\n')
    list_columns(obj=str_list, cols=3, columnwise=True, gap=4)

if __name__ == "__main__":
    main()
