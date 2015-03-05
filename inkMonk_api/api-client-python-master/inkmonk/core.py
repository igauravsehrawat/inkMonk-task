from base64 import b64encode
from hashlib import sha1
import requests
import config
import json
import hmac


JSON_MIME_TYPE = 'application/json'


def get_basic_authorization_header(key):
    return "Basic %s" % b64encode(key+":")


def get_signed_authorization_header(key, secret, message):
    return b64encode("%s:%s" % (
        key, hmac.new(secret, message, sha1).hexdigest()))


def result(response):
    if response.status_code == 200:
        rjson = response.json()
        if rjson['status'] == 'success':
            return rjson['result']
    return None


def get(resource, identifier, params=[], version=config.API_VERSION,
        url=config.API_URL, key=config.API_KEY,
        secret=config.API_SECRET):
    return result(requests.get(
        '%s/%s/%s/%s' % (url, version, resource, identifier),
        headers={'Content-Type': JSON_MIME_TYPE,
                 'Authorization': get_signed_authorization_header(
                     key, secret,
                     "GET:{0}/{1}/{2}:{3}".format(
                         version, resource, identifier, JSON_MIME_TYPE)
                     )},
        params=params))


def all(resource, params=[], version=config.API_VERSION,
        url=config.API_URL, key=config.API_KEY,
        secret=config.API_SECRET):
    return result(requests.get(
        '{0}/{1}/{2}'.format(url, version, resource),
        headers={'Content-Type': JSON_MIME_TYPE,
                 'Authorization': get_signed_authorization_header(
                     key, secret,
                     "GET:{0}/{1}:{2}".format(
                         version, resource, JSON_MIME_TYPE)
                     )},
        params=params))


def create(resource, data=None, version=config.API_VERSION,
           url=config.API_URL, key=config.API_KEY,
           secret=config.API_SECRET):
    return result(requests.post(
        '{0}/{1}/{2}'.format(url, version, resource),
        data=json.dumps(data),
        headers={'Content-Type': JSON_MIME_TYPE,
                 'Authorization': get_signed_authorization_header(
                     key, secret,
                     "POST:{0}/{1}:{2}".format(
                         version, resource, JSON_MIME_TYPE)
                     )}
        ))
