from django.http import HttpResponse


class myMixins(object):
    def myfunction(self, json_d):
        return HttpResponse(json_d, content_type='application/json')
