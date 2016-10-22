#-*- coding:utf-8 -*-
"""
Wrapper for the requests library,
which will retry automatically a query,
add timeout,
etc.
"""
import logging
import os
import requests
from requests.packages.urllib3.util.retry import Retry

LOGGER = logging.getLogger(__name__)


class Request(object):
    """
    Little wrapper around requests.
    """
    def __init__(self, base_url, timeout=60, retries=5, backoff=0.1,
                 limit=100, status_force=None):
        if not base_url.startswith('http'):
            base_url = 'https://' + base_url
        self.base_url = base_url
        self.timeout = timeout
        status_force = status_force or [500, 502, 503, 504]
        self.retries = retries
        self.session = requests.Session()
        self.limit = limit
        retry = Retry(total=self.retries, backoff_factor=backoff,
                      status_forcelist=status_force)
        self.session.mount('http://',
                           requests.adapters.HTTPAdapter(max_retries=retry))
        self.session.mount('https://',
                           requests.adapters.HTTPAdapter(max_retries=retry))

    def request(self, endpoint, *args, **kwargs):
        url = os.path.join(self.base_url, endpoint)
        method = getattr(self.session, kwargs.pop('__method__'))
        kwargs['timeout'] = self.timeout
        LOGGER.info('Calling %s(args=%s, kwargs=%s)..., with timeout %s and max retries %s',
                    url, args, kwargs, self.timeout, self.retries)
        result = method(url, *args, **kwargs)
        try:
            result.raise_for_status()
        except:
            LOGGER.exception('Call to %s failed. Status code : %s.',
                             result.url, result.status_code)
            return {'status': result.status_code, 'error': result.json(), 'result': None}
        # Always jsonify
        try:
            return {'status': 0, 'error': None, 'result': result.json()}
        except:
            LOGGER.exception('Jsonify call to %s failed, text response : %s.',
                             result.url, result.text)
            return {'status': 2, 'error': result.text, 'result': None}

    def idontwantpagination(self, endpoint, *args, **kwargs):
        """Retrieve all the data of a paginated endpoint, using GET.

        :returns: The endpoint unpaginated data
        :rtype: dict
        """
        # 1. Initialize the pagination parameters.
        kwargs.setdefault('params', {})['offset'] = 0
        kwargs.setdefault('params', {})['limit'] = self.limit
        kwargs['__method__'] = 'get'
        # 2. Create an initial paginated request.
        payload = self.request(endpoint, *args, **kwargs)
        has_next = payload['result'].setdefault('meta', {'next': None})['next']
        # 3. Loop until the end
        while has_next:
            # 4. Increment the offset
            kwargs['params']['offset'] += self.limit
            # 5. Query again
            _payload = self.request(endpoint, *args, **kwargs)
            # 6. Add the paginated data to the global one
            payload['result']['data'].extend(_payload['result']['data'])
            # 7. Compute has_next
            has_next = _payload['result']['meta']['next']
        del(payload['result']['meta'])
        return payload

    def get(self, endpoint, *args, **kwargs):
        kwargs['__method__'] = 'get'
        return self.request(endpoint, *args, **kwargs)

    def post(self, endpoint, *args, **kwargs):
        kwargs['__method__'] = 'post'
        return self.request(endpoint, *args, **kwargs)

    def put(self, endpoint, *args, **kwargs):
        kwargs['__method__'] = 'put'
        return self.request(endpoint, *args, **kwargs)

    def patch(self, endpoint, *args, **kwargs):
        kwargs['__method__'] = 'patch'
        return self.request(endpoint, *args, **kwargs)

    def delete(self, endpoint, *args, **kwargs):
        kwargs['__method__'] = 'delete'
        return self.request(endpoint, *args, **kwargs)
