## Set Up Environment

1. Download and install [latest version of git](https://git-scm.com/downloads).
2. Clone the repository locally
     ```shell script
    $ git clone https://github.com/Diaga/python-candidate-challenge.git
    $ cd python-candidate-challenge
    ```
3. Create a virtualenv.
    ```shell script
    $ python3 -m venv venv
    $ . venv/bin/activate
    ```
    On Windows, activating is different.
    ```shell script
    $ venv/Scripts/activate
    ```
4. Install requirements.
    ```shell script
    $ pip install -r requirements.txt
    ```
5. Run migrations.
    ```shell script
    $ python manage.py migrate
    ```
6. Add flickr api keys to your environment variables.
   ```shell script
   FLICKR_API_KEY={YOUR_API_KEY}
   FLICK_SECRET={YOUR_SECRET}
   ```
7. Start django server locally
   ```shell script
    $ python manage.py runserver
    ```

## Requirements
For requirements, see [CHALLENGE.md](https://github.com/Diaga/python-candidate-challenge/blob/main/CHALLENGE.md)