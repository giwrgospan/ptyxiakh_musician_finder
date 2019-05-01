import django_filters
from .models import Profile
from django import forms


class ProfileFilter(django_filters.FilterSet):

    music_category = django_filters.MultipleChoiceFilter(choices=Profile.MUSIC_CHOICES, required=False,
                                                         conjoined=True, widget=forms.CheckboxSelectMultiple(),
                                                         method='filter_list'
                                                         )

    music_nature = django_filters.MultipleChoiceFilter(choices=Profile.MUSIC_NATURE,  required=False,
                                                       conjoined=True, widget=forms.CheckboxSelectMultiple(),
                                                       method='filter_list'
                                                       )

    user__username = django_filters.CharFilter(label='Username', lookup_expr="contains")

    class Meta:
        model = Profile
        fields = ['music_category', 'music_nature']

    def filter_list(self, queryset, name, value):
         choice = value
         return queryset.filter(choice)



