#region generated meta
import typing
class Inputs(typing.TypedDict):
    character_image_url: str
    reference_image_url: str | None
    user_prompt: str | None
class Outputs(typing.TypedDict):
    final_prompt: typing.NotRequired[str]
    image_urls: typing.NotRequired[list[str]]
#endregion

from oocana import Context
from urllib.parse import urlparse

def is_remote_url(url: str) -> bool:
    """Check if the given string is a valid remote URL (http/https)."""
    if not url:
        return False
    try:
        parsed = urlparse(url)
        return parsed.scheme in ('http', 'https') and bool(parsed.netloc)
    except Exception:
        return False

async def main(params: Inputs, context: Context) -> Outputs:
    # Default prompt for pixel art conversion
    default_prompt = """Convert the character from Image 1 into 16-bit style pixel art, with the result referencing the style/form of Image 2. Requirements:
  a. Preserve all clothing details and features of the character
  b. Empty-handed, arms naturally hanging down by the sides, facing the screen frontally
  c. Transform the character into 3-head-body proportions!
  d. Background is pure white and empty
  e. The image contains only the character, with no other unnecessary elements or content"""
    
    # Append user prompt if provided
    final_prompt = default_prompt
    if params.get("user_prompt"):
        final_prompt = f"{default_prompt}\n\nAdditional requirements: {params['user_prompt']}"
    
    # Validate character_image_url is a remote URL
    if not params.get("character_image_url"):
        raise ValueError("character_image_url is required")
    if not is_remote_url(params["character_image_url"]):
        raise ValueError(f"character_image_url must be a remote URL (http/https), got: {params['character_image_url']}")
    
    # Build image URLs array: character first, then reference
    image_urls = [params["character_image_url"]]
    
    # Reference image is optional, but if provided must be a remote URL
    if params.get("reference_image_url"):
        if not is_remote_url(params["reference_image_url"]):
            raise ValueError(f"reference_image_url must be a remote URL (http/https), got: {params['reference_image_url']}")
        image_urls.append(params["reference_image_url"])
    
    return {
        "final_prompt": final_prompt,
        "image_urls": image_urls
    }