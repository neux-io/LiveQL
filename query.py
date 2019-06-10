import graphene
from graphene import relay
from obj.clip import Clip
from obj.track import Track
import loader


class LiveQuery(graphene.ObjectType):

    node = relay.Node.Field()
    clip = graphene.Field(Clip)
    track = graphene.List(lambda: Track)

    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name

    def resolve_clip(self, info):
        return Clip(name="dd")

    def resolve_track(self, info):
        return loader.TrackLoader().load()
