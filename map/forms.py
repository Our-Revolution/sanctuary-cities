from django.forms import ModelForm
from .models import City, State


class CityForm(ModelForm):

    class Meta:
        exclude = []
        labels = {
            'limited_ice_cooperation': "Does the city have policy/legislation that limits or prohibits cooperation with ICE?",
            'limited_ice_cooperation_short_answer': "Please give brief explanation of the policies/practices.",
            'jails_honor_ice_detainers': "Do city jails honor ICE detainers/notices? (Some smaller cities do not have city jails and rely on a county jail. If using county data, please specify.)",
            'jails_honor_ice_detainers_short_answer': "If yes, what are the stipulations?",
            'participate_287g_program': "Does the city participate in the 287(g) program?",
            'participate_287g_program_short_answer': "Source",
            'provide_legal_representation': "Does this jurisdiction provide undocumented immigrants with legal representation in immigration court?",
            'provide_legal_representation_short_answer': "Please list any stipulations attached, e.g. if it's only for minors, etc.",
            'city_services': "Are people asked about their immigration status when applying for or accessing certain city services, like pools, library cards, local IDs or school registration?",
            'city_services_short_answer': "Please expand on services",
            'separate_form_of_id': "If drivers' licenses are not accessible, do cities provide their own form of ID?",
            'separate_form_of_id_short_answer': "What are the limitations to these IDs? E.g. Do police recognize them as an official ID? Can they buy alcohol with these IDs?",
            'office_civic_engagement_immigrant_affairs': "Does the city have an office dedicated to civic engagement and immigrant affairs? Ie. Citizen outreach, language access etc.",
            'office_civic_engagement_immigrant_affairs_short_answer': "Brief description of the services provided",
            'other_policies_and_services': "Are there any other policies/services in place that are not in this spreadsheet but make the city more welcoming to immigrants?"
        }