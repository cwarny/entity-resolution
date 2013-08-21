# -*- coding: utf-8 -*-

###############################################################################
#
# Bill
# Retrieves bills and resolutions in the U.S. Congress since 1973 (the 93rd Congress).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Bill(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Bill Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/Bill')


    def new_input_set(self):
        return BillInputSet()

    def _make_result_set(self, result, path):
        return BillResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BillChoreographyExecution(session, exec_id, path)

class BillInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Bill
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BillID(self, value):
        """
        Set the value of the BillID input for this Choreo. ((optional, integer) Specify the ID number of the bill to return only the record for that bill.)
        """
        InputSet._set_input(self, 'BillID', value)
    def set_BillType(self, value):
        """
        Set the value of the BillType input for this Choreo. ((optional, string) The bill's type. See documentation for acceptable bill types.)
        """
        InputSet._set_input(self, 'BillType', value)
    def set_Congress(self, value):
        """
        Set the value of the Congress input for this Choreo. ((optional, integer) The number of the congress in which the bill was introduced. The current congress is 112.)
        """
        InputSet._set_input(self, 'Congress', value)
    def set_CurrentStatusDate(self, value):
        """
        Set the value of the CurrentStatusDate input for this Choreo. ((optional, string) The date of the last major action on the bill corresponding to the CurrentStatus (in YYYY-MM-DD format).)
        """
        InputSet._set_input(self, 'CurrentStatusDate', value)
    def set_CurrentStatus(self, value):
        """
        Set the value of the CurrentStatus input for this Choreo. ((optional, string) The current status of the bill. See documentation for acceptable inputs.)
        """
        InputSet._set_input(self, 'CurrentStatus', value)
    def set_IntroducedDate(self, value):
        """
        Set the value of the IntroducedDate input for this Choreo. ((optional, string) The date the bill was introduced (in YYYY-MM-DD format).)
        """
        InputSet._set_input(self, 'IntroducedDate', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((optional, integer) The bill's number (just the integer part).)
        """
        InputSet._set_input(self, 'Number', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) You can order the results using fieldname (ascending) or -fieldname (descending) where "fieldname" is one of these values: current_status_date, introduced_date, senate_floor_schedule_postdate.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SchedulePostdate(self, value):
        """
        Set the value of the SchedulePostdate input for this Choreo. ((optional, string) The date on which the bill was posted on the Senate Floor Schedule which is different from the date it was expected to be debated (in YYYY-MM-DD format).)
        """
        InputSet._set_input(self, 'SchedulePostdate', value)
    def set_Sponsor(self, value):
        """
        Set the value of the Sponsor input for this Choreo. ((optional, integer) The ID of the sponsor of the bill.)
        """
        InputSet._set_input(self, 'Sponsor', value)

class BillResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Bill Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The resopnse from GovTrack.)
        """
        return self._output.get('Response', None)

class BillChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BillResultSet(response, path)
