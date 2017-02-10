from django import forms
from django.utils.translation import ugettext as _


class CityForm(forms.ModelForm):
    shapefile = forms.FileField(required=False)
    shapefile_url = forms.URLField(required=False)

    class Meta:
        exclude = []
        labels = {
            'limited_ice_cooperation': _("Does the city have policy/legislation that limits or prohibits cooperation with ICE?"),
            'limited_ice_cooperation_short_answer': _("Please give brief explanation of the policies/practices."),
            'jails_honor_ice_detainers': _("Do city jails honor ICE detainers/notices? (Some smaller cities do not have city jails and rely on a county jail. If using county data, please specify.)"),
            'jails_honor_ice_detainers_short_answer': _("If yes, what are the stipulations?"),
            'participate_287g_program': _("Does the city participate in the 287(g) program?"),
            'participate_287g_program_short_answer': _("Source"),
            'provide_legal_representation': _("Does this jurisdiction provide undocumented immigrants with legal representation in immigration court?"),
            'provide_legal_representation_short_answer': _("Please list any stipulations attached, e.g. if it's only for minors, etc."),
            'city_services': _("Are people asked about their immigration status when applying for or accessing certain city services, like pools, library cards, local IDs or school registration?"),
            'city_services_short_answer': _("Please expand on services"),
            'separate_form_of_id': _("If drivers' licenses are not accessible, do cities provide their own form of ID?"),
            'separate_form_of_id_short_answer': _("What are the limitations to these IDs? E.g. Do police recognize them as an official ID? Can they buy alcohol with these IDs?"),
            'office_civic_engagement_immigrant_affairs': _("Does the city have an office dedicated to civic engagement and immigrant affairs? Ie. Citizen outreach, language access etc."),
            'office_civic_engagement_immigrant_affairs_short_answer': _("Brief description of the services provided"),
            'police_use_body_cameras': _("Does City PD use body cameras?"),
            'police_use_body_cameras_short_answer': _("Source"),
            'policies_against_profiling': _("Has local law enforcement adopted and implemented policies and directives against profiling based on actual or perceived sexual orientation, gender, gender identity, disability, immigration status, housing, HIV status, or age? Does it prohibit to use of race, religion, color, ethnicity, national origin, immigration status, gender, disability, sexual orientation, or gender identity as a factor in establishing reasonable suspicion or probable cause, exercising discretion to conduct a warrantless search or seek a search warrant?"),
            'policies_against_profiling_short_answer': _("Brief description of the services provided"),
            'other_policies_and_services': _("Are there any other policies/services in place that are not in this spreadsheet but make the city more welcoming to immigrants, people of color, the LGBTQ community and religious minorities?"),
            'local_effort': _("Is there already a known local effort to push for the city to become sanctuary or strengthen policies in place?"),
            'local_effort_short_answer': _("Source"),
            'igsa': _("Do city jails have an Intergovernmental Service Agreement (IGSA)?"),
            'igsa_short_answeer': _("Please explain"),
            'political_landscape': _("What is the political landscape of the city? Briefly power-map the flow of power.")
        }


class CountyForm(forms.ModelForm):
    shapefile = forms.FileField(required=False)
    shapefile_url = forms.URLField(required=False)

    class Meta:
        exclude = []
        labels = {
            'jails_honor_ice_detainers': _("Do county jails honor ice detainers?"),
            'jails_honor_ice_detainers_short_answer': _("If yes, what are the stipulations?"),
            'jails_prohibit_inquiries': _("Do county jails prohibit inquiries into immigration status and/or place of birth?"),
            'jails_prohibit_inquiries_short_answer': _("Source"),
            'ice_contracts': _("Does the county have a contract with ICE such as 287(g) or other programs in which there is entanglement with ICE like the Joint Terrorism Task Forces and the Organized Crime and Drug Enforcement Task Force?"),
            'ice_contracts_short_answer': _("Please explain"),
            'isga': _("Do county jails have an Intergovernmental Service Agreement (IGSA) or any other detention contracts?"),
            'isga_short_answer': _("Please explain."),
            'preventing_policies': _("Are there any policies in place put forth by the County Sheriff's office that prevent local police from acting as immigration agents?"),
            'preventing_policies_short_answer': _("Please explain."),
            'permitting_policies': _("Are there any policies in place put forth by the County Sheriff's office that permit local police from acting as immigration agents?"),
            'permitting_policies_short_answer': _("Please explain."),
            'other_policies_and_services': _("Are there any other policies/services in place that are mentioned here but make the county more welcoming/not welcoming to immigrants?"),
        }


class StateForm(forms.ModelForm):
    shapefile = forms.FileField(required=False)
    shapefile_url = forms.URLField(required=False)

    class Meta:
        exclude = []
        labels = {
            'limited_ice_cooperation': _("Does the state have policy/legislation that limits or prohibits cooperation with ICE?"),
            'limited_ice_cooperation_short_answer': _("Brief explanation of the policies/practices."),
            'ice_contracts': _("Does the State have a contracts with ICE such as 287(g) or other programs in which there is entanglement with ICE like the Joint Terrorism Task Forces and the Organized Crime and Drug Enforcement Task Force?"),
            'ice_contracts_short_answer': _("Please explain."),
            'isga': _("Do state jails have an Intergovernmental Service Agreement (IGSA)?"),
            'isga_short_answer': _("Please explain."),
            'provide_legal_representation': _("Does this jurisdiction provide undocumented immigrants with legal representation in immigration court?"),
            'provide_legal_representation_short_answer': _("Please list any stipulations attached, e.g. if it's only for minors, etc."),
            'drivers_license': _("Can undocumented immigrants get driver's licenses?"),
            'drivers_license_short_answer': _("Source"),
            'in_state_tuition': _("Can undocumented students access in-state tuition at public colleges?"),
            'in_state_tuition_short_answer': _("Source"),
            'barrier': _("Does immigration status act as a barrier in accessing state services?"),
            'barrier_short_answer': _("Source"),
            'policies_against_profiling': _("Has the state adopted and implemented policies and directives against profiling based on actual or perceived sexual orientation, gender, gender identity, disability, immigration status, housing, HIV status, or age? Does it prohibit to use of race, religion, color, ethnicity, national origin, immigration status, gender, disability, sexual orientation, or gender identity as a factor in establishing reasonable suspicion or probable cause, exercising discretion to conduct a warrantless search or seek a search warrant?"),
            'policies_against_profiling_short_answer': _("Brief explanation of the policies."),
            'other_policies_and_services': _("Are there any other policies/services in place that are not here, but make the state more welcoming to immigrants, people of color, the LGBTQ community and religious minorities?"),
            'local_effort': _("Is there already a known local effort to push for the state to become sanctuary or strengthen policies in place?"),
            'local_effort_short_answer': _("Source")
        }