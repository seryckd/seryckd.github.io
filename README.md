# seryckd.github.io

The blog has a custom domain called [clutteredspaces.com](http://clutteredspaces.com) but can also be reached from the standard GitHub Pages link [seryckd.github.io](https://seryckd.github.io).

The blog was originally started on Wordpress I moved it here as it got difficult managing the posts on Wordpress and the images on Flickr or Vimeo.


## Jekyll

This uses Jekyll and the Minima Theme to generate a static site.

### Ruby Setup
```
Use ruby-install to install Ruby versions
$ brew install ruby-install
$ ruby-install ruby

Use chruby to manage different Ruby versions
$ brew install chruby
$ chruby ruby-3.4.4

Ruby provides gem and bundler to manage projects
$ gem list
$ bundler
```

### Jekyll Setup

Jekyl can be added as a Gem using a Gemfile

```rb
source "https://rubygems.org"

gem "jekyll", "~> 4.2"

group :jekyll_plugins do
  gem "minima", github: "jekyll/minima", ref: "v2.5.2"
  gem 'jekyll_img'
end```
```

### Running Locally

Run locally by using 'jekyl serve'
```
bundle install
bundle exec jekyll serve --baseurl=""
```

### Running with GitHub Pages

There is a github action copied from the Pages docuentation to build the site and upload as an artifact for pages.

The GitHub action runs under linux so I needed to get the linux runtimes in the gem lockfile.
```
bundle lock --add-platform x86_64-linux
```

## Notes

Minima integrates with jekyl-paginate (v1) and will show a specified number of posts followed by 3 boxes representing previous, current, and next.  I didn't like this because you have to scroll down the list to get the controls and then selecting the next page means you can't see the top of the list.  It also breaks the inifnity scroll that works better on mobile.


### Jekyl_img Plugin

I used the [Jekyl_img](https://www.mslinn.com/jekyll_plugins/jekyll_img.html) for images.

It has Jekyl/Liquid tags and supports captions, center alignment and can specify abstact sizes.

```
{% img src="hello.png" caption="I am a caption"%}

{% img src="https://live.staticflickr.com/65535/51791743297_339e7b253f_z.jpg" caption="I am a caption" align='center' size='quartersize' %}
```

### Simple Jekyll Search

I am using [Simple Jekyll Search](https://github.com/christian-fei/Simple-Jekyll-Search) from Christian Fei (thanks!).

# TODO

- can images scale according to width? so they show larger on mobile
- archive page
- can we add inifinity scroll instead of loading the whole page?
- exerpts (https://jekyllrb.com/docs/posts/#post-excerpts) should be set better.  Can we get a picture and paragraph for each?
- can we freeze the top part of the page as the rest scrolls?
- can we have an archive by month/year ?
- tag cloud?
