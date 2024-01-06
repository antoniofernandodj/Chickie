# from src.presenters import controllers
from src.infra.database_postgres.repository import Repository
from src.exceptions import (
    UnauthorizedException,
    NotFoundException,
    ConflictException
)

from fastapi.routing import APIRouter
from src.api import security
from src.dependencies import (
    current_company,
    oauth2_password_request_form_dependency
)
from src.dependencies import (  # noqa
    loja_repository_dependency,
    connection_dependency
)
from fastapi import HTTPException, status, Path, Response
from typing import Any, Optional, List
from src.schemas import (
    Cliente,
    UsuarioSignUp,
    LojaSignUp,
    # Endereco,
    EnderecoLoja as Endereco,  # noqa
    LojaToken,
    Loja,
    Produto,
    LojaGETResponse,
    ProdutoGET,
    LojaUpdateImageCadastro,
    UsuarioFollowEmpresaRequest
)
from src.services import (
    ImageUploadService,
    ProdutoService
)


from typing import Annotated
from src import use_cases  # noqa


router = APIRouter(prefix="/loja", tags=["Loja", "Auth"])


@router.get(
    "/{uuid}"
)
async def requisitar_loja(
    repository: loja_repository_dependency,
    connection: connection_dependency,
    # endereco_repository: endereco_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid da loja a fazer get")]
) -> LojaGETResponse:
    """
    Busca uma loja pelo seu uuid.

    Args:
        uuid (str): O uuid da loja a ser buscada.

    Returns:
        Loja: A loja encontrada.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """
    loja: Optional[Loja] = await repository.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    endereco_repository = Repository(Endereco, connection=connection)
    print(endereco_repository)

    # endereco: Optional[Endereco] = await endereco_repository.find_one(
    #     uuid=loja.endereco_uuid
    # )

    # if endereco is None:
    #     raise NotFoundException('Endereco de loja não encontrado')

    if loja.uuid is None:
        raise NotFoundException('Loja com erros no cadastro')

    response = LojaGETResponse(
        nome=loja.nome,
        username=loja.username,
        email=loja.email,
        celular=loja.celular,
        uuid=loja.uuid,
        # endereco=endereco,
        telefone=loja.telefone
    )

    image_service = ImageUploadService(loja=loja)
    public_url = image_service.get_public_url_image_cadastro()
    response.imagem_cadastro = public_url

    return response


@router.get(
    "/"
)
async def requisitar_lojas(
    repository: loja_repository_dependency,
    # endereco_repository: endereco_repository_dependency,
    connection: connection_dependency,
) -> List[LojaGETResponse]:
    """
    Busca uma loja pelo seu uuid.

    Args:
        uuid (str): O uuid da loja a ser buscada.

    Returns:
        Loja: A loja encontrada.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """

    endereco_repository = Repository(Endereco, connection=connection)
    print(endereco_repository)

    response: List[LojaGETResponse] = []
    lojas: List[Loja] = await repository.find_all()
    for loja in lojas:

        # endereco: Optional[Endereco] = await endereco_repository.find_one(
        #     uuid=loja.endereco_uuid
        # )

        # if endereco is None:
        #     raise NotFoundException('Endereco de loja não encontrado')

        if loja.uuid is None:
            raise NotFoundException('Loja com erros no cadastro')

        response_item = LojaGETResponse(
            nome=loja.nome,
            username=loja.username,
            email=loja.email,
            celular=loja.celular,
            uuid=loja.uuid,
            # endereco=endereco,
            telefone=loja.telefone
        )

        image_service = ImageUploadService(loja=loja)
        public_url = image_service.get_public_url_image_cadastro()
        response_item.imagem_cadastro = public_url
        response.append(response_item)

    return response


@router.post(
    "/login",
    response_model=LojaToken
)
async def login_post(
    form_data: oauth2_password_request_form_dependency,
    # endereco_repository: endereco_repository_dependency,
    connection: connection_dependency
) -> Any:
    """
    Realiza o login de uma loja.

    Args:
        form_data (OAuth2PasswordRequestForm): Dados do formulário de login.

    Returns:
        dict: Um dicionário contendo o token de acesso e o uuid da loja.

    Raises:
        HTTPException: Se as credenciais forem inválidas.
    """

    endereco_repository = Repository(Endereco, connection=connection)
    print(endereco_repository)

    loja = await security.authenticate_company(
        form_data.username, form_data.password
    )
    if not loja:
        raise UnauthorizedException("Credenciais inválidas!")

    access_token = security.create_access_token(data={"sub": loja.username})

    # endereco: Optional[Endereco] = await endereco_repository.find_one(
    #     uuid=loja.endereco_uuid
    # )

    # if endereco is None:
    #     raise NotFoundException("Endereço da loja não encontrado")
    if loja.uuid is None:
        raise NotFoundException('Loja com erros no cadastro')

    loja_data = LojaGETResponse(
        nome=loja.nome,
        username=loja.username,
        email=loja.email,
        celular=loja.celular,
        uuid=loja.uuid,
        # endereco=endereco,
        telefone=loja.telefone
    )

    image_service = ImageUploadService(loja=loja)
    public_url = image_service.get_public_url_image_cadastro()
    loja_data.imagem_cadastro = public_url

    return LojaToken(
        access_token=access_token,
        token_type='bearer',
        loja=loja_data
    )


@router.put("/{uuid}", summary='Atualizar dados de cadastro da Loja')
async def update_loja(
    loja_repository: loja_repository_dependency,
    # endereco_loja_repository: endereco_loja_repository_dependency,
    connection: connection_dependency,
    updated_data: LojaSignUp,
    uuid: Annotated[str, Path(title="O uuid da loja a ser atualizada")],
):
    """
    Atualiza os detalhes de uma loja existente.

    Args:
        `uuid` (str): O uuid da loja a ser atualizada.
        `updated_data` (LojaSignUp): Os novos detalhes da loja.

    Returns:
        `dict`: Um dicionário confirmando a atualização.

    Raises:
        `HTTPException`: Se a loja não for encontrada ou ocorrer um erro na atualização.  # noqa
    """

    endereco_repository = Repository(Endereco, connection=connection)
    print(endereco_repository)

    loja: Optional[Loja] = await loja_repository.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    def only_numbers(string: str | None) -> str | None:
        if string is None:
            return None

        return ''.join([n for n in string if n.isdecimal()])

    try:
        loja_data_updated = dict(
            nome=updated_data.nome,
            username=updated_data.username,
            email=updated_data.email,
            celular=only_numbers(updated_data.celular),
            telefone=only_numbers(updated_data.telefone),
            horarios_de_funcionamento=updated_data.horarios_de_funcionamento
        )

        updated_loja = await loja_repository.update(
            loja,
            loja_data_updated
        )

        # endereco = await endereco_repository.find_one(
        #     loja_uuid=loja.uuid
        # )

        # await endereco_repository.update(
        #     endereco, {
        #         ...
        #     }
        # )

        return {
            "message": "Loja atualizada com sucesso!",
            "uuid": loja.uuid,
            "success": updated_loja
        }

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar a loja! Detalhes: {error}"
        )


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED
)
async def signup(
    loja: LojaSignUp,
    loja_repository: loja_repository_dependency
) -> Any:
    """
    Realiza o cadastro de uma nova loja.

    Args:
        loja (LojaSignUp): Os detalhes da loja a ser cadastrada.

    Returns:
        dict: Um dicionário contendo o uuid da loja cadastrada.
    """
    try:
        loja_cadastrada = await use_cases.lojas.registrar(loja_data=loja)

    except use_cases.lojas.InvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Senha inválida! A senha deve ser maior que 5"
        )

    except use_cases.lojas.LojaJaCadastradaException:
        raise ConflictException(detail="Credenciais inválidas!")

    if loja.image_bytes and loja.image_filename:
        try:
            image_service = ImageUploadService(loja=loja_cadastrada)
            image_bytes_base64 = loja.image_bytes.replace(
                'data:image/jpeg;base64,', ''
            )
            image_service.upload_image_cadastro(
                base64_string=image_bytes_base64
            )

        except Exception:
            del_result = await loja_repository.delete(loja_cadastrada)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro no upload da imagem! res: {del_result}"
            )

    return {"uuid": loja_cadastrada.uuid}


@router.get("/{loja_uuid}/produtos")
async def requisitar_produtos_de_loja(
    connection: connection_dependency,
    loja_uuid: str,
    categoria_uuid: str
) -> List[ProdutoGET]:

    """
    Requisita os produtos de uma loja específica
    cadastrados na plataforma.
    Aceita um uuid como query para buscar os
    produtos de uma empresa específica

    Args:
        loja_uuid (Optional[str]): O uuid da empresa,
        caso necessário

    Returns:
        list[Produto]
    """
    loja_repository = Repository(Loja, connection=connection)
    produto_repository = Repository(Produto, connection=connection)
    loja: Optional[Loja] = await loja_repository.find_one(
        uuid=loja_uuid
    )
    if loja is None:
        raise NotFoundException('Loja de produto não encontrada!')
    produto_service = ProdutoService(connection=connection, loja=loja)

    kwargs = {}
    if categoria_uuid is not None:
        kwargs["categoria_uuid"] = categoria_uuid

    response = []
    produtos: List[Produto] = await produto_repository.find_all(**kwargs)
    for produto in produtos:
        precos = await produto_service.get_precos(produto)
        image_url = await produto_service.get_public_url_image(produto)
        response_item = ProdutoGET(
            uuid=produto.uuid,
            nome=produto.nome,
            descricao=produto.nome,
            preco=produto.preco,
            categoria_uuid=produto.categoria_uuid,
            loja_uuid=produto.loja_uuid,
            precos=precos,
            image_url=image_url
        )
        response.append(response_item)
    return response


@router.patch(
    '/atualizar_img_cadastro',
    summary="Atualizar imagem de cadastro da loja",
    responses={
        404: {"description": "Loja não encontrada"}
    }
)
async def atualizar_img_cadastro(
    loja: current_company,
    image: LojaUpdateImageCadastro,
    response: Response
) -> Any:
    """
    Atualiza a imagem de cadastro de uma loja.

    Args:
    - `uuid` (str): O UUID da loja a ser atualizada na imagem de cadastro.
    - `image` (LojaUpdateImageCadastro): Detalhes da imagem a ser atualizada.

    Returns:
    - `JSONResponse`: Retorna um JSON vazio com um status code de 204 se a atualização for bem-sucedida.  # noqa

    Raises:
    - `HTTPException`: Se ocorrer um erro durante o upload da imagem.
    """

    try:
        image_service = ImageUploadService(loja=loja)
        image_bytes_base64 = image.bytes_base64.split(',')[1]
        result = image_service.upload_image_cadastro(
            base64_string=image_bytes_base64
        )
        return {'result': result}

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no upload da imagem! Detalhes: {error}"
        )


@router.get(
    "/protected"
)
async def home(current_company: current_company):
    """
    Rota de exemplo protegida por autenticação.

    Args:
        current_company (Loja): O objeto da loja autenticada.

    Returns:
        dict: Uma mensagem de resposta.
    """
    return {"msg": "ok"}


@router.patch(
    "/{uuid}/ativar_inativar"
)
async def ativar_inativar_loja(
    loja_repository: loja_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid da loja a ativar/inativar")],
    ativar: bool
) -> Any:
    """
    Ativa ou inativa uma loja baseada no UUID.

    Args:
        uuid (str): O UUID da loja a ativar/inativar.
        ativar (bool): Define se a loja será ativada (True) ou inativada (False).  # noqa

    Returns:
        dict: Uma mensagem de confirmação.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """
    loja: Optional[Loja] = await loja_repository.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    await loja_repository.update(loja, {'ativo': ativar})

    status_msg = "ativada" if ativar else "inativada"
    return {"message": f"Loja {status_msg} com sucesso!"}


@router.delete(
    "/{uuid}"
)
async def deletar_loja(
    loja_repository: loja_repository_dependency,
    uuid: Annotated[str, Path(title="O uuid da loja a ser deletada")]
) -> Any:
    """
    Deleta uma loja baseada no UUID.

    Args:
        uuid (str): O UUID da loja a ser deletada.

    Returns:
        dict: Uma mensagem de confirmação.

    Raises:
        HTTPException: Se a loja não for encontrada.
    """
    loja: Optional[Loja] = await loja_repository.find_one(uuid=uuid)
    if loja is None:
        raise NotFoundException('Loja não encontrada')

    await loja_repository.delete(loja)

    return {"message": "Loja deletada com sucesso!"}


@router.post("/cliente", status_code=status.HTTP_201_CREATED)
async def cadastrar_cliente(
    connection: connection_dependency,
    current_company: current_company,
    usuario: UsuarioFollowEmpresaRequest
) -> Any:
    """
    Cadastra um novo cliente associado à loja autenticada.

    Args:
        current_company (Loja): O objeto da loja autenticada.
        usuario (UsuarioFollowEmpresaRequest): Os detalhes do cliente a ser cadastrado.  # noqa

    Returns:
        dict: Um dicionário contendo o uuid do usuário (cliente) cadastrado.

    Raises:
        HTTPException: Se não for fornecido o uuid da loja.
    """
    if usuario.loja_uuid is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="uuid da loja em falta",
        )

    cliente = Cliente(
        usuario_uuid=usuario.usuario_uuid,
        loja_uuid=usuario.loja_uuid
    )

    cliente_repository = Repository(Cliente, connection=connection)
    cliente_uuid = await cliente_repository.save(cliente)

    return {"uuid": cliente_uuid}


@router.post("/cliente_v2/{loja_uuid}", status_code=status.HTTP_201_CREATED)
async def cadastrar_cliente_v2(
    connection: connection_dependency,
    current_company: current_company,
    usuario: UsuarioSignUp,
    loja_uuid: str
) -> Any:
    """
    Cadastra um novo cliente associado à loja autenticada.

    Args:
        current_company (Loja): O objeto da loja autenticada.
        usuario (UsuarioSignUp): Os detalhes do cliente a ser cadastrado.

    Returns:
        dict: Um dicionário contendo o uuid do usuário (cliente) cadastrado.

    Raises:
        HTTPException: Se não for fornecido o uuid da loja.
    """

    try:
        usuario_cadastrado = await use_cases.usuarios.registrar(
            user_data=usuario
        )
    except use_cases.usuarios.InvalidPasswordException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Senha inválida! A senha deve ser maior que 5"
        )

    if usuario_cadastrado.uuid is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro no cadastro de usuário: usuario_uuid nulo"
        )

    cliente = Cliente(
        usuario_uuid=usuario_cadastrado.uuid,
        loja_uuid=loja_uuid
    )

    cliente_repository = Repository(Cliente, connection=connection)
    cliente_uuid = await cliente_repository.save(cliente)

    return {
        "usuario_uuid": usuario_cadastrado.uuid,
        "cliente_uuid": cliente_uuid
    }
