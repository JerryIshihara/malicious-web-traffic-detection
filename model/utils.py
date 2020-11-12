

def check_data_format(X):
    try:
        assert type(X['SourceIP']) == str
        assert type(X['DestinationIP']) == str
        assert type(X['SourcePort']) == int
        assert type(X['DestinationPort']) == int
        assert type(X['TimeStamp']) == str
        assert type(X['Duration']) == float
        assert type(X['FlowBytesSent']) == int
        assert type(X['FlowSentRate']) == float
        assert type(X['FlowBytesReceived']) == int
        assert type(X['FlowReceivedRate']) == float
        # assert type(X['PacketLengthVariance']) == float
        # assert type(X['PacketLengthStandardDeviation']) == float
        assert type(X['PacketLengthMean']) == float
        # assert type(X['PacketLengthMedian']) == float
        # assert type(X['PacketLengthMode']) == float
        # assert type(X['PacketLengthSkewFromMedian']) == float
        # assert type(X['PacketLengthSkewFromMode']) == float
        # assert type(X['PacketLengthCoefficientofVariation']) == float
        # assert type(X['PacketTimeVariance']) == float
        # assert type(X['PacketTimeStandardDeviation']) == float
        assert type(X['PacketTimeMean']) == float
        # assert type(X['PacketTimeMedian']) == float
        # assert type(X['PacketTimeMode']) == float
        # assert type(X['PacketTimeSkewFromMedian']) == float
        # assert type(X['PacketTimeSkewFromMode']) == float
        # assert type(X['PacketTimeCoefficientofVariation ']) == float
        # assert type(X['ResponseTimeTimeVariance']) == float
        # assert type(X['ResponseTimeTimeStandardDeviation']) == float
        assert type(X['ResponseTimeTimeMean']) == float
        # assert type(X['ResponseTimeTimeMedian']) == float
        # assert type(X['ResponseTimeTimeMode']) == float
        # assert type(X['ResponseTimeTimeSkewFromMedian']) == float
        # assert type(X['ResponseTimeTimeSkewFromMode']) == float
        # assert type(X['ResponseTimeTimeCoefficientofVariation ']) == float
        assert type(X['DoH']) == bool
    except: return False
    return True