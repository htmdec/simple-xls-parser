import xls
import glob

for fn in sorted(glob.glob("data/*.xls")):
    print(fn)
    ll = xls.Xls.from_file(fn)

