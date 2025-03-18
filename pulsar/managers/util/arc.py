try:
    import pyarcrest
    import pyarcrest.arc
except ImportError:
    pyarcrest = None

__all__ = ("ensure_pyarc", "pyarcrest")


PYARCREST_UNAVAILABLE_MESSAGE = (
    "Pulsar ARC client requires the Python package `pyarcrest` - but it is unavailable. Please install `pyarcrest`."
)

def ensure_pyarc():
    if pyarcrest is None:
        raise ImportError(PYARCREST_UNAVAILABLE_MESSAGE)
