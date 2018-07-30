#!/usr/bin/perl

use strict;
use warnings;

use DBI;
use CGI qw/param redirect/;
use CGI::Carp qw/fatalsToBrowser/;

my $dbh = DBI->connect("dbi:mysql:", "helloworld","helloworld");
$dbh->do("use helloworld");

my $addr2   = param('addr2');
my $state   = param('state');
my $zip     = param('zip');
my $country = param('country');

redir() unless my $fName   = param('fName');
redir() unless my $lName   = param('lName');
redir() unless my $addr1   = param('addr1');
redir() unless my $city    = param('city');

redir() unless $state =~ /[a-z]{2}/i;
redir() unless $country =~ /US/i;

if($zip =~ /^\d{5}$/)
{}
elsif($zip =~ /^(\d{5})\D(\d{4})$/)
{
  $zip = "$1-$2";
}
elsif($zip =~ /^(\d{5})(\d{4})$/)
{
  $zip = "$1-$2";
}
else
{
  redir();
}

$dbh->do(qq[INSERT INTO User(fName,lName,addr1,addr2,city,state,zip,country,timestamp) values(?,?,?,?,?,?,?,?,?)],
  undef,$fName,$lName,$addr1,$addr2//"",$city,$state,$zip,$country,time);

redir(1);

sub redir
{
  if(shift)
  {
    print redirect("/registration/confirm?q=SUCCESS");
  }
  else
  {
    print redirect("/registration/confirm?q=ERROR");
  }
}
