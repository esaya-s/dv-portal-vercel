#!/bin/bash
echo "🌐 Setting up ngrok tunnel for anvilu.com..."
echo "================================================"

echo ""
echo "📋 This will create a public tunnel to your Django app"
echo ""

# Check if ngrok is installed
if command -v ngrok &> /dev/null; then
    echo "✅ ngrok is already installed"
else
    echo "📦 Installing ngrok..."
    
    # Download ngrok
    wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
    tar -xzf ngrok-v3-stable-linux-amd64.tgz
    chmod +x ngrok
    
    echo "✅ ngrok installed"
fi

echo ""
echo "🚀 Starting Django on port 8080..."
# Start Django in background
DJANGO_SETTINGS_MODULE=dv_portal.settings_production python manage.py runserver 127.0.0.1:8080 &
DJANGO_PID=$!

echo "✅ Django started (PID: $DJANGO_PID)"

echo ""
echo "🌐 Starting ngrok tunnel..."
echo "This will give you a public URL for your Django app"

# Start ngrok tunnel
./ngrok http 8080

echo ""
echo "🎉 Setup complete!"
echo "🌐 Your Django app will be available at the ngrok URL shown above"
echo "👤 Admin panel: [ngrok-url]/admin/"
echo "📧 Username: usadv27"
echo ""
echo "💡 To stop the service:"
echo "kill $DJANGO_PID"
