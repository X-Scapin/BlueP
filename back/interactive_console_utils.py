import gc
import inspect

def compute_instance_list():
    instances = [[]]
    gc.collect()
    oo = gc.get_objects()
    count = 0
    for o in oo:
        if getattr(o, "__class__", None):
            className = o.__class__.__name__
            count = count + 1
            if instances.__len__() < count:
                instances.append([])
            instances[instances.__len__() - 1].append(className)
            if hasattr(o, 'name') and o.name is not None:
                instances[instances.__len__() - 1].append(o.name)
            else:
                instances[instances.__len__() - 1].append(str(hex(id(o))))
    for i in range(instances.__len__()):
        for j in range(2):
            print(instances[i][j])
