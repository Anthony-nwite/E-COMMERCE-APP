#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate

#postgresql://ecommerce_3qkp_user:i2gjHuZned1s1QXwUDo8q6blKZt426vu@dpg-dan5ombm8hqs73a5afi0-a/ecommerce_3qkp