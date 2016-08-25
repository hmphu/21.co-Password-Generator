import flask
from two1.wallet import Wallet
from two1.bitserv.flask import Payment
import yaml
import json
from flask import request
from random import randint
app = flask.Flask(__name__)
payment = Payment(app, Wallet())

@app.route('/gen')
@payment.required(1000)
def gen():
    chars = '0123456789abcdefghijklmnopqrstuzwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-.'
    try:
        test = request.args['len']
        test = 1
    except KeyError:
        test = 0

    if test == 1:
        length = int(request.args.get('len'))
        if length < 8: length = 8
    else:
        length = randint(12,24)
    passwd = ''
    for i in range(0,length):
        passwd += chars[randint(0,(len(chars)-1))]
    return "Your password is:\n{0}".format(passwd)

@app.route('/manifest')
def manifest():
    """Provide the app manifest to the 21 crawler.
    """
    with open('./manifest.yaml', 'r') as f:
        manifest = yaml.load(f)
    return json.dumps(manifest)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
