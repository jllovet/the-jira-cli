import click

@click.command(name="project", help="Manage projects")
def project_cmd():
    raise click.UsageError("This command hasn't been implemented yet")