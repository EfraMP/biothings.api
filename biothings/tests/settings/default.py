###################################################################################
# Nosetest settings
###################################################################################

# This is the name of the environment variable to load for testing
HOST_ENVAR_NAME = ''
# This is the URL of the production server, if the above envar can't be loaded, nosetest defaults to this
NOSETEST_DEFAULT_URL = "http://{% base_url %}"

###################################################################################
# Nosetests used in tests.py, fill these in with IDs/queries.
###################################################################################

# This is the test for fields in the {% annotation_endpoint %} object.  You should pick an ID
# with a representative set of root level annotations associated with it.
ANNOTATION_OBJECT_ID = ''
# This is the list of expected keys that the JSON object returned by the ID above
ANNOTATION_OBJECT_EXPECTED_ATTRIBUTE_LIST = []

# -----------------------------------------------------------------------------------

# This is a list of IDs (& options) to test a GET to the /{% annotation_endpoint %} endpoint
ANNOTATION_GET_IDS = []

# -----------------------------------------------------------------------------------

# This is a list of dictionaries to test a POST to the /{% annotation_endpoint %} endpoint

ANNOTATION_POST_DATA = []

# -----------------------------------------------------------------------------------

# This is a list of query strings (& options to test a GET to the /{% query_endpoint %} endpoint
QUERY_GETS = []

# -----------------------------------------------------------------------------------

# This is a list of dictionaries to test a POST to the /{% query_endpoint %} endpoint
QUERY_POST_DATA = []

# -----------------------------------------------------------------------------------

# This is a sample ID that will have non-ascii characters injected into it to test non-ascii 
# handling on the /{% annotation_endpoint %} endpoint
ANNOTATION_NON_ASCII_ID = ''

# -----------------------------------------------------------------------------------

# This is a sample query that will have non-ascii characters injected into it to test
# non-ascii handling on the /{% query_endpoint %} endpoint
QUERY_NON_ASCII = ''

# -----------------------------------------------------------------------------------

# This is a sample query to test the callback function
QUERY_CALLBACK_TEST = ''

# -----------------------------------------------------------------------------------

# This is a sample query to test the query size cap.  This query should be one that has more than 1000 total hits.
QUERY_SIZE_TEST = ''

