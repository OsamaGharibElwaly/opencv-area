# update_readme_links.py
import re
import os
import shutil

# Configuration
README_FILE = "README.md"  # Your README file name
GITHUB_RAW_BASE = "https://github.com/OsamaGharibElwaly/opencv-area/raw/main/images"

# All directories to handle
DIRECTORIES = [
    '02-core-operations',
    '03-image-processing',
    '03-image-processing/03-image-thresholding',
    '03-image-processing/04-smoothing-images',
    '03-image-processing/05-morphological-transformations',
    '03-image-processing/06-image-gradients',
    '03-image-processing/07-canny-edge-detection',
    '03-image-processing/08-image-pyramids',
    '03-image-processing/09-contours',
    '03-image-processing/10-histograms',
    '03-image-processing/12-template-matching',
    '03-image-processing/13-hough-line-transform',
    '03-image-processing/14-hough-circle-transform',
    '03-image-processing/15-watershed-segmentation',
    '03-image-processing/16-grabcut-foreground-extraction',
    '03-image-processing/01-changing-colorspaces',
    '04-feature-detection',
    '04-feature-detection/02-harris-corner-detection',
    '04-feature-detection/04-sift-features',
    '04-feature-detection/08-orb-features',
    '04-feature-detection/09-feature-matching',
    '05-camera-calibration',
    '06-machine-learning',
    '06-machine-learning/kmeans',
    '07-computational-photography',
    '08-object-detection',
    '99-miscellaneous',
]

def create_backup(filepath):
    """Create backup of original file"""
    backup_path = f"{filepath}.backup"
    shutil.copy2(filepath, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def convert_all_urls(content):
    """Convert ALL image URLs to GitHub raw format"""
    
    # Pattern for any URL starting with https://images/ followed by any path
    # This matches: https://images/02-core-operations/xxx.jpg
    #              https://images/03-image-processing/.../xxx.jpg
    #              https://images/04-feature-detection/xxx.jpg
    #              https://images/05-camera-calibration/xxx.jpg
    #              https://images/06-machine-learning/xxx.jpg
    #              https://images/07-computational-photography/xxx.jpg
    #              https://images/08-object-detection/xxx.jpg
    #              https://images/99-miscellaneous/xxx.jpg
    
    # Pattern for URLs in markdown images: ![alt](url)
    def replace_markdown_image(match):
        alt_text = match.group(1)
        old_url = match.group(2)
        
        if 'https://images/' in old_url:
            # Extract everything after 'https://images/'
            path = old_url.replace('https://images/', '')
            new_url = f"{GITHUB_RAW_BASE}/{path}"
            return f'![{alt_text}]({new_url})'
        return match.group(0)
    
    # Pattern for URLs not in markdown syntax
    def replace_plain_url(match):
        old_url = match.group(0)
        
        # Skip if already a GitHub URL
        if 'github.com' in old_url:
            return old_url
        
        # Skip if not our old pattern
        if 'https://images/' not in old_url:
            return old_url
        
        # Extract path and convert
        path = old_url.replace('https://images/', '')
        new_url = f"{GITHUB_RAW_BASE}/{path}"
        return new_url
    
    # Pattern for Result: format
    def replace_result(match):
        alt_text = match.group(1)
        old_url = match.group(2)
        
        if 'https://images/' in old_url:
            path = old_url.replace('https://images/', '')
            new_url = f"{GITHUB_RAW_BASE}/{path}"
            return f'Result: ![alt]({new_url})'
        return match.group(0)
    
    # Pattern for table links: [text](url)
    def replace_table_link(match):
        text = match.group(1)
        old_url = match.group(2)
        
        if 'https://images/' in old_url:
            path = old_url.replace('https://images/', '')
            new_url = f"{GITHUB_RAW_BASE}/{path}"
            return f'[{text}]({new_url})'
        return match.group(0)
    
    # Apply all conversions in order
    print("\n🔄 Converting image links...")
    
    # 1. Convert markdown images: ![alt](url)
    pattern_md_image = r'!\[([^\]]*)\]\(([^)]+)\)'
    content = re.sub(pattern_md_image, replace_markdown_image, content)
    print("   ✓ Markdown images converted")
    
    # 2. Convert Result: format
    pattern_result = r'Result:\s*!\[([^\]]*)\]\(([^)]+)\)'
    content = re.sub(pattern_result, replace_result, content)
    print("   ✓ Result patterns converted")
    
    # 3. Convert table links: [text](url)
    pattern_table = r'\[([^\]]+)\]\(([^)]+)\)'
    content = re.sub(pattern_table, replace_table_link, content)
    print("   ✓ Table links converted")
    
    # 4. Convert plain URLs (last to avoid double conversion)
    pattern_plain = r'https://images/[^\s<>"\')\]]+'
    content = re.sub(pattern_plain, replace_plain_url, content)
    print("   ✓ Plain URLs converted")
    
    return content

def verify_conversion(content):
    """Verify that all old URLs were converted"""
    old_pattern = r'https://images/[^\s"\')\]]+'
    remaining = re.findall(old_pattern, content)
    
    if remaining:
        print(f"\n⚠️ Warning: {len(remaining)} old URLs still found:")
        for url in remaining[:5]:
            print(f"   • {url}")
        return False
    else:
        print("\n✅ All old URLs successfully converted!")
        return True

def show_statistics(content):
    """Show conversion statistics"""
    # Count new GitHub URLs
    github_pattern = r'https://github\.com/OsamaGharibElwaly/opencv-area/raw/main/images/[^\s"\')\]]+'
    new_urls = re.findall(github_pattern, content)
    
    # Group by directory
    stats = {}
    for url in new_urls:
        # Extract directory from URL
        match = re.search(r'/images/([^/]+(?:/[^/]+)?)', url)
        if match:
            dir_name = match.group(1)
            stats[dir_name] = stats.get(dir_name, 0) + 1
    
    print("\n📊 Conversion Statistics:")
    print("="*50)
    for dir_name, count in sorted(stats.items()):
        print(f"   {dir_name}: {count} images")
    print("="*50)
    print(f"   TOTAL: {len(new_urls)} images converted")
    
    return stats

def preview_changes():
    """Preview changes without saving"""
    print("="*60)
    print("🔍 DRY RUN - Preview changes only")
    print("="*60)
    
    if not os.path.exists(README_FILE):
        print(f"❌ Error: {README_FILE} not found!")
        return
    
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find old URLs
    old_pattern = r'https://images/[^\s"\')\]]+'
    old_urls = re.findall(old_pattern, content)
    
    if old_urls:
        print(f"\n📸 Found {len(old_urls)} old image URLs:")
        
        # Group by directory
        old_stats = {}
        for url in old_urls:
            match = re.search(r'https://images/([^/]+(?:/[^/]+)?)', url)
            if match:
                dir_name = match.group(1)
                old_stats[dir_name] = old_stats.get(dir_name, 0) + 1
        
        print("\n   Old URLs by directory:")
        for dir_name, count in sorted(old_stats.items()):
            print(f"   • {dir_name}: {count} images")
        
        print(f"\n🔄 Will convert to:")
        for url in old_urls[:5]:
            path = url.replace('https://images/', '')
            new_url = f"{GITHUB_RAW_BASE}/{path}"
            print(f"   • {new_url}")
        
        if len(old_urls) > 5:
            print(f"   ... and {len(old_urls) - 5} more")
        
        print(f"\n📊 Total URLs to convert: {len(old_urls)}")
    else:
        print("\n✅ No old image URLs found! Already converted.")

def main():
    print("="*60)
    print("🔧 OpenCV README Image Link Updater")
    print("   Converting all directories: 02, 03, 04, 05, 06, 07, 08, 99")
    print("="*60)
    
    # Check if README exists
    if not os.path.exists(README_FILE):
        print(f"❌ Error: {README_FILE} not found in current directory!")
        print(f"   Current directory: {os.getcwd()}")
        print("\n   Files found:")
        for f in os.listdir('.'):
            print(f"   • {f}")
        return
    
    # Create backup
    create_backup(README_FILE)
    
    # Read original content
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n📖 Read {len(content)} characters from {README_FILE}")
    
    # Convert all URLs
    new_content = convert_all_urls(content)
    
    # Verify conversion
    verify_conversion(new_content)
    
    # Show statistics
    stats = show_statistics(new_content)
    
    # Write updated content
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ Updated {README_FILE} with new GitHub raw URLs")
    
    print("\n" + "="*60)
    print("✅ Done! You can now commit and push to GitHub:")
    print("   git add README.md")
    print("   git commit -m 'Update all image links to GitHub raw URLs'")
    print("   git push")
    print("="*60)

def convert_specific_file(input_file, output_file=None):
    """Convert a specific markdown file"""
    global README_FILE
    README_FILE = input_file
    
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = convert_all_urls(content)
    
    output = output_file if output_file else input_file
    with open(output, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ Converted {input_file} -> {output}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--dry-run":
            preview_changes()
        elif sys.argv[1] == "--file" and len(sys.argv) > 2:
            convert_specific_file(sys.argv[2])
        else:
            print("Usage:")
            print("  python update_readme_links.py           # Run normal conversion")
            print("  python update_readme_links.py --dry-run # Preview changes only")
            print("  python update_readme_links.py --file <filename> # Convert specific file")
    else:
        main()