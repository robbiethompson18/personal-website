# AI-generated images for posts

Written 2026-11-22 while illustrating `posts/rewilded-sf/` (twelve generated images, three real
photos).

## What Robbie picked

Five methods were run on every concept. Of the twelve final images, nine are GPT Image 2 and three
are Nano Banana 2.1.

- **GPT Image 2 and Nano Banana 2.1** are the two worth running. Start with both.
- **Gemini 3 Pro Image** and the **local FLUX.2 klein model** were never picked.
- **Python-painted images** (Claude writes code that paints every pixel): Robbie's verdict was
  "python claude always sucks dont use those". Don't offer them.
- His repeated notes were "more subtle", "more photorealistic", fewer people, fewer animals, smaller
  structures. Default to restraint in the first prompt: one or two small figures, nothing
  spectacular.
- Captions: none, except a before/after pair, which gets "Place, year" on each ("Hunters Point,
  2020" / "Hunters Point, 2040").

## How to generate

**GPT Image 2 through the Codex CLI.** Robbie's `codex` is logged in with his ChatGPT subscription
and has `image_generation` on (`codex features list`), so it costs nothing extra. About a minute per
image, 1536x1024 or 1024x1536, and six run fine in parallel.

```bash
codex exec --skip-git-repo-check -s workspace-write -C <work dir> -i <work dir>/photo.jpg - < prompt.txt
```

- Pass the prompt on stdin (the trailing `-`). `-i` takes a list of files, so a prompt placed after
  it is swallowed as a filename and Codex exits with "No prompt provided".
- Say in the prompt to use the built-in image generation tool, not a script, and to copy the result
  into the current directory. The image is first written to
  `~/.codex/generated_images/<session id>/`.

**Nano Banana 2.1 through OpenRouter** (`google/gemini-nano-banana-2.1`): POST to
`/api/v1/chat/completions` with `"modalities": ["image", "text"]`, input images as `image_url` data
URLs, and `"image_config": {"aspect_ratio": "3:2"}`. The image comes back base64 in
`choices[0].message.images`. About 12 seconds and a few cents each. Ask Robbie which OpenRouter key
to use: the one in the shell environment was out of credit on 2026-11-22.

**Local, if ever wanted:** `uv tool install mflux`, then `mflux-generate-flux2` /
`mflux-generate-flux2-edit --image-paths ...` with
`--model flux2-klein-4b -q 8 --low-ram --steps 4`. FLUX.2 klein 4B is Apache-2.0, a 16 GB download,
about a minute per image, and peaks near 11 GB, under the 16 GB oom-guard limit. `--low-ram`
matters: without it the peak was 13 GB.

## Techniques that worked

- **Before/after from a real photo:** attach the photo and write "Edit this photograph... keep the
  camera position, X, Y and Z exactly as they are", then describe the change. GPT Image 2 keeps the
  framing almost pixel-aligned. Nano Banana sometimes reframes.
- **Revising:** attach the previous output and ask for the one change ("remove only the three
  climbers nearest the camera", "halve the number of animals"). Much more reliable than rewriting
  the original prompt. Say what must stay, or the model removes too much: "at most two people" came
  back with nobody.
- **Scale in aerial shots:** state it outright ("every tree looks tiny from up here; an oak reaches
  a fifth of the crane's height"), or the trees come out enormous.
- **Text-only generation is fine for famous places.** Both models know the Painted Ladies, Oracle
  Park and Sutro Tower without a reference photo.

## What doesn't exist

- **Anthropic:** Claude models don't generate images.
- **Midjourney:** no public API, OpenRouter doesn't carry it, and Robbie has no subscription.

## Sources, licences, files

- Real photos: Wikimedia Commons through its API. It only serves standard thumbnail widths (use
  1920), and originals rate-limit hard (429 with a 600-second retry).
- CC BY-SA photos need a credit, and an AI edit of one is a derivative under the same licence, even
  when the real photo isn't shown. Since Robbie wants no captions, the credits go in one small
  `<span class="chart-src">` line at the end of the post.
- Convert outputs to JPEG at 1280 px on the long edge, quality 82 (about 250 KB), since each image
  lives in git twice (`posts/` and `blog/`). Re-saving through a fresh Pillow image strips EXIF and
  GPS.
- Put the images in a subfolder of the post (`gen/`) and keep the model, source photo and exact
  prompts in the post folder's `IMAGE_PROMPTS.md` (the build ignores every `.md` except
  `FINAL_POST.md`).
- When several agents share a scratch folder, give each its own subfolder. A helper script named
  `assemble.py` was overwritten by a subagent that picked the same name.
