from dataclasses import dataclass


@dataclass
class Breadcrumb:
    root_link_name_text: str
    current_page_item_text: str
