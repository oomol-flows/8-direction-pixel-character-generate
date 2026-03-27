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
    
    # 添加8向图的参考图，以保证方向不出错
    input_urls.append("https://static.oomol.com/community-banner/images/8d.png")
    # Limit to max 3 images as required by nano-banana-pro
    output_urls = input_urls[:3]
    
    return {"imageUrls": output_urls}