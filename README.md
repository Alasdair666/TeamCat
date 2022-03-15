# TeamCat

## Initialize the development environment

1. install poetry - `pip3 install poetry` or `nix-shell -I nixpkgs=https://nixos.org/channels/nixpkgs-unstable/nixexprs.tar.xz -p poetry`
2. install dependencies - `poetry install`
3. enter the virtual environment - `poetry shell`
4. `export FLASK_APP=main:app`
5. `export FLASK_ENV=development`
6. `flask run --reload` - --reload allows the app to automatically refresh on a code change.