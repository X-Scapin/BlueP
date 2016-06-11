import gc


def compute_instance_list():
    gc.collect()
    oo = gc.get_objects()
    for o in oo:
        if getattr(o, "__class__", None):
            name = o.__class__.__name__
            #name in class_names
            if name == "Voiture":
                print("one instance of Voiture founded")
