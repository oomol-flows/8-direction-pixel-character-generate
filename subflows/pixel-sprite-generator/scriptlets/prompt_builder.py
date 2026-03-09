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

def main(params: Inputs, context) -> Outputs:
    """Build combined prompt and image URL array."""
    
    # Default prompt
    default_prompt = """Convert the character from Image 1 into 16-bit style pixel art, with the result referencing the style/form of Image 2. Requirements:
a. Preserve all clothing details and features of the character
b. Empty-handed, arms naturally hanging down by the sides, facing the screen frontally
c. Transform the character into 3-head-body proportions!
d. Background is pure white and empty
e. The image contains only the character, with no other unnecessary elements or content"""
    
    # Combine with user prompt if provided
    user_prompt = params.get("user_prompt", "") or ""
    if user_prompt:
        final_prompt = f"{default_prompt}\n\n{user_prompt}"
    else:
        final_prompt = default_prompt
    
    # Build image URL array (character first, then reference if provided)
    image_urls = [params["character_image_url"]]
    reference_url = params.get("reference_image_url")
    if reference_url:
        image_urls.append(reference_url)
    
    return {
        "final_prompt": final_prompt,
        "image_urls": image_urls
    }