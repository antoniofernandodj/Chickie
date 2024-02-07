from __feature__ import snake_case, true_property  # type: ignore  # noqa
import base64
import json


class FileService:

    @classmethod
    def get_text(cls, filepath: str) -> str:
        with open(filepath) as f:
            text = f.read()

        return text

    @classmethod
    def get_json(cls, filepath: str) -> dict[str, str]:
        text = cls.get_text(filepath=filepath)
        return json.loads(text)

    @classmethod
    def set_json(cls, filepath: str, data: dict) -> None:
        with open(filepath, 'w') as f:
            json.dump(data, f)

    @classmethod
    def get_bytes(cls, filepath: str) -> bytes:
        with open(filepath, 'rb') as f:
            file_bytes = f.read()

        return file_bytes

    @classmethod
    def get_base64_string(cls, filepath: str) -> str:
        file_bytes = cls.get_bytes(filepath=filepath)
        return base64.b64encode(file_bytes).decode('utf-8')
