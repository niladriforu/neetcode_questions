"""Unit tests for API client."""

import pytest
from unittest.mock import Mock, patch
from src.api.client import APIClient


def test_api_client_init():
    """Test API client initialization."""
    client = APIClient(
        base_url="https://api.example.com",
        api_key="test-key",
        timeout=30
    )
    
    assert client.base_url == "https://api.example.com"
    assert client.api_key == "test-key"
    assert client.timeout == 30


@patch('src.api.client.requests.Session')
def test_api_client_get(mock_session):
    """Test GET request."""
    # Setup mock
    mock_response = Mock()
    mock_response.json.return_value = {"data": "test"}
    mock_response.raise_for_status = Mock()
    mock_session_instance = Mock()
    mock_session_instance.request.return_value = mock_response
    mock_session.return_value = mock_session_instance
    
    # Create client and make request
    client = APIClient(base_url="https://api.example.com")
    result = client.get("/endpoint")
    
    # Verify
    assert result == {"data": "test"}


@patch('src.api.client.requests.Session')
def test_api_client_post(mock_session):
    """Test POST request."""
    # Setup mock
    mock_response = Mock()
    mock_response.json.return_value = {"status": "created"}
    mock_response.raise_for_status = Mock()
    mock_session_instance = Mock()
    mock_session_instance.request.return_value = mock_response
    mock_session.return_value = mock_session_instance
    
    # Create client and make request
    client = APIClient(base_url="https://api.example.com")
    result = client.post("/endpoint", data={"key": "value"})
    
    # Verify
    assert result == {"status": "created"}


def test_fetch_paginated_data_empty():
    """Test paginated data fetching with empty response."""
    client = APIClient(base_url="https://api.example.com")
    
    # Mock the get method to return empty data
    with patch.object(client, 'get', return_value={"data": []}):
        result = client.fetch_paginated_data("/endpoint")
        
        # Verify
        assert result == []
