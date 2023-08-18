from dataclasses import dataclass


@dataclass
class Point:
    id: int
    lon: float
    lat: float


@dataclass
class DistanceCalculation:
    p1: Point
    p2: Point
    distance: float
