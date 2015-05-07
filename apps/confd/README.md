# confd

`confd` is a lightweight configuration management tool focused on:

* keeping local configuration files up-to-date using data stored in [etcd](https://github.com/coreos/etcd),
  [consul](http://consul.io), or env vars and processing [template resources](docs/template-resources.md).
* reloading applications to pick up new config file changes

See https://github.com/kelseyhightower/confd