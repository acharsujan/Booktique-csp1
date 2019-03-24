
from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.models import Book
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	all_posts = Book.objects.all()
	return render(request, "home.html",{'all_posts': all_posts})

def create_post(request):
	if not request.user.is_authenticated:
		return redirect("/")

	if request.method == "POST":
		form_title = request.POST['title']
		form_author = request.POST['author']
		form_description = request.POST['description']
		form_condn = request.POST['condn']
		form_email = request.POST['email']
		file = request.FILES['mycover']
		if file.name.endswith(".jpg") or file.name.endswith(".png") or file.name.endswith(".jpeg"):
			new_post = Book.objects.create(title=form_title, Author=form_author, description=form_description, condn=form_condn , email=form_email , cover=file)
            
			return redirect(f"/post/{new_post.id}/")

		else:

			return render(request,"create_post.html",{'msg':'Invalid file format'})


	return render(request, "create_post.html")


def post_page(request, post_id):
	if not request.user.is_authenticated:
		return redirect("/signin/")
	else:
		post = Book.objects.get(id = post_id)	
		return render(request, "page.html", {"post":post})	

def signin(request):
	if request.method == "POST":
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		print(password,password)
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			print("Im in")
			login (request,user)
			return redirect("/")
	return render(request,"login.html")


def signup(request):
	if request.method == "POST":
		fullname = request.POST.get('fullname', None)
		email = request.POST.get('email', None)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		print(password)

		user_exists = User.objects.filter(username=username).exists()
		if not user_exists:
			user = User.objects.create_user(
				username = username,
				password = password,
				email = email,
				first_name = fullname.split()[0],
				last_name = " ".join(fullname.split()[1:])
				)
			login(request, user)
			return redirect("/")
		else:
			return HttpResponse("User already exists. Try new username.")
	return  render(request,"signup.html")



def signout(request):
	logout(request)
	return redirect("/")
