# Homepage
def test_access_homepage(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_homepage_is_cat_related(client):
    resp = client.get("/")
    assert b"cat" in resp.data


# About page
def test_access_aboutpage(client):
    resp = client.get("/about")
    assert resp.status_code == 200


def test_aboutpage_mentions_one_of_us(client):
    resp = client.get("/about")
    assert b"qiyang" in resp.data.lower()


# Contact page
def test_access_contactpage(client):
    resp = client.get("/contact")
    assert resp.status_code == 200


def test_contactpage_has_mailto(client):
    resp = client.get("/contact")
    assert b"mailto:" in resp.data.lower()


# Diet page
def test_access_dietpage(client):
    resp = client.get("/diet")
    assert resp.status_code == 200


def test_dietpage_mentions_diets(client):
    resp = client.get("/diet")
    assert b"diets" in resp.data.lower()


# 404 Non existing
def test_access_non_existing_page(client):
    resp = client.get("/no_page")
    assert resp.status_code == 404
