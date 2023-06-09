"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^v(%%qv!*)=mt@rynq*m$h!um0q4y3s1k_3zspz%=so)u#0=&='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['79.143.180.14', 'localhost', '138.48.211.245']


# Application definition

INSTALLED_APPS = [
    'jet.dashboard', # for django-admin design
    'jet', # for django-admin design
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # Need for Rest API
    'rest_framework.authtoken', # for token generation
    'corsheaders', # for cors (API)
    'chatdata',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # for cors (API)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dqchatbot_db',
        'USER': 'dqchatbotuser',
        'PASSWORD': 'd72zdN9cjBBWU4YQ',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/files/'
MEDIA_ROOT = os.path.join(BASE_DIR,'files')

# To solve the problem of popup denied on django jet dashboard
X_FRAME_OPTIONS = 'SAMEORIGIN'
# for cors (API)
CORS_ORIGIN_ALLOW_ALL = True
DATASET_EXTENSIONS = ["csv","json","xls", "xlsx"]
NON_PROPRIO_DATASET_EXTENSIONS = ["csv","json"]
PROCESS_MIMETYPES = ["text/csv","application/json", "application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                     "text/plain"]
#https://opendatacommons.org/licenses/pddl/
#https://creativecommons.org/licenses
#https://help.figshare.com/article/what-is-the-most-appropriate-licence-for-my-data
LICENCES = ["CC0", "CC-BY", "CC BY-SA", "CC BY-ND", "CC BY-NC", "CC BY-NC-SA", "CC BY-NC-ND", "ODC-BY", "BSD 3-CLAUSE", "ODBL", "PDDL"]
OPEN_LICENSES = ["CC0", "CC-BY", "CC BY-SA", "CC BY-ND", "CC BY-NC", "CC BY-NC-SA", "CC BY-NC-ND", "ODC-BY", "BSD 3-CLAUSE", "ODBL", "PDDL"]
DEFAULT_SEPERATOR = ";"
MAX_UPLOAD_FILE = 2e8
SETTINGS_METADATA_DIMENSIONS = [
    {
        "id":"md1", "name":"Completeness","description":"Completeness", "weight": 1,
        "metrics": [
            {'id':'md1_1', 'name':'Percentage of not empty fields in metadata','description':'Indicates the percent of not empty fields in metadata', 'weight': 1,'formula':'100- (Number of empty fields * 100/Total number of fields)'}
        ]
    },
    {
        "id":"md2", "name":"Findability","description":"Findability", "weight": 1,
        "metrics": [
            {'id':'md2_1', 'name':'Keywords assigned','description':'Indicates if the keywords field is assigned ', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md2_2', 'name':'Categories assigned','description':'Indicates if the categories field is assigned', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md2_3', 'name':'Title given','description':'Indicates if the dataset title is set', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md2_4', 'name':'Description of data given','description':'Indicates if the dataset description is given', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md2_5', 'name':'Temporal information given','description':'Indicates if the date/period of the dataset belongs to is given', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md2_6', 'name':'Spatial information given','description':'Indicates if the information about the region the dataset belongs to is given', 'weight': 1,'formula':'100 if yes else 0'}
        ]
    },
    {
        "id":"md3", "name":"Accessibility","description":"Accessibility", "weight": 1,
        "metrics": [
            {'id':'md3_1', 'name':'Access URL accessible','description':'Indicates if the access URL of the dataset is accessible', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md3_2', 'name':'Download URL given','description':'Indicates if the download URL of the dataset is given', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md3_3', 'name':'Download URL accessible without registration','description':'Indicates if the download URL of the dataset is accessible', 'weight': 1,'formula':'100 if yes else 0'},
        ]
    },
    {
        "id":"md4", "name":"Conformance","description":"Conformance", "weight": 1,
        "metrics": [
            {'id':'md4_1', 'name':'Conformity of URLs','description':'The extent to which the values of access properties (HTTP, URLs) are valid', 'weight': 1,'formula':'Number of valid URL fields/Total URL fields'},
            {'id':'md4_2', 'name':'Conformity of date formats','description':'The extent to which the date fields are using a valid date format', 'weight': 1,'formula':'Number of valid date fields /Total number of date fields '},
            {'id':'md4_3', 'name':'Conformity of email addresses','description':'The extent to which the email fields are valid', 'weight': 1,'formula':'Number of valid email fields/Total number of email fields'},
            {'id':'md4_4', 'name':'DCAT-AP compliance of metadata','description':'Indicates if the metadata of the dataset is provided in DCAT format and  is compliant with DCAT-AP', 'weight': 1,'formula':'100 if yes else 0'}

        ]
    },
    {
        "id":"md5", "name":"Machine readability/ processability","description":"Machine readability/ processability", "weight": 1,
        "metrics": [
            {'id':'md5_1', 'name':'Processability of file format and media type','description':'Indicates if the file format and media type can be handled by automated processes (CSV, JSON, Excel accepted in this study)', 'weight': 1,'formula':'100 if yes else 0'}
        ]
    },
    {
        "id":"md6", "name":"Openess","description":"Openess", "weight": 1,
        "metrics": [
            {'id':'md6_1', 'name':'Openness of file format and media type','description':'Indicates if the file format and media type is in a non-proprietary format (CSV, JSON accepted in this study)', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md6_2', 'name':'License information given','description':'Indicates if the license information is given', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md6_3', 'name':'Openness of License','description':'Indicates if the license corresponds to one of the open Licenses listed in opendefinition.org', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md6_4', 'name':'Correctness of License','description':'Indicates if the License corresponds to one of the Licenses listed in opendefinition.org', 'weight': 1,'formula':''}

        ]
    },
    {
        "id":"md7", "name":"Timeliness","description":"Timeliness", "weight": 1,
        "metrics": [
            {'id':'md7_1', 'name':'Update information given','description':'Indicates if the frequency/periodicity of the dataset update is given', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md7_2', 'name':'Creation date given','description':'Indicates if the creation date is given', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md7_3', 'name':'Modification date given','description':'Indicates if the modified date is given', 'weight': 1,'formula':'100 if yes else 0'}
        ]
    },
    {
        "id":"md8", "name":"Accuracy","description":"Accuracy", "weight": 1,
        "metrics": [
            {'id':'md8_1', 'name':'File format accuracy','description':'Indicates if information given about file format can be compared with the actual file format of the resource', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md8_2', 'name':'Content size accuracy','description':'Indicates if information given about content size can be compared with the actual content size of the resource', 'weight': 1,'formula':'100 if yes else 0'}
        ]
    },
    {
        "id":"md9", "name":"Understandability","description":"Understandability", "weight": 1,
        "metrics": [
            {'id':'md9_1', 'name':'Percentage of columns with metadata','description':'Indicates the percentage of columns in a dataset that has associated descriptive metadata.', 'weight': 1,'formula':'Number of columns with metadata / Total number of columns '},
            {'id':'md9_2', 'name':'Percentage of columns in comprehensible format','description':'Indicates the percentage of columns in a dataset that is represented in a format that can be easily understood by the users and it is also machine-readable', 'weight': 1,'formula':'Number of columns in comprehensible format / Total number of columns'}
        ]
    },
    {
        "id":"md10", "name":"Credibility","description":"Credibility", "weight": 1,
        "metrics": [
            {'id':'md10_1', 'name':'Contact point given','description':'Indicates if the contact point of the dataset is given', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md10_2', 'name':'Dataset publisher given','description':'Indicates if the dataset publisher information is given', 'weight': 1,'formula':'100 if yes else 0'}
        ]
    },
    {
        "id":"md11", "name":"Uniqueness","description":"Uniqueness", "weight": 1,
        "metrics": [
            {'id':'md11_1', 'name':'Title is unique','description':'Indicates if the dataset title is unique', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md11_2', 'name':'Description is unique','description':'Indicates if the dataset description is unique', 'weight': 1,'formula':'100 if yes else 0'},
            {'id':'md11_3', 'name':'Identifier is unique','description':'Indicates if the dataset identifier is unique', 'weight': 1,'formula':'100 if yes else 0'}
        ]
    }
]
SETTINGS_DATA_DIMENSIONS = [
    {
        "id":"dt1", "name":"Completeness","description":"Completeness", "weight": 1,
        "metrics": [
            {'id':'dt1_1', 'name':'Percentage of complete cells','description':'A cell which is not empty or null is considered as complete', 'weight': 1,'formula':'Number of complete cells * 100 / Total number of cells '},
            {'id':'dt1_2', 'name':'Percentage of complete rows','description':'A row which all the cells are not empty or null is considered as complete', 'weight': 1,'formula':'Number of complete rows * 100 / Total number of rows'}
        ]
    },
    {
        "id":"dt2", "name":"Accuracy","description":"Accuracy", "weight": 1,
        "metrics": [
            {'id':'dt2_1', 'name':'Percentage of accurate cells','description':'Accurate cells are identified by their corresponding column type. Therefore, a cell is deemed accurate if its type matches the column type. For instance, if a column has a type of “email”, a cell with the value “abc” in that column would be regarded as inaccurate.', 'weight': 1,'formula':'Number of accurate cells / Total number of cells'}
        ]
    },
    {
        "id":"dt3", "name":"Uniqueness","description":"Uniqueness", "weight": 1,
        "metrics": [
            {'id':'dt3_1', 'name':'Percentage of unique rows','description':'Indicates the percentage of unique rows in the dataset ', 'weight': 1,'formula':'Number of unique rows / Total number of rows'}
        ]
    },
]
