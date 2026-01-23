#!/usr/bin/env python3
"""
Generate HTML preview page for all press package assets
"""

import os
from pathlib import Path

def generate_preview_html(output_dir='output/press-package'):
    """Generate HTML preview of all assets"""
    
    base_dir = Path(output_dir)
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RIFT Press Package - Asset Preview</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: system-ui, -apple-system, sans-serif;
            background: #0a1f1a;
            color: #ffffff;
            padding: 20px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        h1 {
            color: #fbbf24;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #10b981;
            margin-bottom: 40px;
            font-size: 1.2em;
        }
        .section {
            margin-bottom: 60px;
        }
        .section-title {
            color: #fbbf24;
            font-size: 1.8em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #0d4d3f;
        }
        .asset-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .asset-card {
            background: #0f3d32;
            border: 1px solid #065f46;
            border-radius: 8px;
            padding: 15px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .asset-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(251, 191, 36, 0.2);
            border-color: #fbbf24;
        }
        .asset-preview {
            width: 100%;
            height: 200px;
            background: #0a1f1a;
            border: 1px solid #065f46;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
            overflow: hidden;
        }
        .asset-preview svg,
        .asset-preview img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }
        .asset-name {
            color: #ffffff;
            font-size: 0.9em;
            font-weight: 600;
            margin-bottom: 5px;
            word-break: break-word;
        }
        .asset-path {
            color: #10b981;
            font-size: 0.75em;
            opacity: 0.7;
        }
        .info-box {
            background: #0d4d3f;
            border: 1px solid #10b981;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 40px;
        }
        .info-box h2 {
            color: #fbbf24;
            margin-bottom: 15px;
        }
        .info-box ul {
            list-style: none;
            padding-left: 0;
        }
        .info-box li {
            padding: 8px 0;
            border-bottom: 1px solid #065f46;
        }
        .info-box li:last-child {
            border-bottom: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 RIFT Press Package</h1>
        <p class="subtitle">Complete Marketing Asset Collection</p>
        
        <div class="info-box">
            <h2>📋 Asset Overview</h2>
            <ul>
                <li><strong>Enhanced Logos:</strong> Rift designs with integrated bike/cog elements</li>
                <li><strong>Social Media:</strong> Banners for Twitter, Facebook, Instagram</li>
                <li><strong>Ad Designs:</strong> Multiple variations with "Ride It" slogans</li>
                <li><strong>Overlays & Frames:</strong> Video overlays and frame templates</li>
                <li><strong>All Assets:</strong> Scalable SVG format for any size</li>
            </ul>
        </div>
'''

    # Find all SVG files
    svg_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.svg') and file != 'preview.html':
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                svg_files.append((rel_path, os.path.join(root, file)))
    
    # Group by category
    categories = {}
    for rel_path, full_path in svg_files:
        parts = rel_path.split(os.sep)
        if len(parts) > 1:
            category = parts[0]
        else:
            category = 'root'
        
        if category not in categories:
            categories[category] = []
        categories[category].append((rel_path, full_path))
    
    # Generate sections
    category_names = {
        'logos': '🎯 Enhanced Logos',
        'social-media': '📱 Social Media Assets',
        'ads': '📢 Ad Designs',
        'overlays': '🎬 Video Overlays',
        'frames': '🖼️ Frame Templates',
        'banners': '🎴 Banner Designs',
    }
    
    for category in sorted(categories.keys()):
        category_title = category_names.get(category, category.title())
        html_content += f'''
        <div class="section">
            <h2 class="section-title">{category_title}</h2>
            <div class="asset-grid">
'''
        
        for rel_path, full_path in sorted(categories[category]):
            # Read SVG content
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    svg_content = f.read()
                    # Extract just the SVG tag content (remove XML declaration if present)
                    if '<svg' in svg_content:
                        svg_start = svg_content.find('<svg')
                        svg_content = svg_content[svg_start:]
            except:
                svg_content = '<svg><text>Error loading</text></svg>'
            
            filename = os.path.basename(rel_path)
            html_content += f'''
                <div class="asset-card">
                    <div class="asset-preview">
                        {svg_content}
                    </div>
                    <div class="asset-name">{filename}</div>
                    <div class="asset-path">{rel_path}</div>
                </div>
'''
        
        html_content += '''
            </div>
        </div>
'''
    
    html_content += '''
    </div>
</body>
</html>
'''
    
    # Save preview
    preview_path = os.path.join(base_dir, 'preview.html')
    with open(preview_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Generated preview: {preview_path}")
    print(f"🌐 Open in browser: file://{os.path.abspath(preview_path)}")

if __name__ == '__main__':
    generate_preview_html()
