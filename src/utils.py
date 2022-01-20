import csv
from dataclasses import asdict


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def csv_iterator(rows, columns):
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    yield writer.writerow(columns)
    for row in rows:
        yield writer.writerow(list(asdict(row).values()))
