# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteMultipleObjects
# Deletes multiple objects from an S3 Bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteMultipleObjects(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteMultipleObjects Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/DeleteMultipleObjects')


    def new_input_set(self):
        return DeleteMultipleObjectsInputSet()

    def _make_result_set(self, result, path):
        return DeleteMultipleObjectsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteMultipleObjectsChoreographyExecution(session, exec_id, path)

class DeleteMultipleObjectsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteMultipleObjects
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
        Set the value of the BucketName input for this Choreo. ((required, string) The the name of the bucket that contains the objects that you want to delete.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_FileNames(self, value):
        """
        Set the value of the FileNames input for this Choreo. ((required, string) A list of file names to delete (separated by commas).)
        """
        InputSet._set_input(self, 'FileNames', value)

class DeleteMultipleObjectsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteMultipleObjects Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. Note that no content is returned for a successful delete operation.)
        """
        return self._output.get('Response', None)

class DeleteMultipleObjectsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteMultipleObjectsResultSet(response, path)
