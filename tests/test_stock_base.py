# -*- coding: utf-8 -*-
# Stocker a data conversion tool for stock image/video sites.
# Copyright (C) 2018 Erkan Ozgur Yilmaz
#
# This file is part of Stocker.
#
# Stocker is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# Stocker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with Stocker.  If not, see <http://www.gnu.org/licenses/>


def test_to_csv():
    """testing if StockBase.to_csv() raises a NotImplementedError
    """
    from stocker.models import StockBase
    sb = StockBase()
    import pytest
    with pytest.raises(NotImplementedError):
        sb.to_csv()


# def test_from_file():
#     """testing if StockBase.from_file() raises a NotImplementedError
#     """
#     from stocker.models import StockBase
#     sb = StockBase()
#     import pytest
#     with pytest.raises(NotImplementedError):
#         sb.from_file('')


def test_initialization():
    """testing StockBase initialization
    """
    from stocker.models import StockBase

    kwargs = {
        'filename': 'some_file_name.mp4',
        'path': '/path/to/the/media',
        'title': 'This is the media title',
        'keywords': ['keyword1', 'keyword2', 'keyword3', 'keyword4']
    }

    sb = StockBase(**kwargs)

    assert sb.filename == kwargs['filename']
    assert sb.path == kwargs['path']
    assert sb.title == kwargs['title']
    assert sb.keywords == kwargs['keywords']


def test_read_from_file_is_working_properly(media_with_sidecar):
    """testing if reading metadata from file is working properly
    """
    import os
    media_file_full_path, sidecar_file_full_path = media_with_sidecar
    path, filename = os.path.split(media_file_full_path)

    # fill the test data to the sidecar file
    data = {
        'title': 'Test Title',
        'keywords': [
            'keyword1', 'keyword2'
        ]
    }
    import json
    with open(sidecar_file_full_path, 'w') as f:
        json.dump(data, f)

    from stocker.models import StockBase
    sb = StockBase(
        path=path,
        filename=filename,
    )
    sb.from_file(sidecar_file_full_path)

    assert sb.title == data['title']
    assert sb.keywords == data['keywords']


def test_read_from_sidecar_is_working_properly(media_with_sidecar):
    """testing if reading metadata from sidecar file is working properly
    """
    import os
    media_file_full_path, sidecar_file_full_path = media_with_sidecar
    path, filename = os.path.split(media_file_full_path)

    # fill the test data to the sidecar file
    data = {
        'title': 'Test Title',
        'keywords': [
            'keyword1', 'keyword2'
        ]
    }
    import json
    with open(sidecar_file_full_path, 'w') as f:
        json.dump(data, f)

    from stocker.models import StockBase
    sb = StockBase(
        path=path,
        filename=filename,
    )
    sb.from_sidecar_file()

    assert sb.title == data['title']
    assert sb.keywords == data['keywords']


def test_sidecar_filename_is_working_properly(media_with_sidecar):
    """testing if sidecar_filename property is working properly
    """
    import os
    media_file_full_path, sidecar_file_full_path = media_with_sidecar
    path, filename = os.path.split(media_file_full_path)

    from stocker.models import StockBase
    sb = StockBase(
        path=path,
        filename=filename,
    )
    filename_wo_ext, ext = os.path.splitext(filename)
    sidecar_filename = '%s.json' % filename_wo_ext

    assert sb.sidecar_filename == sidecar_filename


def test_sidecar_full_path_is_working_properly(media_with_sidecar):
    """testing if sidecar_full_path property is working properly
    """
    import os
    media_file_full_path, sidecar_file_full_path = media_with_sidecar
    path, filename = os.path.split(media_file_full_path)

    from stocker.models import StockBase
    sb = StockBase(
        path=path,
        filename=filename,
    )
    filename_wo_ext, ext = os.path.splitext(filename)
    sidecar_filename = '%s.json' % filename_wo_ext

    assert sb.sidecar_full_path == os.path.join(path, sidecar_filename)


def test_to_sidecar_file_creates_sidecar_file_properly(media_with_sidecar):
    """testing if to_sidecar_file creates sidecar file properly
    """
    import os
    media_file_full_path, sidecar_file_full_path = media_with_sidecar
    path, filename = os.path.split(media_file_full_path)

    from stocker.models import StockBase
    sb = StockBase(
        path=path,
        filename=filename,
        title='Test Title 1',
        keywords=['keyword1', 'keyword2', 'keyword3']
    )

    assert not os.path.exists(sidecar_file_full_path)
    sb.to_sidecar_file()
    assert os.path.exists(sidecar_file_full_path)


def test_to_sidecar_file_is_working_properly(media_with_sidecar):
    """testing if to_sidecar_file is working properly
    """
    import os
    media_file_full_path, sidecar_file_full_path = media_with_sidecar
    path, filename = os.path.split(media_file_full_path)

    from stocker.models import StockBase
    sb = StockBase(
        path=path,
        filename=filename,
        title='Test Title 1',
        keywords=['keyword1', 'keyword2', 'keyword3']
    )

    sb.to_sidecar_file()

    # check the content
    import json
    with open(sidecar_file_full_path) as f:
        data = json.load(f)

    assert sb.keywords == data['keywords']
    assert sb.title == data['title']


def test_to_sidecar_file_content(media_with_sidecar):
    """testing if to_sidecar_file content is plain json
    """
    import os
    media_file_full_path, sidecar_file_full_path = media_with_sidecar
    path, filename = os.path.split(media_file_full_path)

    from stocker.models import StockBase
    sb = StockBase(
        path=path,
        filename=filename,
        title='Test Title 1',
        keywords=['keyword1', 'keyword2', 'keyword3']
    )

    sb.to_sidecar_file()

    # check the content
    with open(sidecar_file_full_path) as f:
        data = f.read()

    print('data: %s' % data)
    assert data == """{
  "title": "Test Title 1",
  "keywords": [
    "keyword1",
    "keyword2",
    "keyword3"
  ]
}"""