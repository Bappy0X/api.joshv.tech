from sanic import Blueprint, response

bp = Blueprint("me", url_prefix="/me")

@bp.get("/projects")
async def projects(req):
    return response.json({"success": True})