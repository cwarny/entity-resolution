# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUserInfo
# Updates a user's profile data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateUserInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUserInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/Profile/UpdateUserInfo')


    def new_input_set(self):
        return UpdateUserInfoInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserInfoChoreographyExecution(session, exec_id, path)

class UpdateUserInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUserInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AboutMe(self, value):
        """
        Set the value of the AboutMe input for this Choreo. ((optional, string) The user's About Me string.)
        """
        InputSet._set_input(self, 'AboutMe', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Birthday(self, value):
        """
        Set the value of the Birthday input for this Choreo. ((optional, date) Date of Birth; in the format yyyy-MM-dd.)
        """
        InputSet._set_input(self, 'Birthday', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The user's city information.)
        """
        InputSet._set_input(self, 'City', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) The two-character code for the user's country.)
        """
        InputSet._set_input(self, 'Country', value)
    def set_FoodLocale(self, value):
        """
        Set the value of the FoodLocale input for this Choreo. ((optional, string) Food Database Locale; in the format "xx_XX".)
        """
        InputSet._set_input(self, 'FoodLocale', value)
    def set_FullName(self, value):
        """
        Set the value of the FullName input for this Choreo. ((optional, string) The user's full name.)
        """
        InputSet._set_input(self, 'FullName', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) The user's gender (MALE/FEMALE/NA).)
        """
        InputSet._set_input(self, 'Gender', value)
    def set_GlucoseUnit(self, value):
        """
        Set the value of the GlucoseUnit input for this Choreo. ((optional, decimal) The blood glucose unit of measurement being used. Valid values are: en_US, any,  METRIC.)
        """
        InputSet._set_input(self, 'GlucoseUnit', value)
    def set_HeightUnit(self, value):
        """
        Set the value of the HeightUnit input for this Choreo. ((optional, decimal) The height unit being used. Valid values are: en_US, any,  METRIC.)
        """
        InputSet._set_input(self, 'HeightUnit', value)
    def set_Height(self, value):
        """
        Set the value of the Height input for this Choreo. ((optional, decimal) The user's height; in the format X.XX (inches).)
        """
        InputSet._set_input(self, 'Height', value)
    def set_Locale(self, value):
        """
        Set the value of the Locale input for this Choreo. ((optional, string) Locale of website (country/language); one of the locales, currently – (en_US, fr_FR, de_DE, es_ES, en_GB, en_AU, en_NZ, ja_JP).)
        """
        InputSet._set_input(self, 'Locale', value)
    def set_Nickname(self, value):
        """
        Set the value of the Nickname input for this Choreo. ((optional, string) The user's nickname.)
        """
        InputSet._set_input(self, 'Nickname', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The two-character state abbreviation for the user.)
        """
        InputSet._set_input(self, 'State', value)
    def set_StrideLengthRunning(self, value):
        """
        Set the value of the StrideLengthRunning input for this Choreo. ((optional, decimal) Running stride length; in the format X.XX.)
        """
        InputSet._set_input(self, 'StrideLengthRunning', value)
    def set_StrideLengthWalking(self, value):
        """
        Set the value of the StrideLengthWalking input for this Choreo. ((optional, decimal) Walking stride length; in the format X.XX.)
        """
        InputSet._set_input(self, 'StrideLengthWalking', value)
    def set_Timezone(self, value):
        """
        Set the value of the Timezone input for this Choreo. ((optional, string) The user's timezone; in the format "America/Los_Angeles")
        """
        InputSet._set_input(self, 'Timezone', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        InputSet._set_input(self, 'UserID', value)
    def set_WaterUnit(self, value):
        """
        Set the value of the WaterUnit input for this Choreo. ((optional, decimal) The water unit being used. Valid values are: en_US, any,  METRIC.)
        """
        InputSet._set_input(self, 'WaterUnit', value)
    def set_WeightUnit(self, value):
        """
        Set the value of the WeightUnit input for this Choreo. ((optional, string) The weight unit being used. Valid values are: en_US, any,  METRIC.)
        """
        InputSet._set_input(self, 'WeightUnit', value)

class UpdateUserInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUserInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class UpdateUserInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateUserInfoResultSet(response, path)
