from .forms import EmailListForm

def email_list_form(request):
    return{"email_list_form": EmailListForm}
