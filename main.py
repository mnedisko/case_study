"""
Main entrypoint for The Dyrt web scraper case study.

Usage:
    The scraper can be run directly (`python main.py`) or via Docker Compose (`docker compose up`).

If you have any questions in mind you can connect to me directly via info@smart-maple.com
"""
from src.scapperdb import *
from src.create_tables import create_tables
import os

if __name__ == "__main__":
    print("Hello Smart Maple!")
    print("Fetching campgrounds...")
    # docker compose up
    os.system("docker compose up")
    print("Creating tables...")
    create_tables()

    fetch_campgrounds()
    print("Done!")


