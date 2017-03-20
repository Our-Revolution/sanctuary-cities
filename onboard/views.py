from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import OnboardForm
import os, requests



class NextStepsView(TemplateView):
    template_name = "next_steps.html"



class OnboardView(FormView):
    template_name = 'onboard_form.html'
    form_class = OnboardForm
    success_url = '/research/get-started/next-steps'

    def form_valid(self, form):

        first_name, last_name = ["", ""]
        full_name = form.cleaned_data['full_name']

        if full_name and ' ' in full_name:
            first_name, last_name = full_name.split(' ', 1)
        elif full_name:
            first_name = full_name

        # todo: handle if they already have an account but aren't logged in.

        if not self.request.user.is_authenticated():

            # create user.
            base_username = candidate_username = form.cleaned_data['email'].split('@')[0]
            counter = 0
            
            while User.objects.filter(username=candidate_username).count() > 0:
                counter += 1
                candidate_username = base_username + str(counter)

            password = "sanctuary"

            user = User.objects.create(username=candidate_username, first_name=first_name, last_name=last_name, email=form.cleaned_data['email'])
            user.set_password(password)
            user.save()

            # todo: add as a Staff

            messages.success(self.request, mark_safe("Your account has been created &mdash; your username is <strong>%s</strong> and your password is <strong>%s</strong> ;) Please store these somewhere safe!" % (candidate_username, password)))

            # login
            login(self.request, user)

        # invite to Slack

        params = ["token=%s" % os.environ.get('SLACK_API_KEY', None), "email=%s" % form.cleaned_data['email']]

        if first_name:
            params.append("first_name=%s" % first_name)

        if last_name:
            params.append("last_name=%s" % last_name)

        params.append("channels=C3X6H70L9")

        req = requests.post('https://slack.com/api/users.admin.invite?%s' % '&'.join(params))

        return super(OnboardView, self).form_valid(form)
