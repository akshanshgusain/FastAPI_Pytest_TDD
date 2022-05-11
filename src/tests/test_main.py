def test_ping(test_app):
    """ Home route check"""
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World updated"}


def test_ping_false(test_app):
    """Non-existing routes check"""
    response = test_app.get("/ping")
    assert response.status_code == 404
