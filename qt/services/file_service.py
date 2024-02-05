from PySide6.QtWidgets import QLabel
from typing import Optional
from __feature__ import snake_case, true_property  # type: ignore  # noqa
import base64
import json


class FileService:

    @classmethod
    def get_text(
        cls,
        filepath: Optional[str] = None,
        label: Optional[QLabel] = None
    ) -> str:

        if filepath:
            filepath = filepath
        elif label:
            filepath = label.text
        else:
            msg = 'Escolher filepath ou passar label de referência.'
            raise ValueError(msg)

        with open(filepath) as f:
            text = f.read()

        return text

    @classmethod
    def get_json(
        cls,
        filepath: Optional[str] = None,
        label: Optional[QLabel] = None
    ) -> dict[str, str]:

        text = cls.get_text(filepath=filepath, label=label)
        return json.loads(text)

    @classmethod
    def set_json(
        cls,
        filepath: str,
        data: dict
    ) -> None:

        with open(filepath, 'w') as f:
            json.dump(data, f)

    @classmethod
    def get_bytes(
        cls,
        filepath: Optional[str] = None,
        label: Optional[QLabel] = None
    ) -> bytes:

        if filepath:
            filepath = filepath
        elif label:
            filepath = label.text
        else:
            msg = 'Escolher filepath ou passar label de referência.'
            raise ValueError(msg)

        with open(filepath, 'rb') as f:
            file_bytes = f.read()

        return file_bytes

    @classmethod
    def get_base64_string(
        cls,
        filepath: Optional[str] = None,
        label: Optional[QLabel] = None
    ) -> str:

        file_bytes = cls.get_bytes(filepath=filepath, label=label)
        return base64.b64encode(file_bytes).decode('utf-8')
