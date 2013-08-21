# -*- coding: utf-8 -*-

###############################################################################
#
# FormatTimestamp
# Returns the specified date serial number in the desired format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FormatTimestamp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FormatTimestamp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Formatting/FormatTimestamp')


    def new_input_set(self):
        return FormatTimestampInputSet()

    def _make_result_set(self, result, path):
        return FormatTimestampResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FormatTimestampChoreographyExecution(session, exec_id, path)

class FormatTimestampInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FormatTimestamp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AddDays(self, value):
        """
        Set the value of the AddDays input for this Choreo. ((optional, integer) Adds the specified number of days to the specified date serial number. A negative number will subtract.)
        """
        InputSet._set_input(self, 'AddDays', value)
    def set_AddHours(self, value):
        """
        Set the value of the AddHours input for this Choreo. ((optional, integer) Adds the specified number of hours to the specified date serial number. A negative number will subtract.)
        """
        InputSet._set_input(self, 'AddHours', value)
    def set_AddMinutes(self, value):
        """
        Set the value of the AddMinutes input for this Choreo. ((optional, integer) Adds the specified number of minutes to the specified date serial number. A negative number will subtract.)
        """
        InputSet._set_input(self, 'AddMinutes', value)
    def set_AddMonths(self, value):
        """
        Set the value of the AddMonths input for this Choreo. ((optional, integer) Adds the specified number of months to the specified date serial number. A negative number will subtract.)
        """
        InputSet._set_input(self, 'AddMonths', value)
    def set_AddSeconds(self, value):
        """
        Set the value of the AddSeconds input for this Choreo. ((optional, integer) Adds the specified number of seconds to the specified date serial number. A negative number will subtract.)
        """
        InputSet._set_input(self, 'AddSeconds', value)
    def set_AddYears(self, value):
        """
        Set the value of the AddYears input for this Choreo. ((optional, integer) Adds the specified number of years to the specified date serial number. A negative number will subtract.)
        """
        InputSet._set_input(self, 'AddYears', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((conditional, string) The format that the timestamp should be in. Java SimpleDateFormat conventions are supported. Defaults to "yyyy-MM-dd'T'HH:mm:ss.SSSZ".)
        """
        InputSet._set_input(self, 'Format', value)
    def set_LocaleCountry(self, value):
        """
        Set the value of the LocaleCountry input for this Choreo. ((optional, string) An ISO country code to specify locale.)
        """
        InputSet._set_input(self, 'LocaleCountry', value)
    def set_LocaleLanguage(self, value):
        """
        Set the value of the LocaleLanguage input for this Choreo. ((optional, string) An ISO language code to specify locale.)
        """
        InputSet._set_input(self, 'LocaleLanguage', value)
    def set_LocaleVariant(self, value):
        """
        Set the value of the LocaleVariant input for this Choreo. ((optional, string) A local variant code such as "NY" to add additional context for a locale.)
        """
        InputSet._set_input(self, 'LocaleVariant', value)
    def set_SetDay(self, value):
        """
        Set the value of the SetDay input for this Choreo. ((optional, integer) Sets the day of month (1–31) of the specified date serial number.)
        """
        InputSet._set_input(self, 'SetDay', value)
    def set_SetHour(self, value):
        """
        Set the value of the SetHour input for this Choreo. ((optional, integer) Sets the hours (0–23) of the specified date serial number.)
        """
        InputSet._set_input(self, 'SetHour', value)
    def set_SetMinute(self, value):
        """
        Set the value of the SetMinute input for this Choreo. ((optional, integer) Sets the minutes (0–59) of the specified date serial number.)
        """
        InputSet._set_input(self, 'SetMinute', value)
    def set_SetMonth(self, value):
        """
        Set the value of the SetMonth input for this Choreo. ((optional, integer) Sets the month (1–12) of the specified date serial number.)
        """
        InputSet._set_input(self, 'SetMonth', value)
    def set_SetSecond(self, value):
        """
        Set the value of the SetSecond input for this Choreo. ((optional, integer) Sets the seconds (0–59) of the specified date serial number.)
        """
        InputSet._set_input(self, 'SetSecond', value)
    def set_SetYear(self, value):
        """
        Set the value of the SetYear input for this Choreo. ((optional, integer) Sets the year (such as 1989) of the specified date serial number.)
        """
        InputSet._set_input(self, 'SetYear', value)
    def set_TimeZone(self, value):
        """
        Set the value of the TimeZone input for this Choreo. ((optional, string) The timezone to use for the date formatting function. Defaults to UTC.)
        """
        InputSet._set_input(self, 'TimeZone', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((conditional, date) A number representing the current date and time, expressed as the number of milliseconds since January 1, 1970 (epoch time).)
        """
        InputSet._set_input(self, 'Timestamp', value)

class FormatTimestampResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FormatTimestamp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_FormattedDate(self):
        """
        Retrieve the value for the "FormattedDate" output from this Choreo execution. ((date) The formatted version of the timestamp.)
        """
        return self._output.get('FormattedDate', None)

class FormatTimestampChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FormatTimestampResultSet(response, path)
