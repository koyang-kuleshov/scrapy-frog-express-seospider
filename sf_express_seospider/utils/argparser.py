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
    namespace = parser.parse_args()
    params = {
        'domain': namespace.domain,
        'quick': namespace.q__quick,
    }
    return params


if __name__ == "__main__":
    read_params()
