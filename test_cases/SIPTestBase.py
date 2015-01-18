class SIPTestBase(object):
    """
    SIPTestBase
    """
    class SIPTestError(Exception):
        pass

    def __init__(self, clients, config):
        self.clients = clients
        self.config = config

    def run(self):
        raise NotImplementedError('override me!')

    @staticmethod
    def send_request(client, msg=None):
        if msg is None:
            msg = {}

        data = {
            'type': 'request',
            'headers': {
                'type': ''
            }.update(msg.get('headers') or {}),
            'body': {
                'type': 'sdp'
            }.update(msg.get('body') or {})
        }

        client.send(data)