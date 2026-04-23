# multi-server-fastapi
Two mcp servers(functions) are served on single FastAPI server.

While creating the mcp server make sure to add the port to the arguement. This is important for when you deploy the code, the server will show the access issue without it.
e.g.
  mcp = FastMCP("WebSeach", host="0.0.0.0", port=8080)
  mcp =  FastMCP("math",host="0.0.0.0",port = 8070)

Deployement: This git can directly be used in Render for the testing the deployment.
