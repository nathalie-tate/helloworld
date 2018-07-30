#!/usr/bin/perl

use strict;
use warnings;
use DBI;

my $dbh = DBI->connect("dbi:mysql:", "helloworld","helloworld");
$dbh->do("use helloworld"); 

print<<END;
Content-type:text/html


<html>
  <head>
    <title>Helloworld</title>
    <meta charset='utf-8'>

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      tr:nth-child(even) {background-color: #f2f2f2;}

      th{
        background-color: #4CAF50;
        color: white;
      }
    </style> 
  </head>

  <body>
    <table>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Address 1</th>
        <th>Address 2</th>
        <th>City</th>
        <th>State</th>
        <th>Zip</th>
        <th>Country</th>
        <th>Date</th>
      </tr>
END

  my $query = $dbh->prepare("SELECT * FROM User ORDER BY timestamp DESC;");
  $query->execute();
  while(@_ = $query->fetchrow_array())
  {
    print"<tr>";
    print "<td>$_</td>" for @_[0..7];
    print "<td>";
    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst);
                                           
    ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($_[8]);

    ++$mon;
    $year+=1900;

    printf("%04d-%02d-%02d %02d:%02d:%02d", $year,$mon,$mday,$hour,$min,$sec);
    print "</td>";
    print"</tr>";
  }

print<<END;
    </table>
  </body>
</html>
END
