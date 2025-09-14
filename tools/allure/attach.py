import allure


def attach_data(data, name: str, attachment_type=None, extension=None):
    allure.attach.file(data, name, attachment_type, extension)
