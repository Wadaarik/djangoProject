from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .forms import ContactForm
from .models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def jewellery(request):
    return render(request, 'jewellery.html')


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_subject = request.POST.get('contact_subject', '')
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            c = Contact(nom=contact_name, mail=contact_email, titre=contact_subject, contenu=form_content)
            c.save()

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = {
            'contact_subject': contact_subject,
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "Nouvelle demande de contact",
            content,
            "Your website" + '',
            ['youremail@servor.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })

