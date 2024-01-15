from typing import Annotated, Optional, List, Dict
from src.exceptions import NotFoundException
from fastapi import (  # noqa
    APIRouter,
    HTTPException,
    status,
    Path,
    Query,
    Response
)
from src.dependencies import (
    produto_service_dependency,
    current_company,
)
from src.services import (
    ImageUploadService,
    ImageUploadServiceResponse,
)
from src.domain.models import (
    ProdutoGET,
    ProdutoPOST,
    ProdutoPUT,
    LojaUpdateImageCadastro,
)


router = APIRouter(prefix="/produtos", tags=["Produto"])


@router.get("/")
async def requisitar_produtos(
    produto_service: produto_service_dependency,
    loja_uuid: Optional[str] = Query(None),
    categoria_uuid: Optional[str] = Query(None)
) -> List[ProdutoGET]:

    """
    Requisita os produtos cadastrados na plataforma.
    Aceita um uuid como query para buscar os
    produtos de uma empresa específica

    Args:
        loja_uuid (Optional[str]): O uuid da empresa,
        caso necessário

    Returns:
        list[Produto]
    """

    kwargs = {}
    if loja_uuid is not None:
        kwargs["loja_uuid"] = loja_uuid
    if categoria_uuid is not None:
        kwargs["categoria_uuid"] = categoria_uuid

    produtos = await produto_service.get_all_produtos(**kwargs)
    return produtos


@router.get("/{uuid}")
async def requisitar_produto(
    produto_service: produto_service_dependency,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer get")]
) -> ProdutoGET:

    produto = await produto_service.get_produto(uuid)
    if produto is None:
        raise NotFoundException("Produto não encontrado")

    return produto


@router.post("/", status_code=status.HTTP_201_CREATED)
async def cadastrar_produto(
    produto_data: ProdutoPOST,
    current_company: current_company,
    produto_service: produto_service_dependency
) -> Dict[str, str]:

    try:
        response = await produto_service.save_produto(produto_data)
        return response
    except Exception as error:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=("Erro no cadastro do produto ou"
                    f"upload da imagem! detail: {error}")
        )


@router.put(
    "/{uuid}",
    summary='Atualizar dados de cadastro de produto'
)
async def atualizar_produto_put(
    produto_data: ProdutoPUT,
    current_company: current_company,
    produto_service: produto_service_dependency,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer put")]
):

    try:
        await produto_service.atualizar_produto(
            uuid=uuid, produto_data=produto_data
        )
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=("Erro no cadastro do produto ou"
                    f"upload da imagem! detail: {error}")
        )


@router.post(
    '/{uuid}/imagem',
    summary="Atualizar imagem de produto da loja",
    responses={
        404: {"description": "Loja não encontrada"}
    }
)
async def atualizar_imagem_de_produto(
    uuid: str,
    loja: current_company,
    image: LojaUpdateImageCadastro,
    service: produto_service_dependency
) -> Dict[str, ImageUploadServiceResponse]:

    produto = await service.get(uuid)
    if produto is None:
        raise NotFoundException('O produto não foi encontrado!')

    try:
        image_service = ImageUploadService(loja=loja)
        try:
            image_bytes_base64 = image.bytes_base64.split(',')[1]
        except IndexError:
            image_bytes_base64 = image.bytes_base64

        result = image_service.upload_image_produto(
            base64_string=image_bytes_base64,
            filename=image.filename,
            produto=produto
        )
        return {'result': result}

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no upload da imagem! Detalhes: {error}"
        )


@router.delete(
    '/{uuid}/imagem',
    summary="Remover imagem de produto da loja",
    responses={
        404: {"description": "Loja não encontrada"}
    }
)
async def remover_imagem_de_produto(
    uuid: str,
    loja: current_company,
    service: produto_service_dependency
):

    produto = await service.get(uuid)
    if produto is None:
        raise NotFoundException('O produto não foi encontrado!')

    try:
        image_service = ImageUploadService(loja=loja)
        image_service.delete_image_produto(produto)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except Exception as error:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no upload da imagem! Detalhes: {error}"
        )


@router.delete("/{uuid}")
async def remover_produto(
    current_company: current_company,
    service: produto_service_dependency,
    uuid: Annotated[str, Path(title="O uuid do produto a fazer delete")]
):

    try:
        await service.remove_produto(uuid=uuid)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
