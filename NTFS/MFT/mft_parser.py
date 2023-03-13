import argparse
import os
from Record import Record


def parse_args() -> argparse.Namespace:
    args = argparse.ArgumentParser(
        prog="MFT Parser", description="Parses $MFT File")
    args.add_argument('--mft_path', action='store',
                      required=True, help="Path to $MFT")
    return args.parse_args()


def dump_mft(path: str):
    with open(path, 'rb') as f:
        record_offset = 0
        while record_offset < os.stat(path).st_size:
            mft_record = Record(f.read(1024), record_offset)
            print(mft_record.record_id)
            print(str(mft_record.record_header))
            record_offset += 1024


def main():
    args = parse_args()
    dump_mft(args.mft_path)


if __name__ == "__main__":
    main()
