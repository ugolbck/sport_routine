"""Enums to standardize var names"""

from enum import Enum


class SportTypeEnum(str, Enum):
    RUNNING = "RUNNING"
    CYCLING = "CYCLING"
    SWIMMING = "SWIMMING"
    WORKOUT = "WORKOUT"
