import os

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def index(request):
    return Response(
        {
            "service": "csc325-ci-cd",
            "endpoints": ["/api/health/", "/api/hello/?name=YourName"],
        }
    )


@api_view(["GET"])
def health(request):
    return Response(
        {
            "status": "ok",
            "service": "csc325-ci-cd",
            "commit": os.environ.get("RENDER_GIT_COMMIT", "local"),
        }
    )


@api_view(["GET"])
def hello(request):
    name = request.query_params.get("name", "World").strip() or "World"
    return Response({"message": f"Hello, {name}!"})