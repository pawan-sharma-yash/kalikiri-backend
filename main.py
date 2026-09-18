from fastapi.responses import Response

from app.database import app


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)
