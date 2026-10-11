-- src/relevo/models/service
-- ID is generated in runtime by Python code (uuid4), not by the database
CREATE TABLE IF NOT EXISTS services (
  id TEXT PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,

  status INTEGER NOT NULL DEFAULT 1 CHECK(status IN (0, 1)),
  account_id TEXT NOT NULL,

  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Index for status-based queries (used by ServiceRepository.find_by_status)
CREATE INDEX IF NOT EXISTS idx_services_status
  ON services(status);

-- Index for account-based queries (used by ServiceRepository.find_by_id and relations)
CREATE INDEX IF NOT EXISTS idx_services_account_id
  ON services(account_id);

-- Index for active services queries (used by ServiceRepository.find_active)
CREATE INDEX IF NOT EXISTS idx_services_active
  ON services(status) WHERE status = 1;
