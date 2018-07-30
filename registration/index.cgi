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

    <form id='form' action='/cgi-bin/processForm.cgi' method='POST' onsubmit='validate()'>
            <label for='fName'>First Name: <input name='fName' id='fName' required></label><br />
            <label for='lName'>Last Name: <input name='lName' id='fName' required></label><br />
            <label for='addr1'>Address Line One: <input name='addr1' id='addr1' required></label><br />
            <label for='addr2'>Address Line Two: <input name='addr2' id='addr2'></label><br />
            <label for='city'>City: <input name='city' id='city' required></label><br />
            <label for='state'>State: <select name='state' id='state' required>$states</select></label><br />
            <label for='zip'>Zip Code (or Zip +4): <input name='zip' id='zip' required pattern="\\d{5}([- ]?\\d{4})?" title='Please enter a valid zip code'></label><br />
            <label for='country'>Country: <select name='country' id='country'><option value='US'>US</option></select><br />
            <input type='submit' value='Submit'><br />
    </form>

  </body>
</html>
END
