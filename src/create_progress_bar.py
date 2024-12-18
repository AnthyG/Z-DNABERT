from tqdm.auto import tqdm

def create_progress_bar(disable: bool = False):
    def progress_bar(*wargs, **kwargs):
        return tqdm(*wargs, **kwargs, disable=disable)
    return progress_bar