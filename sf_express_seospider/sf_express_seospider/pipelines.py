# import pudb; pudb.set_trace()
from itemadapter import ItemAdapter

import csv
import os


class SfExpressSeospiderPipeline:

    def process_item(self, item, spider):
        return item


class NodeWritePipeline():
    def __init__(self,):
        self.filename = os.path.join('output', 'output_structure.csv')
        with open(self.filename, 'r', newline='') as csv_file:
            self.tmp_data = csv.DictReader(csv_file).fieldnames

        self.csv_file = open(self.filename, 'a', newline='', encoding='UTF-8')

    def __def__(self):
        self.csv_file.close()

    def process_item(self, item, spider):
        writer = csv.writer(self.csv_file, delimiter=',')
        if not self.tmp_data:
            writer.writerow(('URL,Status,Node #1,Node #2,Node #3,Node #4,'
                            'Node #5,Node #6,Node #7').split(','))
            self.tmp_data = True
        row = f'{item.get("url")},{item.get("status_code")},'
        row = row + ','.join(item.get('nodes'))
        writer.writerow(row.split(','))
        return item
