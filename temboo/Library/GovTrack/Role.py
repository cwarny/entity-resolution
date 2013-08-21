# -*- coding: utf-8 -*-

###############################################################################
#
# Role
# Returns terms held in office by Members of Congress and U.S. Presidents.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Role(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Role Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GovTrack/Role')


    def new_input_set(self):
        return RoleInputSet()

    def _make_result_set(self, result, path):
        return RoleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RoleChoreographyExecution(session, exec_id, path)

class RoleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Role
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Current(self, value):
        """
        Set the value of the Current input for this Choreo. ((optional, string) Whether the role is currently held, or it is archival information.)
        """
        InputSet._set_input(self, 'Current', value)
    def set_District(self, value):
        """
        Set the value of the District input for this Choreo. ((optional, string) For representatives, the number of their congressional district. 0 for at-large districts, -1 in historical data if the district is not known.)
        """
        InputSet._set_input(self, 'District', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) The date the role ended - when the person resigned, died, etc. (in YYYY-MM-DD format).)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Results are paged 20 per call by default. Set the limit input to a high value to get all of the results at once.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) You can order the results by date using fieldname (ascending) or -fieldname (descending), where "fieldname" is either startdate or enddate.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) The political party of the person. If the person changes party, it is usually the most recent party during this role.)
        """
        InputSet._set_input(self, 'Party', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify the format of the response. Default is JSON, but XML is also possible.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_RoleID(self, value):
        """
        Set the value of the RoleID input for this Choreo. ((optional, integer) Specify the ID number of a role object to retrieve the record for only that role.)
        """
        InputSet._set_input(self, 'RoleID', value)
    def set_RoleType(self, value):
        """
        Set the value of the RoleType input for this Choreo. ((optional, string) Acceptable values: senator, representative, or president.)
        """
        InputSet._set_input(self, 'RoleType', value)
    def set_SenatorClass(self, value):
        """
        Set the value of the SenatorClass input for this Choreo. ((optional, integer) For senators, their election class, which determines which years they are up for election. Acceptable values: class1, class2, class3.)
        """
        InputSet._set_input(self, 'SenatorClass', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) The date the role began  - when the person took office (in YYYY-MM-DD format).)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, integer) For senators and representatives, the two-letter USPS abbreviation for the state or territory they are serving. See documentation for more on territories and historical data.)
        """
        InputSet._set_input(self, 'State', value)

class RoleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Role Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The resopnse from GovTrack.)
        """
        return self._output.get('Response', None)

class RoleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RoleResultSet(response, path)
