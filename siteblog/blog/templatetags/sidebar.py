from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular_posts(count=3):
    posts = Post.objects.order_by('-views')[:count]
    return {'posts': posts, 'count': count}


@register.inclusion_tag('blog/tag_cloud_tpl.html')
def get_tag_cloud(count=30):
    tags = Tag.objects.all()[:count]
    return {'tags': tags}


@register.inclusion_tag('blog/search_in_title_tpl.html')
def search_in_title(count=30):
    tags = Tag.objects.all()[:count]
    return {'tags': tags}
