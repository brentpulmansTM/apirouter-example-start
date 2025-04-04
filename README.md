# APIRouter example
Using this repository, you will learn how to work with the APIRouter in FastAPI.

## Cloning the Repository

Clone the repository from GitHub:

```git
git clone <repository_url>
cd <repository_name>
```

## Setting up a virtual environment

It is a good practice to use a virtual environment to manage dependencies and avoid conflicts with system-wide packages. Follow these steps:

1. **Open the repository in PyCharm**

2. **Create a Virtual Environment**  
Execute the following command from your terminal:
   ```sh
   python -m venv .venv
   ```

   This creates a directory named `.venv` inside your project, which contains the virtual environment files.

3. **Activate the Virtual Environment**

   - **Windows:**
     ```sh
     .venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```sh
     source .venv/bin/activate
     ```

   After activation, your terminal prompt should change, indicating that you are working inside the virtual environment.

## Installing Dependencies

Once the virtual environment is activated, install all required libraries from `requirements.txt` by running:

```sh
pip install -r requirements.txt
```

This command installs all the packages listed in the `requirements.txt` file.

## Add a .env file

Add your own .env file to your repository. You can make use of the following content to start from and change the values to your own values (e.g. your own connection string to Neon).

```
DB_CONNECTION=your_neon_connection_string
DOCS_URL=/docs
ALLOWED_ORIGINS="http://localhost,https://localhost,http://127.0.0.1:8080,https://127.0.0.1:8080,https://mysite.netlify.app"
```
