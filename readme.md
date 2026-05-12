# Nistula Technical Assessment - Bhoomi Ladia

### Setup Instructions
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file based on `.env.example`.
4. Run the server: `uvicorn app.main:app --reload`.

### Confidence Scoring Logic
The confidence score is calculated by the LLM based on **Context Matching**. 
- **1.0 (High):** The query is explicitly answered in the `PROPERTY_CONTEXT` (e.g., WiFi password).
- **0.5 (Medium):** The query is related to the context but requires inference (e.g., asking for a late check-out when only standard check-out is listed).
- **< 0.5 (Low):** The query is outside the scope of the context or is a high-emotion complaint where the AI should not provide a definitive resolution.