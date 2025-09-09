from dataclasses import dataclass


@dataclass
class ModalDialog:
    title: str
    note_text: str
    navigation_link_text: str
    continue_button_text: str
