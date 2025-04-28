import jmcomic
from jmcomic import JmOption

def download_album_by_id(album_id, option_file_path):
    option = jmcomic.create_option_by_file(option_file_path)
    jmcomic.download_album(album_id, option)

if __name__ == "__main__":
    import sys
    album_id = sys.argv[1]
    option_file_path = sys.argv[2]
    download_album_by_id(album_id, option_file_path)
