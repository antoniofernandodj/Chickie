import pickle
from src.tasks.command_handler import handler
from aioamqp.properties import Properties
from aioamqp.envelope import Envelope
from aioamqp.channel import Channel


async def callback(
    channel: Channel,
    body_bytes: bytes,
    envelope: Envelope,
    properties: Properties
):
    headers = properties.headers
    method = headers.get('method')

    if method is None or not isinstance(method, str):
        raise ValueError('No method found')

    decoded_body = pickle.loads(body_bytes)
    command = handler[method]
    await command(decoded_body)
