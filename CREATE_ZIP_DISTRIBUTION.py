#!/usr/bin/env python3
"""
Script to create a zip distribution of the Auctionator addon.

This script packages the Auctionator addon into a zip file that can be
directly downloaded for distribution to users.

Usage:
    python3 CREATE_ZIP_DISTRIBUTION.py
"""

import zipfile
import os
from pathlib import Path


def create_addon_zip(project_dir=None, output_filename="Auctionator.zip"):
    """
    Create a zip file containing the Auctionator addon.
    
    Args:
        project_dir: The project root directory (defaults to script location's parent)
        output_filename: The name of the output zip file
    
    Returns:
        Path to the created zip file
    """
    if project_dir is None:
        project_dir = Path(__file__).parent
    else:
        project_dir = Path(project_dir)
    
    auctionator_dir = project_dir / "Auctionator"
    output_zip = project_dir / output_filename
    
    if not auctionator_dir.exists():
        raise FileNotFoundError(f"Auctionator directory not found at {auctionator_dir}")
    
    # Create zip file with compression
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(auctionator_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(project_dir)
                zipf.write(file_path, arcname)
    
    file_size_mb = output_zip.stat().st_size / 1024 / 1024
    print(f"✓ Created {output_zip.name} successfully")
    print(f"✓ File size: {file_size_mb:.2f} MB")
    print(f"✓ Path: {output_zip}")
    
    return output_zip


if __name__ == "__main__":
    try:
        zip_file = create_addon_zip()
        print("\nZip file is ready for distribution!")
    except Exception as e:
        print(f"✗ Error creating zip file: {e}")
        exit(1)
