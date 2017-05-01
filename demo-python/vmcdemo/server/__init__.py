import connexion

from .. import spec_dir, spec_file


app = connexion.App(__name__, specification_dir=spec_dir)
print(spec_dir, spec_file)
app.add_api(spec_file,
            resolver=connexion.RestyResolver("vmcdemo.server.controller"))
app.run(port=8080)
