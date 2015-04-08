#SSO ReverseProxy Service Based on [Apache-Auth-Mellon][mod_auth_mellon]

This service acting as a SSO proxy to backend services. All backend services should be defined in:

##SSO Proxy Configuration

### The backend services should be defined in:

		vols/etc/apache2/sites-enabled/

### The SSL certs and keys should be in:
	
		vols/etc/ssl/

### The auth_mellon conf should be in:

		vols/etc/auth_mellow

##Start Service

	fleetctl units/auth.service


[mod_auth_mellon]: https://github.com/UNINETT/mod_auth_mellon/