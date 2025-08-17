from . import utils
from . import props
from . import icons
from . import ops
from . import ui
from . import events

# modules are in subfolders containing __init__.py files
modules = (
    events,
    icons,
    ops,
    props,
    ui,
    utils,
)

def register():
    for mod in modules:
        mod.register()
    
def unregister():
    for mod in reversed(modules):
        mod.unregister()
