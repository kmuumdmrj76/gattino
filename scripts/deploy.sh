cd .. 
#提交github
git pull origin
git push origin
#提交pypi
python setup.py sdist upload
