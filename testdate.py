from datetime import datetime, timedelta
import pandas as pd
import os

### Datum ab wann man downloaden will, zB alles ab 2019-01-01!!!
AnfangsDatum = "2019-01-01"

gestern = str(datetime.now() - timedelta(1)).split(" ")[0]
daten = pd.date_range(start="2019-01-01",end="2020-07-04")

datenListe = list(str(data).split(" ")[0] for data in daten)
datenListe = datenListe[::-1]

dir = []
for directories in os.listdir():
    dir += [directories.replace(".json","")]

dir.remove("testdate.py")
dir.remove("Import.py")
dir.remove("OldPrograms")
dir.remove("Auswertung.txt")
dir.remove("Plot.py")

letztesDatum = min(dir)

for d in datenListe:
    if d not in dir:
        os.system("snscrape --jsonl --since "+d+" twitter-search \"#bitcoin until:"+str(datetime.strptime(d, "%Y-%m-%d")+timedelta(1)).split(" ")[0]+"\" > "+d+".json")
    else:
        if d != letztesDatum:
            print(d + " ist schon da und wird nicht downloaded.")
        else:
            os.system("snscrape --jsonl --since "+d+" twitter-search \"#bitcoin until:"+str(datetime.strptime(d, "%Y-%m-%d")+timedelta(1)).split(" ")[0]+"\" > "+d+".json")