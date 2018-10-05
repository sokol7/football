import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football_project.settings')
import django
django.setup()
from football.models import Comment, NewsPage, Country

comments = Comment.objects.all()
parent_comments = []
sub_comments = []

for i in comments:
    if i.comment_id == None:
        parent_comments.append(i)
    else:
        sub_comments.append(i)


sorted_comments = []
for par_comment in parent_comments:
    low_comments = []
    for sub_comment in sub_comments:
        if sub_comment.comment_id_id == par_comment.id:
            low_comments.append(sub_comment)
    if low_comments:
        sorted_comments1 = dict([(par_comment, low_comments)])
        sorted_comments.append(sorted_comments1)