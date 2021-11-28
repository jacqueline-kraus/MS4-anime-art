import os

os.environ.setdefault('SECRET_KEY', 'insert-secret-key')
os.environ.setdefault('DEBUG', 'True')
os.environ.setdefault('SITE_NAME', 'insert-site-name')
os.environ.setdefault('DATABASE_URL', 'insert-data-url')
os.environ.setdefault('STRIPE_PUBLIC_KEY', 'insert-stripe-public-key')
os.environ.setdefault('STRIPE_SECRET_KEY', 'insert-stripe-secret-key')
os.environ.setdefault('STRIPE_WH_SECRET', 'insert-stripe-webhook-secret')
os.environ.setdefault('EMAIL_HOST_PASS', 'insert-email-host-password')
os.environ.setdefault('EMAIL_HOST_USER', 'insert-host-user')