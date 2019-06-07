import Live
from promise import Promise
from promise.dataloader import DataLoader


class TrackLoader(DataLoader):

    def batch_load_fn(self):
        # Here we return a promise that will result on the
        # corresponding user for each key in keys
        return Promise.resolve(self.getTracks())

    def getSet(self):
        return Live.Application.get_application().get_document()

    def getTracks(self):
            return Live.Application.get_application().get_document().tracks
