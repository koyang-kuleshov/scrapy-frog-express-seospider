import csv
import os


class ExpressSeoPipeline():
    title_duplicates = set()
    description_duplicates = set()
    header_1_duplicates = set()

    def __init__(self):
        self.filename = os.path.join('output', 'output.csv')
        self.csv_file = open(self.filename, 'a', newline='', encoding='UTF-8')

    def __def__(self):
        self.csv_file.close()

    def process_item(self, item, spider):
        writer = csv.writer(self.csv_file, delimiter=',')
        row = [item.get("url"), item.get("status_code")]
        if item.get('title') not in self.title_duplicates:
            title = [item.get("title"), len(item.get("title")), '0']
            self.title_duplicates.add(item.get('title'))
        else:
            title = [item.get("title"), len(item.get("title")), '1']
        if item.get('description') not in self.description_duplicates:
            description = [
                item.get("description"),
                len(item.get("description")),
                '0'
                ]
            self.description_duplicates.add(item.get('description'))
        else:
            description = [
                item.get("description"),
                len(item.get("description")),
                '1'
                ]
        head_1_len = len(item.get('header_1'))
        if head_1_len == 1:
            header_1 = ''.join(item.get("header_1"))
            if header_1 not in self.header_1_duplicates:
                self.header_1_duplicates.add(header_1)
                header_1 = [header_1, f'{len(header_1)}', '0']
            else:
                header_1 = [header_1, f'{len(header_1)}', '1']
        else:
            header_1 = ';'.join(item.get("header_1"))
            if header_1 not in self.header_1_duplicates:
                self.header_1_duplicates.add(header_1)
                header_1 = [header_1, f'{head_1_len}', '0']
            else:
                self.header_1_duplicates.add(header_1)
                header_1 = [header_1, f'{head_1_len}', '1']
        row += title + description + header_1
        writer.writerow(row)
        return item
