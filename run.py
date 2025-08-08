#!/usr/bin/env python
import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Project imports
from src.data_loader import load_data, get_project_root
from src.preprocessing import clean_data

def resolve_data_dir() -> Path:
    """
    Resolve the data directory using .env DATA_PATH if set, else <project_root>/data.
    Mirrors logic used by load_data so read/write are consistent.
    """
    load_dotenv()
    data_path_env = os.getenv("DATA_PATH")
    if data_path_env:
        return Path(data_path_env).expanduser().resolve()
    return get_project_root() / "data"

def cmd_preprocess(args: argparse.Namespace) -> int:
    """Load a raw CSV, clean it, and save to processed/."""
    df = load_data(args.input, subfolder=args.in_sub)
    if df.empty:
        print("✖ No rows loaded. Check that the input file exists and is non-empty.")
        return 1

    if args.head:
        try:
            n = int(args.head)
            print(df.head(n))
        except Exception:
            print(df.head())

    df_clean = clean_data(df)

    data_dir = resolve_data_dir()
    out_dir = data_dir / args.out_sub
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / args.output

    df_clean.to_csv(out_path, index=False)
    print(f"✔ Saved cleaned data to {out_path}")
    return 0

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Project pipeline CLI")
    sub = p.add_subparsers(dest="command", required=True)

    pp = sub.add_parser("preprocess", help="Clean a raw CSV and write to processed/")
    pp.add_argument("--input", "-i", required=True, help="Input filename in data/<in-sub>/ (e.g., people.csv)")
    pp.add_argument("--in-sub", default="raw", help="Input subfolder under data/ (default: raw)")
    pp.add_argument("--output", "-o", default="people_clean.csv", help="Output filename")
    pp.add_argument("--out-sub", default="processed", help="Output subfolder under data/ (default: processed)")
    pp.add_argument("--head", default=None, help="Print first N rows before cleaning (optional)")
    pp.set_defaults(func=cmd_preprocess)

    return p

def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
