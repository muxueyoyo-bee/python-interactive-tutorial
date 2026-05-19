def connection_made(self, handler: RequestHandler[_Request], transport: asyncio.Transport) -> None:
    return f'connection_made result'