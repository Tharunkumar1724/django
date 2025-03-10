from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_name"] = "Tharun Kumar"
        context["video_title"] = "My Awesome Video"
        context["video_url"] = "/media/videos/myvideo.mp4"  # Ensure your video is in media/videos/
        context["image_title"] = "A Beautiful Image"
        context["image_url"] = "images/myimage.jpeg"
        context["form"] = ContactForm()  # Ensure your image is in static/images/
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form submitted successfully!")
            print("Name:", form.cleaned_data['name'])
            print("Email:", form.cleaned_data['email'])
            print("Message:", form.cleaned_data['message'])
            return self.get(request, *args, **kwargs)  # Re-render with context
        else:
            return render(request, self.template_name, {"form": form})