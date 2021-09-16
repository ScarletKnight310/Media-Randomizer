from core.RandomMedia import randomMedia

base = "https://myanimelist.net/"


def randomAnime():
    return randomMedia(base, "anime/")


def randomManga():  # manga and lN list, sep?
    return randomMedia(base, "manga/")
