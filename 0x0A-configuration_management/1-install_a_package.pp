#!/usr/bin/pup
# Install a specific version of flask (2.1.0)
packge { 'Flask':
  ensure => '2.1.0',
  provider => 'pip3',
}

# Install Wekzeug v2.1.1
package { 'Werkzeug':
  ensure => '2.1.1',
  provider => 'pip3',
  require => Package['Flask'],
}
