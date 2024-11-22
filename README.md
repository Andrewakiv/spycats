git clone [https://github.com/your-username/spycat-missions.git](https://github.com/Andrewakiv/spycats.git)

cd spycats

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Postman Link
https://www.postman.com/andrewakiv/69faaa24-9286-4d97-b987-0a825418e30e
