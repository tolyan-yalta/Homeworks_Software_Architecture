
from typing import List


class Texture:
    pass


class Point3D:
    pass


class Poligon:
    
    def __init__(self, points: Point3D):
        self.points = [points]


class PoligonalModel:
    
    def __init__(self, textures):
        self.poligons = []
        self.poligons.append(Poligon(Point3D()))
        self.textures = textures
        # не совсем понял, у нас же кратнось 0..*
        # то есть список может быть пустым ?
        # self.textures = []


class Angle3D:
    pass


class Color:
    pass


class Flash:
    
    def __init__(self):
        self.location = None
        self.angle = None
        self.color = None
        self.power = None


    def rotate(self, var_angle: Angle3D):
        pass

    def move(self, var_point: Point3D):
        pass


class Camera:

    def __init__(self):
        self.location = None
        self.angle = None

    def rotate(self, var_angle: Angle3D):
        pass

    def move(self, var_point: Point3D):
        pass


class Scene:

    def __init__(self, id_: int, models: PoligonalModel, flashes: Flash, cameras: Camera):
        self.id_ = id_

        if len(models) > 0:
            self.models = models
        else:
            raise Exception("Должна быть одна модель!")

        self.flashes = []

        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise Exception("Должна быть одна камера!")


    def method1(self, type):
        return None

    def method2(self, type1, type2):
        return None
