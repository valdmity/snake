from objects.map_cell import *


def parse_map(sym_map):
    if len(sym_map) == 0 or len(sym_map[0]) == 0:
        raise Exception("map len shouldn't be zero")
    nmap = [[MapCell.empty for _ in range(len(sym_map[0]))] for _ in range(len(sym_map))]
    for y in range(len(nmap)):
        for x in range(len(nmap[0])):
            nmap[y][x] = mapcell_by_sym[sym_map[y][x]]
    return nmap
