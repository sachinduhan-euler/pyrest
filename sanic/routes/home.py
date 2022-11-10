from sanic.views import HTTPMethodView
from sanic.response import json
from util.formatter import http_formatter

class Home(HTTPMethodView):

  def get(self, request):
      return json(http_formatter("I am get method"))

  # You can also use async syntax
  async def post(self, request):
      return json(http_formatter("I am post method"))

  def put(self, request):
      return json(http_formatter("I am put method"))

  def patch(self, request):
      return json(http_formatter("I am patch method"))

  def delete(self, request):
      return json(http_formatter("I am delete method"))