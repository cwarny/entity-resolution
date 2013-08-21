# -*- coding: utf-8 -*-

###############################################################################
#
# EditGroup
# Allows you to create a new group or update an existing one.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EditGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EditGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/EditGroup')


    def new_input_set(self):
        return EditGroupInputSet()

    def _make_result_set(self, result, path):
        return EditGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EditGroupChoreographyExecution(session, exec_id, path)

class EditGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EditGroup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((integer) Private Key for 1 unique customer to connect with - provided by Obad Mobile Marketing)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((string) The description of the group)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_GroupID(self, value):
        """
        Set the value of the GroupID input for this Choreo. ((integer) The id of the group you need to update. In creation mode, leave blank and the id will be returned in the response.)
        """
        InputSet._set_input(self, 'GroupID', value)
    def set_Mode(self, value):
        """
        Set the value of the Mode input for this Choreo. ((optional, boolean) Specify 0 for creating and 1 for updating. Defaults to 0.)
        """
        InputSet._set_input(self, 'Mode', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((string) The title of the group)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of group to perform the action on.  Can be usergroup, shopgroup, or coupongroup. Defaults to usergroup.)
        """
        InputSet._set_input(self, 'Type', value)


class EditGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EditGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Obad)
        """
        return self._output.get('Response', None)

class EditGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EditGroupResultSet(response, path)
