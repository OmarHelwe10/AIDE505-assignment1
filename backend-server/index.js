const express = require("express");
const axios = require("axios");
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.json());

const PORT = 3000;
const FLASK_API_URL = "http://127.0.0.1:5000/predict"; // Flask API endpoint


app.post("/analyze-sentiment", async (req, res) => {
    try {
        const  text = req.body;

        if (!text) {
            return res.status(400).json({ error: "Text is required" });
        }

        // Forward request to Flask API
        const response = await axios.post(FLASK_API_URL, { text });

        // Return Flask API response to the client
        res.json(response.data);
    } catch (error) {
        console.error("Error communicating with Flask API:", error.message);
        res.status(500).json({ error: "Failed to process sentiment analysis" });
    }
});

app.listen(PORT, () => {
    console.log(`Express server is running on http://127.0.0.1:${PORT}`);
});
