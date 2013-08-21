# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketWebsiteRedirectAll
# Configures the specified bucket as a website and redirects all web requests to the designated hostname.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutBucketWebsiteRedirectAll(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketWebsiteRedirectAll Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketWebsiteRedirectAll')


    def new_input_set(self):
        return PutBucketWebsiteRedirectAllInputSet()

    def _make_result_set(self, result, path):
        return PutBucketWebsiteRedirectAllResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketWebsiteRedirectAllChoreographyExecution(session, exec_id, path)

class PutBucketWebsiteRedirectAllInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketWebsiteRedirectAll
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that you wish to configure.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_HostName(self, value):
        """
        Set the value of the HostName input for this Choreo. ((required, string) Name of the host where requests will be redirected. Ex.: example.com)
        """
        InputSet._set_input(self, 'HostName', value)
    def set_Protocol(self, value):
        """
        Set the value of the Protocol input for this Choreo. ((optional, string) Protocol to use (http, https) when redirecting requests. The default is http.)
        """
        InputSet._set_input(self, 'Protocol', value)

class PutBucketWebsiteRedirectAllResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketWebsiteRedirectAll Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful website configuration request, no content is returned and this output variable will be empty.)
        """
        return self._output.get('Response', None)

class PutBucketWebsiteRedirectAllChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketWebsiteRedirectAllResultSet(response, path)
