from sanic import Sanic, text
from sanic.config import Config
from config import *
from routes.home import Home

Config.KEEP_ALIVE = False
app = Sanic(APP_NAME)

app = Sanic(__name__)


app.add_route(Home.as_view(), "/home")

@app.get("/")
async def handler(request):
    return text(str("welcome"))

if __name__ == "__main__":
    app.run(host=APP_HOST_URL, port=PORT, access_log=ALLOW_ACCESS_LOGS)