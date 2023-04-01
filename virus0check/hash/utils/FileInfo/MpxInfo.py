from tinytag import TinyTag


def file_mpx_info(file) -> str:
    out = str()
    out += "File Information:\n"

    audio = TinyTag.get(file)

    info_dict = {
        "File name": file,
        "Title": audio.title,
        "Artist": audio.artist,
        "Genre": audio.genre,
        "Year Released": audio.year,
        "Bitrate (kBits/s)": str(audio.bitrate),
        "Composer": audio.composer,
        "Filesize (bytes)": str(audio.filesize),
        "AlbumArtist": audio.albumartist,
        "Duration (seconds)": str(audio.duration),
        "TrackTotal ": str(audio.track_total)
    }

    for label, value in info_dict.items():
        out += f"{label:25}: {value}\n"

    return out
