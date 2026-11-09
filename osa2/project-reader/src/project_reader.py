from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")

        deserialized = tomli.loads(content)

        project = deserialized["project"]

        name = project["name"].replace("-", " ").capitalize()
        description = project["description"]
        license = project["license"]

        authors = [author["name"] for author in project["authors"]]

        dependencies = [
            dependency.split(">=")[0]
            for dependency in project["dependencies"]
        ]

        dev_dependencies = [
            dependency.split(">=")[0]
            for dependency in deserialized["dependency-groups"]["dev"]
        ]

        return Project(
            name,
            description,
            license,
            authors,
            dependencies,
            dev_dependencies
        )
