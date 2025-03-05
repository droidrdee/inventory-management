from django.http import HttpResponse
from articles.models import Article
import random


def test(request):

    article_obj = Article.objects.get(id=random.randint(1,3))
    string = f"""
    <h1> Title : {article_obj.title} Random : {random.randint(1000, 563256532)}</h1>
    <h3>Content : {article_obj.content}</h3>
    """
    return HttpResponse(string)