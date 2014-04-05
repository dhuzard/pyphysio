__author__ = 'AleB'

from pyHRV.windowing import *
from pyHRV.Files import *
from pyHRV.indexes import TDIndexes as Td


def main():
    rr = load_rr_data_series("../z_data/D01.txt")
    wg = LinearWinGen(0, 20, 40, rr)
    wm = WindowsMapper(rr, wg, Td.Mean)
    ws = WindowsMapper(rr, wg, Td.STD)
    wx = WindowsMapper(rr, wg, Td.DGT20)
    wm.compute()
    ws.compute()
    wx.compute()
    print wm.results
    print ws.results
    print wx.results


if __name__ == "__main__":
    main()
