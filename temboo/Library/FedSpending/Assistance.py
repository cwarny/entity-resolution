# -*- coding: utf-8 -*-

###############################################################################
#
# Assistance
# Allows access to the information in the Federal Assisatance Award Data System (FAADS) database, which reports all financial assistance made by federal agencies.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Assistance(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Assistance Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/FedSpending/Assistance')


    def new_input_set(self):
        return AssistanceInputSet()

    def _make_result_set(self, result, path):
        return AssistanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AssistanceChoreographyExecution(session, exec_id, path)

class AssistanceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Assistance
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AgencyCode(self, value):
        """
        Set the value of the AgencyCode input for this Choreo. ((conditional, string) The 4-character code for a specific governmental agency providing assistance.)
        """
        InputSet._set_input(self, 'AgencyCode', value)
    def set_AssistanceType(self, value):
        """
        Set the value of the AssistanceType input for this Choreo. ((conditional, string) The type of assistance provided. Valid values are: d = Direct Payments (specified and unrestricted), g = Grants and Cooperative Agreements, i = Insurance, l = Loans (direct and guaranteed), o = Other.)
        """
        InputSet._set_input(self, 'AssistanceType', value)
    def set_CFDAProgram(self, value):
        """
        Set the value of the CFDAProgram input for this Choreo. ((conditional, string) An ID for the governmental program.)
        """
        InputSet._set_input(self, 'CFDAProgram', value)
    def set_Detail(self, value):
        """
        Set the value of the Detail input for this Choreo. ((optional, string) Controls the level of detail of the output. Acceptable values: -1 (summary), 0 (low), 1 (medium), 2 (high), and 3 (extensive). Defaults to -1. See docs for more information.)
        """
        InputSet._set_input(self, 'Detail', value)
    def set_FederalID(self, value):
        """
        Set the value of the FederalID input for this Choreo. ((conditional, string) A Federal ID for the award.)
        """
        InputSet._set_input(self, 'FederalID', value)
    def set_FirstYearRange(self, value):
        """
        Set the value of the FirstYearRange input for this Choreo. ((conditional, integer) Specifies the first year in a range of years from 2000-2006; if used, must be used with LastYearRange and without FiscalYear.)
        """
        InputSet._set_input(self, 'FirstYearRange', value)
    def set_FiscalYear(self, value):
        """
        Set the value of the FiscalYear input for this Choreo. ((conditional, integer) Specifies a single year from 2000-2006; defaults to all years.)
        """
        InputSet._set_input(self, 'FiscalYear', value)
    def set_LastYearRange(self, value):
        """
        Set the value of the LastYearRange input for this Choreo. ((conditional, integer) Specifies the last year in a range of years from 2000-2006; if used, must be used with FirstYearRange and without FiscalYear.)
        """
        InputSet._set_input(self, 'LastYearRange', value)
    def set_MajAgency(self, value):
        """
        Set the value of the MajAgency input for this Choreo. ((conditional, string) The 2-character code for a major governmental agency providing assistance.)
        """
        InputSet._set_input(self, 'MajAgency', value)
    def set_MaxRecords(self, value):
        """
        Set the value of the MaxRecords input for this Choreo. ((optional, integer) Allows you to set the maximum number of records retrieved. Defaults to 100.)
        """
        InputSet._set_input(self, 'MaxRecords', value)
    def set_PrincipalPlaceCC(self, value):
        """
        Set the value of the PrincipalPlaceCC input for this Choreo. ((conditional, string) The city or county of the place of performance.)
        """
        InputSet._set_input(self, 'PrincipalPlaceCC', value)
    def set_PrincipalPlaceStateCode(self, value):
        """
        Set the value of the PrincipalPlaceStateCode input for this Choreo. ((conditional, string) The FIPS state code for the state of the place of performance.)
        """
        InputSet._set_input(self, 'PrincipalPlaceStateCode', value)
    def set_RecipientCityName(self, value):
        """
        Set the value of the RecipientCityName input for this Choreo. ((conditional, string) The city in the address of a recipient.)
        """
        InputSet._set_input(self, 'RecipientCityName', value)
    def set_RecipientCountyName(self, value):
        """
        Set the value of the RecipientCountyName input for this Choreo. ((conditional, string) The county in which a recipient is located.)
        """
        InputSet._set_input(self, 'RecipientCountyName', value)
    def set_RecipientDistrict(self, value):
        """
        Set the value of the RecipientDistrict input for this Choreo. ((conditional, string) The Congressional District in which the recipient is located, formatted with four characters.)
        """
        InputSet._set_input(self, 'RecipientDistrict', value)
    def set_RecipientName(self, value):
        """
        Set the value of the RecipientName input for this Choreo. ((conditional, string) The name of a recipient of assistance.)
        """
        InputSet._set_input(self, 'RecipientName', value)
    def set_RecipientStateCode(self, value):
        """
        Set the value of the RecipientStateCode input for this Choreo. ((conditional, string) The FIPS state code for the state in the address of a recipient.)
        """
        InputSet._set_input(self, 'RecipientStateCode', value)
    def set_RecipientType(self, value):
        """
        Set the value of the RecipientType input for this Choreo. ((conditional, string) The type of recipient. Valid values are: f = For Profits, g = Government,h = Higher Education, i = Individuals,n = Nonprofits, o = Other.)
        """
        InputSet._set_input(self, 'RecipientType', value)
    def set_RecipientZip(self, value):
        """
        Set the value of the RecipientZip input for this Choreo. ((conditional, integer) The ZIP code in the address of a recipient.)
        """
        InputSet._set_input(self, 'RecipientZip', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Determines how records are sorted. Valid values: r (contractor/recipient name), f (dollars of awards),g (major contracting agency), p (CFDA Program), d (date of award). Defaults to f.)
        """
        InputSet._set_input(self, 'SortBy', value)
    def set_TextSearch(self, value):
        """
        Set the value of the TextSearch input for this Choreo. ((conditional, string) A free text search on a description of the project.)
        """
        InputSet._set_input(self, 'TextSearch', value)

class AssistanceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Assistance Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FedSpending.org.)
        """
        return self._output.get('Response', None)

class AssistanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AssistanceResultSet(response, path)
