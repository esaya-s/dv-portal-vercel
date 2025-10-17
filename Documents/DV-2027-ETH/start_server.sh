#!/bin/bash
echo "🚀 Starting DV Portal Server..."
echo "================================================"

echo ""
echo "🔧 Starting server on all interfaces..."

# Start Django server on all interfaces
python manage.py runserver 0.0.0.0:8000

echo ""
echo "🌐 Server is now accessible at:"
echo "  - http://localhost:8000"
echo "  - http://127.0.0.1:8000" 
echo "  - http://your-server-ip:8000"
echo "  - http://yourdomain.com:8000"
echo ""
echo "👤 Admin Panel: http://yourdomain.com:8000/admin/"
echo "   Username: usadv27"
echo "   Email: esayasdesta00@gmail.com"
echo ""
echo "Press Ctrl+C to stop the server"
