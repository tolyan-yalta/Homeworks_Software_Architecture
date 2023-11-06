
from model_elements import PoligonalModel, Scene, Flash, Camera
from typing import List
from abc import ABC, abstractmethod


class IModelChangedObserver(ABC):
    """Реализация интерфейса через абстрактный метод"""

    @abstractmethod
    def apply_update_model(self):
        pass


class IModelChenger(ABC):
    """Реализация интерфейса через абстрактный метод"""

    @abstractmethod
    def notify_change(self, sender: IModelChenger):
        pass


class ModelStore(IModelChanger):

    def __init__(self, id_: int, textures,changeObservers: List[IModelChangedObserver]):
        # super().__init__()
        self.models = []
        self.models.append(PoligonalModel(textures))
        self.flashes = []
        self.flashes.append(Flash())
        self.cameras = []
        self.cameras.append(Camera())
        self.scenas = []
        self.scenas.append(Scene(id_, self.models, self.flashes, self.cameras))        
        self.changeObservers = changeObservers


    def get_scena(self, id_):
        for scene in self.scenas:
            if scene.id_ == id_:
                return scene
            
    def notify_change(self, sender: IModelChanger):
        pass