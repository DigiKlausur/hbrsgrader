from notebook.utils import url_path_join as ujoin
from . import api_handlers

def _jupyter_server_extension_paths():
    return [{
        'module': 'customgrader'
    }]

def init_handlers(webapp):
    h = []
    h.extend(api_handlers.default_handlers)

    def rewrite(x):
        pat = ujoin(webapp.settings['base_url'], x[0].lstrip('/'))
        return (pat,) + x[1:]

    webapp.add_handlers(".*$", [rewrite(x) for x in h])

def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    init_handlers(web_app)
