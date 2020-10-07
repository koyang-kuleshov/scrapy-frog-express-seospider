"""Reads command line arguments to run crawler"""
import argparse


def read_params():
    parser = argparse.ArgumentParser(
        prog='Scrapy Frog Express Seospider',
        description='Reads command line arguments to run crawler')
    parser.add_argument('domain', type=str, help='Type domain')
    parser.add_argument(
                        '-q'
                        '--quick',
                        action='store_true',
                        help=(
                            'Quick scan sitemap.xml and swow number of pages'
                            )
                        )
    parser.add_argument(
                        '-t'
                        '--tree',
                        action='store_true',
                        help=(
                            'Scan site for structure of pages and categories'
                            )
                        )
    namespace = parser.parse_args()
    params = {
        'domain': namespace.domain,
        'quick': namespace.q__quick,
        'tree': namespace.t__tree
    }
    return params


if __name__ == "__main__":
    read_params()
