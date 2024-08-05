# Buddytask

![Buddytask Logo](https://img.shields.io/badge/Django-Framework-blue) ![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Overview

**Buddytask** is a robust task manager web application built with the powerful Django Framework. This project delves deep into Django's MVT (Model-View-Template) architecture, showcasing seamless integration and functionality of various features and libraries.

## 🛠️ Key Features

- **MVT Architecture:** Explore Django’s MVT architecture for clean and maintainable code.
- **Crispy Forms:** Enhance form handling and presentation using crispy forms for a better user experience.
- **Gunicorn:** Utilize Gunicorn, a Python WSGI HTTP server, for efficient and scalable deployment.
- **Whitenoise Middleware:** Implement Whitenoise for serving static files directly from the Django application, improving performance and simplifying deployment.
- **Django Default Authentication:** Leverage Django's built-in authentication system for secure user management.
- **Environment Variables:** Manage sensitive data and configuration settings using `.env` files.
- **PostgreSQL Database:** Integrate PostgreSQL for robust and reliable data storage.
- **Railway Deployment:** Seamlessly deploy the application on the Railway platform, leveraging its ease of use and powerful features.

## 📦 Installation

To set up and run Buddytask locally, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Bolliboinapavansai/django_buddytask.git
    cd django_buddytask
    ```

2. **Set Up Your Environment:**

    Ensure you have Python 3.8 or later installed. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables:**

    Create a `.env` file in the root directory and add your environment variables:

    ```plaintext
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    ```

4. **Run Migrations:**

    Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application:**

    Open your browser and navigate to `http://localhost:8000` to view the application.

## 📜 Usage

Once the application is running, you can access and manage tasks via the web interface. Key functionalities include creating, updating, and deleting tasks, as well as managing user accounts.

**Screenshots:**


![image](https://github.com/user-attachments/assets/70bf4015-6194-4097-a33b-f425de5d098f)

![image](https://github.com/user-attachments/assets/af25d884-66a9-4ada-a4ac-1a4dc51db342)

![image](https://github.com/user-attachments/assets/a7eb7832-fe78-4d74-ba16-97dc876041aa)

![image](https://github.com/user-attachments/assets/d76cdd50-f25f-4cd3-93ef-be312d53e583)

![image](https://github.com/user-attachments/assets/225e69c1-61b1-40a2-b0b0-72c12d71dd4b)



**Deployed Web Link:**

You can access the deployed version of Buddytask at: [Buddytask Deployment](https://buddytask.up.railway.app/)

## 🤝 Contributing

Contributions are welcome! To contribute to Buddytask, please follow these steps:

1. **Fork the Repository:**
    Click the “Fork” button at the top right of this page.

2. **Create a Branch:**
    ```bash
    git checkout -b feature/your-feature
    ```

3. **Make Changes and Commit:**
    ```bash
    git add .
    git commit -m "Add your feature"
    ```

4. **Push to Your Fork:**
    ```bash
    git push origin feature/your-feature
    ```

5. **Create a Pull Request:**
    Go to the “Pull Requests” tab and submit a new pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📧 Contact

For questions or feedback, please reach out to [pavansai.bolliboina@gmail.com].

---

**Built with** 🛠️ [Django](https://www.djangoproject.com/), [Gunicorn](https://gunicorn.org/), [Whitenoise](http://whitenoise.evans.io/), and [PostgreSQL](https://www.postgresql.org/).






















