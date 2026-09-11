'''
Multi-Channel Notification System (Multiple Inheritance & MRO)
Scenario
An automated incident response engine sends server health alert broadcasts. Depending on incident severity, it sends 
notifications via Email, SMS, or both using cooperative multiple inheritance.

Problem Description
Implement a cooperative multiple inheritance structure using the following class designs:

Base Class Notifier:
Constructor (__init__): Accepts sender_id (string).
Method send(message): Returns a list containing the log: ["[Notifier <sender_id>] general broadcast: <message>"].
Subclass EmailNotifier (inherits from Notifier):
Constructor (__init__): Accepts email_server (string) along with any other keyword parameters. It must forward parameters to 
the next class in the hierarchy using super().__init__() or direct calls.
Method send(message): Calls super().send(message) to get the log list, prepends the string "[Email via <email_server>] sending: 
<message>" to the list, and returns it.
Subclass SMSNotifier (inherits from Notifier):
Constructor (__init__): Accepts sms_gateway (string) along with any other keyword parameters. It must forward parameters to 
the next class in the MRO.
Method send(message): Calls super().send(message) to get the log list, prepends the string "[SMS via <sms_gateway>] sending: 
<message>" to the list, and returns it.
Subclass HybridAlertChannel (inherits from BOTH EmailNotifier and SMSNotifier in that order):
Constructor (__init__): Accepts sender_id (string), email_server (string), and sms_gateway (string). Passes all values 
cooperatively through super().__init__().
Method send(message): Calls super().send(message) to get the consolidated log list. Prepends "[HYBRID ALERT] Initiating dual 
channels..." to the list and returns it.
Requirements:
The hierarchy must support cooperative initialization and cooperative method dispatch. Calling super().__init__() or 
super().send() must pass details down the entire MRO path without skipping parent classes or duplicating calls.
Print the Method Resolution Order (.__mro__ or .mro()) of HybridAlertChannel to verify the lookup path.
Example Walkthrough
alert = HybridAlertChannel(sender_id="SYS-ADMIN", email_server="smtp.cdac.in", sms_gateway="gw.acts.com")
logs = alert.send("Disk space 95%")

for log in logs:
    print(log)
Expected Console Output Logs:

[HYBRID ALERT] Initiating dual channels...
[Email via smtp.cdac.in] sending: Disk space 95%
[SMS via gw.acts.com] sending: Disk space 95%
[Notifier SYS-ADMIN] general broadcast: Disk space 95%
'''

class Notifier:

    def __init__(self, sender_id, **kwargs):
        self.sender_id = sender_id
        super().__init__(**kwargs)

    def send(self, message):
        return [
            f"[Notifier {self.sender_id}] general broadcast: {message}"
        ]


class EmailNotifier(Notifier):

    def __init__(self, email_server, **kwargs):
        self.email_server = email_server
        super().__init__(**kwargs)

    def send(self, message):
        logs = super().send(message)

        logs.insert(
            0,
            f"[Email via {self.email_server}] sending: {message}"
        )

        return logs


class SMSNotifier(Notifier):

    def __init__(self, sms_gateway, **kwargs):
        self.sms_gateway = sms_gateway
        super().__init__(**kwargs)

    def send(self, message):
        logs = super().send(message)

        logs.insert(
            0,
            f"[SMS via {self.sms_gateway}] sending: {message}"
        )

        return logs


class HybridAlertChannel(EmailNotifier, SMSNotifier):

    def __init__(self, sender_id, email_server, sms_gateway):
        super().__init__(
            sender_id=sender_id,
            email_server=email_server,
            sms_gateway=sms_gateway
        )

    def send(self, message):
        logs = super().send(message)

        logs.insert(
            0,
            "[HYBRID ALERT] Initiating dual channels..."
        )

        return logs


alert = HybridAlertChannel(
    sender_id="SYS-ADMIN",
    email_server="smtp.cdac.in",
    sms_gateway="gw.acts.com"
)

logs = alert.send("Disk space 95%")

for log in logs:
    print(log)

print("\nMRO:")
print(HybridAlertChannel.__mro__)