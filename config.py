# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Suppress warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Set secret key
SECRET_KEY = b'\x82\xbf\x18\x9e\x91o\xc4\xbb\xd8b\xe7\x18\xab\x82\x1d'
