import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'slug',
     [
        'Video Aperitivos: Motivação',
        'Video Aperitivos: Instalação'

     ]
)
def test_titulo_video(resp, slug):
    assert_contains(resp, slug)

@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'instalacao'

    ]
)
def test_link_video(resp, slug):
    video_link = reverse('aperitivos:video', args=('slug',))
    assert_contains(resp, f'href="{video_link}"')

#     assert_contains(resp, '<iframe src="https://player.vimeo.com/video/561956574?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"')
