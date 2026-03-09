#region generated meta
import typing
class Inputs(typing.TypedDict):
    image_urls: list[str] | None
class Outputs(typing.TypedDict):
    imageUrls: typing.NotRequired[list[str] | None]
#endregion

def main(params: Inputs, context) -> Outputs:
    """Convert image_urls format for nano-banana-pro compatibility."""
    
    image_urls = params.get("image_urls")
    
    if not image_urls:
        return {"imageUrls": None}
    
    # Ensure all URLs are valid strings
    valid_urls = [url for url in image_urls if url and isinstance(url, str)]
    
    if not valid_urls:
        return {"imageUrls": None}
    
    # Limit to max 3 URLs for nano-banana-pro
    return {"imageUrls": valid_urls[:3]}