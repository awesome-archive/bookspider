# -*- coding: utf-8 -*-
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Book, BookPage


class BookPageNode(DjangoObjectType):
    class Meta:
        model = BookPage
        filter_fields = {
            'book_number': ['exact'],
            'page_number': ['exact'],
        }
        interfaces = (relay.Node, )


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'author': ['exact', 'icontains', 'istartswith'],
            'category': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(AbstractType):
    book = relay.Node.Field(BookNode)
    book_page = relay.Node.Field(BookPageNode)
    all_books = DjangoFilterConnectionField(BookNode)
    all_pages = DjangoFilterConnectionField(BookPageNode)
