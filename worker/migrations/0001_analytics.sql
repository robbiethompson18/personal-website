-- First-party analytics, aggregates only. Days are UTC, 'YYYY-MM-DD'.

-- Page views. referrer is the referring hostname, '' for none, 'internal' for the site itself.
CREATE TABLE views (
  day      TEXT NOT NULL,
  path     TEXT NOT NULL,
  referrer TEXT NOT NULL,
  count    INTEGER NOT NULL,
  PRIMARY KEY (day, path, referrer)
) WITHOUT ROWID;

-- One row per visitor per page per day; unique visitors = COUNT(*). visitor is a hash of
-- IP + User-Agent salted with that day's row in salts, so it means nothing on any other day.
CREATE TABLE visitors (
  day     TEXT NOT NULL,
  path    TEXT NOT NULL,
  visitor TEXT NOT NULL,
  PRIMARY KEY (day, path, visitor)
) WITHOUT ROWID;

-- Same shape as visitors: the key is what caps likes at one per visitor per page per day.
CREATE TABLE likes (
  day     TEXT NOT NULL,
  path    TEXT NOT NULL,
  visitor TEXT NOT NULL,
  PRIMARY KEY (day, path, visitor)
) WITHOUT ROWID;

-- The random salt for the current day. Only ever holds one row: the Worker deletes older
-- ones when it creates today's, after which earlier hashes cannot be recomputed from an IP.
CREATE TABLE salts (
  day  TEXT PRIMARY KEY,
  salt TEXT NOT NULL
) WITHOUT ROWID;
