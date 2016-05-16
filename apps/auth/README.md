# SSO ReverseProxy Service Based on [Apache-Auth-Mellon][mod_auth_mellon]

This service acting as a SSO proxy to backend services. It is basically a Apache server with [`mod_auth_mellon`][mod_auth_mellon] and mod_proxy.

Apache module [`mod_auth_mellon`][mod_auth_mellon] enables you to authenticate users of a web site against a SAML 2.0 enabled IdP. 
It can grant access to paths and provide attributes to other modules and applications.

## Service Configuration

### The backend service configurations should be put in:

		vols/apache2/sites-enabled/
		vold/apache2/conf-enabled/

### The SSL certs and keys should be in:

		vols/apache2/ssl/

### The auth_mellon conf should be in:

		vols/apache2/mellon

see [auth_mellon configuration spec][mod_auth_mellon] for more details

## Start Service

		fleetctl units/auth.service

## Docker Image
The docker image used by this service can be build with:

		docker build -t apache-mellon docker/

## Know Issus
### Bed SSO request caused by wrong timestamp
If Mac OS X laptop goes to sleep while the VM is running, when the laptop wakes up, all the clocks are wrong in the VM and in the containers. When this happened, SSO requests may have expired timestamps and the auth will fail.

Check VM time status:

	timedatectl status

Usually reload the VM will solve the problem:

	vagrant reload


[mod_auth_mellon]: https://github.com/UNINETT/mod_auth_mellon/blob/master/README
