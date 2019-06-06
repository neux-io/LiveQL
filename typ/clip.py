import graphene

class Clip(graphene.ObjectType):
    name = graphene.String()
    track_id = graphene.Int()
    slot_id = graphene.Int()
    clip_id = graphene.Int()


class CreateClip(graphene.Mutation)
    class Arguments:
        name = graphene.String()
        track_id = graphene.Int()
        slot_id = graphene.Int()
        clip_id = graphene.Int()

    ok = graphene.Boolean()
    clip = graphene.Field(lambda: Clip)

    def mutate(self, info, name)
        clip = Clip(name=name)
        ok = True
        return CreateClip(clip=clip, ok=ok)
        