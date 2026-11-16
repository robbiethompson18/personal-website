// The site's Cloudflare Worker. Static files are served straight from the asset store
// without running this; only the routes in wrangler.jsonc's `run_worker_first` land here.

import { api } from "./api.js";

export default {
  async fetch(request, env) {
    if (new URL(request.url).pathname.startsWith("/api/")) return api(request, env);
    return serveWithRanges(request, env);
  },
};

// Cloudflare's asset store ignores Range headers: it answers 200 with the whole file.
// iOS Safari refuses to play a <video> unless the server answers 206, so video requests
// are routed here and the byte range is cut out by hand. Clips are a few MB, so
// buffering one in memory is fine.
async function serveWithRanges(request, env) {
  const headers = new Headers(request.headers);
  headers.delete("Range");
  const asset = await env.ASSETS.fetch(
    new Request(request.url, { method: request.method, headers }),
  );

  const range = /^bytes=(\d*)-(\d*)$/.exec(request.headers.get("Range") || "");
  const wantsRange = range && (range[1] !== "" || range[2] !== "");
  if (asset.status !== 200 || request.method !== "GET" || !wantsRange) {
    const res = new Response(asset.body, asset);
    res.headers.set("Accept-Ranges", "bytes");
    return res;
  }

  const body = await asset.arrayBuffer();
  const size = body.byteLength;
  // "bytes=-500" means the last 500 bytes; "bytes=100-" means from 100 to the end.
  const start = range[1] === "" ? Math.max(size - Number(range[2]), 0) : Number(range[1]);
  const end = range[1] === "" || range[2] === "" ? size - 1 : Math.min(Number(range[2]), size - 1);

  const resHeaders = new Headers(asset.headers);
  resHeaders.set("Accept-Ranges", "bytes");
  if (start >= size || start > end) {
    resHeaders.set("Content-Range", `bytes */${size}`);
    return new Response(null, { status: 416, headers: resHeaders });
  }
  resHeaders.set("Content-Range", `bytes ${start}-${end}/${size}`);
  resHeaders.set("Content-Length", String(end - start + 1));
  return new Response(body.slice(start, end + 1), { status: 206, headers: resHeaders });
}
