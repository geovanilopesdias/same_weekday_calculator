# Same Weekday Calculator
**Abstract**: Given the month and year of an event (birthday, etc.) and a limit for calculation, the program outputs all the years when the same event date falls on the same weekday of the event date.

## Background
Where I actually live (a brazilian country city), there is a belief that the 50th marriage date falls on the same weekday of the marriage date. For example, if you married (or born, whatever) on 30/7/2021, which falls on a friday, your 50th marriage will also falls on a friday. (As I hereafter mentioned, it might be, but it depends of the event date month and the type of the event year relative to its nearest leap year).

I write down (on paper) some results to give her (my co-worker) a short and quick answer, but I soon realized that the problem wasn't too simple. As one may realize, if there wasn't any leap years, the "phenomenom" would occur every seven years. However, there are leap years, therefore the phenomenon occurs in a a different wat - an odd and ugly way to be more precise: according to four (of five) types of year, it will occur in r years, but the value of r depends of the later year the event occurs. But as the "weekday pushing" occurs from march on (dut to february 29th), the month of the event date also change the r values (and cicle!). These four year type are as follows:

**Leap**: if the phenomenon occurs in a leap year, it will occur again in 6 years, but only if the month of the event date isn't january nor february: in this case, we'll have it in 5 years.
**Later**: if the phenomenon occurs 1 year after a leap year (aka "Later Year"), it will occur again in 6 years anyways.
**Middle**: if the phenomenon occurs 2 years after a leap year (aka "Middle Year"), it will occur again in 11 years, but only if the month of the event date isn't january nor february: in this case, we'll have it in 6 years.
**Previous**: if the phenomenon occurs 3 years after a leap year (aka "Previous Year"), it will occur again in 5 years, but only if the month of the event date isn't january nor february: in this case, we'll have it in 11 years.

So, I figured a code out to list every year the phenomenon occurs, but I soon realize that math above is functional only within a span that does not pass through a fifth type of year: the _anomalous_ one. As it is known, any year divisible by 4 is a leap year (such as 2004, 2008), except if it's also divisible by 100 (such as 1900, 2100) - this later case is the anomalous year concept: a year that _should_ be "leap", but it isn't, according to the [current rule](https://en.wikipedia.org/wiki/Leap_year#Algorithm). Otherwise, years divisible by 400 is an exception of the exception: that's why 2000 was a leap year as weel as 2400 will be; as they're divisble by four, I didn't see a reason to classify them otherway.

## Methods
The first method I code was the simple one: useful in our contemporary span (1901-2099), without any anomalous years. (It is defined in the line 68 of the __init__.py file.) A simpler method, of course, would be necessary (or an within process into it) and so did I: type_analyseis (defined in line 1) returns the type of a given year (leap, later, middle, previous or anomalous).

This week (not full time) I worked on the toughest method: the one that includes anomalous years: what_years_complete (defined in line 110) currently passes all the tests I ran (one may check them out in the calc_aniv_semana_test.py file) except one, which I'm working on. I still doesn't include the algorithm for janury/february condition, besides I already have the data to do so [here](https://docs.google.com/spreadsheets/d/10XFWRVq-Zgk3sIlJqFLPOzkv4eW7MOtfiuUbr-rhNI4).

I'd appreciate any help or improvement one may suggest.

Thank you kindly for reading this far!
