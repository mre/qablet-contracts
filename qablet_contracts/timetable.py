# Define the timetable struct

import pyarrow as pa

DICT_TYPE = pa.dictionary(pa.int64(), pa.string())
EVENT_SCHEMA = pa.schema(
    [
        pa.field("track", DICT_TYPE),
        pa.field("time", pa.float64()),  # TODO: use pa.timestamp() instead?
        pa.field("op", pa.string()),  # TODO: use pa.dictionary() instead?
        pa.field("quantity", pa.float64()),
        pa.field("unit", DICT_TYPE),
    ]
)


def timetable_from_dicts(events: list[dict]) -> dict:
    """Create timetable from a list of dicts.

    Args:
        events: a list of dicts with the following fields:

            - track: string
            - time: float
            - op: string
            - quantity: float
            - unit: string

    Returns:
        a timetable dictionary with the following fields:

            - events: a pyarrow record batch
            - expressions: a dict for expressions, batches, and snappers

    """
    return {
        "events": pa.RecordBatch.from_pylist(events, schema=EVENT_SCHEMA),
        "expressions": {},
    }
