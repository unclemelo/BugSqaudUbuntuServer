from fastapi import FastAPI
from fastapi.responses import JSONResponse
import traceback

from Server.active_users import get_active_users, add_active_user, remove_active_user

app = FastAPI()

# --- API Endpoints ---

## Get the number of active users
@app.get("/api/get_active_users")
def get_active_users_api():
    try:
        users = get_active_users()
        return JSONResponse(content={"active_users": users})
    except Exception as e:
        print(f"[Error] Failed to get active users: {e}")
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": "Failed to retrieve active users"}
        )

## Connect to the API (for testing purposes)
@app.get("/api/connect")
def connect():
    add_active_user()
    return JSONResponse(content={"message": "Connected to the API successfully!"})

## Disconnect from the API (for testing purposes)
@app.api_route("/api/disconnect", methods=["GET", "POST"])
def disconnect():
    remove_active_user()
    return {"message": "Disconnected"}

#######
# Oauth endpoints will be added here in the future
#######

@app.get("/api/discord_oauth")
def discord_oauth():
    return {"message": "Discord OAuth endpoint - to be implemented"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9000)
