from dataclasses import dataclass


@dataclass
class Notification:
    title: str
    main_text: str
    additional_text: str | None
