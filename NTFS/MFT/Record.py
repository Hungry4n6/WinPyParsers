from RecordHeader import RecordHeader


class Record:
    def __init__(self, data: bytes, offset) -> None:
        self.record_id = offset / 1024
        self.record_header = RecordHeader(data)
        
