from fastapi import FastAPI
from fastapi.responses import JSONResponse
import traceback

from Server.active_users import get_active_users

app = FastAPI()


@app.get(f"/api/get_active_users")
def get_active_users_api():
    try:
        users = get_active_users().get_active_users()
        return JSONResponse(content={"active_users": users})
    except Exception as e:
        print(f"[Error] Failed to get active users: {e}")
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": "Failed to retrieve active users"}
        )



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9000)
