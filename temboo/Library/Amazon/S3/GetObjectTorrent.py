# -*- coding: utf-8 -*-

###############################################################################
#
# GetObjectTorrent
# Returns a base64-encoded torrent file from an Amazon S3 bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetObjectTorrent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetObjectTorrent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/GetObjectTorrent')


    def new_input_set(self):
        return GetObjectTorrentInputSet()

    def _make_result_set(self, result, path):
        return GetObjectTorrentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetObjectTorrentChoreographyExecution(session, exec_id, path)

class GetObjectTorrentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetObjectTorrent
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that contains the object to retrieve.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the torrent file to retrieve.)
        """
        InputSet._set_input(self, 'FileName', value)

class GetObjectTorrentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetObjectTorrent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The retrieved file. The response is a Bencoded dictionary as defined by the BitTorrent specification, which is then Base64-encoded by Temboo. Decode to get the Bencoded dictionary.)
        """
        return self._output.get('Response', None)

class GetObjectTorrentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetObjectTorrentResultSet(response, path)
