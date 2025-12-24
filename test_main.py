from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """
    Test that the root endpoint returns 200 OK and contains
    the personalized greeting in the HTML.
    """
    response = client.get("/")
    assert response.status_code == 200

    # We check response.text (HTML) instead of response.json()
    # This ensures your specific template is rendering
    assert "Hi Afnaan" in response.text


def test_health():
    """
    Test the health check endpoint for JSON response.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
