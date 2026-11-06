import osxphotos
import osxphotos.utils


def main():
    photosdb = osxphotos.PhotosDB(osxphotos.utils.get_last_library_path())
    photosdb.photos


if __name__ == "__main__":
    main()
