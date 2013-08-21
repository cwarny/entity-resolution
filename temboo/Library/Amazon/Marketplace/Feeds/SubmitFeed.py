# -*- coding: utf-8 -*-

###############################################################################
#
# SubmitFeed
# Submits a feed, of the specified type, to Amazon Marketplace.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SubmitFeed(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SubmitFeed Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/SubmitFeed')


    def new_input_set(self):
        return SubmitFeedInputSet()

    def _make_result_set(self, result, path):
        return SubmitFeedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SubmitFeedChoreographyExecution(session, exec_id, path)

class SubmitFeedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SubmitFeed
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FeedData(self, value):
        """
        Set the value of the FeedData input for this Choreo. ((conditional, any) The feed data to sumbit to Amazon Marketplace.)
        """
        InputSet._set_input(self, 'FeedData', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_FeedType(self, value):
        """
        Set the value of the FeedType input for this Choreo. ((optional, string) The type of feed being submitted.  Default value is set to  _POST_FLAT_FILE_INVLOADER_DATA_).)
        """
        InputSet._set_input(self, 'FeedType', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        InputSet._set_input(self, 'TimeToWait', value)


class SubmitFeedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SubmitFeed Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ProcessingStatus(self):
        """
        Retrieve the value for the "ProcessingStatus" output from this Choreo execution. ((string) The processing status of the feed submission which is parsed from the Amazon response.)
        """
        return self._output.get('ProcessingStatus', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon after submitting the feed.)
        """
        return self._output.get('Response', None)
    def get_SubmissionId(self):
        """
        Retrieve the value for the "SubmissionId" output from this Choreo execution. ((integer) The submission id parsed from the Amazon response.)
        """
        return self._output.get('SubmissionId', None)
    def get_SubmissionResult(self):
        """
        Retrieve the value for the "SubmissionResult" output from this Choreo execution. ((string) The submission result returned from Amazon.)
        """
        return self._output.get('SubmissionResult', None)

class SubmitFeedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SubmitFeedResultSet(response, path)
