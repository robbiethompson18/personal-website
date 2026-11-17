-- Comments on posts. No accounts: name is whatever the commenter typed. name and body are
-- stored exactly as cleaned up by worker/api.js and are plain text, never HTML.
CREATE TABLE comments (
  id      INTEGER PRIMARY KEY AUTOINCREMENT, -- AUTOINCREMENT: a deleted comment's id is never reused
  path    TEXT NOT NULL,                     -- '/blog/<slug>/'
  name    TEXT NOT NULL,
  body    TEXT NOT NULL,
  created TEXT NOT NULL,                     -- UTC, ISO 8601
  author  INTEGER NOT NULL DEFAULT 0,        -- 1: posted with Robbie's key
  -- The same daily salted hash as visitors.visitor. It is here so one spammer's comments
  -- from one day can be deleted together; it means nothing on any other day.
  visitor TEXT NOT NULL
);

CREATE INDEX comments_by_path ON comments (path, id);
