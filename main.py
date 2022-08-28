#!/usr/bin/env python
from __future__ import annotations

from pathlib import Path

from alfred import AlfredClient
from images_upload_cli.upload import UPLOAD
from images_upload_cli.util import make_thumbnail


def uplaod_to_imgur(imagepath: str | Path, hosting: str = "imgur", bbcode: bool = False, thumbnail: bool = False) -> str:
    """Imgur sitesi üzerine resim yükler ve linki döndürür"""
    if isinstance(imagepath, str):
        imagepath = Path(imagepath)
    upload_func = UPLOAD[hosting]  # get upload func
    img = imagepath.read_bytes()
    if not thumbnail:
        link = f"[img]{upload_func(img)}[/img]" if bbcode else upload_func(img)
    else:
        thumb = make_thumbnail(img)
        link = f"[url={upload_func(img)}][img]{upload_func(thumb)}[/img][/url]"
    return link


alfred_client = AlfredClient()
filename = alfred_client.query.split("/")[-1]
path = Path(alfred_client.query) if alfred_client.query.startswith("/") else (Path.home() / alfred_client.query)
try:
    link = uplaod_to_imgur(path)
    alfred_client.add_result(filename, link, icon_path=path, arg=link)
except Exception as e:
    alfred_client.add_result(e.__class__.__name__, filename, icon_path="not-found.png", arg=str(path))
alfred_client.response()
