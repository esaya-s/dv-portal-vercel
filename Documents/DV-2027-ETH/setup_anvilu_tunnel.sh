#!/bin/bash
echo "🌐 Setting up Cloudflare Tunnel for anvilu.com (no port)..."
echo "================================================"

echo ""
echo "📋 This will make your Django app available at http://anvilu.com"
echo "   (without any port numbers)"
echo ""

# Check if cloudflared is available
if command -v cloudflared &> /dev/null; then
    echo "✅ Cloudflared is already installed"
else
    echo "📦 Installing Cloudflared..."
    
    # Download the latest cloudflared binary
    wget -O cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
    chmod +x cloudflared
    
    echo "✅ Cloudflared installed"
fi

echo ""
echo "🚀 Starting Django on port 8080 (internal)..."
# Start Django in background on port 8080
DJANGO_SETTINGS_MODULE=dv_portal.settings_production python manage.py runserver 127.0.0.1:8080 &
DJANGO_PID=$!

echo "✅ Django started on port 8080 (PID: $DJANGO_PID)"

echo ""
echo "🌐 Starting Cloudflare Tunnel..."
echo "This will create a public tunnel from anvilu.com to localhost:8080"

# Start Cloudflare tunnel
./cloudflared tunnel --url http://127.0.0.1:8080

echo ""
echo "🎉 Setup complete!"
echo "🌐 Your Django app is now available at: http://anvilu.com"
echo "👤 Admin panel: http://anvilu.com/admin/"
echo "📧 Username: usadv27"
echo ""
echo "💡 To stop the service:"
echo "kill $DJANGO_PID"
