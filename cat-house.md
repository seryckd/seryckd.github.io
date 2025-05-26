---
layout: page
title: House
permalink: /house/
---


<ul>
{% for post in site.categories.house %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
