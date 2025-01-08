#!/usr/bin/env python3
import psutil
import sys
import argparse
from typing import List, Dict
import signal

def find_processes(name_pattern: str) -> List[Dict]:
    """
    Find processes matching the given name pattern.
    Returns a list of dictionaries containing process information.
    """
    matching_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if name_pattern.lower() in proc.info['name'].lower():
                matching_processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'username': proc.info['username']
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return matching_processes

def kill_process(pid: int, force: bool = False) -> bool:
    """
    Kill a process by PID.
    Returns True if successful, False otherwise.
    """
    try:
        process = psutil.Process(pid)
        if force:
            process.kill()  # SIGKILL
        else:
            process.terminate()  # SIGTERM
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def main():
    parser = argparse.ArgumentParser(description='Kill processes by partial name match')
    parser.add_argument('pattern', help='Pattern to match process names')
    parser.add_argument('-f', '--force', action='store_true',
                       help='Force kill processes (SIGKILL instead of SIGTERM)')
    parser.add_argument('-y', '--yes', action='store_true',
                       help='Skip confirmation')
    args = parser.parse_args()

    # Find matching processes
    matching_processes = find_processes(args.pattern)

    if not matching_processes:
        print(f"No processes found matching pattern: {args.pattern}")
        sys.exit(0)

    # Display matching processes
    print("\nMatching processes:")
    print("{:<8} {:<20} {}".format("PID", "Name", "User"))
    print("-" * 40)
    for proc in matching_processes:
        print("{:<8} {:<20} {}".format(
            proc['pid'], 
            proc['name'][:20], 
            proc['username']
        ))

    # Skip confirmation if --yes flag is used
    if not args.yes:
        confirm = input(f"\nKill {len(matching_processes)} matching process(es)? (y/N): ")
        if confirm.lower() != 'y':
            print("Operation cancelled.")
            sys.exit(0)

    # Kill processes
    success_count = 0
    fail_count = 0

    for proc in matching_processes:
        pid = proc['pid']
        if kill_process(pid, args.force):
            print(f"Successfully killed process {pid} ({proc['name']})")
            success_count += 1
        else:
            print(f"Failed to kill process {pid} ({proc['name']})")
            fail_count += 1

    # Print summary
    print(f"\nSummary: {success_count} process(es) killed, {fail_count} failed")
    if fail_count > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
