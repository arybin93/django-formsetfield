from django import forms
from .widgets import FormSetWidget


class FormSetField(forms.Field):

    widget = FormSetWidget

    def __init__(self, formset_class, template=None, formset_class_attrs=None, context=None, *args, **kwargs):
        self.formset_class = formset_class
        self._formset_class_attrs = formset_class_attrs or {}
        self.template = template or 'formsetfield/formsetfield.html'
        self._template_context = context or {}
        super(FormSetField, self).__init__(*args, **kwargs)

    @property
    def formset_class_attrs(self):
        return self._formset_class_attrs

    @formset_class_attrs.setter
    def formset_class_attrs(self, value):
        self._formset_class_attrs = value
        self.widget.attrs['formset_class_attrs'] = value

    @property
    def template_context(self):
        return self._template_context

    @template_context.setter
    def template_context(self, value):
        self._template_context = value
        self.widget.attrs['template_context'] = value

    def validate(self, value):
        if not value.is_valid():
            raise forms.ValidationError(self.error_messages['invalid'])

    def clean(self, value):
        return super(FormSetField, self).clean(value).cleaned_data

    def widget_attrs(self, widget):
        return {'formset_class': self.formset_class, 'template': self.template, 'formset_class_attrs': self.formset_class_attrs}
