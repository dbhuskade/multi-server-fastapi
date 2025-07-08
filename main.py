import contextlib
import os
from fastapi import FastAPI, Request, Response
from servers.mathserver import mcp as math_mcp
from servers.web_search import mcp as web_search_mcp

# create a conbined lifespan to manage the lifespan of both MCP instances
@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        # Register the math MCP instance
        await stack.enter_async_context(math_mcp.session_manager.run())
        # Register the web search MCP instance
        await stack.enter_async_context(web_search_mcp.session_manager.run())
        yield

app = FastAPI(lifespan=lifespan)
app.mount("/math", math_mcp.streamable_http_app())
app.mount("/web", web_search_mcp.streamable_http_app())

PORT = os.environ.get("PORT", 10000)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(PORT), log_level="info")
