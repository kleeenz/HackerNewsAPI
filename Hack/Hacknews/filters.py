from .models import Job
import django_filters


class UserFilter(django_filters.FilterSet):

    '''

    This is a module defined to handle filtering in the app
    to do this, i installed an external library
    called django filters. created a class that inherits from
    the Filterset class in the django-filter module
    in the class Meta, i defined the model on
    and the fields to  filter on

    '''

    type = django_filters.CharFilter(lookup_expr = 'icontains')

    class Meta:
        model = Job
        fields = ['type']
