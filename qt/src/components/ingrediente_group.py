from src.views.ingrediente_group_ui import Ui_Form
from PySide6.QtWidgets import QRadioButton
from PySide6.QtCore import QSize
from src.domain.data_models import Ingrediente
from typing import List, Optional

import uuid


class CustomRadioButton(QRadioButton):
    def __init__(self, text, value: bool, parent=None) -> None:
        super().__init__(text, parent)
        self.value: bool = value
        self.ingrediente: Optional[Ingrediente] = None

    def set_ingrediente(self, ingrediente: Ingrediente) -> None:
        self.ingrediente = ingrediente

    def get_ingrediente(self) -> Ingrediente:
        if self.ingrediente:
            return self.ingrediente

        raise ValueError('Sem ingrediente armazenado!')

    def get_value(self) -> bool:
        return self.value


class IngredienteGroup(Ui_Form):

    _data: List[Ingrediente]
    select: dict[str, bool]

    def setup_ui(self, label_text, Form):
        super().setupUi(Form)

        self.horizontalLayout.removeWidget(self.radio_sim)
        self.horizontalLayout.removeWidget(self.radio_nao)

        self.horizontalLayout_2.removeWidget(self.radio_sim)
        self.horizontalLayout_2.removeWidget(self.radio_nao)

        self.radio_sim.deleteLater()
        self.radio_nao.deleteLater()

        del self.radio_nao
        del self.radio_sim

        self.radio_sim = CustomRadioButton(self.frame_3, value=True)
        self.radio_sim.setObjectName(f"radio_sim_{uuid.uuid1()}")
        self.radio_sim.setMaximumSize(QSize(60, 20))

        self.radio_nao = CustomRadioButton(self.frame_3, value=False)
        self.radio_nao.setObjectName(f"radio_nao_{uuid.uuid1()}")
        self.radio_nao.setMaximumSize(QSize(60, 20))

        self.radio_sim.setText('SIM')
        self.radio_nao.setText('NÃO')

        self.horizontalLayout_2.addWidget(self.radio_sim)
        self.horizontalLayout_2.addWidget(self.radio_nao)

        self.label.setText(label_text)

    def setup(self) -> None:
        self._data = []
        self.select = {}

    def add_data(self, ingrediente: Ingrediente):
        self._data.append(ingrediente)

    def get_data(self):
        return self._data
