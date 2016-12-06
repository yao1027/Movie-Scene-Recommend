from flask import Flask, render_template
from flask_socketio import SocketIO
import boto.sns
sns_conn = boto.sns.connect_to_region("us-east-1", profile_name='movie')
# print sns_conn.aws_access_key_id

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('init')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('watch_interval')
def handle_my_custom_event(json):
    # print json["uid"]
    sns_conn.publish(
					topic="arn:aws:sns:us-east-1:612129620405:watch_interval",
					message=json
	)
    # print('received watch: ' + str(json))

if __name__ == '__main__':


    socketio.run(app, port=6888)