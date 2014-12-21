from objectpub import ObjectPublisher

class Root(object):
    def __init__(self):
        self.cool = cool()

    # The "index" method:
    def __call__(self):
        return '''
        <form action="welcome">
        Name: <input type="text" name="name">
        <input type="submit">
        </form>
        '''

    def welcome(self, name):
        return 'Hello %s!' % name

class cool(object):

    def __call__(self):
        return '''
        <form action="/cool/welcome">
        Who's Cool?: <input type="text" name="name">
        <input type="submit">
        </form>
        '''

    def welcome(self, name):
        return "You're a cool guy, %s!" % name


app = ObjectPublisher(Root())

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8079')
