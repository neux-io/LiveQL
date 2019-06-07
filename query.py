import graphene
from graphene import relay
from obj.clip import Clip


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    clip = graphene.Field(Clip)

    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name

    def resolve_clip(self, info):
        return Clip(name="dd")
