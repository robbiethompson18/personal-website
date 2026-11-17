// Comments on a post. build.js renders the empty section (hidden, so a browser without JS
// shows nothing); this fills it from the site's Worker (worker/api.js) and posts new ones.
// No accounts: a comment is a name and plain text, public as soon as it is posted.
(() => {
  const section = document.querySelector(".comments");
  if (!section) return;
  const list = section.querySelector(".comment-list");
  const form = section.querySelector(".comment-form");
  const note = section.querySelector(".comment-status");
  const path = location.pathname;

  // localStorage can be blocked; then nothing is remembered and the form still works.
  const recall = (key) => {
    try {
      return localStorage.getItem(key) || "";
    } catch {
      return "";
    }
  };
  const remember = (key, value) => {
    try {
      localStorage.setItem(key, value);
    } catch {}
  };

  // Robbie's key marks his comments as the author's and lets him delete any comment. He
  // gives it to a browser once by opening any post with #author-key=<key> on the URL. A
  // fragment is never sent to a server, and it is taken off the URL straight away.
  const KEY_HASH = "#author-key=";
  if (location.hash.startsWith(KEY_HASH)) {
    remember("author-key", decodeURIComponent(location.hash.slice(KEY_HASH.length)));
    history.replaceState(null, "", path + location.search);
  }
  const key = recall("author-key") || undefined; // undefined: left out of the JSON
  form.elements.name.value = recall("comment-name") || (key ? "Robbie" : "");

  const post = (endpoint, body) => fetch(endpoint, { method: "POST", body: JSON.stringify(body) });

  // Everything a commenter typed goes in through textContent, never innerHTML, so it is
  // shown as the characters they typed and can't become markup.
  const el = (tag, className, text) => {
    const node = document.createElement(tag);
    node.className = className;
    node.textContent = text;
    return node;
  };

  function show(comment) {
    const item = el("li", "comment");
    const meta = el("p", "comment-meta");
    meta.append(el("span", "comment-name", comment.name));
    if (comment.author) meta.append(el("span", "comment-author", "author"));
    const when = el(
      "time",
      "comment-date",
      new Date(comment.created).toLocaleDateString("en-US", {
        year: "numeric",
        month: "short",
        day: "numeric",
      }),
    );
    when.dateTime = comment.created;
    meta.append(when);
    if (key) {
      const del = el("button", "comment-delete", "delete");
      del.type = "button";
      del.addEventListener("click", async () => {
        const res = await post("/api/comment/delete", { id: comment.id, key }).catch(() => null);
        if (res?.ok) item.remove();
      });
      meta.append(del);
    }
    item.append(meta, el("p", "comment-body", comment.body));
    list.append(item);
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const button = form.querySelector("button");
    const name = form.elements.name.value;
    button.disabled = true;
    note.textContent = "";
    const res = await post("/api/comment", {
      path,
      name,
      body: form.elements.body.value,
      key,
    }).catch(() => null);
    button.disabled = false;
    if (res?.status === 201) {
      show(await res.json());
      form.elements.body.value = "";
      remember("comment-name", name);
    } else {
      // 403 without a key is the one refusal a real reader can hit: Robbie's own name.
      note.textContent =
        res?.status === 403 && !key
          ? "That name is reserved. Pick another."
          : "That didn't post. Try again in a moment.";
    }
  });

  // The form is useful even if the list can't be loaded (and in local dev, where there is
  // no Worker), so show the section either way.
  fetch(`/api/comments?path=${encodeURIComponent(path)}`)
    .then((res) => (res.ok ? res.json() : []))
    .catch(() => [])
    .then((comments) => {
      comments.forEach(show);
      section.hidden = false;
      // A link to #comments (the notification email's) found nothing to scroll to while hidden.
      if (location.hash === "#comments") section.scrollIntoView();
    });
})();
