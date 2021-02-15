"""
File from module `pyvelov`. Contains all features required to manipulate stations and operate on multiple
stations (list of stations).

Author : Matthieu BOUCHET
Author email : matthieu.bouchet@outlook.com
Author website: https://www.matthieubouchet.fr
GitHub project: https://github.com/MatthieuBOUCHET/PyVelov
"""

class VelovStationsList(list):
    def __init__(self,*args) -> None:
        for station in args:
            pass
    
    def append(self, station) -> None:
        """Overloading of append function.
        Call parent list class append method.

        Args:
            station (VelovStation): [description]

        Returns:
            [type]: [description]
        """
        #TYPE VERIFICATION
        typeArg = str(type(station))
        if not('VelovStation' in typeArg):
            raise ValueError('Argument must be VelovStation')
        return super().append(station)

pass