
import re
from config import settings
import base64
from typing import Any, Optional, Dict
from pydantic import BaseModel
from src.schemas import Loja, Produto

import cloudinary.uploader  # type: ignore
import cloudinary.api  # type: ignore
import enum


class ImageType(enum.Enum):
    Produto = 'Produto'
    Cadastro = 'Cadastro'


class ImageUploadServiceResponse(BaseModel):
    """Response structure for image upload service."""
    data: dict
    loja_uuid: str | None = None

    __tablename__ = 'ImagemCadastroCollection'


class ImageUploadServiceBase:
    """Service for uploading, deleting, and retrieving images."""

    def __init__(self, loja: Loja):
        """Initialize Cloudinary configuration."""

        self.loja = loja

        cloudinary.config(
            cloud_name=settings.CLOUDINARY_CLOUD_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET
        )

    def get_image_url_by_asset_id(self, asset_id):
        query = f"resource_type:image AND asset_id={asset_id}"
        search = cloudinary.Search()
        result = search.expression(query) \
            .sort_by("public_id", "desc")\
            .max_results("1")\
            .execute()

        return result

    def delete_image_by_public_id(self, public_id: str):
        public_ids = [public_id]
        image_delete_result = cloudinary.api.delete_resources(
            public_ids, resource_type="image",
            type="upload"
        )
        print(image_delete_result)
        return image_delete_result  # type: ignore

    def safe_name(self, name: str) -> str:
        """Sanitize name to remove special characters."""

        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', name)  # type: ignore
        safe_name = re.sub(r'\s+', '_', safe_name).strip('_')
        return safe_name


class ImageUploadProdutoService(ImageUploadServiceBase):

    def upload_image_produto(
        self,
        produto: Produto,
        base64_string: str
    ) -> ImageUploadServiceResponse:
        """Upload an image to Cloudinary."""

        public_id = self.__get_public_id_image_produto(produto)
        if public_id:
            self.delete_image_by_public_id(public_id)

        bytes_data: bytes = base64.b64decode(base64_string)
        metadata_dict = cloudinary.uploader.upload(
            file=bytes_data,
            folder=self.image_produto_folder_path(produto)
        )

        return ImageUploadServiceResponse(data=metadata_dict)

    def get_public_url_image_produto(self, produto) -> Optional[str]:
        file_metadata = self.image_produto_metadata(produto)
        if file_metadata:
            asset_id = file_metadata['secure_url']
            if isinstance(asset_id, str):
                return asset_id
        return None

    def __get_public_id_image_produto(self, produto) -> Optional[str]:
        file_metadata = self.image_produto_metadata(produto)
        if file_metadata:
            asset_id = file_metadata['public_id']
            if isinstance(asset_id, str):
                return asset_id
        return None

    def image_produto_folder_path(self, produto: Produto):
        dirname = self.safe_name(f'{self.loja.uuid}_{self.loja.username}')
        return (f'lojas/{dirname}/imagem_produto/{produto.uuid}/')

    def image_produto_metadata(
        self, produto: Produto
    ) -> Optional[Dict[str, Any]]:

        """
        {
            'asset_id': 'f3785f1bf01146afcf32e8796f4d21a8',
            'public_id': 'folder_teste/empresa/fmla9sjviktuomuopdva',
            'format': 'jpg',
            'version': 1704084448,
            'resource_type': 'image',
            'type': 'upload',
            'created_at': '2024-01-01T04:47:28Z',
            'bytes': 55801,
            'width': 1500,
            'height': 870,
            'folder': 'folder_teste/empresa',
            'url': 'http://res.cloudinary.com/
                    ddus7rrgr/image/upload/v1704084448/folder_teste/
                    empresa/fmla9sjviktuomuopdva.jpg',
            'secure_url': 'https://res.cloudinary.com/
                    ddus7rrgr/image/upload/v1704084448/folder_teste/
                    empresa/fmla9sjviktuomuopdva.jpg'
        }
        """
        try:
            results = cloudinary.api.resources(
                type='upload',
                prefix=f'{self.image_produto_folder_path(produto)}'
            )
            resources: list[dict[str, str | int]]
            resources = results['resources']
            if isinstance(resources, list) and len(resources) > 0:
                file_metadata = resources[0]
                return file_metadata
        except Exception:
            return None
        return None


class ImageUploadCadastroService(ImageUploadServiceBase):

    def upload_image_cadastro(
        self,
        base64_string: str
    ) -> ImageUploadServiceResponse:
        """Upload an image to Cloudinary."""
        public_id = self.__get_public_id_image_cadastro()
        if public_id:
            self.delete_image_by_public_id(public_id)

        bytes_data: bytes = base64.b64decode(base64_string)
        metadata_dict = cloudinary.uploader.upload(
            file=bytes_data,
            folder=self.image_cadastro_folder_path
        )

        return ImageUploadServiceResponse(data=metadata_dict)

    def get_public_url_image_cadastro(self) -> Optional[str]:
        file_metadata = self.image_cadastro_metadata
        if file_metadata:
            public_url = file_metadata['secure_url']
            if isinstance(public_url, str):
                return public_url
        return None

    def __get_public_id_image_cadastro(self) -> Optional[str]:
        file_metadata = self.image_cadastro_metadata
        if file_metadata:
            asset_id = file_metadata['public_id']
            if isinstance(asset_id, str):
                return asset_id

        return None

    @property
    def image_cadastro_folder_path(
        self
    ) -> str:
        dirname = self.safe_name(f'{self.loja.uuid}_{self.loja.username}')
        return (f'lojas/{dirname}/imagem_cadastro')

    @property
    def image_cadastro_metadata(
        self
    ) -> Optional[Dict[str, Any]]:
        """
        {
            'asset_id': 'f3785f1bf01146afcf32e8796f4d21a8',
            'public_id': 'folder_teste/empresa/fmla9sjviktuomuopdva',
            'format': 'jpg',
            'version': 1704084448,
            'resource_type': 'image',
            'type': 'upload',
            'created_at': '2024-01-01T04:47:28Z',
            'bytes': 55801,
            'width': 1500,
            'height': 870,
            'folder': 'folder_teste/empresa',
            'url': 'http://res.cloudinary.com/
                    ddus7rrgr/image/upload/v1704084448/folder_teste/
                    empresa/fmla9sjviktuomuopdva.jpg',
            'secure_url': 'https://res.cloudinary.com/
                    ddus7rrgr/image/upload/v1704084448/folder_teste/
                    empresa/fmla9sjviktuomuopdva.jpg'
        }
        """
        try:
            results = cloudinary.api.resources(
                type='upload',
                prefix=f'{self.image_cadastro_folder_path}'
            )
            resources: list[dict[str, str | int]]
            resources = results['resources']
            if isinstance(resources, list) and len(resources) > 0:
                file_metadata = resources[0]
                return file_metadata
        except Exception:
            return None
        return None


class ImageUploadService(
    ImageUploadCadastroService,
    ImageUploadProdutoService
):
    ...
