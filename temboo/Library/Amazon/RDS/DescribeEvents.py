# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeEvents
# Returns events related to DB Instances, DB Security Groups, DB Snapshots and DB Parameter Groups for the past 14 days.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DescribeEvents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeEvents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/DescribeEvents')


    def new_input_set(self):
        return DescribeEventsInputSet()

    def _make_result_set(self, result, path):
        return DescribeEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeEventsChoreographyExecution(session, exec_id, path)

class DescribeEventsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeEvents
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
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((optional, integer) The number of minutes to retrieve events for. Defaults to 60.)
        """
        InputSet._set_input(self, 'Duration', value)
    def set_EndTime(self, value):
        """
        Set the value of the EndTime input for this Choreo. ((optional, date) The end of the time interval for which to retrieve events, specified in ISO 8601 format (i.e. 2009-07-08T18:00Z).)
        """
        InputSet._set_input(self, 'EndTime', value)
    def set_Marker(self, value):
        """
        Set the value of the Marker input for this Choreo. ((optional, integer) If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.)
        """
        InputSet._set_input(self, 'Marker', value)
    def set_MaxRecords(self, value):
        """
        Set the value of the MaxRecords input for this Choreo. ((optional, integer) The maximum number of records to include in the response. If more records exist, a marker is included in the response so that the remaining results may be retrieved. Defaults to max (100). Min is 20.)
        """
        InputSet._set_input(self, 'MaxRecords', value)
    def set_SourceIdentifier(self, value):
        """
        Set the value of the SourceIdentifier input for this Choreo. ((optional, string) The identifier of the event source for which events will be returned. If not specified, then all sources are included in the response.)
        """
        InputSet._set_input(self, 'SourceIdentifier', value)
    def set_SourceType(self, value):
        """
        Set the value of the SourceType input for this Choreo. ((optional, string) The event source to retrieve events for. If no value is specified, all events are returned. Valid values are: db-instance | db-parameter-group | db-security-group | db-snapshot.)
        """
        InputSet._set_input(self, 'SourceType', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((optional, date) The beginning of the time interval to retrieve events for, specified in ISO 8601 format (i.e. 2009-07-08T18:00Z))
        """
        InputSet._set_input(self, 'StartTime', value)

class DescribeEventsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeEvents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeEventsResultSet(response, path)
