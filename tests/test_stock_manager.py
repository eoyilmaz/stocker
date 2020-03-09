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


def test_discover_media_method():
    """testing if the discover_media method is working properly
    """
    import os
    HERE = os.path.abspath(os.path.dirname(__file__))
    test_data_path = os.path.join(HERE, 'test_data')

    from stocker.models import StockManager, GenericStock
    sm = StockManager()
    sm.discover_media(test_data_path)

    assert isinstance(sm.media, list)
    assert len(sm.media) == 3

    for s in sm.media:
        assert isinstance(s, GenericStock)

    sd = sorted(sm.media, key=lambda x: x.filename)

    assert sd[0].filename == "some_video_1.mp4"
    assert sd[1].filename == "some_video_2.mp4"
    assert sd[2].filename == "some_video_3.mp4"

    assert sd[0].description == "This is a test video, created just for test!"
    assert sd[1].description == "This is a test video, created just for test!"
    assert sd[2].description == "This is a test video, created just for test!"

    assert sd[0].category1 == "Transportation"
    assert sd[1].category1 == "Food and drink"
    assert sd[2].category1 == "Food and drink"

    assert sd[0].category2 == "Holidays"
    assert sd[1].category2 == "Healthcare/Medical"
    assert sd[2].category2 == "Healthcare/Medical"

    assert sd[0].keywords == ["keyword 1", "keyword 2", "keyword 3"]
    assert sd[1].keywords == ["keyword 4", "keyword 5", "keyword 6"]
    assert sd[2].keywords == ["keyword 5", "keyword 6", "keyword 7"]


def test_generate_csv_method_with_target_is_shutter_stock():
    """testing if the generate_csv method with path="ShutterStock" is working
    properly
    """
    import os
    HERE = os.path.abspath(os.path.dirname(__file__))
    test_data_path = os.path.join(HERE, 'test_data')

    from stocker.models import StockManager, ShutterStock
    sm = StockManager()
    sm.discover_media(test_data_path)

    csv_content = sm.generate_csv(target_class=ShutterStock)

    assert csv_content == """filename,description,keywords,category,editorial
some_video_1.mp4,"This is a test video, created just for test!","keyword 1,keyword 2,keyword 3","Transportation,Holidays",no
some_video_2.mp4,"This is a test video, created just for test!","keyword 4,keyword 5,keyword 6","Food and drink,Healthcare/Medical",no
some_video_3.mp4,"This is a test video, created just for test!","keyword 5,keyword 6,keyword 7","Food and drink,Healthcare/Medical",no"""


def test_generate_csv_method_with_target_is_adobe_stock():
    """testing if the generate_csv method with path="AdobeStock" is working
    properly
    """
    import os
    HERE = os.path.abspath(os.path.dirname(__file__))
    test_data_path = os.path.join(HERE, 'test_data')

    from stocker.models import StockManager, AdobeStock
    sm = StockManager()
    sm.discover_media(test_data_path)

    csv_content = sm.generate_csv(target_class=AdobeStock)

    assert csv_content == '''Filename,Title,Keywords,Category,Releases
some_video_1.mp4,"Test video 1","keyword 1,keyword 2,keyword 3",20,""
some_video_2.mp4,"Test video 2","keyword 4,keyword 5,keyword 6",7,""
some_video_3.mp4,"Test video 3","keyword 5,keyword 6,keyword 7",7,""'''


def test_generate_csv_method_with_target_is_getty_images():
    """testing if the generate_csv method with path="GettyImages" is working
    properly
    """
    import os
    HERE = os.path.abspath(os.path.dirname(__file__))
    test_data_path = os.path.join(HERE, 'test_data')

    from stocker.models import StockManager, GettyImages
    sm = StockManager()
    sm.discover_media(test_data_path)

    csv_content = sm.generate_csv(target_class=GettyImages)

    print(csv_content)

    assert csv_content == '''file name,description,country,title,keywords,poster timecode
some_video_1.mp4,"This is a test video, created just for test!",Turkey,"Test video 1","keyword 1,keyword 2,keyword 3",00:00:05:00
some_video_2.mp4,"This is a test video, created just for test!",Turkey,"Test video 2","keyword 4,keyword 5,keyword 6",00:00:05:00
some_video_3.mp4,"This is a test video, created just for test!",Turkey,"Test video 3","keyword 5,keyword 6,keyword 7",00:00:05:00'''
