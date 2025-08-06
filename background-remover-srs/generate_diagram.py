#!/usr/bin/env python3
"""
Script to generate a visual representation of the Background Remover Use Case Diagram
Since PlantUML server is not accessible, this creates a text-based visual diagram
"""

import os

def create_text_diagram():
    diagram = """
╔══════════════════════════════════════════════════════════════════════════════════╗
║                    Background Remover Application - Use Case Diagram            ║
╚══════════════════════════════════════════════════════════════════════════════════╝

    Actors:                                    System Boundary
    ┌─────────────┐                           ┌────────────────────────────────────┐
    │ Basic User  │◄──────────────────────────┤                                    │
    └─────────────┘                           │  ┌─── Core Functionality ────┐     │
           △                                  │  │ • Upload Image             │     │
           │                                  │  │ • Process Image            │     │
           │                                  │  │ • Download Processed Image │     │
    ┌─────────────┐                           │  │ • Preview Image            │     │
    │Professional │                           │  │ • Monitor Processing       │     │
    │    User     │◄──────────────────────────┤  └────────────────────────────┘     │
    └─────────────┘                           │                                    │
                                              │  ┌── Background Management ──┐     │
    ┌─────────────┐                           │  │ • Remove Background        │     │
    │    Admin    │◄──────────────────────────┤  │ • Replace with Solid Color │     │
    └─────────────┘                           │  │ • Replace with Custom Image│     │
                                              │  │ • Select Predefined Bg     │     │
    ┌─────────────┐                           │  └────────────────────────────┘     │
    │   System    │◄──────────────────────────┤                                    │
    └─────────────┘                           │  ┌──── User Management ───────┐     │
                                              │  │ • User Registration         │     │
                                              │  │ • User Login               │     │
                                              │  │ • View Processing History   │     │
                                              │  │ • Manage Subscription      │     │
                                              │  └────────────────────────────┘     │
                                              │                                    │
                                              │  ┌── Professional Features ──┐     │
                                              │  │ • Batch Processing         │     │
                                              │  │ • Advanced Background Opts │     │
                                              │  │ • Unlimited Usage          │     │
                                              │  │ • Custom Processing        │     │
                                              │  └────────────────────────────┘     │
                                              │                                    │
                                              │  ┌───── Administrative ──────┐     │
                                              │  │ • Manage Users             │     │
                                              │  │ • Monitor System Performance│     │
                                              │  │ • Handle Support Requests  │     │
                                              │  │ • System Maintenance       │     │
                                              │  └────────────────────────────┘     │
                                              │                                    │
                                              │  ┌───── System Features ─────┐     │
                                              │  │ • Auto-delete Images       │     │
                                              │  │ • Cloud Storage Integration│     │
                                              │  │ • API Integration          │     │
                                              │  │ • AI Processing Engine     │     │
                                              │  └────────────────────────────┘     │
                                              └────────────────────────────────────┘

Key Relationships:
═══════════════

• Professional User ──extends──► Basic User
• Upload Image ──extends──► Upload from Local Storage, Upload from URL  
• Download Processed Image ──extends──► Download as PNG, Download as JPEG
• Process Image ──includes──► AI Processing Engine, Monitor Processing Status
• Background Management Use Cases ──includes──► Process Image
• Batch Processing ──includes──► Process Image, Remove Background
• Cloud Storage Integration ──includes──► Auto-delete Images
• Upload/Download ──includes──► Cloud Storage Integration

Actor Descriptions:
═════════════════

🔹 Basic User: Individual users who upload images for background removal
🔹 Professional User: Power users with advanced features and batch processing
🔹 Admin: System administrators managing the platform and users
🔹 System: Automated components including AI engine and cloud storage
"""
    return diagram

def main():
    # Create the text-based diagram
    diagram_content = create_text_diagram()
    
    # Save to a text file
    with open('use-case-diagram.txt', 'w', encoding='utf-8') as f:
        f.write(diagram_content)
    
    print("Text-based use case diagram created successfully!")
    print("File: use-case-diagram.txt")

if __name__ == "__main__":
    main()