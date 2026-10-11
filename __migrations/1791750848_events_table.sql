-- src/relevo/models/event
-- ID is generated in runtime by Python code (uuid4), not by the database
-- timestamp has default value CURRENT_TIMESTAMP
CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY NOT NULL,
  service_id TEXT NOT NULL,
  timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  url TEXT NOT NULL,
  body_payload TEXT,
  query_payload TEXT,

  CONSTRAINT fk_events_service
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Index for service-based queries (used by EventRepository.find_by_service_id)
CREATE INDEX IF NOT EXISTS idx_events_service_id
  ON events(service_id);

-- Index for timestamp-based queries (common filter pattern)
CREATE INDEX IF NOT EXISTS idx_events_timestamp
  ON events(timestamp);

-- Index for URL-based queries
CREATE INDEX IF NOT EXISTS idx_events_url
  ON events(url);
