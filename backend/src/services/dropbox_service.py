import logging
from typing import Any
from config import settings as s
from dropbox import Dropbox
from dropbox.files import WriteMode
from dropbox.files import CommitInfo, UploadSessionCursor
from typing import Union

from fastapi import UploadFile
from io import BytesIO

Buffer = Union[UploadFile, BytesIO]


class DropboxService:
    def __init__(self):
        self.CHUNK_SIZE = 4 * 1024 * 1024  # 4MB
        self.dbx = Dropbox(
            app_key=s.DROPBOX_APP_KEY,
            app_secret=s.DROPBOX_APP_SECRET,
            oauth2_refresh_token=s.DROPBOX_OUTH2_REFRESH_TOKEN,
        )

    def download(self, item: Any) -> bytes:
        _, response = self.dbx.files_download(path=item.path)
        logging.info("Download de item realizado com sucesso")
        return response.content

    def upload(self, item: Any, file_bytes: bytes):
        response = self.dbx.files_upload(
            f=file_bytes, path=item.path, mode=WriteMode("overwrite")
        )
        logging.info("Item upload realizado com sucesso")
        return response

    def delete(self, item: Any):
        response = self.dbx.files_delete_v2(path=item.path)
        logging.debug("Item removido com sucesso do Dropbox")
        return response

    def buffer_upload(self, database_item: Any, f: Buffer, file_size: int):
        if isinstance(f, UploadFile):
            self.buffer_upload_fastapi(database_item, f, file_size)
        elif isinstance(f, BytesIO):
            self.buffer_upload_fastapi(database_item, f, file_size)
        else:
            raise Exception("Type unsupported.")

    def buffer_upload_file_io(
        self, database_item: Any, f: BytesIO, file_size: int
    ):
        uploaded_size = 0
        dest_path = database_item.path
        if file_size <= self.CHUNK_SIZE:
            self.dbx.files_upload(
                f=f.read(), path=dest_path, mode=WriteMode("overwrite")
            )

        else:
            upload_session_start_result = self.dbx.files_upload_session_start(
                f.read(self.CHUNK_SIZE)
            )
            cursor = UploadSessionCursor(
                session_id=upload_session_start_result.session_id,
                offset=f.tell(),
            )
            commit = CommitInfo(path=dest_path)
            while f.tell() <= file_size:
                if (file_size - f.tell()) <= self.CHUNK_SIZE:
                    # last chunk
                    self.dbx.files_upload_session_finish(
                        f.read(self.CHUNK_SIZE), cursor, commit
                    )

                    break
                else:
                    self.dbx.files_upload_session_append_v2(
                        f.read(self.CHUNK_SIZE), cursor
                    )
                    cursor.offset = f.tell()
                    uploaded_size += self.CHUNK_SIZE

    def buffer_upload_fastapi(
        self, database_item: Any, f: UploadFile, file_size: int
    ):
        uploaded_size = 0
        dest_path = database_item.path

        if file_size <= self.CHUNK_SIZE:
            self.dbx.files_upload(
                f.file.read(), path=dest_path, mode=WriteMode("overwrite")
            )
        else:
            upload_session_start_result = self.dbx.files_upload_session_start(
                f.read(self.CHUNK_SIZE)
            )
            cursor = UploadSessionCursor(
                session_id=upload_session_start_result.session_id,
                offset=f.tell(),
            )
            commit = CommitInfo(path=dest_path)
            with f.file as file_stream:
                chunk = file_stream.read(self.CHUNK_SIZE)
                while chunk:
                    if len(chunk) < self.CHUNK_SIZE:
                        # last chunk
                        self.dbx.files_upload_session_finish(
                            chunk, cursor=cursor, commit=commit
                        )
                        break
                    else:
                        self.dbx.files_upload_session_append_v2(
                            chunk, cursor=cursor
                        )
                        chunk = file_stream.read(self.CHUNK_SIZE)
                        cursor.offset = file_stream.tell()
                        uploaded_size += self.CHUNK_SIZE
