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


def test_initialization():
    """testing initialization
    """
    from stocker.models import GenericStock
    gst = GenericStock()
    assert isinstance(gst, GenericStock)


def test_init_with_arguments():
    """testing initialization with keyword arguments
    """
    from stocker.models import GenericStock
    # test data
    kwargs = {
        'filename': 'footage_filename.mov',
        'title': 'Up to 200 characters,Most important keywords first. '
                 'Max 50 keywords.',
        'category1': 'Holidays',
        'category2': 'Transportation',
        'keywords': [
            'background',
            'bay',
            'behind',
            'blue',
            'boat',
            'city',
            'cloud',
        ],
        'country': 'Turkey',
        'editorial': False,
        'releases': ['release1.pdf', 'release2.pdf'],
        'poster_timecode': '00:00:00'
    }

    gst = GenericStock(**kwargs)
    assert gst.filename == kwargs['filename']
    assert gst.title == kwargs['title']
    assert gst.category1 == kwargs['category1']
    assert gst.category2 == kwargs['category2']
    assert gst.keywords == kwargs['keywords']
    assert gst.editorial == kwargs['editorial']
    assert gst.releases == kwargs['releases']
    assert gst.poster_timecode == kwargs['poster_timecode']
    assert gst.country == kwargs['country']
