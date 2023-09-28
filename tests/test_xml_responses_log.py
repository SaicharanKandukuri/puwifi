import re


def response_log(response: str) -> str:
    """Function for parsing the xml response. Note that the xml_response strings are hardcoded here.

    Args:
        response (str): The xml reponse passed as a string.

    Returns:
        str: The parsed string from the xml response.
    """

    pattern = r'(\[CDATA\[(.*?)\]\])'
    patterns_matched = re.findall(pattern=pattern, string=response)
    return patterns_matched[1][1]


def test_login_response_parse():
    """Test function for parsing the login xml response.
    Note that the xml_response strings are hardcoded here."""
    login_response = ("?><requestresponse><status><![CDATA[LIVE]]"
                      "></status><message><![CDATA[You are signed in as username "
                      "Systems Support Cell, Parul University.]]></message><logoutmessage> "
                      "<![CDATA[You have successfully logged off]]></logoutmessage><state> "
                      "<![CDATA[]]></state></requestresponse> \n', 200] "
                      )

    assert response_log(
        login_response) == ('You are signed in as username '
                            'Systems Support Cell, Parul University.')


def test_logout_response_parse():
    """Test function for parsing the login xml response. 
    Note that the xml_response strings are hardcoded here."""
    logout_response = ("<?xml version='1.0' ?><requestresponse><status> "
                       "<![CDATA[LOGIN]]></status><message><![CDATA[You&#39;ve signed out. "
                       "Systems Support Cell, Parul puwifi.py:265 University.]]></message> "
                       "</requestresponse>\n")

    assert response_log(
        logout_response) == ('You&#39;ve signed out. Systems Support Cell, '
                             'Parul puwifi.py:265 University.')
