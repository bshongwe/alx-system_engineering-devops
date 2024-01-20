#!/usr/bin/pup
# Install a specific version of flask (2.1.0)
class { 'python':
  pip_provider => 'pip3',
}

python::pip { 'flask':
  ensure => '2.1.0',
  pkgname => 'flask',
  pip_provider => 'pip3',
}
