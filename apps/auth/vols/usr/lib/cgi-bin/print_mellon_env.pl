#!/usr/bin/env perl

print "Content-type: text/html\n\n";
print "<pre>\n";

foreach $key (sort keys(%ENV)) {
	if ($key =~ /MELLON/) {
  	  print "$key = $ENV{$key}<p>";
  	}
}
print "</pre>\n";
