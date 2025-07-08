from typing import Dict, Any, Optional   # type hints to understand what types of values are used in the code.
import requests                          # library that allows you to send HTTP requests (GET, POST).
import json

def enhance_prompt(
    api_key: str,
    prompt: str,
    **kwargs
) -> str:
    """
    Enhance a prompt using Bria AI's prompt enhancement service.
    
    Args:
        api_key: Secret token to access Bria AI API key
        prompt: Original prompt to enhance
        **kwargs: Additional parameters for the API
    
    Returns:
        Enhanced prompt string"""

    url = "https://engine.prod.bria-api.com/v1/prompt_enhancer"   # web address where the prompt enhancement API lives
    
    headers = {                      # tells the API, who u r?, what type of data u r sending?, what type of data u expect back?
        'api_token': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    data = {                        # building the data to send to the API
        'prompt': prompt,           # original prompt
        **kwargs                    # other additional settings
    }
    
    try:
        print(f"Making request to: {url}")
        print(f"Headers: {headers}")
        
        response = requests.post(url, headers=headers, json=data)       # sending post request
        response.raise_for_status()                                     # throws an error if the request failed
        
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        
        result = response.json()                        # converts the API’s reply(JSON format) into a Python dict
        return result.get("prompt variations", prompt)  #  tries to get the key "prompt variations" from the response, if it fails, return original prompt 
    except Exception as e:
        print(f"Error enhancing prompt: {str(e)}")      # prints error
        return prompt                                   # Return original prompt on error 