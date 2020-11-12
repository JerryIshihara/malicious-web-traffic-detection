import pytest
import tempfile
import numpy as np
import json
import os
import sys
sys.path.append('../model')
import model

benign_data = {
	"SourceIP": "0.0.0.0", 
	"DestinationIP": "0.0.0.0", 
	"SourcePort": 12, 
	"DestinationPort": 24, 
	"TimeStamp": "21231", 
	"Duration": 12.4124, 
	"FlowBytesSent": 125, 
	"FlowSentRate": 8692.12, 
    "FlowBytesReceived": 515, 
    "FlowReceivedRate": 515.523,
    "PacketLengthMean": 515.523, 
    "PacketTimeMean": 515.523, 
    "ResponseTimeTimeMean": 515.523, 
    "DoH": True
}

mal_data = {
	"SourceIP": "192.168.20.212", 
	"DestinationIP": "9.9.9.11", 
	"SourcePort": 54066, 
	"DestinationPort": 443, 
	"TimeStamp": "2020-03-31 21:24:25", 
	"Duration": 34.0556, 
	"FlowBytesSent": 1875, 
	"FlowSentRate": 55.0571, 
    "FlowBytesReceived": 4964, 
    "FlowReceivedRate": 145.762,
    "PacketLengthMean": 213.719, 
    "PacketTimeMean": 7.86213, 
    "ResponseTimeTimeMean": 0.0098586, 
    "DoH": True
}

wrong_data = {
	"SourceIP": 192, 
	"DestinationIP": "9.9.9.11", 
	"SourcePort": 54066, 
	"DestinationPort": 443, 
	"TimeStamp": "2020-03-31 21:24:25", 
	"Duration": 34.0556, 
	"FlowBytesSent": 1875, 
	"FlowSentRate": 55.0571, 
    "FlowBytesReceived": 4964, 
    "FlowReceivedRate": 145.762,
    "PacketLengthMean": 213.719, 
    "PacketTimeMean": 7.86213, 
    "ResponseTimeTimeMean": 0.0098586, 
    "DoH": True
}


@pytest.fixture
def client():
    # db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    model.app.config['TESTING'] = True
    with model.app.test_client() as client:
        # with model.app.app_context():
        #     model.init_db()
        yield client
    # os.close(db_fd)
    # os.unlink(flaskr.app.config['DATABASE']


def test_forward(client):
    """[summary: test baseline model forward pass]

    Args:
        client ([type: class]): [description: Flask test client]
    """
    # with correct input format
    URL = '/predict'
    TYPE = 'application/json'
    response = client.post(URL, 
                           data=json.dumps(benign_data),
                           content_type=TYPE)
    assert response.status_code == 200
    response = client.post(URL, 
                           data=json.dumps(mal_data),
                           content_type=TYPE)
    assert response.status_code == 200
    # with wrong data type
    response = client.post(URL, 
                        data=json.dumps(wrong_data),
                        content_type=TYPE)
    assert response.status_code == 403
    # with no input
    response = client.post(URL)
    assert response.status_code == 403