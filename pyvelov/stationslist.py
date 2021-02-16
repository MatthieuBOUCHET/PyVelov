"""
File from module `pyvelov`. Contains all features required to manipulate stations and operate on multiple
stations (list of stations).

Author : Matthieu BOUCHET
Author email : matthieu.bouchet@outlook.com
Author website: https://www.matthieubouchet.fr
GitHub project: https://github.com/MatthieuBOUCHET/PyVelov
"""

from pyvelov import *

from datetime import datetime
import os
import sqlite3

RAW_DATAS = createAPIInstance()


class VelovStationsList(list):
    """Class `VelovStationsList` is a class based on built-in `list` class.
    This class herits all attributes & methods from built-in `list` class.

    OVERLOADED METHODS
    -------------------
    - `append()`

    Parent
    -------
        - list (built-in): [description]
    """

    def __init__(self, total, *args) -> None:
        """Constructor with a variable number of arguments.
        Each *args argument must be a `VelovStation` class instanciation.

        Args
        ----
            total(bool): If True, create a list of entire stations released from API, if False, each stations must be specified via a dict data.

            *args MUST BE `VelovStation` class instanciations.

        Examples
        -------
        Example (Creation of list with specific stations):
            station1 = VelovStation(dataStation1)
            station2 = VelovStation(dataStation2)
            station3 = VelovStation(dataStation3)

            stationsList = VelovStationsList(False,station1, station2, station3)

            print(stationsList) => [station1,station2,station3]

        Example (Creation of list with all stations from API):
            stationsList = VelovStationsList(True)

        """
        if total:
            for stat in RAW_DATAS:
                stationCreation = VelovStation(stat)
                self.append(stationCreation)
        else:
            for station in args:
                self.append(station)

        self.totalAvailableBikes = self.__sumAttribute('availableBikes')
        self.totalAvailableStands = self.__sumAttribute('availableStands')
        self.totalStands = self.__sumAttribute('totalStands')
        self.percentageAvailableStands = round(
            self.totalAvailableStands * 100 / self.totalStands, 2)
        self.statusStations = self.__sumStationsBoolean('status')
        self.bankingStations = self.__sumStationsBoolean('banking')
        self.polesSet = self.__browserSet('pole')
        self.communesSet = self.__browserList('commune')

    ## OVERLOAD ##

    def append(self, station) -> None:
        """Overloading of append function.
        Call parent list class append method.
        Append an object at the end of the list.

        Args
        -----
            station (VelovStation): A `VelovStation` class instanciation.

        Raises
        ------
            ValueError if `station`argument is not a `VelovStation` class instanciation.
        Returns
        -------
            None
        """

        # TYPE VERIFICATION
        typeArg = str(type(station))
        if not('VelovStation' in typeArg):
            raise ValueError('Argument must be a VelovStation object')

        return super().append(station)

    ## STATS ##
    def __sumAttribute(self, attribute) -> int:
        """Calculate the sum of attribute from station stacked in `VelovStationList`

        Args
        -----
            attribute (string): One attribute from `VelovStation` class.
        """
        total = 0

        for station in self:
            temp = station.getAttribute(attribute)
            if temp is None:
                temp = 0

            total += temp

        return total

    def __sumStationsBoolean(self, attribute) -> tuple:
        """Calculate number of stations with attribute true or false.

        Args
        -----
            attribute (string): One attribute from `VelovStation` class.

        Returns
        --------
            (tuple): Tuple with 2 indexs
                [0] YES/OPEN/ON (int)
                [1] NO/CLOSED/ (int)

        Examples:
        ---------
            a = VelovStationsList()

            stats = a.getStats()

            stats => {
                ...
                'status':(121,205),
                'banking':(2,129)
            }

            Here, we can read => 121 stations OPEN and 205 stations CLOSED
                              => 002 stations WITH BANKING and 129 stations WITHOUT BANKING
        """

        total1 = 0
        total2 = 0

        for station in self:
            temp = station.getAttribute(attribute)

            if temp:
                total1 += 1
            else:
                total2 += 1

        return total1, total2

    def __browserList(self, attribute) -> set:
        """Method browses StationsList and Stations attribute selected

        Args
        ----
            attribute (string): One attribute from `VelovStation` class.

        Returns:
            set
        """
        convertibleiterable = []
        for station in self:
            convertibleiterable.append(station.getAttribute(attribute))

        return set(convertibleiterable)

    def __browserSet(self, attribute) -> set:
        """Method browses StationsList and Stations attribute (tuple) selected.

        Args
        -----
            attribute (tuple): One attribute from `VelovStation` class.

        Returns:
            set
        """
        convertibleIterable = []
        for station in self:
            attr = station.getAttribute(attribute)

            if attr is None:
                convertibleIterable.append(None)
            else:
                for element in attr:
                    convertibleIterable.append(element)

        return set(convertibleIterable)

    ## GETTERS ##
    def getProperties(self) -> dict:
        """Return all attributes (self.__dict__)

        Returns:
            dict: Dict of statistics

            Keys:
            - totalAvailableBikes (int)
            - totalAvailableStands (int)
            - percentageAvailableStands (float)
            - totalStands (int)
            - statusStations (tuple)
            - bankingStations (tuple)
            - polesSet (set)
            - communesSet (set)
        """

        return {
            'totalAvailableBikes': self.totalAvailableBikes,
            'totalAvailableStands': self.totalAvailableStands,
            'percentageAvailableStands': self.percentageAvailableStands,
            'totalStands': self.totalStands,
            'statusStations': self.statusStations,
            'bankingStations': self.bankingStations,
            'polesSet': self.polesSet,
            'communesSet': self.communesSet
        }

    ## EXPORTATION ##
    def exportListJSON(self) -> str:
        """Method export a JSON string

        Returns:
            strExp(str)
        """
        length = len(self)
        strExp = '['
        for station in range(length):
            strExp += self[station].exportJSON()
            if station != length - 1:
                strExp += ','
        strExp += ']'

        return strExp

    def exportListJSONFile(self, fileName=None) -> bool:
        """Method creates and write a file with JSON datas of all list.
        The file created is default named : VELOVStationList_date

        Args
        ----
        fileName(string): Optional. Name given to file
        Returns
        -------
            bool: True if success and False if fail.
        """
        dateTime = datetime.now()
        dateTime = dateTime.strftime('%d-%m-%Y-%H-%M-%S')
        if fileName is None:
            fileName = "VELOVStationList_{0}.json".format(dateTime)
        else:
            fileName = str(fileName)

        # CREATE JSONDATAS
        try:
            jsonDatas = self.exportListJSON()
        except:
            return False

        # WRITE AND CREATE FILE
        try:
            fileWrite = open(fileName, 'w+')
        except:
            return False

        try:
            fileWrite.write(jsonDatas)
        except:
            return False

        fileWrite.close()
        return True

    def exportJSONFilesIndex(self, path=None) -> bool:
        """Method creates a directory index with all JSON files.
        Directory is named 'VelovStationsJSONIndex_%d-%m-%Y-%H-%M-%S' and created
        in CWD.

        Returns:
            bool: True if success and False if fail.
        """
        dateTime = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        dirName = 'VelovStationsJSONIndex_{0}'.format(dateTime)
        initialCWD = os.getcwd()

        # Create directory
        try:
            os.mkdir(dirName)
        except:
            return False

        os.chdir('./'+dirName)

        for station in self:
            if not(station.exportJSONFile()):
                return False

        os.chdir(initialCWD)
        return True


pass
