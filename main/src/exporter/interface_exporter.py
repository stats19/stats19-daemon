from typing import Any


class ExporterInterface(object):
    def export_data(self, *args) -> Any:
        pass
