from operator import le
from re import L

class figures:
   def __init__(self, length : int, width :  int , height: int ):
      self.length = length
      self.width = width
      self.height = height

class circle(figures):
   def __init__(self,length : int, width :  int ,  height: int , radius : int):
      super().init(length, width, height )
      self.radius = radius


class triangle(figures):
   def __init__(self,length : int, width :  int ,  height: int , square: int):
      super().init(length, width, height)
      self.square = square


class cylinder(figures):
   def __init__(self,length : int, width :  int ,  height: int , volume: int):
      super().init(length, width, height)
      self.volume = volume


class cone(figures):
   def __init__(self,length : int, width :  int ,  height: int , creating : int ):
      super().init(length, width, height)
      self.creating = creating


class sphere(figures):
   def __init__(self,length : int, width :  int ,  height: int , diameter: int):
      super().init(length, width, height)
      self.diameter = diameter
