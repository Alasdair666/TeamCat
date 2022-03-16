def test_access_homepage(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_homepage_is_cat_related(client):
    resp = client.get("/")
    assert b"cat" in resp.data


def test_access_aboutpage(client):
    resp = client.get("/about")
    assert resp.status_code == 200


def test_aboutpage_mentions_one_of_us(client):
    resp = client.get("/about")
    assert b"qiyang" in resp.data.lower()


def test_access_non_existinf_page(client):
def test_access_non_existing_page(client):
    resp = client.get("/no_page")
    assert resp.status_code == 404
