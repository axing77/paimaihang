# Auctionator Addon Distribution Guide

## Direct ZIP Download

The Auctionator addon is now available as a direct ZIP download for easy distribution and installation.

### File Information

- **Filename**: `Auctionator.zip`
- **Size**: ~0.84 MB
- **Format**: ZIP archive (compressed)
- **Contents**: Complete Auctionator addon folder structure

### Installation Instructions

#### Option 1: Manual Installation

1. **Download** the `Auctionator.zip` file from the repository

2. **Extract** the ZIP file:
   - On Windows: Right-click → Extract All
   - On macOS: Double-click to auto-extract
   - On Linux: `unzip Auctionator.zip`

3. **Locate your WoW AddOns folder**:
   - Windows: `C:\Program Files (x86)\World of Warcraft\_retail_\Interface\AddOns\`
   - macOS: `/Applications/World of Warcraft/_retail_/Interface/AddOns/`
   - Linux: `~/.wine/drive_c/Program\ Files\ \(x86\)/World\ of\ Warcraft/_retail_/Interface/AddOns/`
   - For Classic: Replace `_retail_` with `_classic_`, `_classic_era_`, or `_wrath_` as appropriate

4. **Copy the Auctionator folder** extracted from the ZIP into your AddOns folder

5. **Restart World of Warcraft** to load the addon

#### Option 2: Using a Download Manager

You can include this link in automation scripts or download managers:

```
https://[repository-url]/releases/download/Auctionator.zip
```

### Updating the ZIP Distribution

When the addon source code is modified, regenerate the ZIP file using the included script:

```bash
python3 CREATE_ZIP_DISTRIBUTION.py
```

This will:
- Create/update `Auctionator.zip` with the latest addon files
- Display the file size and confirmation message
- Compress all files in the Auctionator folder

### File Structure

After extraction, you should have:

```
World of Warcraft/_retail_/Interface/AddOns/
└── Auctionator/
    ├── Auctionator.toc
    ├── Source/
    ├── Source_Classic/
    ├── Source_LegacyAH/
    ├── Source_Mainline/
    ├── Source_ModernAH/
    ├── Source_Vanilla/
    ├── Libs/
    ├── Libs_ModernAH/
    ├── Locales/
    ├── Imports_*/
    ├── Assets_*/
    ├── Data_*/
    ├── Images/
    ├── Patches/
    └── [other addon files]
```

### Compatibility

The Auctionator addon supports:
- World of Warcraft Retail (Mainline)
- WoW Classic Era
- TBC Classic
- Wrath of the Lich King Classic
- And other supported game versions

The ZIP contains version-specific source files for each game version.

### Troubleshooting

**AddOn doesn't appear in-game:**
- Ensure it's extracted to the correct AddOns folder
- Restart World of Warcraft completely
- Check that the folder is named exactly `Auctionator`
- Verify `Auctionator.toc` file exists in the root of the extracted folder

**Old version still loads:**
- Delete the old `Auctionator` folder from your AddOns directory
- Extract the new ZIP file fresh
- Clear WoW's cache folder if problems persist

### Distribution Notes

- The ZIP file contains the complete addon
- No additional configuration is needed after extraction
- The addon includes both modern and legacy auction house support
- All localization files are included

### Version Information

- Current Distribution Format: ZIP
- Last Updated: December 2024
- Addon Version: See `Auctionator.toc` for version info

---

For more information about the addon itself, see [README.md](README.md)
