const express = require('express');
const mariadb = require('mariadb');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Config of connection with MariaDB
const db = mariadb.createPool({
    host: 'localhost',
    user: 'root',
    password: 'pass', // Substituir
    database: 'base de dados', // Substituir
    connectionLimit: 5
});

// Testing connection
async function testConnection() {
    try {
        const conn = await db.getConnection();
        console.log("Connected to MariaDB!");
        conn.release();
    } catch (err) {
        console.error("Error while trying to connect to MariaDB:", err);
    }
}
testConnection();

app.get('/raspberry', async (req, res) => {
    try {
        const conn = await db.getConnection();
        const results = await conn.query('SELECT id, nome FROM raspberry_pis');
        conn.release();
        res.json(results);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.get('/raspberry/:id', async (req, res) => {
    const id = req.params.id;
    try {
        const conn = await db.getConnection();
        const results = await conn.query('SELECT * FROM raspberry_pis WHERE id = ?', [id]);
        conn.release();
        res.json(results[0]);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.get('/raspberry/:id/ping', async (req, res) => {
    const id = req.params.id;
    try {
        const conn = await db.getConnection();
        const results = await conn.query(
            'SELECT timestamp, latency FROM ping_data WHERE raspberry_id = ? ORDER BY timestamp DESC LIMIT 10',
            [id]
        );
        conn.release();
        res.json(results);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Run server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running port: ${PORT}`);
});
