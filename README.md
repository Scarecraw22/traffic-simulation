Converting:

`netconvert --osm-files bronowice.osm -o bronowice.net.xml --geometry.remove --roundabouts.guess --ramps.guess --junctions.join --tls.guess-signals --tls.discard-simple --tls.join`

Random trips:

`python .\randomTrips.py -n custom.net.xml -e 200 -r custom.routes.xml -l --begin 0 --end 800 --period 2`

Speed limits:

- 5.55 - 20km/h
- 8.33 - 30km/h
- 11.11 - 40km/h
- 13.89 - 50km/h
- 16.67 - 60km/h
- 19.44 - 70km/h

Algorithm:
```
jednostka = 0
samochody = []
trasy = generujTrasy()

while jednostka < 1000

    for each samochod in samochody:
        samochod.kolejnyKrok()
    
    if jednostka % 2 == 0 && jednostka < 800:
        wierzcholek = losuj(A, G)
        trasa = wybierzTrase(trasy)
        samochod = generujSamochod(wierzcholek, trasa)
        samochody.add(samochod)
```