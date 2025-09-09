from pathlib import Path

from filelock import FileLock

from config.settings import settings

COUNTER_FILE = Path(settings.test_data.counter_file)
LOCK_FILE = COUNTER_FILE.with_suffix(".lock")


def get_unique_id():
    with FileLock(str(LOCK_FILE)):
        value = int(COUNTER_FILE.read_text().strip() or 0)
        value += 1
        COUNTER_FILE.write_text(str(value))

    return value
