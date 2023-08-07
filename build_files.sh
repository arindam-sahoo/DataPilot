
echo " BUILD START"
python -m pip install -r requirements.txt
cd datapilot
python manage.py collectstatic --noinput --clear
echo " BUILD END"
