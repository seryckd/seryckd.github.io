# seryckd.github.io
Blog

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

nav_pages are not in the right order

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


