# Setup Instructions

After cloning this repo,

## Frontend

Enter the 'frontend' directory in a terminal session (`cd frontend`) and then run:

```bash
npm run dev
```

to set up the development server. By default it runs at _localhost:5173_

## Backend

Enter the 'backend' directory in a separate terminal (`cd backend`) session and then run:

```bash
python3 -m venv venv
```

Followed by:

```bash
source venv/bin/activate
```

This is to create and activate a virtual environment. Next step is to install the required dependencies by running:

```bash
pip install -r requirements.txt
```

Now, let's set up the Uvicorn server at _localhost:8000_ (or some other availabe port):

```bash
uvicorn main:app --reload --port 8000
```