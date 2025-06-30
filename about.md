---
layout: page
title: About
permalink: /about/
---

<ul class="social-media-list">
    {%- for entry in site.minima.social_links -%}
    <li>
        <a rel="me" href="{{ entry.url }}" target="_blank" title="{{ entry.title }}">
        <span class="grey fa-brands fa-{{ entry.icon }} fa-lg"></span>
        </a>
    </li>
    {%- endfor -%}
    <li>
        <a href="{{ site.feed.path | default: 'feed.xml' | absolute_url }}" target="_blank" title="Subscribe to syndication feed">
            <svg class="svg-icon grey" viewbox="0 0 16 16">
                <path d="M12.8 16C12.8 8.978 7.022 3.2 0 3.2V0c8.777 0 16 7.223 16 16h-3.2zM2.194
                    11.61c1.21 0 2.195.985 2.195 2.196 0 1.21-.99 2.194-2.2 2.194C.98 16 0 15.017 0
                    13.806c0-1.21.983-2.195 2.194-2.195zM10.606
                    16h-3.11c0-4.113-3.383-7.497-7.496-7.497v-3.11c5.818 0 10.606 4.79 10.606 10.607z"
                />
            </svg>
        </a>
    </li>
</ul>

<i>Darren Seryck lives in Ontario, Canada. He gets very interested in things that normal people wouldn't (at least according to his wife, a very normal person) and then just as suddenly loses interest and switches to other things. Hence he tends to accumulate a lot of what most people would call junk and he calls 'useful things waiting for a purpose'.</i>

I wrote the above for the first post some years ago. But how accurate is it? I posted the above into a generic text-to-image AI tool and asked it to generate a picture of the person in the text.

{% img src="aboutme.jpg" align="center" caption="me!" size="halfsize" %}

It's ... not entirely wrong.

and I love the drill with the spanner bit.