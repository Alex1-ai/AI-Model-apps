from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    # if request.method == "POST":
    #     Contact.objects.create(
    #         name=request.POST["name"],
    #         email=request.POST["email"],
    #         subject=request.POST["subject"],
    #         message=request.POST["message"],
    #     )
    #     messages.info(request, "Thanks, we’ll get back to you soon.")
    return render(request, "contact.html")


def about(request):
    # if request.method == "POST":
    #     Contact.objects.create(
    #         name=request.POST["name"],
    #         email=request.POST["email"],
    #         subject=request.POST["subject"],
    #         message=request.POST["message"],
    #     )
    #     messages.info(request, "Thanks, we’ll get back to you soon.")
    return render(request, "about.html")



def project(request):
    # if request.method == "POST":
    #     Contact.objects.create(
    #         name=request.POST["name"],
    #         email=request.POST["email"],
    #         subject=request.POST["subject"],
    #         message=request.POST["message"],
    #     )
    #     messages.info(request, "Thanks, we’ll get back to you soon.")
    return render(request, "project.html")


def service(request):
    # if request.method == "POST":
    #     Contact.objects.create(
    #         name=request.POST["name"],
    #         email=request.POST["email"],
    #         subject=request.POST["subject"],
    #         message=request.POST["message"],
    #     )
    #     messages.info(request, "Thanks, we’ll get back to you soon.")
    return render(request, "service.html")


# def uploadDog(request):
#     if request.method == "POST":
#         dog = Dog.objects.create(
#             name=request.POST["name"],
#             image=request.FILES["image"]
#         )

#         image_path = f"{settings.BASE_DIR}{dog.image.url}"
#         print("Image path:", image_path)
#         predicted_label = preprocess_image([image_path])[0]

#         return render(
#             request,
#             "dog-upload.html",
#             {
#                 "name": dog.name,
#                 "pics": dog.image.url,
#                 "predicted_label": predicted_label,
#             }
#         )

#     return render(request, "dog-upload.html")
