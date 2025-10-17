#!/bin/bash
echo "🌐 Django Server Access Information"
echo "================================================"

echo ""
echo "✅ Django server is now running!"
echo ""

# Get server IP (if possible)
echo "📋 Access your Django application at:"
echo ""

# Try to get external IP
if command -v curl &> /dev/null; then
    EXTERNAL_IP=$(curl -s ifconfig.me 2>/dev/null || curl -s ipinfo.io/ip 2>/dev/null || echo "your-server-ip")
else
    EXTERNAL_IP="your-server-ip"
fi

echo "🌐 Main Site:"
echo "   http://$EXTERNAL_IP:8000"
echo "   http://anvilu.com:8000 (if DNS is configured)"
echo ""

echo "👤 Admin Panel:"
echo "   http://$EXTERNAL_IP:8000/admin/"
echo "   http://anvilu.com:8000/admin/"
echo ""

echo "📧 Admin Credentials:"
echo "   Username: usadv27"
echo "   Email: esayasdesta00@gmail.com"
echo ""

echo "🔧 To hide the port number (:8000), you can:"
echo "1. Use Cloudflare Tunnel (recommended)"
echo "2. Set up port forwarding in cPanel"
echo "3. Use a reverse proxy"
echo ""

echo "💡 Quick Cloudflare Tunnel setup:"
echo "   chmod +x setup_anvilu_tunnel.sh"
echo "   ./setup_anvilu_tunnel.sh"
echo ""

echo "🛑 To stop the server:"
echo "   Press Ctrl+C in the terminal where Django is running"
