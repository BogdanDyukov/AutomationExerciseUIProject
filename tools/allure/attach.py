from pathlib import Path

import allure
from allure_commons.types import AttachmentType


def attach_file(file_path: str | Path, name: str, attachment_type: AttachmentType = None, extension: str = None):
    allure.attach.file(file_path, name=name, attachment_type=attachment_type, extension=extension)


def attach_content(content: str, name: str, attachment_type: AttachmentType):
    allure.attach(body=content, name=name, attachment_type=attachment_type)
