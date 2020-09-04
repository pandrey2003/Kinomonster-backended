*********************
Kinomonster-backended
*********************

``Kinomonster-backended`` is an example of using `Flask <https://flask.palletsprojects.com/en/1.1.x/#>`_, a web micro-framework, with `SQLAlchemy <https://www.sqlalchemy.org/>`_ and `SQLite <https://www.sqlite.org/index.html>`_ to provide back-end to the `website <https://n1rvanas.github.io/Kinomonster/>`_.

The original version of the website is specified in ``CREDITS.rst``.

**Committed changes**:

*Front-end*
  1. Replaced Bootstrap's default ``margin-top: 20px;`` for ``h2`` with ``margin-top: 5px;``. This resulted in better looking sidebars.

  2. Removed the fixed height for the footer. Now the footer does not have the white line on the end of the page.

  3. Removed unnecessary JavaScript, SCSS, Bootstrap files and imports of them.

  4. Movie blocks in the ``movies`` page have ``display: block; overflow: auto;`` styles instead of the fixed height for each block. Hence, all ``div`` blocks there now act as containers for a picture, a paragraph and the **Watch** button.

  5. Paragraphs for posts in ``index.html`` have a bigger font size, which is comfortable for a reader.

  6. Created the ``about`` webpage about my work on the project.

  7. Replaced the ``Serials`` page with the ``Posts`` page (see the back-end section below).

  8. Other minor changes.

*Back-end*
  1. The contact form has Python backend: it accepts user input and sends user mails to kinomonsterbackend@gmail.com.

  2. Signing up is real and all changes with the website's members are reflected in the SQLite database.

  3. The website allows signing in, signing in allows writing posts on the website (see below). After a(n) (un)successful attempt of signing in, JavaScript alert function is called to notify the user.

  4. Members can restore their password with the email.

  5. All movies and serials pages have a real **Reviews** section. You can write reviews which will be retrieved from the SQLite database.

  6. The homepage shows two last posts on the website, which are retrieved from the SQLite database.

  7. As the ``Serials`` page was replaced by ``Posts``, the ``Posts`` page shows all website posts, new ones go first.

  8. All posts (both on the ``Posts`` page and Homepage) are stored in cache, the cache is released when an authenticated user publishes a new post.

  9. Authenticated users can write posts. Writing posts includes providing this information: ``title`` (mandatory and must be unique), ``description`` (optional, but displayed in the list of posts), ``picture`` (optional, but displayed in the list of posts), ``contents`` (HTML formatting is preferred, for example ``<p>Write your paragraph here</p>``), ``resource`` (can be added to the database manually, but we assume members do not copy-paste the posts of others), ``author`` (this field is automatically filled by the ``login`` of the member).

  10. The last piece of news is shown only on the homepage and is retrieved from the SQLite database.

  11. All HTML pages use Jinja2 inheritance from ``index.html``, which resulted in allocating less space for HTML files. 


**Note**: the production server works with ``key.key`` file (decrypts the movie portal gmail password). Secret variables such as ``CSRF_SESSION_KEY`` and ``SECRET_KEY`` (they sign data and cookies) were changed from defined in GitHub's ``config.py``. Database works with different credentials.
