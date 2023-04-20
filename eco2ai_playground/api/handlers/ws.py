from starlette.concurrency import run_until_first_complete
from starlette.routing import WebSocketRoute

from eco2ai_playground.api.broadcaster import broadcaster


async def chatroom_ws(websocket):
    await websocket.accept()
    await run_until_first_complete(
        (chatroom_ws_receiver, {"websocket": websocket}),
        (chatroom_ws_sender, {"websocket": websocket}),
    )


async def chatroom_ws_receiver(websocket):
    async for message in websocket.iter_text():
        await broadcaster.publish(channel="general", message=message)


async def chatroom_ws_sender(websocket):
    async with broadcaster.subscribe(channel="general") as subscriber:
        async for event in subscriber:
            await websocket.send_text(event.message)


ws_starlette_routes = [WebSocketRoute("/ws", chatroom_ws, name="chatroom_ws")]
