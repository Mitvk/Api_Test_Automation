from config import LOG, HideSensitiveData

def build_request_headers(access_token, accept_type="application/json", **kwargs):
    LOG.info('build_request_headers')
    header = {
        "Authorization": f"Bearer {access_token}",
        "Accept": accept_type
    }

    if "content_type" in kwargs:
        header['Content-Type'] = kwargs['content_type']
    LOG.info(f'Request Header : {header}')
    return header