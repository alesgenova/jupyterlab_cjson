from IPython.display import display, JSON, DisplayObject

# Running `npm run build` will create static resources in the static
# directory of this Python package (and create that directory if necessary).

def _jupyter_labextension_paths():
    return [{
        'name': 'jupyterlab_cjson',
        'src': 'static',
    }]

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyterlab_cjson',
        'require': 'jupyterlab_cjson/extension'
    }]

# A display class that can be used within a notebook.
#   from jupyterlab_cjson import CJSON
#   CJSON(data)

DEFAULT_ISO = 43 / 2000.0;
DEFAULT_ISO_SURFACES = [{
    'value': DEFAULT_ISO,
    'color': 'blue',
    'opacity': 0.9,
  }, {
    'value': -DEFAULT_ISO,
    'color': 'red',
    'opacity': 0.9
  }]

class CJSON(JSON):
    """A display class for displaying CJSON visualizations in the Jupyter Notebook and IPython kernel.

    CJSON expects a JSON-able dict, not serialized JSON strings.

    Scalar types (None, number, string) are not allowed, only dict containers.
    """



    def __init__(self, data=None, url=None, filename=None, vibrational=True, structure=True,
                 iso_surfaces=DEFAULT_ISO_SURFACES, animate_mode=None, calculation_id=None,
                 mo=None):
        super(CJSON, self).__init__(data, url, filename)
        self.metadata['vibrational'] = vibrational
        self.metadata['structure'] = structure
        self.metadata['isoSurfaces'] = iso_surfaces
        self.metadata['animateMode'] = animate_mode
        self.metadata['mo'] = mo
        self.metadata['calculationId'] = calculation_id

    def _ipython_display_(self):
        bundle = {
            'application/cjson+json': self.data,
            'text/plain': '<jupyterlab_cjson.CJSON object>'
        }
        metadata = {
            'application/cjson+json': self.metadata
        }
        display(bundle, metadata=metadata, raw=True)

class FreeEnergy(JSON):
    """A display class for displaying free energy visualizations in the Jupyter Notebook and IPython kernel.

    FreeEnergy expects a JSON-able dict.

    """

    def __init__(self, data=None, url=None, filename=None):
        super(FreeEnergy, self).__init__(data, url, filename)

    def _ipython_display_(self):
        bundle = {
            'application/cjson-free_energy+json': self.data,
            'text/plain': '<jupyterlab_cjson.FreeEnergy object>'
        }
        metadata = {
            'application/cjson-free_energy+json': self.metadata
        }
        display(bundle, metadata=metadata, raw=True)

class CalculationMonitor(DisplayObject):
    """
    A display class for monitoring calculations Jupyter Notebook and IPython kernel.
    """

    def __init__(self, data=None, url=None, filename=None):
        super(CalculationMonitor, self).__init__(data, url, filename)

    def _ipython_display_(self):
        bundle = {
            'application/calculation+json': self.data,
            'text/plain': '<jupyterlab_cjson.CalculationMonitor object>'
        }
        metadata = {
            'application/calculation+json': {}
        }
        display(bundle, metadata=metadata, raw=True)

    def __getattr__(self, name):
        # This is a little fragile, it seem that ipython is looking for the
        # absence of _ipython_canary_method_should_not_exist_, so only return
        # self for 'public' methods.
        if name[0] != '_':
            return self
        else:
            return DisplayObject.__getattr__(self, name)

    def __call__(self):
        return self
