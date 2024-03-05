# Fixes bad `phpp` extensions to `php` in WordPress file `wp-settings.php`
# Fix 505 Apache error

exec { 'fix-wordpress':
  command => 'sudo sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
