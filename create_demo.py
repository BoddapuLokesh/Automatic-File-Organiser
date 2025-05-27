#!/usr/bin/env python3
"""
Demo script to test the File Organizer GUI
Creates a temporary demo directory with sample files for testing
"""

import os
import tempfile
from pathlib import Path

def create_demo_files():
    """Create a temporary directory with sample files for testing the organizer."""
    
    # Create temporary directory
    demo_dir = Path(tempfile.mkdtemp(prefix="file_organizer_demo_"))
    print(f"🎯 Created demo directory: {demo_dir}")
    
    # Sample files to create with realistic content
    sample_files = [
        # Documents
        ("annual_report.pdf", "📄 Sample PDF document for testing"),
        ("meeting_notes.docx", "📝 Important meeting notes and action items"),
        ("budget_2025.xlsx", "📊 Financial spreadsheet with quarterly data"),
        ("project_plan.pptx", "📈 Project timeline and milestones"),
        ("contacts.csv", "📋 Customer contact information database"),
        ("readme.txt", "📖 Instructions and documentation"),
        
        # Images  
        ("vacation_sunset.jpg", "🌅 Beautiful sunset photo from vacation"),
        ("team_photo.png", "👥 Company team building event photo"),
        ("logo_design.svg", "🎨 Vector graphics logo design"),
        ("app_icon.ico", "📱 Application icon for desktop app"),
        ("screenshot.webp", "📸 Website screenshot for documentation"),
        
        # Videos
        ("family_vacation.mp4", "🎬 Home video from summer vacation"),
        ("tutorial_demo.avi", "🎥 Software tutorial and demonstration"),
        ("presentation_recording.mov", "📹 Recorded video presentation"),
        ("conference_talk.mkv", "🎤 Conference presentation recording"),
        
        # Music & Audio
        ("favorite_song.mp3", "🎵 Popular music track"),
        ("podcast_episode.wav", "🎙️ Technology podcast episode"),
        ("interview_audio.m4a", "🗣️ Recorded interview audio"),
        ("sound_effect.ogg", "🔊 Game sound effect audio"),
        
        # Archives
        ("project_backup.zip", "📦 Complete project backup archive"),
        ("old_photos.rar", "🖼️ Compressed photo collection"),
        ("source_code.tar.gz", "💻 Compressed source code package"),
        ("documents.7z", "📁 Highly compressed document archive"),
        
        # Code & Development
        ("main_script.py", "🐍 # Python application main entry point\nprint('Hello, World!')"),
        ("website.html", "🌐 <!DOCTYPE html><html><head><title>Demo</title></head><body><h1>Sample Website</h1></body></html>"),
        ("styles.css", "🎨 /* Modern CSS styles */\nbody { font-family: 'Segoe UI', sans-serif; }"),
        ("app.js", "⚡ // JavaScript application logic\nconsole.log('App initialized');"),
        ("config.json", "⚙️ {\"version\": \"1.0\", \"debug\": true}"),
        
        # Executables & Installers
        ("software_installer.exe", "💿 Windows application installer"),
        ("update_package.msi", "🔄 Software update package"),
        ("mobile_app.apk", "📱 Android application package"),
        ("mac_application.dmg", "🍎 macOS application disk image"),
        
        # Miscellaneous & Unknown
        ("custom_data.xyz", "❓ Proprietary data format file"),
        ("backup_config.bak", "💾 Configuration backup file"),
        ("temp_file.tmp", "🗂️ Temporary processing file"),
        ("readme", "📚 Documentation without extension"),  # no extension
        ("important_notes", "📝 Important notes without extension"),  # no extension
    ]
    
    # Create sample files with content
    created_count = 0
    for filename, description in sample_files:
        file_path = demo_dir / filename
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"{description}\n\n")
                f.write(f"This is a sample {filename} file created for testing the File Organizer.\n")
                f.write(f"Created automatically by the demo script.\n")
                f.write(f"File type: {file_path.suffix or 'No extension'}\n")
                f.write(f"Timestamp: {file_path.stat().st_mtime}\n")
            created_count += 1
        except Exception as e:
            print(f"⚠️  Could not create {filename}: {e}")
    
    print(f"\n✅ Successfully created {created_count} sample files:")
    print("📄 Documents: PDF, DOCX, XLSX, PPTX, CSV, TXT")
    print("🖼️ Images: JPG, PNG, SVG, ICO, WEBP") 
    print("🎬 Videos: MP4, AVI, MOV, MKV")
    print("🎵 Audio: MP3, WAV, M4A, OGG")
    print("📦 Archives: ZIP, RAR, TAR.GZ, 7Z")
    print("💻 Code: PY, HTML, CSS, JS, JSON")
    print("⚙️ Executables: EXE, MSI, APK, DMG")
    print("❓ Unknown: XYZ, BAK, TMP, (no extension)")
    
    print(f"\n🎯 Demo directory ready: {demo_dir}")
    print("📋 Copy this path and use it in the File Organizer GUI!")
    print("🚀 Run: python file_organizer_gui.py")
    
    # Also print path for easy copying
    print(f"\n📋 Path to copy:")
    print(f"    {demo_dir}")
    
    return demo_dir

if __name__ == "__main__":
    print("🎉 File Organizer Demo Setup")
    print("=" * 50)
    create_demo_files()
    print("=" * 50)
    print("💡 Next steps:")
    print("   1. Copy the demo directory path above")
    print("   2. Run: python file_organizer_gui.py")
    print("   3. Click 'Browse' and paste the path")
    print("   4. Click 'Scan Files' to preview organization")
    print("   5. Click 'Organize Files' to see the magic! ✨")
