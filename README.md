Mowglipedia - Notes Sharing Website
A collaborative platform for students to upload and download academic notes. This project aims to simplify access to educational resources by allowing students to share their notes with each other.



Table of Contents
About the Project
Features
Tech Stack
Getting Started
Prerequisites
Installation
Environment Variables
Run Migrations
Running the Application
Usage
Contributing
License
Contact
About the Project
Mowglipedia is a Django-based web application designed for students to share their academic notes. It provides a centralized platform where students can easily upload, download, and search for study materials. The system also includes an admin approval process to ensure the quality and relevance of uploaded notes.


Features
 User authentication (Sign up, Login, Logout)
 Notes upload functionality
 Admin approval for uploaded notes
 Downloadable notes after admin approval
 Search and filter by subject or category
 User profile to manage uploaded notes
Tech Stack
Django - Web framework
Python - Backend logic
PostgreSQL / SQLite - Database for storing users and notes data
HTML / CSS / JavaScript - Frontend technologies
Bootstrap - Responsive UI framework
Getting Started
Follow these instructions to get a copy of the project running on your local machine.

Prerequisites
You need to have Python and Django installed on your system. Make sure you have pip and virtualenv available:

bash
Copy code
# Install virtualenv if you don't have it
pip install virtualenv
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/mowglipedia.git
cd mowglipedia
Create and activate a virtual environment:
bash
Copy code
virtualenv venv
source venv/bin/activate  # For MacOS/Linux
# or
venv\Scripts\activate      # For Windows
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Environment Variables
Create a .env file in the project root and add the following environment variables:

bash
Copy code
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost/dbname  # Use SQLite URL for development
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password
Run Migrations
Apply database migrations to set up the database structure:

bash
Copy code
python manage.py migrate
Running the Application
Start the Django development server:

bash
Copy code
python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/.

Usage
Uploading Notes
Register an account and log in.
Navigate to the "Upload Notes" section from the dashboard.
Fill out the form with the necessary details (subject, description, file).
After admin approval, your notes will be available for other users to download.
Downloading Notes
Browse or search for notes by subject or category.
Download available notes once they have been approved by the admin.
Admin Panel
Admins can review, approve, or reject uploaded notes. To access the admin panel, create a superuser:

bash
Copy code
python manage.py createsuperuser
Visit http://127.0.0.1:8000/admin/ to log in and manage notes.

Contributing
We welcome contributions! To contribute:

Fork the repository
Create a new branch (git checkout -b feature/NewFeature)
Make your changes and commit (git commit -m 'Add some NewFeature')
Push to your branch (git push origin feature/NewFeature)
Open a pull request
Guidelines
Ensure your code follows Django best practices.
Write clear commit messages.
Test your changes before submitting a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Dhruv Rohatgi – rohatgidhruv28@gmail.com

Project Link: [(https://github.com/Courage003/Notes-Making-Application)](https://notes-making-application-production.up.railway.app/)
