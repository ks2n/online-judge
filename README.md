# LTOJ: Le Thuy Online Judge

[![License](https://img.shields.io/badge/license-AGPL--3.0-blue)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![Python](https://img.shields.io/badge/python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04%20%7C%2022.04%20%7C%2024.04-E95420?logo=ubuntu&logoColor=white)](https://ubuntu.com/download)

Homepage: [https://ltoj.edu.vn](https://ltoj.edu.vn)

An online judge platform for competitive programming, based on [DMOJ](https://dmoj.ca/). Designed for Vietnamese high school and university students.

## Features

- Contest management with multiple formats (IOI, ICPC, custom scoring)
- Plagiarism detection via [Stanford MOSS](https://theory.stanford.edu/~aiken/moss/)
- User rating and performance tracking
- Real-time chat system
- Multi-language interface (Vietnamese / English)
- Dark/Light theme with modern Edu design system
- Organization and group management
- Problem recommendations via ML (collaborative filtering)

## Supported Languages

| Language | Versions |
|----------|----------|
| C | GCC |
| C++ | C++03, C++11, C++14, C++17, C++20, C++23 |
| Java | OpenJDK |
| Pascal | Free Pascal |
| Python | Python 2, Python 3, PyPy 2, PyPy 3 |
| Assembly | x64 |
| AWK | GNU AWK |
| Perl | Perl 5 |

## Quick Start (Docker)

The fastest way to get a development environment running:

```bash
git clone https://github.com/LQDJudge/online-judge.git
cd online-judge/.docker/dev-local
docker compose up -d
```

This starts 6 services:

| Service | Purpose | Port |
|---------|---------|------|
| web | Django dev server | 8001 |
| db | MariaDB 10.11 | 3306 (internal) |
| redis | Session/cache | 6379 (internal) |
| memcached | Django cache | 11211 (internal) |
| bridge | Judge relay | 9999 (internal) |
| judge | Code execution | — |

Access the site at **http://localhost:8001**. Default credentials: `admin` / `admin`.

### Common Docker Commands

```bash
# View logs
docker compose logs -f web

# Run Django management commands
docker compose exec web python3 manage.py migrate
docker compose exec web python3 manage.py createsuperuser

# Build SCSS
docker compose exec web bash -c "cd /code && bash make_style.sh && python3 manage.py collectstatic --noinput"

# Restart services
docker compose restart web
```

## Manual Installation

For development without Docker or for production deployment.

### Prerequisites

```bash
sudo apt update
sudo apt install git gcc g++ make python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev gettext curl redis-server pkg-config
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs
sudo npm install -g sass postcss-cli postcss autoprefixer
```

### Database Setup

Install MariaDB (≥ 10.5):

```bash
sudo apt install mariadb-server libmysqlclient-dev
```

Create the database:

```sql
sudo mysql
CREATE DATABASE dmoj DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci;
GRANT ALL PRIVILEGES ON dmoj.* TO 'dmoj'@'localhost' IDENTIFIED BY '<password>';
EXIT;
```

Load timezone data:

```bash
mariadb-tzinfo-to-sql /usr/share/zoneinfo | sudo mariadb -u root mysql
```

### Application Setup

```bash
python3 -m venv dmojsite
source dmojsite/bin/activate

git clone https://github.com/LQDJudge/online-judge.git
cd online-judge
git submodule init
git submodule update
pip3 install -r requirements.txt
pip3 install mysqlclient
pre-commit install
```

Create `dmoj/local_settings.py` from the sample:

```bash
cp dmoj/sample_local_settings.py dmoj/local_settings.py
# Edit local_settings.py with your database credentials
python3 manage.py check
```

### Build Assets

```bash
./make_style.sh
python3 manage.py collectstatic
python3 manage.py compilemessages
python3 manage.py compilejsi18n
```

### Initialize Database

```bash
python3 manage.py migrate
python3 manage.py loaddata navbar
python3 manage.py loaddata language_small
python3 manage.py loaddata demo
```

### Run Development Server

```bash
python3 manage.py runserver 0.0.0.0:8000
```

Access at **http://localhost:8000**.

## Testing

Create the test database:

```sql
sudo mysql
CREATE DATABASE test_dmoj DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci;
GRANT ALL PRIVILEGES ON test_dmoj.* TO 'dmoj'@'localhost';
FLUSH PRIVILEGES;
```

Run tests:

```bash
python3 manage.py test judge.tests --keepdb
```

## Development

### Updating Styles

Edit `.scss` files in `resources/`, then:

```bash
./make_style.sh && python3 manage.py collectstatic --noinput
```

Hard refresh browser (`Ctrl+Shift+R`) to see changes.

### Updating Translations

```bash
python3 manage.py makemessages -l vi
python3 manage.py makedmojmessages -l vi --no-mark-obsolete
# Edit locale/vi/*.po files
python3 manage.py compilemessages -l vi
python3 manage.py compilejsi18n -l vi
```

### Useful Aliases

```bash
alias pr='python3 manage.py runserver'
alias sd='source ~/dmojsite/bin/activate'
alias css='./make_style.sh && python3 manage.py collectstatic --noinput'
alias trans='python3 manage.py compilemessages -l vi && python3 manage.py compilejsi18n -l vi'
```

## Optional Components

### WebSocket (Live Updates)

For real-time features like chat:

```bash
cd websocket && npm install
node websocket/daemon.js
```

Add to `local_settings.py`:

```python
EVENT_DAEMON_KEY = 'ltoj'
EVENT_DAEMON_URL = 'http://127.0.0.1:15100'
EVENT_DAEMON_PUBLIC_URL = 'http://127.0.0.1:15100'
```

### Celery (Background Tasks)

```bash
celery -A dmoj_celery worker
```

### Judge (Manual Setup)

Install in a separate directory:

```bash
sudo apt install python3-dev python3-pip build-essential libseccomp-dev
git clone https://github.com/LQDJudge/judge-server.git
cd judge-server
sudo pip3 install -e .
```

Register a judge via Admin UI or CLI:

```bash
python3 manage.py addjudge <id> <key>
```

Run bridge and judge:

```bash
# Terminal 1: Bridge
python3 manage.py runbridged

# Terminal 2: Judge
dmoj -c judge.yml localhost
```

### Distributed Judges (JuiceFS)

For running judges across multiple servers with shared problem data via S3/R2. See [docs/juicefs-setup.md](docs/juicefs-setup.md).

### ML Recommendations

Problem recommendation system using collaborative filtering with MariaDB 11.7+ vector search. See [judge/ml/README.md](judge/ml/README.md).

## Production Deployment

Production uses Nginx + uWSGI + Supervisor + Docker (bridge/judges).

Key steps:
1. Set `DEBUG = False` and generate a strong `SECRET_KEY` in `local_settings.py`
2. Configure Nginx as reverse proxy ([sample_conf/nginx/](sample_conf/nginx/))
3. Configure uWSGI ([sample_conf/uwsgi.ini](sample_conf/uwsgi.ini))
4. Configure Supervisor for process management ([sample_conf/supervisor/](sample_conf/supervisor/))
5. Build and run Docker bridge (`.docker/bridge/`)
6. Build and run Docker judges (`.docker/judge/`)

For SSL: `sudo certbot --nginx -d <your-domain>`

For S3 media storage: `pip install django-storages[boto3]` and configure in `local_settings.py`.

Recommended cron jobs:

```crontab
0 4 * * * <venv>/bin/python3 <site>/manage.py cleanup_inactive --users --orgs
4 4 * * * <venv>/bin/python3 <site>/manage.py batch_clearsessions
7 4 * * * <venv>/bin/python3 <site>/manage.py recompute_comment_scores
10 4 * * * <venv>/bin/python3 <site>/manage.py delete_old_notifications
11 4 * * * <venv>/bin/python3 <site>/manage.py recompute_contributions
15 4 * * * <venv>/bin/python3 <site>/manage.py fix_organization_private
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Missing `local_settings.py` | Copy from `dmoj/sample_local_settings.py` |
| Missing problem/static folder | Create directories and configure paths in `local_settings.py` |
| Missing timezone data | Run `mariadb-tzinfo-to-sql /usr/share/zoneinfo \| sudo mariadb -u root mysql` |
| Missing chat secret key | Generate Fernet key: `python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"` |
| `mysqlclient` install fails | Try `pip3 install mysqlclient==2.1.1` |
| WSL: MariaDB not starting | Run `sudo service mysql restart` after each WSL session |

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for development workflow, commit conventions, and PR guidelines.

## License

This project is licensed under the [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html).

Based on [DMOJ/online-judge](https://github.com/DMOJ/online-judge) by the DMOJ team.
