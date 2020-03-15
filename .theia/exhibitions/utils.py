from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
import datetime
from .models import Exhibitions


class ExhibitionsCalendar(HTMLCalendar):
    def __init__(self, exhibitions=None):
        super(ExhibitionsCalendar, self).__init__()
        self.exhibitions = exhibitions

    def formatday(self, day, weekday, events):
        """
        Return a day as a table cell.
        """
        exhibitions_from_day = exhibitions.filter(day__day=day)
        exhibitions_html = "<ul>"
        for exhibitions in exhibitions_from_day:
            exhibitions_html += exhibitions.get_absolute_url() + "<br>"
        exhibitions_html += "</ul>"

        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, exhibitions_html)

    def formatweek(self, theweek, exhibitions):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, exhibitions) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """

        exhibitions = Exhibitions.objects.filter(day__month=themonth)

        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, exhibitions))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)