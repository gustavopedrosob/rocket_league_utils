from typing import Callable, TypeVar, List, Any, Dict

ST = TypeVar('ST')
AR = TypeVar('AR')

def respective_attributes(function: Callable[..., ST]) -> Callable[..., ST]:
    def new_func(*args: List[Any], **kwargs: Dict[str, Any]) -> ST:
        return function(*args, **kwargs)
    return new_func