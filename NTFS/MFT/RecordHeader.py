class RecordHeader:
    def __init__(self, data: bytes) -> None:
        self.magic_number: bytes = data[0:4]
        if self.magic_number != b"FILE":
            self.good_mft = False
            return
        else:
            self.good_mft = True
        self.update_sequence_offset: int = int.from_bytes(data[4:6], 'little')
        self.update_sequence_size: int = int.from_bytes(data[6:8], 'little')
        self.logfile_sequence_number: int = int.from_bytes(
            data[8:16], 'little')
        self.sequence_number: int = int.from_bytes(data[16:18], 'little')
        self.hard_link_count: int = int.from_bytes(data[18:20], 'little')
        self.first_attr_offset: int = int.from_bytes(data[20:22], 'little')
        self.flags: int = int.from_bytes(data[22:24], 'little')
        self.is_in_use: bool = self.check_in_use()
        self.is_directory: bool = self.check_is_directory()
        self.is_extension: bool = self.check_is_extension()
        self.is_special_index: bool = self.check_is_special_index()
        self.real_size: int = int.from_bytes(data[24:28], 'little')
        self.allocated_size: int = int.from_bytes(data[28:32], 'little')
        self.reference_to_base_record: int = int.from_bytes(
            data[32:40], 'little')
        self.next_attribute_id: int = int.from_bytes(data[40:42], 'little')
        self.allignment_padding: bytes = data[42:44]
        self.mft_record_id: int = int.from_bytes(data[42:46], 'little')
        self.update_sequence_number: int = int.from_bytes(
            data[46:48], 'little')
        self.update_sequence_array: bytes = data[48:48 +
                                                 ((self.update_sequence_size*2) - 2)]

    def check_in_use(self) -> bool:
        return bool(self.flags & (1 << 0))

    def check_is_directory(self) -> bool:
        return bool(self.flags & (1 << 1))

    def check_is_extension(self) -> bool:
        return bool(self.flags & (1 << 2))

    def check_is_special_index(self) -> bool:
        return bool(self.flags & (1 << 3))

    def __str__(self) -> str:
        if self.good_mft:
            record_string = f"""
                                Magic: {self.magic_number}, 
                                Update Sequence Offset: {self.update_sequence_offset}
                                Update Sequence Size: {self.update_sequence_size}
                                Logfile Sequence Number: {self.logfile_sequence_number}
                                Sequence Number: {self.sequence_number}
                                Hard Link Count: {self.hard_link_count}
                                First Attribute Offset: {self.first_attr_offset}
                                Record is In Use: {self.is_in_use}
                                Record is Dir: {self.is_directory}
                                Record is Extension: {self.is_extension}
                                Record is Special: {self.is_special_index}
                                Record Real Size: {self.real_size}
                                Record Allocated Size: {self.allocated_size}
                                Base Record: {self.reference_to_base_record}
                                Next Attr ID: {self.next_attribute_id}
                                Allignment Padding: {self.allignment_padding}
                                Record ID: {self.mft_record_id}
                                Update Sequence Number: {self.update_sequence_number}
                                Update Sequence Array: {self.update_sequence_array}
            """
        else:
            record_string = "BAD MFT"
        return record_string