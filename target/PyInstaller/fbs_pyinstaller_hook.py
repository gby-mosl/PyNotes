import importlib
module = importlib.import_module('fbs_runtime._frozen')
module.PUBLIC_SETTINGS = {'app_name': 'PyNotes', 'author': 'Guillaume', 'version': '0.0.0', 'environment': 'local'}