import argparse


def read_user_cli_args():

    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
    )

    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Insira um ou mais URLs separadas por espaço"
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Leia URLs de um arquivo",
    )
    return parser.parse_args()


def display_check_result(result, url, error=""):
    print(f'Os status da "{url}" é:', end=" ")
    if result:
        print('"Status: Online!👍"')
    else:
        print(f'"Status: Offline?" 👎 \n  Erro: "{error}"')
