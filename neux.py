import Live
from _Framework.ControlSurface import ControlSurface # Central base class for scripts based on the new Framework


class Neux(ControlSurface):

    def __init__(self, c_instance):

        ControlSurface.__init__(self, c_instance)

        # self.log_message(sys.path)
        self.getTracks()[0].clip_slots[0].create_clip(4)

    def getSet(self):
        return Live.Application.get_application().get_document()

    def getTracks(self):
        return Live.Application.get_application().get_document().tracks


