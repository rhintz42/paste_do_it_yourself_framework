from objectpub import ObjectPublisher, Root
from paste.exceptions.errormiddleware import ErrorMiddleware
from paste.evalexception import EvalException

app = ObjectPublisher(Root())
#wrapped_app = EvalException(app)
exc_wrapped_app = ErrorMiddleware(app)

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(exc_wrapped_app, host='127.0.0.1', port='8079')
