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

import pytest


@pytest.fixture(scope='function')
def media_with_sidecar():
    """creates a media file with a sidecar file
    """
    import os
    import tempfile

    # create a test file
    media_file_full_path = tempfile.mktemp(suffix='.mov')
    temp_path, media_file_base_name = os.path.split(media_file_full_path)

    sidecar_file_name = '%s.json' % (media_file_base_name.split('.')[0])
    sidecar_file_full_path = os.path.join(temp_path, sidecar_file_name)

    yield media_file_full_path, sidecar_file_full_path

    # clean up the test
    try:
        os.remove(media_file_full_path)
    except FileNotFoundError:
        pass

    try:
        os.remove(sidecar_file_full_path)
    except FileNotFoundError:
        pass
