import graphene



class Clip(graphene.ObjectType):
    name = graphene.String()
    track_id = graphene.Int()
    slot_id = graphene.Int()
    clip_id = graphene.Int()


class ClipInput(graphene.InputObjectType):
    pass


class CreateClip(graphene.Mutation):
    class Arguments:
        clip_data = ClipInput(required=True)

    clip = graphene.Field(Clip)

    @staticmethod
    def mutate(root, info, clip_data=None):
        clip = Clip(
            name=clip_data.name,
            track_id=clip_data.track_id,
            slot_id=clip_data.slot_id,
            clip_id=clip_data.clip_id
        )
        return CreateClip(clip=clip)
