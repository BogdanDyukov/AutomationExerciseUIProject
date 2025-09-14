import json

from filelock import FileLock

from config.settings import settings

COUNTER_FILE = settings.counter_file


def get_unique_id():
    with FileLock(str(COUNTER_FILE) + ".lock"):
        data = json.loads(COUNTER_FILE.read_text())
        data['unique_value'] += 1
        COUNTER_FILE.write_text(json.dumps(data))

    return data['unique_value']
