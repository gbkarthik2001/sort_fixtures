import click
import os
from subprocess import check_output


@click.command("reorder-fixtures", help="Reorder JSON fixtures based on sort-by fields using jq")
@click.option("--app", required=True, help="App for which reordering is required")
@click.option("--sort-by", default=".dt,.fieldname", help="Sort-by args for jq")
def reorder_fixtures(app, sort_by):
    print(f"Reordering JSON fixtures with {sort_by} for {app} \n")
    
    fixtures_dir = os.path.join(os.getcwd(), "..", "apps", app, app, "fixtures")
    
    if not os.path.isdir(fixtures_dir):
        print(f"Fixtures directory not found: {fixtures_dir}")
        return
    
    for filename in os.listdir(fixtures_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(fixtures_dir, filename)
            print(f"Processing {file_path}")
            
            try:
                result = check_output(
                    f"jq --indent 1 --raw-output '[.[]] | sort_by({sort_by})' {file_path}",
                    shell=True, cwd=os.getcwd()
                )
                with open(file_path, "wb") as f:
                    f.write(result)
                print(f"Successfully reordered {file_path} \n")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

commands = [reorder_fixtures]