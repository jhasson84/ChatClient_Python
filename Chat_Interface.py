from flask import Flask, render_template
from flask_socketio import SocketIO,emit

app = Flask(__name__)


app.config[ 'Secret_Key' ] = 'ArbitraryPlaceholder'

socketio = SocketIO( app )

@app.route('/')

def index():
	return 'hello world'

if __name__ == '__main__':
	socketio.run( app,debug = True )
