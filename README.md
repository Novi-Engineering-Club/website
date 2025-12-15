# Website CMS

A simple Flask-based CMS that serves HTML pages generated from Markdown.

## Setup

1.  Install dependencies:
    ```bash
    uv sync
    ```
    Or with pip:
    ```bash
    pip install -r requirements.txt
    ```

2.  (Optional) Create a `.env` file to set the admin password:
    ```env
    ADMIN_PASSWORD=your_secure_password
    SECRET_KEY=your_secret_key
    ```
    Default password is `admin`.

## Usage

1.  Run the application:
    ```bash
    uv run src/main.py
    python src/main.py
    ```

2.  Open your browser:
    -   **Site:** [http://localhost:5000](http://localhost:5000)
    -   **Admin:** [http://localhost:5000/admin](http://localhost:5000/admin)

## Features

-   **Markdown Editing:** Create and edit pages using Markdown in the admin interface.
-   **Dynamic Navigation:** Navigation is automatically generated from the page structure.
-   **Page Priority:** Set priority to control the order of pages in the navigation.
-   **File-based:** Content is stored as HTML files in the `pages/` directory.
