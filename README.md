_This is one of the steps in the Truss interview process. If you've
stumbled upon this repository and are interested in a career with
Truss, [check out our jobs page](https://truss.works/jobs)._

# Truss Software Engineering Interview

## Introduction and expectations

Hi there! Please complete the problem described below to the best of
your ability, using the tools you're most comfortable with. Assume
you're sending your submission in for code review from peers;
we'll be talking about your submission in your interview in that
context.

We expect this to take less than 4 hours of actual coding time. Please
submit a working but incomplete solution instead of spending more time
on it. We're also aware that getting after-hours coding time can be
challenging; we'd like a submission within a week and if you need more
time please let us know.

If you have any questions, please contact hiring@truss.works; we're
happy to help if you're not sure what we're asking for or if you have
questions.

## How to submit your response

Please send hiring@truss.works a link to a public git repository
(Github is fine) that contains your code and a README.md that tells us
how to build and run it. Your code will be run on either macOS 10.15
or Ubuntu 16.04 LTS, your choice.

## The problem: CSV normalization

Please write a tool that reads a CSV formatted file on `stdin` and
emits a normalized CSV formatted file on `stdout`. For example, if
your program was named `normalizer` we would test your code on the
command line like this:

```sh
./normalizer < sample.csv > output.csv
```

Normalized, in this case, means:

* The entire CSV is in the UTF-8 character set.
* The `Timestamp` column should be formatted in ISO-8601 format.
* The `Timestamp` column should be assumed to be in US/Pacific time;
  please convert it to US/Eastern.
* All `ZIP` codes should be formatted as 5 digits. If there are less
  than 5 digits, assume 0 as the prefix.
* The `FullName` column should be converted to uppercase. There will be
  non-English names.
* The `Address` column should be passed through as is, except for
  Unicode validation. Please note there are commas in the Address
  field; your CSV parsing will need to take that into account. Commas
  will only be present inside a quoted string.
* The `FooDuration` and `BarDuration` columns are in HH:MM:SS.MS
  format (where MS is milliseconds); please convert them to the
  total number of seconds expressed in floating point format.
  You should not round the result.
* The `TotalDuration` column is filled with garbage data. For each
  row, please replace the value of `TotalDuration` with the sum of
  `FooDuration` and `BarDuration`.
* The `Notes` column is free form text input by end-users; please do
  not perform any transformations on this column. If there are invalid
  UTF-8 characters, please replace them with the Unicode Replacement
  Character.

You can assume that the input document is in UTF-8 and that any times
that are missing timezone information are in US/Pacific. If a
character is invalid, please replace it with the Unicode Replacement
Character. If that replacement makes data invalid (for example,
because it turns a date field into something unparseable), print a
warning to `stderr` and drop the row from your output.

You can assume that the sample data we provide will contain all date
and time format variants you will need to handle.

## My Personal Notes

This project was super fun! I did not manage to meet all the requirements in the time alloted, but I have a runnable state and the TODOs in my code explain the missing work. It's been a while since I worked with Python, but I couldn't think of a better language for simple csv handling.

I made a few assumptions:
* That Uppercase Names meant the whole string was uppercase, mostly because I am not familiar with capitalization standards in other cultures and didn't want to offend.
* That adding a timezone indicator would be acceptable. I could just manipulated the values but I thought it would be more complete with DST if I added it as an obj

With more time:
* better met the file in and file out requirements
* I would have finished up the UTF-8 formatting and removing rows that are not valid. (I have some of it written, but it doesn't quite do what I want)
* I would have created more data to better test
* Cleaned up my code for flow and readability
* Looked into a neater solution for file reading/writing and UTF-8 handling. 
* Dedicated more time to ask questions and do research before starting, however, I had to work around real-life commitments, and didn't want to send midnight emails.

How To Run This Guy:
This assumes you know how to run Python 3 specifically on your machine.
This assumes you have already pulled the files on to your computer.
Please install the pytz library before running this program, which can be done through command line. This user used 'sudo pip3 install pytz' and a restart, however your exact install may vary.
* Navigate via command line to the file location
* In the command line type 'truss_csv_normalization.py sample.csv output.csv' and 'truss_csv_normalization.py sample-with-broken-utf8.csv output1.csv' where output.csv and output1.csv can be changed to whatever you would like to name the file.

This was tested on Mac 10.15 Catalina, and Windows 10 Home (which wasn't required but it ran, and I was excited, so...)