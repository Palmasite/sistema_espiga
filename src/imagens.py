# -*- coding: utf-8 -*-
from django.core.files.storage import FileSystemStorage
import re, Image, os
from django.conf import settings


class StorageComLimpeza(FileSystemStorage):
    
    def get_available_name(self, name):
        return name
        
    def _save(self, name, content):
        if self.exists(os.path.join(settings.MEDIA_ROOT, name)):
            os.unlink(os.path.join(settings.MEDIA_ROOT, name))

        return super(StorageComLimpeza, self)._save(name, content)

meu_storage = StorageComLimpeza()

GET_THUMB_PATTERN = re.compile(r'^get_foto_(\d+)x(\d+)_(url|filename)$')

def getattr_thumb_foto(self, name):
    
    
    """
    Deploys dynamic methods for on-demand thumbnails creation with any
    size.

    http://www.djangosnippets.org/snippets/619/

    Syntax::

        get_photo_[WIDTH]x[HEIGHT]_[METHOD]

    Where *WIDTH* and *HEIGHT* are the pixels of the new thumbnail and
    *METHOD* can be ``url`` or ``filename``.

    Example usage::

        >>> photo = Photo(photo="/tmp/example.jpg", ...)
        >>> photo.save()
        >>> photo.get_photo_320x240_url()
        u"http://media.example.net/photos/2008/02/26/example_320x240.jpg"
        >>> photo.get_photo_320x240_filename()
        u"/srv/media/photos/2008/02/26/example_320x240.jpg"
    """
    match = re.match(GET_THUMB_PATTERN, name)
    
    if match is None:
        raise AttributeError, name
    width, height, method = match.groups()
    size = int(width), int(height)

    # Se não existir o arquivo de imagem original, retorna vazio
    try:
        if not self.img_foto or not os.path.exists(self.img_foto.file.name):
            return ''
    except IOError:
        return ''

    def get_photo_thumbnail_filename():
        file, ext = os.path.splitext(self.img_foto.file.name)
        return file + '_%sx%s' % size + ext

    def get_photo_thumbnail_url():
        url, ext = os.path.splitext(self.img_foto.url)
        return url + '_%sx%s' % size + ext

    thumbnail = get_photo_thumbnail_filename()
    if not os.path.exists(thumbnail):
        
        img = Image.open(self.img_foto.file.name)
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(thumbnail)
    
    if method == "url":
        return get_photo_thumbnail_url
    else:
        return get_photo_thumbnail_filename
        
