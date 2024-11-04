from django.forms.widgets import RadioSelect

class IconRadioSelect(RadioSelect):
    template_name = 'widgets/icon_radio_select.html'
    option_template_name = 'widgets/icon_radio_option.html'