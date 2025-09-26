# Hand-Written Equation SolveR

A **Streamlit app** to solve hand-written equations using image upload and AI.

This project allows users to:

* Upload an image of a hand-written equation.
* Automatically process it using Cloudinary and OpenRouter AI.
* View the solution directly in the web app.

---

## Setup & Usage Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/Madipadige-ManishKumar/Hand-Written-equation-solver.git
cd Hand-Written-equation-solver
```

2. **Create a Python Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
```

Activate the virtual environment:

* **Windows:**

```bash
venv\Scripts\activate
```

* **macOS / Linux:**

```bash
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` File**

Make a copy of `demo-env`:

* **Windows:**

```bash
copy demo-env .env
```

* **macOS / Linux:**

```bash
cp demo-env .env
```

Open `.env` and replace the placeholder values with your credentials:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
CLOUDINARY_CLOUD_NAME=your_cloud_name
```

5. **Run the Streamlit App**

```bash
streamlit run app.py
```

* This will start the Streamlit server.
* Open your browser at the URL displayed in the terminal (usually `http://localhost:8501`).

6. **Use the App**

* Upload a hand-written equation image using the file uploader.
* Click **Solve**.
* View the solution and API resp
