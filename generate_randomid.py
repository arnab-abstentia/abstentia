import argparse
import random
from os.path import join
from settings import output_dir

def generate_radom_uid(num_uuid, len_uuid):
    chars = list('abcdefghijklmnopqrstuvwxyz0123456789')
    uids = set()
    while len(uids) < num_uuid:
        choice = random.choices(chars, k=len_uuid)
        uids.add(''.join(choice))
    return uids

if __name__=="__main__":
    argument_parser = argparse.ArgumentParser()
    
    argument_parser.add_argument('--num_uuid', type=int, default=20_000_000)
    argument_parser.add_argument('--len_uuid', type=int, default=8)
    argument_parser.add_argument('--num_cols', type=int, default=20)
    argument_parser.add_argument('--csv_fname', type=str, default='random_uuid.csv')

    parse_args = argument_parser.parse_args()

    num_uuid = parse_args.num_uuid
    len_uuid = parse_args.len_uuid
    num_cols = parse_args.num_cols
    csv_fname = parse_args.csv_fname
    
    csv_fpath = join(output_dir, csv_fname)

    uid_container = list(generate_radom_uid(num_uuid, len_uuid))
    # creating batch of 20 rows
    container_batch = [uid_container[x:x+num_cols] for x in range(0, len(uid_container), num_cols)]
    # reducing memory footprint by deleting the set object
    del uid_container
    # writing the csv file
    with open(csv_fpath, 'w') as fd:
        while len(container_batch) > 0:
            batch = container_batch.pop()
            fd.write(','.join(batch))
            fd.write('\n')
