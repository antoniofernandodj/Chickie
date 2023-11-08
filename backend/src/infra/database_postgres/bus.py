import typing as t
from src.infra.database_postgres.handlers import database_handler, event_handler
from typing import Any
from src.infra.database_postgres.commands import (
    CreateCommand, UpdateCommand, DeleteCommand
)

HandlersDict = t.Dict[Any, t.List[t.Callable]]


class MessageBus:
    def __init__(self) -> None:
        self.handlers: HandlersDict = {}

    def register_handler(self, command: Any, handler: t.Callable):
        if command not in self.handlers:
            self.handlers[command] = []
        if handler not in self.handlers[command]:
            self.handlers[command].append(handler)

    async def send_message(self, message):
        command = type(message)
        if command in self.handlers:
            handlers = self.handlers[command]
            for handler in handlers:
                await handler(message)


def get_message_bus():
    bus = MessageBus()

    bus.register_handler(CreateCommand, database_handler)
    bus.register_handler(CreateCommand, event_handler)

    bus.register_handler(UpdateCommand, database_handler)
    bus.register_handler(UpdateCommand, event_handler)

    bus.register_handler(DeleteCommand, database_handler)
    bus.register_handler(DeleteCommand, event_handler)
    return bus
