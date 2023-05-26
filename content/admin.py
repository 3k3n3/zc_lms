from django.contrib import admin
from .models import Article, Task, Tag, Audience, Submission


admin.site.register(Article)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Audience)
admin.site.register(Submission)
