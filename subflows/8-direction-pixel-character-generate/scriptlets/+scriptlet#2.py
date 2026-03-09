#region generated meta
import typing
class Inputs(typing.TypedDict):
    image_urls: list[str] | None
class Outputs(typing.TypedDict):
    imageUrls: typing.NotRequired[list[str] | None]
#endregion

from oocana import Context

async def main(params: Inputs, context: Context) -> Outputs:
    # Convert nano-banana2 output format to nano-banana-pro input format
    # nano-banana2 outputs "image_urls" (array), nano-banana-pro expects "imageUrls" (array with max 3)
    
    input_urls = params.get("image_urls")
    
    if not input_urls:
        return {"imageUrls": None}
    
    # Limit to max 3 images as required by nano-banana-pro
    output_urls = input_urls[:3]
    
    return {"imageUrls": output_urls}