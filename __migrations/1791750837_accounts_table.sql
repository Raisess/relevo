-- src/relevo/models/account
-- ID is generated in runtime by Python code (uuid4), not by the database
CREATE TABLE IF NOT EXISTS accounts (
  id TEXT PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,

  status INTEGER NOT NULL DEFAULT 1 CHECK(status IN (0, 1)),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  api_access_token TEXT NOT NULL
);

-- Index for status-based queries (used by AccountRepository.find_by_status)
CREATE INDEX IF NOT EXISTS idx_accounts_status
  ON accounts(status);

-- Index for email lookups (common query pattern)
CREATE UNIQUE INDEX IF NOT EXISTS uq_accounts_email
  ON accounts(LOWER(email));
