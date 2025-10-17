#!/bin/bash
echo "🔍 Checking hosting provider options for anvilu.com..."
echo "================================================"

echo ""
echo "📋 Let's check what options are available on your server:"
echo ""

# Check if we can bind to port 80
echo "1. Testing port 80 access..."
if timeout 1 bash -c "</dev/tcp/localhost/80" 2>/dev/null; then
    echo "   ✅ Port 80 is accessible"
else
    echo "   ❌ Port 80 is not accessible (requires root)"
fi

# Check available ports
echo ""
echo "2. Checking available ports..."
netstat -tuln | grep LISTEN | head -10

# Check if there's a web server running
echo ""
echo "3. Checking for existing web server..."
if pgrep -f "apache\|nginx\|httpd" > /dev/null; then
    echo "   ✅ Web server is running"
    echo "   💡 You can configure it to proxy to your Django app"
else
    echo "   ❌ No web server found"
fi

# Check for Python web server capabilities
echo ""
echo "4. Checking Python web server options..."
python3 -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('0.0.0.0', 80))
    print('   ✅ Can bind to port 80')
    s.close()
except PermissionError:
    print('   ❌ Cannot bind to port 80 (permission denied)')
except Exception as e:
    print(f'   ⚠️ Error: {e}')
"

echo ""
echo "📋 Recommendations:"
echo "1. Try: chmod +x try_port_80.sh && ./try_port_80.sh"
echo "2. Use Cloudflare Tunnel: chmod +x setup_anvilu_tunnel.sh && ./setup_anvilu_tunnel.sh"
echo "3. Use ngrok: chmod +x setup_ngrok_tunnel.sh && ./setup_ngrok_tunnel.sh"
echo "4. Check your hosting control panel for port forwarding options"
