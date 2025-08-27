from dataclasses import dataclass


@dataclass
class Notification:
    title: str
    main: str
    additional: str
