import jsonpickle
from baseService import BaseService

from python.datamodel.dao.localizationDao import LocalizationDao

class LocalizationService(BaseService):
    def __init__(self):
        pass

    def processRequest(self, request):
        data = request.read()
        print 'Request data: %s' % data
        
        dao = LocalizationDao()
        
        if data != '{}':
            localization = dao.getByLocalization(data)

            if localization:
                if localization.data:
                    #jsonpickle.load_backend('django.utils.simplejson','dumps','loads',ValueError)
                    #jsonpickle.set_preferred_backend('django.utils.simplejson')
                    #jsonpickle.set_encoder_options('django.utils.simplejson', ensure_ascii=False); #it is needed

                    return jsonpickle.encode(localization.data)
        else:
            languages = {"data" : dao.getLanguages()}
            return jsonpickle.encode(languages)

        return '{"null": "true"}'