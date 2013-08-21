# -*- coding: utf-8 -*-

###############################################################################
#
# GetReportList
# Returns a list of reports that were created in the previous 90 days.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetReportList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReportList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/GetReportList')


    def new_input_set(self):
        return GetReportListInputSet()

    def _make_result_set(self, result, path):
        return GetReportListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReportListChoreographyExecution(session, exec_id, path)

class GetReportListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReportList
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
    def set_Acknowledged(self, value):
        """
        Set the value of the Acknowledged input for this Choreo. ((optional, boolean) A Boolean value that indicates if an order report has been acknowledged by a prior call to UpdateReportAcknowledgements. Set to "true" to list order reports that have been acknowledged.)
        """
        InputSet._set_input(self, 'Acknowledged', value)
    def set_AvailableFromDate(self, value):
        """
        Set the value of the AvailableFromDate input for this Choreo. ((optional, date) The earliest date you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        InputSet._set_input(self, 'AvailableFromDate', value)
    def set_AvailableToDate(self, value):
        """
        Set the value of the AvailableToDate input for this Choreo. ((optional, date) The most recent date you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        InputSet._set_input(self, 'AvailableToDate', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_MaxCount(self, value):
        """
        Set the value of the MaxCount input for this Choreo. ((optional, integer) A non-negative integer that represents the maximum number of report requests to return. Defaults to 10. Max is 100.)
        """
        InputSet._set_input(self, 'MaxCount', value)
    def set_ReportRequestId(self, value):
        """
        Set the value of the ReportRequestId input for this Choreo. ((optional, integer) A ReportRequestId value. If you pass a ReportRequestId value, other query conditions are ignored.)
        """
        InputSet._set_input(self, 'ReportRequestId', value)
    def set_ReportType(self, value):
        """
        Set the value of the ReportType input for this Choreo. ((optional, string) A ReportType enumeration value (i.e. GET_ORDERS_DATA_).)
        """
        InputSet._set_input(self, 'ReportType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((conditional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetReportListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReportList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ReportId(self):
        """
        Retrieve the value for the "ReportId" output from this Choreo execution. ((integer) The report id parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        return self._output.get('ReportId', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class GetReportListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReportListResultSet(response, path)
