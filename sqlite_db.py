import sqlite3


class SQLiteBackend:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        # --- players: current per-user state ---
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS players (
                uid            INTEGER PRIMARY KEY,
                points         INTEGER  DEFAULT 0,
                times_sniped   INTEGER  DEFAULT 0,
                rarity_value   INTEGER  DEFAULT 0,
                rarity_label   TEXT,
                last_sniped_at DATETIME
            )
            """
        )

        # --- snipes: history of every snipe event ---
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS snipes (
                snipe_id      INTEGER PRIMARY KEY AUTOINCREMENT,
                shooter_uid   INTEGER NOT NULL,
                target_uid    INTEGER NOT NULL,
                timestamp     DATETIME DEFAULT CURRENT_TIMESTAMP,
                success       BOOLEAN NOT NULL,
                image_url     TEXT NOT NULL,
                message_id    INTEGER,
                points_awarded INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (shooter_uid) REFERENCES players(uid),
                FOREIGN KEY (target_uid)  REFERENCES players(uid)
            )
            """
        )

        # --- game_stats: global info (one row) ---
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS game_stats (
                id           INTEGER PRIMARY KEY CHECK (id = 1),
                total_snipes INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self.conn.execute(
            "INSERT OR IGNORE INTO game_stats (id, total_snipes) VALUES (1, 0)"
        )

        self.conn.commit()

    def increment_total_snipes(self, increment=1):
        # Increment the total_snipes count
        self.conn.execute(
            "UPDATE game_stats SET total_snipes = total_snipes + ?", (increment,))
        self.conn.commit()
    
    def get_total_snipes(self):
        # Get the total_snipes count
        cursor = self.conn.execute("SELECT total_snipes FROM game_stats WHERE id = 1")
        result = cursor.fetchone()
        return result[0] if result else 0

