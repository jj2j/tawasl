from flask import Flask
server = Flask(__name__)
@server.route('/')
def h():
	return 'ksy'
if __name__ == "__main__":
    server.run(debug=True, port=9000)
