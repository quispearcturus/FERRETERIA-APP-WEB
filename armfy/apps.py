DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # 'oauth2_provider',
    # 'rest_framework',
    # 'corsheaders',
]

ARMFY_APPS = [
    'apps.auths.apps.AuthsConfig',
    'apps.templifys.apps.TemplifysConfig',
    'apps.dashboards.apps.DashboardsConfig',
    'apps.products.apps.ProductsConfig',
    'apps.branches.apps.BranchesConfig',
    'apps.sales.apps.SalesConfig',
    'apps.customers.apps.CustomersConfig',
    'apps.suppliers.apps.SuppliersConfig',
]


ALL_APPS = DJANGO_APPS + THIRD_PARTY_APPS + ARMFY_APPS
