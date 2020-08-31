*********************
Kinomonster-backended
*********************

``Kinomonster-backended`` is an example of using `Flask <https://flask.palletsprojects.com/en/1.1.x/#>`_, a web micro-framework, with `SQLAlchemy <https://www.sqlalchemy.org/>`_ and `SQLite <https://www.sqlite.org/index.html>`_ to provide back-end to the `website <https://n1rvanas.github.io/Kinomonster/>`_.

The original version of the website is specified in ``CREDITS.rst``.

**Committed changes**:

*Front-end*
  1. Replaced Bootstrap's default ``margin-top: 20px;`` for ``h2`` with ``margin-top: 5px;``. This resulted in better looking sidebars.

  2. Removed fixed height for the footer. Now the footer does not have a white line on the end of the page.

  3. Removed unnecessary JavaScript, SCSS, Bootstrap imports.

  4. Movie blocks in the ``movies`` page have ``display: block; overflow: auto;`` styles instead of the fixed height for each block. Hence, all ``div`` there now act as containers for the picture, paragraph and **Watch** button.

  5. Paragraphs for posts in ``index.html`` have bigger font size, which is convenient for a reader.

  6. Created the ``about`` webpage about my work on the project.

  7. Replaced the ``Serials`` page with the ``Posts`` page (see back-end section).

  8. Other minor changes.

*Back-end*
  1. The contact form has Python backend and accepts user input and sends user mails to kinomonsterbackend@gmail.com.

  2. Signing up is real and all changes with the website's members are reflected in the SQLite database.

  3. The website allows signing in, signing in allows writing posts on the website (see below). After an(a) (un)successful attempt of signing in, JavaScript alert function is called to notify the user.

  4. Members can restore their password, specifying their email.

  5. All pages with movies and serials have real **Reviews** section. You can write reviews which will be retrieved from the SQLite database.

  6. The homepage shows two last posts on the website, which are retrieved from the SQLite database.

  7. As the ``Serials`` page was replaced by ``Posts``, the ``Posts`` page shows all website posts, new ones go first.

  8. All posts (both on the ``Posts`` page and Homepage) are stored in cache, cache is released when a member writes a new post.

  9. Authenticated users can write their posts. Writing posts includes providing this information: title (mandatory and must be unique), description (optional, but displayed in the list of posts), picture (optional, but displayed in the list of posts), contents (HTML formatting is preferred, the example for paragraphs is provided), resource (can be added to the database manually, but we assume members do not copy-paste the posts of others), author (this field is automatically filled by the ``login`` of the member).

  10. All HTML pages use Jinja2 inheritance from ``index.html``, which resulted in allocating less space for HTML files. 
