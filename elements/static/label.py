from elements.base_element import BaseElement


# <label>, а также иногда <span> или <div>
# Когда текст визуально играет роль «подписи» или «объяснения» к какому-то элементу интерфейса
# Подсказка к полю ввода, чекбоксу/радиокнопке или просто краткая характеристика рядом с элементом
class Label(BaseElement):
    @property
    def _type_of(self) -> str:
        return "text"
