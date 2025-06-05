from django.shortcuts import render

# Create your views here.


@login_required
def create_chat_room(request):
    if request.method == 'POST':
        form = ChatInitializeForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()

            # Send email to the user with room details directly within the same function
            subject = f'Join the Chat Room: {room.room_name} - Invitation from {room.user.first_name}'

            # Define the HTML message directly
            html_message = f"""
            <html>
<head>
    <style>
        body {{
            font-family: 'Poppins', sans-serif;
            background-color: #f4f7fb;
            color: #333;
            padding: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            text-align: center;
        }}
        h1 {{
            color: #007bff;
            font-size: 28px;
            margin-bottom: 20px;
        }}
        p {{
            font-size: 16px;
            line-height: 1.6;
            color: #555;
        }}
        a {{
            color: #fff;
            background-color: #007bff;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
        }}
        a:hover {{
            background-color: #0056b3;
        }}
        .footer {{
            margin-top: 30px;
            font-size: 14px;
            color: #888;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>You've Been Invited to Join a Chat Room!</h1>
        <p>Hi,</p>
        <p>{room.user.first_name} has created a chat room and would like you to join the conversation.</p>
        <p>The room, <strong>{room.room_name}</strong>, offers a seamless, real-time communication experience. Enjoy encrypted and secure conversations with your friends, family, or colleagues in a modern, professional environment.</p>
        <p>Click the button below to join the chat room:</p>
        <p><a href="http://127.0.0.1:8000/create_chat_room/join_chat/{room.room_name}/">Join Chat Room</a></p>
        <p>You can rejoin the room anytime. We look forward to seeing you there!</p>
        
        <div class="footer">
            <p>Thank you for choosing <strong>LiveLink</strong> – your go-to platform for secure and dynamic live interactions!</p>
        </div>
    </div>
</body>
</html>
            """

            # Define the plain text version of the message
            plain_message = f"""
            Hi,

            {room.user.first_name} has invited you to join the chat room '{room.room_name}'. 
            
            Feel free to join using the link below:

            http://127.0.0.1:8000/create_chat_room/join_chat/{room.room_name}/

            We look forward to having you in the chat room.

            Thank you for using LiveLink – your solution for real-time communication!
            """

            from_email ='your-email@gmail.com'
          # Split the comma-separated string into a list of email addresses
            recipient_list = [email.strip() for email in room.emails.split(',') if email.strip()]# The email address entered in the form

            # Send the email using Django's send_mail function
            send_mail(
                subject,
                plain_message,
                from_email,
                recipient_list,
                html_message=html_message
            )

            return redirect('join_chat', room_name=room.room_name)
    else:
        form = ChatInitializeForm()

    # Get the current time and format it correctly
    t = time.localtime()
    actual_time = time.strftime('%d-%m-%y %H:%M:%S', t)

    # Render the form and pass the actual time to the template
    return render(request, 'chatapp/create_chatroom.html', {'form': form, 'actual_time': actual_time})