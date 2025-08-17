class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")

        self._title = title
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be empty")

        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    def articles(self):
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list({a.magazine.category for a in self.articles()})
        return categories if categories else None


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        titles = [a.title for a in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [
            author for author in self.contributors()
            if sum(1 for a in self.articles() if a.author == author) > 2
        ]
        return authors if authors else None

