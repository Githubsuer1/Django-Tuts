from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import createPostForm, editPostForm
# Create your views here.



# 1. Home view, user will be redirected to here after login immediately 

@login_required
def home(request):
    return render(request,'article/home.html')


# 2. create_post view, user can create articles using this function

@login_required
def create_post(request):
    if request.method == "POST":
        # creating form object
        form = createPostForm(request.POST,request.FILES)
        # if form is valid then go next
        if form.is_valid():
            # create an object of form that will not be saved immediately.
            article = form.save(commit=False)
            # modifying the attributes of article 
            article.author = request.user 
            # saving the article in database
            # print(article.author,request.user)
            article.save()
            return redirect('all_posts')
        form = createPostForm()
        return render(request,'article/createPost.html',{'form':form})
    else:
        form = createPostForm()
        return render(request,'article/createPost.html',{'form':form})


# 3. view_details view to provide the full details of the object
 
@login_required
def view_details(request,pk):
    full_detail = get_object_or_404(Article,id=pk)
    context = {
        "full_detail":full_detail
    }
    return render(request,'article/view_details.html',context)


# 4. delete_article view to open the delete form . 

@login_required
def delete_articles(request,pk=None):
    obj_to_delete = get_object_or_404(Article,id=pk)
    if obj_to_delete.author != request.user:
        return HttpResponse('You are not allowed to delete this post.')
    return render(request,'article/delete_post.html',{"delete_obj":obj_to_delete})

# 5. delete view to finally delete the article from the database

@login_required
def delete(request,pk):
    obj = get_object_or_404(Article,id=pk)
    # if user is not the author of article, will be redirected to another page
    if obj:
        if obj.author != request.user:
            return HttpResponse("You are not allowed to delete this object..")
        obj.delete()
        return redirect('all_posts')



# 6. all_posts view to provide the access of all the articles to user

@login_required
def all_posts(request):
    articles = Article.objects.all()
    return render(request,'article/all_posts.html',{'articles':articles})


# 7. Login view 

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("User is not active.")
        else:
            return HttpResponse("Invalid credentials.")
    else:
        return render(request,'article/login.html')

    # return render(request,'article/login.html')


# 8. register view

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            return HttpResponse("Password and confirm password are not same")
        else:
            user = User.objects.create_user(username,email,pass1)
            user.save()
            return redirect('login')
    return render(request,'article/signup.html')


# 9. logout view

@login_required
def signout(request):
    logout(request)
    return redirect('login')


# 10. edit view

@login_required
def edit_article(request,pk):
    # get current article 
    article = get_object_or_404(Article,id=pk)

    # if user is not the author of article, will be redirected to another page
    if article.author != request.user:
        return HttpResponse("You are not allowed to Edit this object..")

    # if method is post then perform the operation
    if request.method == 'POST':

        # instance of editPostForm class with post data sent by user.
        form = editPostForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('view_details',pk=pk)
    else:
        # user will be given this template as starter.
        form = editPostForm(instance=article)
    return render(request,'article/edit.html',{'form':form,"article":article})


