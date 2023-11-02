def tower_of_hanoi(disk, start, auxiliary, end) -> None:
    if disk == 1:
        print(f'Move disk {disk} from rod {start} to rod {end}')
        return

    tower_of_hanoi(disk - 1, start, end, auxiliary)
    print(f'Move disk {disk} from rod {start} to rod {end}')
    tower_of_hanoi(disk - 1, auxiliary, start, end)


if __name__ == '__main__':
    disk_count = int(input())
    tower_of_hanoi(disk_count, 'A', 'B', 'C')
