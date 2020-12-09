AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]




# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

SOCIALACCOUNT_PROVIDERS = {
    "apple": {
            "APP": {
                # Your service identifier.
                "client_id": "your.service.id",

                # The Key ID (visible in the "View Key Details" page).
                "secret": "KEYID",

                 # Member ID/App ID Prefix -- you can find it below your name
                 # at the top right corner of the page, or it’s your App ID
                 # Prefix in your App ID.
                "key": "MEMAPPIDPREFIX",

                # The certificate you downloaded when generating the key.
                "certificate_key": """-----BEGIN PRIVATE KEY-----
    s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr
    3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3
    c3ts3cr3t
    -----END PRIVATE KEY-----
    """
            }
        },

    "github": {
        # For each provider, you can choose whether or not the
        # email address(es) retrieved from the provider are to be
        # interpreted as verified.
        "VERIFIED_EMAIL": True
    },
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": "123",
            "secret": "456",
            "key": ""
        },
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}