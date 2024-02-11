from src.views.ingrediente_group_ui import Ui_Form
from src.domain.data_models import Ingrediente
from typing import List


class IngredienteGroup(Ui_Form):

    _data: List[Ingrediente]
    select: dict[str, bool]

    def setup_ui(self, label_text, Form):
        super().setupUi(Form)
        self.label.setText(label_text)

    def setup(self) -> None:
        self._data = []
        self.select = {}

    def add_data(self, ingrediente: Ingrediente):
        self._data.append(ingrediente)

    def get_data(self):
        return self._data
