from typing import Any, List, Union

from fake_dragonflydb import _msgs as msgs
from fake_dragonflydb._commands import command, DbIndex
from fake_dragonflydb._helpers import SimpleError, OK, SimpleString, Database

PONG = SimpleString(b"PONG")


class ConnectionCommandsMixin:
    # Connection commands
    # TODO: auth, quit

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ConnectionCommandsMixin, self).__init__(*args, **kwargs)
        self._db: Database
        self._db_num: int
        self._pubsub: int
        self._server: Any

    @command((bytes,))
    def echo(self, message: bytes) -> bytes:
        return message

    @command((), (bytes,))
    def ping(self, *args: bytes) -> Union[List[bytes], bytes, SimpleString]:
        if len(args) > 1:
            msg = msgs.WRONG_ARGS_MSG6.format("ping")
            raise SimpleError(msg)
        if self._pubsub:
            return [b"pong", args[0] if args else b""]
        else:
            return args[0] if args else PONG

    @command((DbIndex,))
    def select(self, index: DbIndex) -> SimpleString:
        self._db = self._server.dbs[index]
        self._db_num = index  # type: ignore
        return OK
