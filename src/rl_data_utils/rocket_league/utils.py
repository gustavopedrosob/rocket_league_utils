def initialize(cls, primitives, value):
    if isinstance(value, cls):
        return value
    elif isinstance(value, primitives):
        return cls(value)
    elif value is None:
        return cls()


def initialize_iterable(cls, members_cls, primitives, value):
    if all(isinstance(each, members_cls) for each in value):
        return value
    elif any(all(isinstance(each, primitive) for each in value) for primitive in primitives):
        return cls(members_cls(each) for each in value)
