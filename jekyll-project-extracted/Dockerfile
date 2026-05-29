FROM ruby:3.2

WORKDIR /srv/jekyll

COPY Gemfile Gemfile.lock* ./
RUN bundle install

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--watch", "--force_polling", "--host", "0.0.0.0"]