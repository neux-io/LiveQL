import graphene



class Track(graphene.ObjectType):
    name = graphene.String()
    track_id = graphene.Int()


class TrackInput(graphene.InputObjectType):
    pass


class CreateTrack(graphene.Mutation):
    class Arguments:
        track_data = TrackInput(required=True)

    track = graphene.Field(Track)

    @staticmethod
    def mutate(root, info, track_data=None):
        track = Track(
            name=track_data.name,
            track_id=track_data.track_id
        )
        return CreateTrack(track=track)
