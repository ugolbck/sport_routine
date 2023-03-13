"""Enums to standardize var names"""

from enum import Enum


class SportTypeEnum(str, Enum):
    RUNNING = "RUNNING"
    CYCLING = "CYCLING"
    SWIMMING = "SWIMMING"
    WORKOUT = "WORKOUT"


class WeatherEnum(str, Enum):
    SUNNY = "SUNNY"
    CLOUDY = "CLOUDY"
    RAINY = "RAINY"
    WINDY = "WINDY"
    STORMY = "STORMY"
    STILL = "STILL"
    HAZY = "HAZY"
