LABELS = (
    ('Rect',  {'type': 'rect'}),
    ('Point', {'type': 'point'}),
)

HOTKEYS = (
)

# Defines the mapping from the annotation type to the visualization item. The
# values need to be either python callables, or a module path string that
# points to a python callable. The callable is responsible for creating and
# returning the corresponding visualization item.
ITEMS = {
    'rect':  'sloth.items.RectItem',
    'point': 'sloth.items.PointItem',
}

INSERTERS = {
    'rect':  'sloth.items.RectItemInserter',
    'point': 'sloth.items.PointItemInserter',
}

CONTAINERS = (
    ('*.json',   'sloth.annotations.container.JSONContainer'),
    ('*.yaml',   'sloth.annotations.container.YAMLContainer'),
    ('*.pickle', 'sloth.annotations.container.PickleContainer'),
)

PLUGINS = (
)

