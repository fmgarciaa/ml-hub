c = get_config()  # noqa

# Port where JupyterHub will run
c.JupyterHub.port = 8000

# Directory where notebooks are stored
c.Spawner.notebook_dir = "/home/jupyter/notebooks"
c.Spawner.default_url = "/lab"

# Disable user authentication (anyone can access)
c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"
c.DummyAuthenticator.password = ""  # No password required

# Allow execution as the Jupyter user
c.JupyterHub.spawner_class = "simple"

# Optional: Disable the "Logout" button
c.JupyterHub.template_vars = {"login_error": "", "disable_logout": True}

c.Spawner.environment = {"NB_USER": "jupyter", "NB_UID": "1000", "NB_GID": "100"}

c.Spawner.args = ["--NotebookApp.allow_root=True"]
c.Spawner.http_timeout = 60
