# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveReport
# Creates a report request of any report type, polls for the status of the report, and downloads the report when it's available.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveReport(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveReport Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/RetrieveReport')


    def new_input_set(self):
        return RetrieveReportInputSet()

    def _make_result_set(self, result, path):
        return RetrieveReportResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveReportChoreographyExecution(session, exec_id, path)

class RetrieveReportInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveReport
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
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) The end of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_ReportType(self, value):
        """
        Set the value of the ReportType input for this Choreo. ((optional, string) A ReportType enumeration value. Defaults to _GET_FLAT_FILE_OPEN_LISTINGS_DATA_.)
        """
        InputSet._set_input(self, 'ReportType', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) The start of a date range used for selecting the data to report, in ISO8601 date format (i.e. 2012-01-01).)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        InputSet._set_input(self, 'TimeToWait', value)

class RetrieveReportResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveReport Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_GeneratedReportId(self):
        """
        Retrieve the value for the "GeneratedReportId" output from this Choreo execution. ((integer) The GeneratedReportId parsed from the Amazon response.)
        """
        return self._output.get('GeneratedReportId', None)
    def get_ReportProcessingStatus(self):
        """
        Retrieve the value for the "ReportProcessingStatus" output from this Choreo execution. ((string) The status of the report request parsed from the Amazon response.)
        """
        return self._output.get('ReportProcessingStatus', None)
    def get_ReportRequestId(self):
        """
        Retrieve the value for the "ReportRequestId" output from this Choreo execution. ((integer) The ReportRequestId parsed from the Amazon response. This id is used in GetReportRequestList.)
        """
        return self._output.get('ReportRequestId', None)
    def get_Report(self):
        """
        Retrieve the value for the "Report" output from this Choreo execution. (The report contents.)
        """
        return self._output.get('Report', None)

class RetrieveReportChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveReportResultSet(response, path)
