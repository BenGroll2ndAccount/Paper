from abc import ABC, abstractmethod
from paper.Drivers.drawcalls import *
    

class AutoFlushDisplayDriver(ABC): #DisplayDriver that draws each call seperately after another. Simpler Logic, but in most cases the slower variant
    @abstractmethod
    def __init__():
        pass

    @abstractmethod
    def _Circle(circle : udraw_Circle) -> None:
        raise NotImplementedError

    @abstractmethod
    def _Pixel(pixel : udraw_Pixel) -> None:
        raise NotImplementedError

    @abstractmethod
    def _Line(line : udraw_Line) -> None:
        raise NotImplementedError

    @abstractmethod
    def _Rectangle(rect : udraw_Rectangle) -> None:
        raise NotImplementedError

    @abstractmethod
    def _Text(text : udraw_Text) -> None:
        raise NotImplementedError

    def _draw(self, drawcalls : list) -> None:
        for call in drawcalls:
            if hasattr(self, "__" +  call.__class__.__name__.split("_")[1]):
                getattr(self, "__" + call.__class__.__name__.split("_")[1])(call)
            else:
                raise ValueError(self.__class__.__name__ + " has no function " + call.__class__.__name__.split("_")[1])

class QueueDisplayDriver(ABC): 
    #DisplayDriver that queues all calls and then draws them in a single instruction. In most cases this is more efficient
    #Requires Display to support this queue-system ( Example: graphics.py )
    @abstractmethod
    def __init__():
        raise NotImplementedError
        
    @abstractmethod
    def _Circle(circle : udraw_Circle):
        raise NotImplementedError
    
    @abstractmethod
    def _Pixel(pixel : udraw_Pixel):
        raise NotImplementedError
    
    @abstractmethod
    def _Line(line : udraw_Line):
        raise NotImplementedError
    
    @abstractmethod
    def _Rectangle(rect : udraw_Rectangle):
        raise NotImplementedError
    
    @abstractmethod
    def _Text(text : udraw_Text):
        raise NotImplementedError
    
    @abstractmethod
    def _Update():
        raise NotImplementedError

    def _draw(self, drawcalls : list) -> list:
        for call in drawcalls:
            if hasattr(self, "_" +  call.__class__.__name__.split("_")[1]):
                getattr(self, "_" + call.__class__.__name__.split("_")[1])(call)
            else:
                raise ValueError(self.__class__.__name__ + " has no function " + call.__class__.__name__.split("_")[1])
        self._Update()
            

            
            
            