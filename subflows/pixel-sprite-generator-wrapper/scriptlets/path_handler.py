#region generated meta
import typing
class Inputs(typing.TypedDict):
    character_input: str
    character_uploaded_url: str | None
    reference_input: str | None
    reference_uploaded_url: str | None
class Outputs(typing.TypedDict):
    character_url: typing.NotRequired[str]
    reference_url: typing.NotRequired[str | None]
#endregion

def is_url(path: str) -> bool:
    """Check if the path is a URL."""
    if not path:
        return False
    parsed = urlparse(path)
    return bool(parsed.scheme and parsed.scheme in ('http', 'https', 'ftp'))

def main(params: Inputs, context) -> Outputs:
    """Handle both local paths and URLs for images."""
    
    character_input = params.get("character_input", "")
    character_uploaded_url = params.get("character_uploaded_url")
    reference_input = params.get("reference_input")
    reference_uploaded_url = params.get("reference_uploaded_url")
    
    # Handle character image
    if is_url(character_input):
        # Input is already a URL, use it directly
        character_url = character_input
    else:
        # Input is a local path, use the uploaded URL
        character_url = character_uploaded_url
        if not character_url:
            raise ValueError(f"Failed to get uploaded URL for character image: {character_input}")
    
    # Handle reference image (optional)
    reference_url = None
    if reference_input:
        if is_url(reference_input):
            # Input is already a URL, use it directly
            reference_url = reference_input
        else:
            # Input is a local path, use the uploaded URL
            reference_url = reference_uploaded_url
    
    return {
        "character_url": character_url,
        "reference_url": reference_url
    }