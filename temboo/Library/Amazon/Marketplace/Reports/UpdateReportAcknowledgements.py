# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateReportAcknowledgements
# Updates the acknowledged status of a report.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateReportAcknowledgements(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateReportAcknowledgements Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Reports/UpdateReportAcknowledgements')


    def new_input_set(self):
        return UpdateReportAcknowledgementsInputSet()

    def _make_result_set(self, result, path):
        return UpdateReportAcknowledgementsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateReportAcknowledgementsChoreographyExecution(session, exec_id, path)

class UpdateReportAcknowledgementsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateReportAcknowledgements
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
        Set the value of the Acknowledged input for this Choreo. ((optional, boolean) A Boolean value that indicates if an order report has been acknowledged by a prior call to UpdateReportAcknowledgements. Set to true to list order reports that have been acknowledged.)
        """
        InputSet._set_input(self, 'Acknowledged', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_ReportId(self, value):
        """
        Set the value of the ReportId input for this Choreo. ((required, integer) The id of the report to acknowledge.)
        """
        InputSet._set_input(self, 'ReportId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class UpdateReportAcknowledgementsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateReportAcknowledgements Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateReportAcknowledgementsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateReportAcknowledgementsResultSet(response, path)
