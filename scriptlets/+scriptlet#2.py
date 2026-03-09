#region generated meta
import typing

class Inputs(typing.TypedDict):
    image_urls: list

class Outputs(typing.TypedDict):
    imageUrls: list

#endregion

from oocana import Context

async def main(params: Inputs, context: Context) -> Outputs:
    """
    Convert image_urls array to imageUrls format for nano-banana-pro
    
    Handles type conversion between different block schemas.
    """
    image_urls = params.get("image_urls", [])
    
    # Ensure we have valid URIs
    converted = []
    for url in image_urls:
        if url and isinstance(url, str):
            converted.append(url)
    
    return {
        "imageUrls": converted
    }