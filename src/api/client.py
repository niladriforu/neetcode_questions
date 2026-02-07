"""API client for making HTTP requests."""

import requests
import logging
from typing import Optional, Dict, Any
from time import sleep

logger = logging.getLogger(__name__)


class APIClient:
    """
    Client for making API requests with retry logic.
    """
    
    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3,
        retry_delay: int = 5
    ):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for the API
            api_key: Optional API key for authentication
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
            retry_delay: Delay between retries in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.session = requests.Session()
        
        # Set default headers
        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
        self.session.headers.update({"Content-Type": "application/json"})
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Make an HTTP request with retry logic.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            params: Query parameters
            data: Request body data
            headers: Additional headers
            
        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Making {method} request to {url} (attempt {attempt + 1})")
                
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    json=data,
                    headers=headers,
                    timeout=self.timeout
                )
                
                response.raise_for_status()
                
                logger.info(f"Request successful: {method} {url}")
                return response.json()
            
            except requests.exceptions.RequestException as e:
                logger.warning(f"Request failed (attempt {attempt + 1}): {e}")
                
                if attempt < self.max_retries - 1:
                    sleep(self.retry_delay)
                else:
                    logger.error(f"Max retries exceeded for {method} {url}")
                    raise
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a GET request."""
        return self._make_request("GET", endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a POST request."""
        return self._make_request("POST", endpoint, data=data)
    
    def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a PUT request."""
        return self._make_request("PUT", endpoint, data=data)
    
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request."""
        return self._make_request("DELETE", endpoint)
    
    def fetch_paginated_data(
        self,
        endpoint: str,
        params: Optional[Dict] = None,
        page_param: str = "page",
        max_pages: Optional[int] = None
    ) -> list:
        """
        Fetch paginated data from an API.
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            page_param: Name of the pagination parameter
            max_pages: Maximum number of pages to fetch
            
        Returns:
            List of all records from all pages
        """
        all_data = []
        page = 1
        
        while True:
            if max_pages and page > max_pages:
                break
            
            page_params = params.copy() if params else {}
            page_params[page_param] = page
            
            logger.info(f"Fetching page {page} from {endpoint}")
            
            try:
                response = self.get(endpoint, params=page_params)
                
                # Assume response has 'data' or 'results' field
                data = response.get('data') or response.get('results') or response
                
                if not data or len(data) == 0:
                    logger.info(f"No more data at page {page}")
                    break
                
                all_data.extend(data if isinstance(data, list) else [data])
                page += 1
                
            except Exception as e:
                logger.error(f"Error fetching page {page}: {e}")
                break
        
        logger.info(f"Fetched {len(all_data)} total records")
        return all_data
