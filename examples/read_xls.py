import xls
import glob
import time

for fn in sorted(glob.glob("data/*.xls")):
    t1 = time.time()
    with open(fn, "rb") as f:
        b = f.read()
    t2 = time.time()
    ll = xls.Xls.from_bytes(b)
    t3 = time.time()
    print(f"Reading {fn} - {t2-t1:0.3f} Parsing: {t3-t2:0.3f}")

for fn in sorted(glob.glob("data/*.xls")):
    t1 = time.time()
    ll = xls.Xls.from_file(fn)
    t2 = time.time()
    print(f"Reading and parsing {fn} - {t2-t1:0.3f}")

