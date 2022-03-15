def test_access_homepage(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_homepage_is_cat_related(client):
    resp = client.get("/")
    assert b"cat" in resp.data


def test_access_aboutpage(client):
    resp = client.get("/about")
    assert resp.status_code == 200
