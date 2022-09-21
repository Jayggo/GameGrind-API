from .users.routes import ns as users_ns
from .auth.routes import ns as auth_ns
from .games.routes import ns as games_ns

namespaces = [users_ns,auth_ns, games_ns]
