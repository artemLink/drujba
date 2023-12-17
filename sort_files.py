import os
import shutil
folders = [
    'зображення', ' відео файли', 'документи', "музика", "архіви"
]
path_to_files = []

dir_list = ['images', 'documents', 'audio', 'video', 'archives']
image_extensions = ('.jpeg', '.png', '.jpg', '.svg')
video_extensions = ('.avi', '.mp4', '.mov', '.mkv')
document_extensions = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
music_extensions = ('.mp3', '.ogg', '.wav', '.amr')
archive_extensions = ('.zip', '.gz', '.tar')


def find_files(path):
    for file in os.listdir(path):
        new_path = os.path.join(path, file)

        if os.path.isdir(new_path):
            find_files(new_path)
        else:
            path_to_files.append(new_path)
    return path_to_files


def sort_by_type(path):
    image_dir = os.path.join(path, "images")
    video_dir = os.path.join(path, "videos")
    document_dir = os.path.join(path, "documents")
    music_dir = os.path.join(path, "music")
    archive_dir = os.path.join(path, "archives")
    unknown_dir = os.path.join(path, "unknown")

    files = find_files(path)

    for file in files:
        name, extension = os.path.splitext(file)
        if extension.lower() in image_extensions:
            shutil.move(file, image_dir)
        elif extension.lower() in video_extensions:
            shutil.move(file, video_dir)
        elif extension.lower() in document_extensions:
            shutil.move(file, document_dir)
        elif extension.lower() in music_extensions:
            shutil.move(file, music_dir)
        elif extension.lower() in archive_extensions:
            shutil.move(file, archive_dir)
        else:
            shutil.move(file, unknown_dir)

    print("Список зображень:", os.listdir(image_dir))
    print("Список відеофайлів:", os.listdir(video_dir))
    print("Список документів:", os.listdir(document_dir))
    print("Список музичних файлів:", os.listdir(music_dir))
    print("Список архівів:", os.listdir(archive_dir))
    print("Список файлів з невідомим розширенням:", os.listdir(unknown_dir))