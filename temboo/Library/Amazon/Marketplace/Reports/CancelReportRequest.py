# -*- coding: utf-8 -*-

###############################################################################
#
# CancelReportRequest
# Cancels one or more report requests.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CancelReportRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CancelReportRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/CancelReportRequest')


    def new_input_set(self):
        return CancelReportRequestInputSet()

    def _make_result_set(self, result, path):
        return CancelReportRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CancelReportRequestChoreographyExecution(session, exec_id, path)

class CancelReportRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CancelReportRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
    def set_ReportProcessingStatus(self, value):
        """
        Set the value of the ReportProcessingStatus input for this Choreo. ((optional, string) A report processing status by which to filter report requests. Valid values are: _SUBMITTED_, _IN_PROGRESS_, _CANCELLED_, _DONE_, _DONE_NO_DATA_.)
        """
        InputSet._set_input(self, 'ReportProcessingStatus', value)
    def set_ReportRequestId(self, value):
        """
        Set the value of the ReportRequestId input for this Choreo. ((optional, string) A ReportRequestId value. If you pass in a ReportRequestId value, other query conditions are ignored.)
        """
        InputSet._set_input(self, 'ReportRequestId', value)
    def set_ReportType(self, value):
        """
        Set the value of the ReportType input for this Choreo. ((optional, string) A ReportType enumeration value (i.e. GET_ORDERS_DATA_).)
        """
        InputSet._set_input(self, 'ReportType', value)
    def set_RequestedFromDate(self, value):
        """
        Set the value of the RequestedFromDate input for this Choreo. ((optional, date) The start of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        InputSet._set_input(self, 'RequestedFromDate', value)
    def set_RequestedToDate(self, value):
        """
        Set the value of the RequestedToDate input for this Choreo. ((optional, date) The end of the date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        InputSet._set_input(self, 'RequestedToDate', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class CancelReportRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CancelReportRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Count(self):
        """
        Retrieve the value for the "Count" output from this Choreo execution. ((integer) A non-negative integer that represents the total number of report requests that were cancelled.)
        """
        return self._output.get('Count', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class CancelReportRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CancelReportRequestResultSet(response, path)
