# PyVelov
 Python library interacting with Velov API.

## Origin of data

Data are provided by *Data Grand Lyon Métropole* (https://data.grandlyon.com/jeux-de-donnees/stations-velo-v-metropole-lyon-disponibilites-temps-reel/donnees)

All legal informations on data can be found here : https://download.data.grandlyon.com/licences/ETALAB-Licence-Ouverte-v2.0.pdf

![https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Logo_Grand_Lyon.svg/1280px-Logo_Grand_Lyon.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Logo_Grand_Lyon.svg/1280px-Logo_Grand_Lyon.svg.png)

![Résultat de recherche d'images pour "velov logo"](https://upload.wikimedia.org/wikipedia/fr/thumb/0/05/Logo_V%C3%A9lo%27V.svg/700px-Logo_V%C3%A9lo%27V.svg.png)

## Installation

### *Via* PIP

```
pip install -i https://test.pypi.org/simple/ pyvelov
```

### *Via* GitHub

```
git clone https://github.com/MatthieuBOUCHET/PyVelov.git
python -m setup.py install
```

## Package use

### Parts

There are 3 parts in this package :

- `api`
- `station`
- `stationslist`

#### How to import a part ?

```python
from pyvelov.api import *
from pyvelov.station import *
from pyvelov.stationslist import *
```

If you import `stationslist`, `api` and `station` are already imported and are accessible via `api.` and `station.`

### Reserved variable

The variable named `RAW_DATAS` is **RESERVED**.

### `api` 

#### How to access raw data from API ?

```python
>>> import pyvelov.api as api
>>> data = api.createAPIInstance()
({'number': 32001, 'pole': ' ', 'available_bikes': 7, 'code_insee': '69068', 'lng': 4.83241213375528, 'availability': 'Vert', 'availabilitycode': 1, 'etat': None, 'startdate': None, 'langue': None, 'bike_stands': 17, 'last_update': '2021-02-17 11:21:20', 'available_bike_stands': 10, 'gid': 1277, 'titre': None, 'status': 'OPEN', 'commune': "COUZON-AU-MONT-D'OR", 'description': None, 'nature': None, 'bonus': '', 'address2': None, 'address': 'Quai Jean Lavergne', 'lat': 45.84599768675746, 'last_update_fme': '2021-02-17 11:29:02', 'enddate': None, 'name': 'Couzon - Centre', 'banking': False, 'nmarrond': None}, {'number': 5016, 'pole': 'Mairie de Lyon 5ème', 'available_bikes': 10, 'code_insee': '69385', 'lng': 4.802711079169014, 'availability': 'Vert', 'availabilitycode': 1, 'etat': None, 'startdate': None, 'langue': None, 'bike_stands': 13, 'last_update': '2021-02-17 11:28:21', 'available_bike_stands': 3, 'gid': 809, 'titre': None, 'status': 'OPEN', 'commune': 'Lyon 5 ème', 'description': None, 'nature': None, 'bonus': '', 'address2': None, 'address': '49, Avenue du Point du Jour', 'lat': 45.75619392865888, 'last_update_fme': '2021-02-17 11:29:02', 'enddate': None, 'name': 'Point du Jour / Granges', 'banking': False, 'nmarrond': 16},...)
```

##### `createAPIInstance()`

`createAPIInstance()`is a public function called in order to instantiate an `APIConnection`. If a problem occurred during `APIConnection` construction, a `VelovAPIError` is raised. Else, a tuple of dictionaries is returned. 

Data are pure raw and untreated.

### `station`

#### How to manipulate data of ONE station

A class named `VelovStation` is available. In order to create a `VelovStation` object, raw data from API is necessary.

Example below shows a `VelovStation` based on first station returned by API.

```python
>>> import pyvelov.api as api
>>> import pyvelov.station as station

>>> dataAPI = api.createAPIInstance()
>>> dataStation = dataAPI[0]

>>> velovStation = VelovStation(dataStation)
```

All unknown attributes will be `None`

### `stationslist`

#### How to manipulate data of MULTIPLE station

A class named `VelovStationsList` is available. In order to create a `VelovStationsList` object, `VelovStation` object are necessary.

Example below shows a `VelovStationsList` based on three first stations returned by API.

```python
>>> import pyvelov.api as api
>>> import pyvelov.station as station

>>> dataAPI = api.createAPIInstance()
>>> dataStationA = dataAPI[0]
>>> dataStationB = dataAPI[1]
>>> dataStationC = dataAPI[2]

>>> velovStationA = VelovStation(dataStationA)
>>> velovStationB = VelovStation(dataStationB)
>>> velovStationC = VelovStation(dataStationC)
```

