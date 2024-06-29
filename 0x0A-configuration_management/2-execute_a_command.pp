# Using Puppet, create a manifest that
#kills a process named killmenow.

exec { 'kill-process':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
  timeout => 0,
}
