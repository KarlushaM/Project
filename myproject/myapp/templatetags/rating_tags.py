from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def render_rating_stars(rating):
    try:
        rating = int(rating)
    except (ValueError, TypeError):
        rating = 0

    full_stars = min(max(rating, 0), 5)
    stars_html = ""

    for i in range(1, 6):
        if i <= full_stars:
            stars_html += '<span class="star full">★</span>'
        else:
            stars_html += '<span class="star">★</span>'

    return mark_safe(f'<span class="user-rating">{stars_html}</span>')