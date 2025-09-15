
from fastapi import APIRouter

from rest_lib.client import mcp_client_context

router = APIRouter(
    prefix="/client",
    tags=["client"],
)


@router.post("/do_something")
async def main(message: dict):
    async with mcp_client_context() as (client, agent):
        result = await agent.run(message)
        await client.close_all_sessions()
        return {"result": result}
