import django_filters
from .models import Profile
from django import forms


class ProfileFilter(django_filters.FilterSet):

    rock = django_filters.MultipleChoiceFilter(choices=Profile.ROCK_CHOICES, required=False,
                                                          widget=forms.CheckboxSelectMultiple(),
                                                         method='rock_filter'
                                                         )

    metal = django_filters.MultipleChoiceFilter(choices=Profile.METAL_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='metal_filter'
                                               )

    punk = django_filters.MultipleChoiceFilter(choices=Profile.PUNK_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='punk_filter'
                                               )

    pop = django_filters.MultipleChoiceFilter(choices=Profile.POP_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='pop_filter'
                                               )

    blues = django_filters.MultipleChoiceFilter(choices=Profile.BLUES_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='blues_filter'
                                               )

    jazz = django_filters.MultipleChoiceFilter(choices=Profile.JAZZ_CHOICES, required=False,
                                               conjoined=False, widget=forms.CheckboxSelectMultiple(),
                                               method='jazz_filter'
                                               )

    funk = django_filters.MultipleChoiceFilter(choices=Profile.FUNK_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='funk_filter'
                                               )

    soul = django_filters.MultipleChoiceFilter(choices=Profile.SOUL_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='soul_filter'
                                               )

    electronic = django_filters.MultipleChoiceFilter(choices=Profile.ELECTRONIC_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='electronic_filter'
                                               )

    hiphop_rap = django_filters.MultipleChoiceFilter(choices=Profile.HIP_HOP_RAP_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='hiphop_rap_filter'
                                               )

    greek = django_filters.MultipleChoiceFilter(choices=Profile.GREEK_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='greek_filter'
                                               )

    other = django_filters.MultipleChoiceFilter(choices=Profile.OTHER_CHOICES, required=False,
                                                widget=forms.CheckboxSelectMultiple(),
                                               method='other_filter'
                                               )

    music_nature = django_filters.MultipleChoiceFilter(choices=Profile.MUSIC_NATURE,  required=False,
                                                        widget=forms.CheckboxSelectMultiple(),
                                                       method='narure_filter'
                                                       )

    user__username = django_filters.CharFilter(label='Username', lookup_expr="contains")

    class Meta:
        model = Profile
        fields = ['rock', 'music_nature','metal', 'punk', 'pop', 'blues', 'jazz', 'funk', 'soul',
                  'electronic', 'hiphop_rap', 'greek', 'other', 'music_nature', ]

    def narure_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(music_nature=value)

    def rock_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(rock=value)

    def other_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(other=value)

    def greek_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(greek=value)

    def hiphop_rap_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(hiphop_rap=value)

    def electronic_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(electronic=value)

    def soul_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(soul=value)

    def funk_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(funk=value)

    def jazz_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(jazz=value)

    def blues_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(blues=value)

    def pop_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(pop=value)

    def punk_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(punk=value)

    def metal_filter(self, queryset, name, value):
        print(value)
        choice = value
        return queryset.filter(metal=value)







