#!/usr/bin/perl

use strict;
use warnings;

use CGI qw/url_param/;
use LWP::Simple;

my $states = get('https://marketplace.herculeze.com/cgi-bin/getStates.cgi');
my $q = url_param('q');
my $msg = $q eq "ERROR"   ? "There was an error creating the user" : 
          $q eq "SUCCESS" ? "User created":
          "";

print<<END;
Content-type:text/html


<html>
  <head>
    <title>Helloworld</title>
    <meta charset='utf-8'>

    <meta name="viewport" content="width=device-width, initial-scale=1">

  </head>

  <body>
    <p>$msg</p>

    <p><a href="/registration">Go back to Registration</a></p>
    <p><a href="/adminReport">Go to Admin Report</a></p>

  </body>
</html>
END
