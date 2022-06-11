import os
import weakref


class TempFile:

    def __init__(self, path) -> None:
        super().__init__()
        self._f = open(path, 'wb')
        self._finalizer = weakref.finalize(self, self.on_delete, self._f, path)

    @staticmethod
    def on_delete(file, path):
        file.close()
        os.remove(path)
