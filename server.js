import express from "express";
import cors from "cors";

const app = express(); // 👈 создаётся app СНАЧАЛА

// ======================
// MIDDLEWARE (ВОТ СЮДА)
// ======================
app.use(cors());        // 👈 разрешает React доступ к backend
app.use(express.json()); // 👈 позволяет читать JSON из request.body

// ======================
// ROUTES (пример)
// ======================
app.get("/bugs", (req, res) => {
    res.json([]);
});

// ======================
// START SERVER
// ======================
app.listen(5000, () => {
    console.log("Server running on http://localhost:5000");
});