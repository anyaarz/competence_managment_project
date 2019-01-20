from django.forms.models import modelformset_factory
from .models import Knowledge

SomeFormSet = modelformset_factory(Knowledge)

formset = SomeFormSet(queryset=Knowledge.objects.all())