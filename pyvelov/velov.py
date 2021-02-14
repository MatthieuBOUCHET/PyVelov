import api

RAW_DATAS = api.createAPIInstance()

class VelovStation:
    """
    Class represents a Velov' Station.

    Attributes:
    -----------

    """
    def __init__(self,dictData) -> None:
        """Constructor

        Args:
            dictData (dictionnary): Dictionnary released from `api.createAPIInstance()`

        Returns:
            None
        """
        self.id = dictData['number']
        self.gid = dictData['gid']

        self.name = dictData['name']
        self.adress = dictData['adress']
        self.adress2 = dictData['adress2']
        self.commune = dictData['commune']
        self.pole = dictData['pole']
        self.latitude = dictData['lat']
        self.longitude = dictData['lng']
        self.totalStands = dictData['bike_stands']
        self.availableStands = dictData['available_bike_stands']
        self.availableBikes = dictData['available_bikes']
        self.status = self.statusConvert(dictData['status'])
        self.availability = dictData['availabilityCode']
        self.banking = dictData['banking']
        self.updateDateTime = dictData['last_update']
        self.insee = self.stringToInt(dictData['code_insee'])


        return None

    def statusConvert(self,status) -> bool:
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

    def stringToInt(self,parameter) -> int:
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


pass