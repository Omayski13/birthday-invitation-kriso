from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from birthday_invitation.invitation.forms import NameForm

invited_guests = [
            "кристиян",
            "радостина",
            "мартин",
            "зоя",
            "винченцо", "вини"
            "николета",
            "симеон", "мони"
            "благовест","веско"
            "ивайло", "иво"
            "владимир", "влади"
            "славина",
            "светослава","сиси"
            "иван",
            "цветомира", "цвети"
            "владислав", "влади"
            "габриела", "габи"
            "константин",
            "александър","сашо"
            "тодор",
            "огнян", "оги"
        ]


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = NameForm
    success_url = reverse_lazy('invitation')

    def form_valid(self, form):
        name = form.cleaned_data['name'].lower()

        if name in invited_guests:
            self.request.session['guest_name'] = name
            return super().form_valid(form)
        else:
            form.add_error('name', 'This name is not recognized.')
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)

        context['invalid_name_image'] = 'static/images/middle-finger.png'
        context['error_message'] = 'Сори, не си поканен'

        return self.render_to_response(context)


class InvitationView(TemplateView):
    template_name = 'invitation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        guest_name = self.request.session.get('guest_name')
        context['guest_name'] = guest_name

        return context
