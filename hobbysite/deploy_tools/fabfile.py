from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

# Based on fabfile use in TDD, but with a separate work are
# for the changes needed after the git clone. It also allows
# just DJANGO_PROJECT_ROOT to be copied to the live site

# name given for 'django-admin.py startproject' 
# (assuming nothing changed to source)
DJANGO_NAME='hobbysite'

# Attempt to follow two scoops three tiered directory
REPOSITORY_ROOT="hobbysite_project"
DJANGO_PROJECT_ROOT="hobbysite"  # TDD renamed this source
CONFIGURATION_ROOT="hobbysite"

#
# github repo url
REPO_URL = 'https://github.com/bobm123/hobbysite_project.git'


def deploy():
    work_folder = '/home/%s/work' % env.user
    site_url = 'balsachips.net'
    site_dir = 'hobbysite-staging'
    #site_dir = 'balsachips-live'
   
    #site_root = '/home/%s/sites/%s' % (env.user, env.host)
    site_root = '/home/%s/sites/%s' % (env.user, site_dir)
    source_folder = site_root + '/%s' % (DJANGO_NAME,)
    _create_directory_structure_if_necessary(site_root)
    _get_latest_source(work_folder)
    _update_settings(work_folder, site_url)
    #if not exists(django_project_root):
    #    run('ln -s %s/TDD/source %s' % (work_folder, site_root))
    run('cp -r %s/hobbysite_project/hobbysite %s' % (work_folder, site_root))
    _update_virtualenv(django_project_root)
    _update_static_files(django_project_root)
    _update_database(django_project_root)


def _create_directory_structure_if_necessary(site_root):
    proj_folders = ('database', 'static', 'virtualenv', DJANGO_NAME)
    for pf in proj_folders:
        run('mkdir -p %s/%s' % (site_root, pf))

        
def _get_latest_source(work_folder):
    if exists(work_folder + '/.git'):
        run('cd %s && git fetch' % (work_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, work_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (work_folder, current_commit))


def _update_settings(work_folder, site_name=env.host):
    configuration_root = work_folder + 'hobbysite_project/hobbysite/hobbysite'
    settings_path = configuration_root + '/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False") 
    sed(settings_path, 'DOMAIN = "localhost"', 'DOMAIN = "%s"' % (site_name,))
    secret_key_file = configuration_root + '/secret_key.py'
    if not exists(secret_key_file): 
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_virtualenv(source_folder):
    virtualenv_folder = '/home/ubuntu/sites/balsachips-staging/virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' % (
            virtualenv_folder, source_folder
    ))


def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' % (
        source_folder,
    ))


def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinput' % (
        source_folder,
    ))

