# -*- coding: utf-8 -*-

###############################################################################
#
# GetReportRequestList
# Returns a list of report requests that you can use to get the ReportProcessingStatus and ReportId in order to retrieve a report.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetReportRequestList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReportRequestList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/GetReportRequestList')


    def new_input_set(self):
        return GetReportRequestListInputSet()

    def _make_result_set(self, result, path):
        return GetReportRequestListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReportRequestListChoreographyExecution(session, exec_id, path)

class GetReportRequestListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReportRequestList
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
    def set_MaxCount(self, value):
        """
        Set the value of the MaxCount input for this Choreo. ((optional, integer) A non-negative integer that represents the maximum number of report requests to return. Defaults to 10. Max is 100.)
        """
        InputSet._set_input(self, 'MaxCount', value)
    def set_ReportProcessingStatusList(self, value):
        """
        Set the value of the ReportProcessingStatusList input for this Choreo. ((optional, string) A comma separated list of up to three ReportProcessingStatuses by which to filter report requests.)
        """
        InputSet._set_input(self, 'ReportProcessingStatusList', value)
    def set_ReportRequestIdList(self, value):
        """
        Set the value of the ReportRequestIdList input for this Choreo. ((optional, string) A comma separated list of up to three ReportRequestId values. If you pass in a ReportRequestId values, other query conditions are ignored.)
        """
        InputSet._set_input(self, 'ReportRequestIdList', value)
    def set_ReportTypeList(self, value):
        """
        Set the value of the ReportTypeList input for this Choreo. ((optional, string) A comma separated list of up to three ReportType enumeration values.)
        """
        InputSet._set_input(self, 'ReportTypeList', value)
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

class GetReportRequestListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReportRequestList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_GeneratedReportId(self):
        """
        Retrieve the value for the "GeneratedReportId" output from this Choreo execution. ((integer) The GeneratedReportId parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        return self._output.get('GeneratedReportId', None)
    def get_ReportProcessingStatus(self):
        """
        Retrieve the value for the "ReportProcessingStatus" output from this Choreo execution. ((string) The report status parsed from the Amazon response. If multiple records are returned, this output variable will contain the report status in the list.)
        """
        return self._output.get('ReportProcessingStatus', None)
    def get_ReportRequestId(self):
        """
        Retrieve the value for the "ReportRequestId" output from this Choreo execution. ((integer) The report request id parsed from the Amazon response. If multiple records are returned, this output variable will contain the first id in the list.)
        """
        return self._output.get('ReportRequestId', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class GetReportRequestListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReportRequestListResultSet(response, path)
