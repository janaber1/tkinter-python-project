numbers =[500,400,37,24]
index=0
while index < len(numbers):
    numbers [index] =numbers[index]**2
    index+=1
    print(numbers)
    class events:
        def __init__(self, event_name, tickets):
            self.event_name= event_name
            self.tickets= tickets

            def get_name(self):
                return self.event_name

            def set_name(self, name):
                self.event_name = name

            def get_tickets(self):
                return self.tickets

           def set_tickets(self, tickets)
                self.tickets = tickets

        def get_event_by_id(events_list, event_id):
            for event in events_list:
                if event.get_id() == event_id:
                    return event
            return None
        people_list = []
        people_list.append(events("connference",0))
        people_list.append(events("wedding",0))
        people_list.append(events("birthday",0))
        people_list.append(events("music party",0))

        for events in people_list:
            print("eventname:", person.eventname)
            print("ticket:", person.tickets)
             ticket_numebr = input("Enter ticket number:")
        # Example usage: Set ticket number for a specific event
        event_id_to_set = "musicparty" # ID of the event for which we want to set ticket number
        new_ticket_number = 75  # New ticket number to set

        # Get the event by ID
        event_to_set = get_event_by_id(events_list, event_id_to_set)

        if event_to_set:
            # Set the new ticket number for the event
            event_to_set.set_tickets(new_ticket_number)
            print("Ticket number for event '{}' set to {}.".format(event_to_set.get_name(), new_ticket_number))
        else:
            print("Event with ID {} not found.".format(event_id_to_set))
my_ events= events("connfernce","wedding","birthday","musicparty")
print("event 1:",my_events.event1)
print("event 2:",my_events.event2)
print("event 3:",my_events.event3)
print("event 4:",my_events.event4)