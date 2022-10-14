from django.db import models
from pygments.lexers import get_all_lexers


class Platform(models.Model):
    """
    Models all the available
    hosting platforms that a
    flipify user can switch to
    or switch from.
    """

    # TODO: Add more platforms or find a package that provides them.
    PLATFORM_OPTIONS = (
        ("gcp", "Google Cloud Platform"),
        ("aws", "Amazon Web Services"),
        ("heroku", "Heroku"),
        ("azure", "Azure"),
        ("do", "Digital Ocean"),
        ("netlify", "Netlify"),
    )

    # TODO: Define a better convention for status options.
    STATUS_OPTIONS = (("active", "Active"), ("inactive", "Inactive"))
    name = models.CharField(max_length=100, choices=PLATFORM_OPTIONS)
    status = models.CharField(max_length=40, choices=STATUS_OPTIONS)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Technology(models.Model):
    """
    Models all the frontend and backend
    technologies supported by flipify
    """

    TYPE_OPTIONS = (("frontend", "Frontend"), ("backend", "Backend"))

    # Generates a list of programming languages using
    # `pygments` package to provide the language choice
    # of the `Technology`
    LEXERS = [item for item in get_all_lexers() if item[1]]
    LANGUAGE_OPTIONS = sorted([(item[1][0], item[0]) for item in LEXERS])

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=TYPE_OPTIONS)
    language = models.CharField(max_length=50, choices=LANGUAGE_OPTIONS)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"
