import subprocess
import os
import requests
import spotdl


class Downloader:
    def __init__(self, links_filepath):
        self.links_filepath = links_filepath

    def get_links(self):
        with open(self.links_filepath, "r") as file:
            links = file.readlines()
        return links

    def download(self, link):
        command = ["spotdl", "download", link, "--save-file", "metadata.spotdl"]
        subprocess.Popen(command)
