#!/usr/bin/env python3
"""
Generate a PNG use case diagram for the Background Remover application
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_use_case_diagram():
    # Create a large canvas
    width, height = 1400, 1000
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a system font, fallback to default
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        header_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
        normal_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        normal_font = ImageFont.load_default()
    
    # Colors
    actor_color = '#E8F4FD'
    usecase_color = '#FFF2CC'
    system_boundary_color = '#D5E8D4'
    line_color = '#000000'
    
    # Title
    title = "Background Remover Application - Use Case Diagram"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_width) // 2, 20), title, fill='black', font=title_font)
    
    # System boundary
    system_x, system_y = 200, 80
    system_w, system_h = 1100, 850
    draw.rectangle([system_x, system_y, system_x + system_w, system_y + system_h], 
                   outline=line_color, fill=None, width=2)
    draw.text((system_x + 10, system_y + 10), "Background Remover Application", 
              fill='black', font=header_font)
    
    # Actors (left side)
    actors = [
        ("Basic User", 50, 200),
        ("Professional User", 50, 350),
        ("Admin", 50, 500),
        ("System", 50, 650)
    ]
    
    actor_boxes = []
    for actor, x, y in actors:
        # Draw actor box
        bbox = draw.textbbox((0, 0), actor, font=normal_font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        box_width = text_width + 20
        box_height = text_height + 20
        
        draw.rectangle([x, y, x + box_width, y + box_height], 
                       outline=line_color, fill=actor_color)
        draw.text((x + 10, y + 10), actor, fill='black', font=normal_font)
        actor_boxes.append((actor, x + box_width // 2, y + box_height // 2, x + box_width, y + box_height // 2))
    
    # Use case packages
    packages = [
        ("Core Functionality", 250, 120, [
            "Upload Image", "Process Image", "Download Processed Image", 
            "Preview Image", "Monitor Processing Status"
        ]),
        ("Background Management", 250, 280, [
            "Remove Background", "Replace Background with Solid Color",
            "Replace Background with Custom Image", "Select Predefined Background"
        ]),
        ("User Management", 250, 440, [
            "User Registration", "User Login", "View Processing History", "Manage Subscription"
        ]),
        ("Professional Features", 680, 120, [
            "Batch Processing", "Advanced Background Options", 
            "Unlimited Usage", "Custom Processing Settings"
        ]),
        ("Administrative", 680, 280, [
            "Manage Users", "Monitor System Performance", 
            "Handle Support Requests", "System Maintenance"
        ]),
        ("System Features", 680, 440, [
            "Auto-delete Images", "Cloud Storage Integration", 
            "API Integration", "AI Processing Engine"
        ])
    ]
    
    use_case_centers = []
    
    for package_name, pkg_x, pkg_y, use_cases in packages:
        # Package boundary
        pkg_width = 400
        pkg_height = 140
        draw.rectangle([pkg_x, pkg_y, pkg_x + pkg_width, pkg_y + pkg_height], 
                       outline=line_color, fill=system_boundary_color, width=1)
        draw.text((pkg_x + 5, pkg_y + 5), package_name, fill='black', font=header_font)
        
        # Use cases within package
        uc_x, uc_y = pkg_x + 10, pkg_y + 25
        for i, use_case in enumerate(use_cases):
            row = i // 2
            col = i % 2
            x = uc_x + col * 190
            y = uc_y + row * 25
            
            # Draw ellipse for use case
            ellipse_width = 180
            ellipse_height = 20
            draw.ellipse([x, y, x + ellipse_width, y + ellipse_height], 
                        outline=line_color, fill=usecase_color)
            
            # Center text in ellipse
            text_bbox = draw.textbbox((0, 0), use_case, font=normal_font)
            text_width = text_bbox[2] - text_bbox[0]
            text_x = x + (ellipse_width - text_width) // 2
            text_y = y + 5
            draw.text((text_x, text_y), use_case, fill='black', font=normal_font)
            
            # Store center for connections
            center_x = x + ellipse_width // 2
            center_y = y + ellipse_height // 2
            use_case_centers.append((use_case, center_x, center_y, package_name))
    
    # Draw connections from actors to use cases
    connections = [
        ("Basic User", ["Upload Image", "Process Image", "Download Processed Image", 
                       "Preview Image", "Remove Background", "User Registration", "User Login"]),
        ("Professional User", ["Batch Processing", "Advanced Background Options", 
                              "Unlimited Usage", "Custom Processing Settings"]),
        ("Admin", ["Manage Users", "Monitor System Performance", 
                  "Handle Support Requests", "System Maintenance"]),
        ("System", ["Auto-delete Images", "Cloud Storage Integration", 
                   "API Integration", "AI Processing Engine"])
    ]
    
    for actor_name, connected_use_cases in connections:
        actor_info = next((a for a in actor_boxes if a[0] == actor_name), None)
        if actor_info:
            actor_x, actor_y = actor_info[3], actor_info[4]
            
            for use_case_name in connected_use_cases:
                uc_info = next((uc for uc in use_case_centers if uc[0] == use_case_name), None)
                if uc_info:
                    uc_x, uc_y = uc_info[1], uc_info[2]
                    draw.line([actor_x, actor_y, uc_x, uc_y], fill=line_color, width=1)
    
    # Add legend
    legend_y = height - 120
    draw.text((50, legend_y), "Legend:", fill='black', font=header_font)
    
    # Actor legend
    draw.rectangle([50, legend_y + 20, 120, legend_y + 40], outline=line_color, fill=actor_color)
    draw.text((125, legend_y + 25), "Actor", fill='black', font=normal_font)
    
    # Use case legend
    draw.ellipse([50, legend_y + 50, 120, legend_y + 70], outline=line_color, fill=usecase_color)
    draw.text((125, legend_y + 55), "Use Case", fill='black', font=normal_font)
    
    # Package legend
    draw.rectangle([50, legend_y + 80, 120, legend_y + 100], outline=line_color, fill=system_boundary_color)
    draw.text((125, legend_y + 85), "Package/System Boundary", fill='black', font=normal_font)
    
    return img

def main():
    # Generate the diagram
    diagram = create_use_case_diagram()
    
    # Save as PNG
    diagram.save('use-case-diagram.png', 'PNG', dpi=(300, 300))
    print("Use case diagram PNG created successfully!")
    
    # Also save as high quality
    diagram.save('use-case-diagram-hq.png', 'PNG', optimize=True, dpi=(300, 300))
    print("High quality PNG also created!")

if __name__ == "__main__":
    main()