import click
import os
import gsextract.gse_parser as gse_parser

def input_path(value):
    if value == '-':
        return value
    if not os.path.isfile(value):
        raise click.BadParameter('file does not exist')
    return value

@click.command()
@click.argument('input_file', callback=lambda ctx, param, value: input_path(value))
@click.argument('output_file', type=click.Path())
@click.option('--stream/--no-stream', default=False, help='Stream continuously from the file. Use the --stream flag to dump to a pcap from a real time GSE recording.')
@click.option('--reliable/--no-reliable', default=True, help='Add the --no-reliable flag to attempt to brute force IP headers in certain situations. Increases recovery but also can result in fake packets.')
@click.option('--format', 'input_format', type=click.Choice(['auto', 'b8', 'standard', 'ts']), default='auto', show_default=True, help='Input format: auto detects MPEG-TS or an inserted 0xB8 byte; ts extracts the BBFrame PID from MPEG-TS; b8 expects it; standard starts directly with the BBFrame header.')
def gsextract(input_file, output_file, stream, reliable, input_format):
    gse_parser.gse_parse(file=input_file, outfile=output_file, stream=stream, reliable=reliable, input_format=input_format)

def cli_runner():
    gsextract()
