from django.contrib.auth.models import User
from projects.models import Project
from users.models import Profile
from random import randint
# create 20 test users
names = ['testUser' + str(i).zfill(3) for i in range(1, 21)]
password = '123456&&'
for name in names:
    user = User.objects.create_user(name, password=password)
    user.save()
    user = Profile.objects.get(username=name)
    user.name = name
    user.email = f"{name}@{name}.com"
    print(user.name, user.email)
    user.save()
# create 50 test projects
titles = ['projectTest' + str(i).zfill(3) for i in range(1, 51)]
for title in titles:
    num =  str(randint(1, 20)).zfill(3)
    owner = Profile.objects.get(username='testUser' + num)
    description = 'testing proj' + num
    new = Project.objects.create(owner=owner, title=title, description=description)
