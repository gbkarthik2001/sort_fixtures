import click
import os
from subprocess import check_output


@click.command("reorder-fixtures", help="Reorder JSON fixtures based on sort-by fields using jq")
@click.option("--app", required=True, help="App for which reordering is required")
@click.option("--sort-by", default=".dt,.fieldtdtype", help="Sort-by args for jq")
@click.option("--descending", is_flag=True, help="Sort in descending order")

def reorder_fixtures(app, sort_by, descending):
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
                # If --descending is set, add reverse to the jq command
                jq_command = f"jq --indent 1 --raw-output '[.[]] | sort_by({sort_by})"
                if descending:
                    jq_command += " | reverse"
                jq_command += f"' {file_path}"

                # Run the jq command
                result = check_output(
                    jq_command, shell=True, cwd=os.getcwd()
                )
                
                # Write the result back to the file
                with open(file_path, "wb") as f:
                    f.write(result)
                print(f"Successfully reordered {file_path} \n")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")


commands = [reorder_fixtures]
