import calendar
from datetime import date

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Action


class MonthDueFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('due date')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'month_due'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        months = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
        }
        today = date.today()
        current_month = today.month
        current_year = today.year
        month_indexes = range(current_month, current_month + 12)

        for index in month_indexes:
            index_ = index if index == 12 else index % 12
            year = current_year if index <= 12 else current_year + 1
            lookup = (index_, u'{} {}'.format(months[index_], year))
            yield lookup

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        query_month = self.value()
        if query_month is None:
            return queryset

        query_month = int(query_month)

        today = date.today()
        current_month = today.month
        query_year = today.year if query_month >= current_month else today.year + 1

        begin_date = date(query_year, query_month, 1)
        last_day = calendar.monthrange(query_year, query_month)[1]
        end_date = date(query_year, query_month, last_day)

        return queryset.filter(due__range=(begin_date, end_date))


class ActionAdmin(admin.ModelAdmin):
    list_filter = (MonthDueFilter, 'assigned_to', 'completed', 'deleted')
    date_hierarchy = 'due'
    list_display = ('name', 'assigned_to', 'due', 'completed')
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        (None, {'fields': ('name', 'slug', 'description')}),
        ('Details', {'fields': ('assigned_to', 'due', 'completed', 'deleted')}),
    )

    list_editable = ('assigned_to', 'due', 'completed')


admin.site.register(Action, ActionAdmin)
