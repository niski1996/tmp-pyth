import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="tmp_pyth",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="tmp_pyth_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from tmp_pyth.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export tmp_pyth_KEY=value
export tmp_pyth_KEY="@int 42"
export tmp_pyth_KEY="@jinja {{ this.db.uri }}"
export tmp_pyth_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
tmp_pyth_ENV=production tmp_pyth run
```

Read more on https://dynaconf.com
"""
