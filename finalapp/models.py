from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# PRODUCT_SIZE = (
#     ('S', 'Small'),
#     ('M', 'Medium'),
#     ('L', 'Large'),
#     ('XL', 'Extra Large'),
# )
# CATEGORY = (
#     ('M', 'MENS'),
#     ('W', 'WOMENS'),
#     ('K', 'KIDS'),
# )


class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Please enter a valid email'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match.'
        if len(form['firstName']) < 2:
            errors['firstName'] = 'Please enter a valid first name.'
        if len(form['lastName']) < 2:
            errors['lastName'] = 'Please enter a valid last name.'
        return errors

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False
        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())


class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    about_me = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    user = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    message = models.ForeignKey(
        Message, related_name='messageComments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='userComments', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class About(models.Model):
    # file = models.FileField(upload_to='user_images',
    #                         default='static/img/default.png')
    message = models.TextField()
    user = models.ForeignKey(
        User, related_name='abouts', on_delete=models.CASCADE)
    mood = models.CharField(max_length=7, default='No Mood')
    meet = models.CharField(max_length=255, default='')
    motto = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProfilePicture(models.Model):
    file = models.FileField(upload_to='user_images',
                            default=None)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, default=None, related_name='profilepicture')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostManager(models.Manager):
    def validatePost(self, post):
        errors = {}
        if len(post) > 280:
            errors['length'] = 'Tweet cannot exceed 280 characters.'
        return errors


class Post(models.Model):
    post = models.CharField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
