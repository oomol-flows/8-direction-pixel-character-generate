# Pixel Character Generator

## Project Overview

Transform character images into game-ready pixel art sprite sheets with 8 viewing angles. Ideal for game developers, artists, and animators creating 2D game assets or character reference sheets.

## Block Capabilities

### 8-Direction Pixel Character Generate (Subflow)

Main workflow that orchestrates the entire transformation process. Accepts remote URLs for character and optional reference images, outputs a complete 8-direction sprite sheet.

**Inputs:**
- `remote_url` (required): Remote URL to character image (http/https)
- `input` (optional): Remote URL to reference pixel art style image

**Outputs:**
- `images`: Array of generated sprite sheet image paths

### Input & Prompt Builder

Combines character and reference images with pixel art generation instructions. Validates that inputs are remote URLs.

**Inputs:**
- `character_image_url` (required): Remote URL to character image
- `reference_image_url` (optional): Remote URL to style reference
- `user_prompt` (optional): Additional customization text

**Outputs:**
- `final_prompt`: Complete generation instructions
- `image_urls`: Array of image URLs for processing

### URL Format Converter

Converts image URL arrays between different block formats, filtering invalid values.

## Block Combination Suggestions

**Basic Flow:**
Upload Character Image → 8-Direction Pixel Character Generate

**Enhanced Flow:**
Upload Character Image + Upload Reference Image → 8-Direction Pixel Character Generate

**Custom Flow:**
Upload images → Input & Prompt Builder (with custom prompt) → Generate Pixel Art → Generate Sprite Sheet

## Basic Usage

1. Upload your character image using a file upload block (cloudflare-r2 or upload-to-cloud)
2. Optionally upload a reference image for style guidance
3. Connect the remote URLs to the 8-Direction Pixel Character Generate subflow
4. Run the workflow to generate your 8-direction sprite sheet

## Examples

**Game Development:** Convert concept art into sprite sheets for top-down or isometric games where characters move in any direction.

**Character Art:** Transform modern character designs into retro 16-bit pixel art style for profile pictures or social media content.

**Animation Reference:** Generate character reference sheets showing all 8 viewing angles for consistent animation work.

## Tips for Best Results

- **Character images** work best when the character is clearly visible with a simple or transparent background
- **Reference images** should show the pixel art style you admire—perhaps from a game you love
- **Custom prompts** let you add specific requests, like "make the hair more spiky" or "add a cape"
- **Consistent style** comes from using the same reference image across multiple characters

## What You Get

The final output is a single image file containing all 8 character views arranged in a grid. This format is:

- Ready to import into game engines
- Suitable for animation software
- Easy to split into individual frames if needed
- Perfect for character reference sheets