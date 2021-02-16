"""
File from module `pyvelov`. Contains all features required to manipulate stations and operate on stations.

Author: Matthieu BOUCHET
Author email: matthieu.bouchet@outlook.com
Author website: https://www.matthieubouchet.fr
GitHub project: https://github.com/MatthieuBOUCHET/PyVelov
"""


from os import remove
from json import dumps
from datetime import datetime




class VelovStation:
    """
    Class represents a Velov' Station.

    Attributes:
    -----------

    """

    def __init__(self, dictData) -> None:
        """Constructor

        Args:
            dictData (dictionnary): Dictionnary released from `api.createAPIInstance()`

        Returns:
            None
        """
        self.uid = dictData['number']
        self.gid = dictData['gid']

        self.name = dictData['name']
        self.adress = dictData['address']
        self.adress2 = dictData['address2']
        self.commune = dictData['commune']
        self.pole = self.__poleSplit(dictData['pole'])
        self.latitude = dictData['lat']
        self.longitude = dictData['lng']
        self.totalStands = dictData['bike_stands']
        self.availableStands = dictData['available_bike_stands']
        self.availableBikes = dictData['available_bikes']
        self.status = self.__statusConvert(dictData['status'])
        self.availability = dictData['availabilitycode']
        self.banking = dictData['banking']
        self.updateDateTime = dictData['last_update']
        self.insee = self.__stringToInt(dictData['code_insee'])

        self.availabilityStandsPercentage = self.__availabilityStandsPercentageCalculator()

        return None

    def __str__(self) -> str:
        return self.getAttribute('name')

    def __statusConvert(self, status) -> bool:
        """Method convert a string to boolean

        Args:
            status (string OR None): "OPEN" or "CLOSED" or None

        Returns:
            (bool): True if "OPEN", False if else.
        """
        if status == "OPEN":
            return True
        else:
            return False

    def __stringToInt(self, parameter) -> int:
        """Method convert string INSEE code to integer.

        Args:
            parameter (string OR None): parameter from API datas.

        Returns:
            (int OR None): INSEE released from API datas.
        """

        if parameter is not None:
            try:
                return int(parameter)
            except:
                return parameter
        return parameter

    def __availabilityStandsPercentageCalculator(self) -> float:
        """Calculate percentage of Stands available

        Returns:
            float or None: Return float(2 digits after comma) or None
        """
        if self.availableStands is None or self.totalStands is None:
            return None

        percentage = (100 * self.availableStands) / self.totalStands
        return round(percentage, 2)

    def __poleSplit(self,datasPole) -> tuple:
        """Split poles

        Args
        ----
        datasPole(string):String of datas

        Returns
        --------
            tuple: Tuple of poles
        """
        if datasPole is None:
            return None

        polesSplited = datasPole.split(', ')

        polesSplited = tuple(polesSplited)
        return polesSplited

    ## GETTERS ##
    def getAll(self) -> dict:
        """Return all attributes (self.__dict__)

        Returns:
            dict: Dict of attributes
        """
        return self.__dict__

    def getAttribute(self, attribute):
        """Return attribute passed in parameter

        Args:
            attribute (string): Attribute searched

        Returns:
            Mixed or None: Attribute
        """
        try:
            return self.getAll()[attribute]
        except KeyError:
            return None

    ## PUBLIC METHODS ##
    def dateTimeExport(self) -> object:
        """Method convert a attribute `updateDateTime`(string) to datetime object

        Args:
            self.strDateTime (string OR None): String of datetime released from API datas.
            (%Y-%m-%d %X)

        Returns:
            (datetime object): Return a date time object
            (None): If argument `strDateTime` is None
        """
        if self.updateDateTime is None:
            return None

        DateTimeSplit = self.getAttribute("updateDateTime").split(" ")
        date = DateTimeSplit[0]
        time = DateTimeSplit[1]

        dateSplited = date.split('-')
        timeSplited = time.split(':')

        dateSplited = [int(element) for element in dateSplited]
        timeSplited = [int(element) for element in timeSplited]

        return datetime(dateSplited[0], dateSplited[1], dateSplited[2], timeSplited[0], timeSplited[1], timeSplited[2])

    
    def exportJSON(self) -> str:
        """Method exports in JSON datas (string) the datas of station

        Returns:
            string: String of JSON serialized datas.
        """
        datas = self.getAll()
        return dumps(datas)

    def exportJSONFile(self, fileName=None) -> bool:
        """Method creates and write a file with JSON datas.
        The file created is named : VELOVStation_[UID]

        Args
        ----
        fileName(string): Optional. Name given to file
        Returns
        -------
            bool: True if success and False if fail.
        """
        uid = self.getAttribute("uid")
        if fileName is None:
            fileName = "VELOVStation_{0}.json".format(uid)
        else:
            fileName = str(fileName)

        # CREATE JSONDATAS
        try:
            jsonDatas = self.exportJSON()
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

pass
