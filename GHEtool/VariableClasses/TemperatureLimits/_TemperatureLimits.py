import abc

import numpy as np

from GHEtool.VariableClasses.BaseClass import BaseClass


class _TemperatureLimits(BaseClass, abc.ABC):
    """
    Contains information regarding the temperature limits of the borefield.
    """

    def __init__(self, constant_limits: bool):
        """

        Parameters
        ----------
        constant_limits : bool
            True if the limit class uses constant limits
        """
        self.constant_limits = constant_limits
        self._max_temperature = None
        self._min_temperature = None
        # TODO check that L2 does not work with non-constant temperature limits

    @abc.abstractmethod
    def check_input(self, temperature_limit) -> bool:
        """
        Checks the input for the temperature limit.

        Parameters
        ----------
        temperature_limit
            Temperature limit to be checked

        Returns
        -------
        bool
            True if the input is correct, False otherwise
        """

    @abc.abstractmethod
    def set_max_temperature(self, max_temperature: int | list | np.ndarray) -> None:
        """
        Sets the maximum temperature limit of the borefield.

        Parameters
        ----------
        max_temperature : int, list or np.ndarray
            Maximum temperature limit of the borefield

        Returns
        -------
        None
        """

    @abc.abstractmethod
    def set_min_temperature(self, min_temperature: int | list | np.ndarray) -> None:
        """
        Sets the minimum temperature limit of the borefield.

        Parameters
        ----------
        min_temperature : int, list or np.ndarray
            Minimum temperature limit of the borefield

        Returns
        -------
        None
        """

    @abc.abstractmethod
    def get_min_temperature_monthly(self, simulation_period: int) -> np.ndarray:
        """
        Get the monthly minimum temperature limit for the whole simulation period.

        Parameters
        ----------
        simulation_period : int
            Simulation period in years

        Returns
        -------
        Monthly minimum temperature limit : np.ndarray
        """

    @abc.abstractmethod
    def get_min_temperature_hourly(self, simulation_period: int, UPM: np.ndarray) -> np.ndarray:
        """
        Get the hourly minimum temperature limit for the whole simulation period.

        Parameters
        ----------
        simulation_period : int
            Simulation period in years
        UPM : np.ndarray
            Hours per month

        Returns
        -------
        Hourly minimum temperature limit : np.ndarray
        """

    @abc.abstractmethod
    def get_max_temperature_monthly(self, simulation_period: int) -> np.ndarray:
        """
        Get the monthly maximum temperature limit for the whole simulation period.

        Parameters
        ----------
        simulation_period : int
            Simulation period in years

        Returns
        -------
        Monthly maximum temperature limit : np.ndarray
        """

    @abc.abstractmethod
    def get_max_temperature_hourly(self, simulation_period: int, UPM: np.ndarray) -> np.ndarray:
        """
        Get the hourly maximum temperature limit for the whole simulation period.

        Parameters
        ----------
        simulation_period : int
            Simulation period in years
        UPM : np.ndarray
            Hours per month

        Returns
        -------
        Hourly maximum temperature limit : np.ndarray
        """

# TODO monthly can go to hourly, not vice versa!