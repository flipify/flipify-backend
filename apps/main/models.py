from django.db import models
from pygments.lexers import get_all_lexers
import requests



class Platform(models.Model):
    """
    Models all the available
    hosting platforms that a
    flipify user can switch to
    or switch from.
    """
    # TODO: Add more platforms or find a package that provides them.
    PLATFORM_OPTIONS = (
        ('gcp', 'Google Cloud Platform'),
        ('aws', 'Amazon Web Services'),
        ('heroku', 'Heroku'),
        ('azure', 'Azure'),
        ('do', 'Digital Ocean'),
        ('netlify', 'Netlify'),
    )



    name = models.CharField(max_length=100, choices=PLATFORM_OPTIONS)
    # TODO in the  future a method should be witten to automatically get sever url
    url  = models.URLField(max_length=100, )
    logo = models.ImageField()

   # TODO: currently using python requests package to track server status
   # if the future we can use another flexible package that can give us more detail
    @property
    def server_status(self):
        url = self.url 
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return 'online'
        except requests.exceptions.ConnectionError as e:
            return 'offline'



    def __str__(self) -> str:
        return self.name


class Technology(models.Model):
    """
    Models all the frontend and backend
    technologies supported by flipify
    """
    TYPE_OPTIONS = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend')
    )

    # Generates a list of programming languages using
    # `pygments` package to provide the language choice
    # of the `Technology`
    LEXERS = [item for item in get_all_lexers() if item[1]]
    LANGUAGE_OPTIONS = sorted([(item[1][0], item[0]) for item in LEXERS])

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=TYPE_OPTIONS)
    language = models.CharField(max_length=50, choices=LANGUAGE_OPTIONS)
    logo = models.ImageField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"
