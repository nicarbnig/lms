from whitenoise.storage import CompressedManifestStaticFilesStorage

class CustomStaticFilesStorage(CompressedManifestStaticFilesStorage):
    def post_process(self, *args, **kwargs):
        files_to_ignore = [name for name in self.hashed_files if name.endswith('.map')]
        for name in files_to_ignore:
            del self.hashed_files[name]
        return super().post_process(*args, **kwargs)
