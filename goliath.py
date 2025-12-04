def send_sms(message_body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )
    print(f"Message envoyé avec l'ID {message.sid}")


def notify_appointment(appointment_date, appointment_description, notification_minutes_before=15):
    # Ajoutez une condition pour vérifier que la date du rendez-vous est demain
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    if appointment_date.date() == tomorrow.date():
        # Calculer la différence de temps en minutes
        time_until_appointment = appointment_date - datetime.datetime.now()
        minutes_until_appointment = int(time_until_appointment.total_seconds() / 60)

        # Si la notification est dans le délai spécifié
        if 0 <= minutes_until_appointment <= notification_minutes_before:
            message_body = f"Rappel: Vous avez un rendez-vous à {appointment_date.strftime('%H:%M')}. {appointment_description}"
            send_sms(message_body)


if __name__ == "__main__":
    try:
        # Remplacez ces valeurs avec les détails de votre rendez-vous
        appointment_date = datetime.datetime(2023, 12, 13, 11, 0,
                                             0)  # Remplacez avec votre date et heure de rendez-vous
        appointment_description = "Rendez-vous avec l'assistance sociale"

        notify_appointment(appointment_date, appointment_description)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")