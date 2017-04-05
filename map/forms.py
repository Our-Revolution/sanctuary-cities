from django import forms
from django.utils.translation import ugettext as _


class CityForm(forms.ModelForm):
    shapefile = forms.FileField(required=False)
    shapefile_url = forms.URLField(required=False)

    class Meta:
        exclude = []
        labels = {
            'limited_ice_cooperation': _("Does the city have policy/legislation that limits or prohibits cooperation with ICE?"),
            'limited_ice_cooperation_short_answer': _("Please provide a short description of the city's policy/legislation."),
            'limited_ice_cooperation_source': _("Source:"),
            'jails_honor_ice_detainers': _("Do city jails honor ICE detainers/notices? (Some smaller cities do not have city jails and rely on a county jail. If using county data, please specify.)"),
            'jails_honor_ice_detainers_short_answer': _("Please provide a short description of the city's policy. If yes, what are the stipulations?"),
            'jails_honor_ice_detainers_source':_("Source:"),
            'participate_287g_program': _("Does the city participate in the 287(g) program?"),
            'participate_287g_program_short_answer': _("Please provide a short description of the city's involvement with the 287(g) program."),
            'participate_287g_program_source': _("Source:"),
            'provide_legal_representation': _("Does this jurisdiction provide undocumented immigrants with legal representation in immigration court?"),
            'provide_legal_representation_short_answer': _("Please provide a short description of the city's legal representation policies, including any stipulations attached, e.g. if it's only for minors, etc."),
            'provide_legal_representation_source': _("Source:"),
            'city_services': _("Are people asked about their immigration status when applying for or accessing certain city services, like pools, library cards, local IDs or school registration?"),
            'city_services_short_answer': _("Please provide a short description of the city's policies about disclosing immigration status to use city services."),
            'city_services_source': _("Source:"),
            'separate_form_of_id': _("If drivers' licenses are not accessible, do cities provide their own form of ID?"),
            'separate_form_of_id_short_answer': _("Please provide a short description of the city's policies. What are the limitations to these IDs? E.g. Do police recognize them as an official ID?"),
            'separate_form_of_id_source': _("Source:"),
            'police_use_body_cameras': _("Does City PD use body cameras?"),
            'police_use_body_cameras_short_answer':_("Please provide a short description of the city's body camera policies."),
            'police_use_body_cameras_source': _("Source"),
            'other_policies_and_services': _("Are there any other policies/services in place that are not in this spreadsheet but make the city more welcoming to immigrants, people of color, the LGBTQ community and religious minorities?"),
            'other_policies_short_answer': _("Please provide a short description of the city's other policeis and services."),
            'other_policies_source': _("Source:"),
            'local_effort': _("Is there already a known local effort to push for the city to become sanctuary or strengthen policies in place?"),
            'local_effort_short_answer': _("Please provide a short description of the primary local effort."),
            'local_effort_link': _("Link to send people to get involved with the primary local effort."),
            'resources':_("Please list any other resources or local efforts to be displayed under a resources section to users."),
            'isga': _("Do city jails have an Intergovernmental Service Agreement (IGSA)?"),
            'isga_source': _("Source:"),
            # 'political_landscape': _("What is the political landscape of the city? Briefly power-map the flow of power."),
            'city_council_contact_info': _("List city council contact information: Name, Title (District 1/ At Large/ Etc), Phone, Email")
        }


class CountyForm(forms.ModelForm):
    shapefile = forms.FileField(required=False)
    shapefile_url = forms.URLField(required=False)

    class Meta:
        exclude = []
        labels = {
            'jails_honor_ice_detainers': _("Do county jails honor ice detainers?"),
            'jails_honor_ice_detainers_short_answer': _("If yes, what are the stipulations?"),
            'jails_honor_ice_detainers_source': _("Source:"),
            'jails_prohibit_inquiries': _("Do county jails prohibit inquiries into immigration status and/or place of birth?"),
            'jails_prohibit_inquiries_short_answer': _("Please provide a short description of the city's policy/legislation."),
            'jails_prohibit_inquiries_source': _("Source"),
            'ice_contracts': _("Does the county have a contract with ICE such as 287(g) or other programs in which there is entanglement with ICE like the Joint Terrorism Task Forces and the Organized Crime and Drug Enforcement Task Force?"),
            'ice_contracts_short_answer': _("Please explain"),
            'ice_contracts_source': _("Source:"),
            'isga': _("Do county jails have an Intergovernmental Service Agreement (IGSA) or any other detention contracts?"),
            'isga_short_answer': _("Please explain."),
            'isga_source': _("Source:"),
            'preventing_policies': _("Are there any policies in place put forth by the County Sheriff's office that prevent local police from acting as immigration agents?"),
            'preventing_policies_short_answer': _("Please explain."),
            'preventing_policies_source': _("Source:"),
            'permitting_policies': _("Are there any policies in place put forth by the County Sheriff's office that permit local police from acting as immigration agents?"),
            'permitting_policies_short_answer': _("Please explain."),
            'permitting_policies_source': _("Source:"),
            'other_policies_and_services': _("Are there any other policies/services in place that are mentioned here but make the county more welcoming/not welcoming to immigrants?"),
            'other_policies_and_source': _("Source:"),
            'local_effort': _("Is there already a known local effort to push for the county to become sanctuary or strengthen policies in place?"),
            'local_effort_short_answer': _("Please provide a short description of the primary local effort."),
            'local_effort_link': _("Link to send people to get involved with the primary local effort."),
            'resources':_("Please list any other resources or local efforts to be displayed under a resources section to users.")
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
