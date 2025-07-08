from typing import Dict, Any
import requests
import base64

def create_packshot(
    api_key: str,
    image_data: bytes,
    background_color: str = "#FFFFFF",
    sku: str = None,
    force_rmbg: bool = False,
    content_moderation: bool = False
) -> Dict[str, Any]:
    """
    Create a professional packshot from a product image.
    
    Args:
        api_key: Bria AI API key
        image_data: Image data in bytes
        background_color: Background color in hex format or 'transparent'
        sku: Optional SKU identifier for the product
        force_rmbg: Whether to force background removal even if alpha channel exists
        content_moderation: Whether to enable content moderation
    
    Returns:
        Dict containing the API response
    """
    url = "https://engine.prod.bria-api.com/v1/product/packshot"
    
    headers = {
        'api_token': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Convert image data to base64
    image_base64 = base64.b64encode(image_data).decode('utf-8')      # downloads the image as binary data, converts it to base64 format with base64.b64encode, and decodes it into a UTF-8 string for easy embedding in HTML or JSON.
    
    # Prepare request data
    data = {
        'file': image_base64,
        'background_color': background_color,
        'force_rmbg': force_rmbg,
        'content_moderation': content_moderation
    }
    
    # Add optional SKU((Stock Keeping Unit) unique identifier for a product) if provided
    if sku:
        data['sku'] = sku         # checks if a value for sku is provided (it's not empty or None). If it is, it adds it to the data dictionary, which will likely be sent to an API or used somewhere else.


    
    try:
        print(f"Making request to: {url}")
        print(f"Headers: {headers}")
        print(f"Data keys: {list(data.keys())}")
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        
        return response.json()
    except Exception as e:
        raise Exception(f"Packshot creation failed: {str(e)}") 