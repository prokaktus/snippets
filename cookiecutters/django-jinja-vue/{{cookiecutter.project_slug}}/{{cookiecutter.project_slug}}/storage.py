from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class FileStorage(ManifestStaticFilesStorage):
    manifest_strict = False
