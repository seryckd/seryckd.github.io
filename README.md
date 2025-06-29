# seryckd.github.io

[Blog Link](https://seryckd.github.io)

## Gem Lock File

```
bundle lock --add-platform x86_64-linux
```

## Running Locally

```
bundle install
bundle exec jekyll serve --baseurl=""
```

## TODO

- flickr videos
- click on images to make them bigger
- can images scale according to width? so they show larger on mobile
- custom DNS
- footer of the page: name, email, social links, description
- search - include a tag cloud?
- archive page
- can we add inifinity scroll instead of loading the whole page?
- exerpts (https://jekyllrb.com/docs/posts/#post-excerpts) should be set better.  Can we get a picture and paragraph for each?
- convert the page "butterfly fence" to a post
- can we freeze the top part of the page as the rest scrolls?
- can we have an archive by month/year ?
- google analytics

## Notes

Minima integrates with jekyl-paginate (v1) and will show a specified number of posts followed by 3 boxes representing previous, current, and next.  I didn't like like because you have to scroll down the list to get the controls and then selecting the next page means you can't see the top of the list.  It also breaks the inifnity scroll that works better on mobile.

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


