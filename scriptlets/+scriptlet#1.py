#region generated meta
import typing

class Inputs(typing.TypedDict):
    character_image_url: str
    reference_image_url: str
    user_prompt: str

class Outputs(typing.TypedDict):
    final_prompt: str
    image_urls: list

#endregion

from oocana import Context

async def main(params: Inputs, context: Context) -> Outputs:
    """
    Input & Prompt Builder Block
    
    Collects character image and optional reference image into an array,
    builds the final prompt by combining default and user-provided prompts.
    """
    
    # Default prompt for pixel art conversion
    default_prompt = """Convert the character from Image 1 into 16-bit style pixel art, with the result referencing the style/form of Image 2. Requirements:
  a. Preserve all clothing details and features of the character
  b. Empty-handed, arms naturally hanging down by the sides, facing the screen frontally
  c. Transform the character into 3-head-body proportions!
  d. Background is pure white and empty
  e. The image contains only the character, with no other unnecessary elements or content"""
    
    # Collect image URLs into array
    # Character image is always first (index 0)
    image_urls = []
    
    character_url = params.get("character_image_url", "")
    if character_url:
        image_urls.append(character_url)
    
    # Reference image is optional (index 1 if provided)
    reference_url = params.get("reference_image_url", "")
    if reference_url:
        image_urls.append(reference_url)
    
    # Build final prompt
    user_prompt = params.get("user_prompt", "")
    if user_prompt:
        final_prompt = f"{default_prompt}\n\n{user_prompt}"
    else:
        final_prompt = default_prompt
    
    return {
        "final_prompt": final_prompt,
        "image_urls": image_urls
    }