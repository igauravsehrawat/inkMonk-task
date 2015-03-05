import config
import core


class Resource(object):

    _resource_ = None

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        return str(self.id)

    @classmethod
    def get(cls, identifier, params=[], version=config.API_VERSION,
            url=config.API_URL, key=config.API_KEY,
            secret=config.API_SECRET):
        return Resource(**core.get(cls._resource_, identifier, params=params,
                        version=version, url=url, key=key,
                        secret=secret))

    @classmethod
    def all(cls, params=[], version=config.API_VERSION,
            url=config.API_URL, key=config.API_KEY,
            secret=config.API_SECRET):
        return [Resource(**kwargs) for kwargs in core.all(
            cls._resource_, params=params,
            version=version, url=url, key=key, secret=secret)]

    @classmethod
    def create(cls, **kwargs):
        version = kwargs.pop("version", config.API_VERSION)
        url = kwargs.pop("url", config.API_URL)
        key = kwargs.pop("key", config.API_KEY)
        secret = kwargs.pop("secret", config.API_SECRET)
        result = core.create(
            cls._resource_, data=kwargs, version=version, url=url,
            key=key, secret=secret)
        if isinstance(result, dict):
            return Resource(**result)
        elif isinstance(result, list):
            return [Resource(**params) for params in result]
