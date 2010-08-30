
def content_types(app):
    def gen():
        for mod in app.modules.values():
            if hasattr(mod, "flaskcma") and "content_list" in mod.flaskcma:
                for doc in mod.flaskcma['content_list']:
                    yield (doc._class_name, doc)

    return dict(gen())

def content_type(app, content_type_name):
    return content_types(app)[content_type_name]
