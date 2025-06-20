# seryckd.github.io

[Blog Link](https://seryckd.github.io)

## Gem Lock File

```
bundle lock --add-platform x86_64-linux
```

## Running Locally

```
bundle install
bundle update github-pages
bundle exec jekyll serve --baseurl=""
```

## TODO

- flickr images need resolving to github
- flickr videos
- click on images to make them bigger
- custom DNS
- "Aout" page needs to be on the right hand side of the nav_page links
- footer of the page: name, email, social links, description
- front page is one long list, needs to page
- exerpts (https://jekyllrb.com/docs/posts/#post-excerpts) should be set better.  Can we get a picture and paragraph for each?
- convert the page "butterfly fence" to a post
- can we freeze the top part of the page as the rest scrolls?
- can we have an archive by month/year ?

## Jekyll Documentation

https://cloudcannon.com/cheat-sheets/jekyll/

## Plugins

## Image

https://www.mslinn.com/jekyll_plugins/jekyll_img.html

{% img src="https://live.staticflickr.com/65535/51791743297_339e7b253f_z.jpg" caption="I am a caption"%}

loads from /assets/images

{% img src="hello.png" caption="I am a caption"%}


{% img src="https://live.staticflickr.com/65535/51791743297_339e7b253f_z.jpg" caption="I am a caption" align='center' size='quartersize' %}

size="quartersize"
align='center' center|right|left

size='eighthsize|fullsize|halfsize|initial|quartersize|XXXYY|XXX%' – Defines width of image.
CSS units can also be used, for those cases XXX is a float and YY is unit (see below)


