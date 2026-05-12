# PART 3 — THINKING QUESTION

### Question A — The Immediate Response

**AI Message:** 
"I am so sorry to hear there is no hot water at Villa B1. I am trying to contact our team right now. If no one is available immediately, I will keep trying every 15 minutes to make sure this is resolved before 7 am so your guests are not affected. As a small peace offering for the trouble, I'll arrange for a special breakfast hamper to be delivered for you and your guests. I will make sure the water issue is fixed before they arrive."

**Reasoning:** 
I chose this wording to give the guest immediate reassurance that the problem is being handled actively. By mentioning the 15-minute follow-ups and the 7 am deadline, it shows the system is "awake" and working even at 3 am.

---

### Question B — The System Design

Beyond sending the message, the platform should do the following:
1. **Notification:** The agent notifies the caretaker if the timings match; otherwise, it notifies the available night staff or property manager.
2. **Logging:** The system logs the time of the issue, guest name, villa number (B1), and when it was resolved. It also logs who solved it and how it was fixed.
3. **Escalation:** If no human responds within 30 minutes, the system sends an emergency alert (like an automated call). It also sends another apology to the guest with a peace offering, like a breakfast hamper or food basket, and reports this specific case to management.

---

### Question C — The Learning

When the AI notices that this hot water issue is repeating for the third time, it starts an "Alert Mode":
1. **Daily Reminders:** It reminds the caretaker every day twice about the issue until it is marked as fully resolved in the system.
2. **Reporting:** If after resolving the issue it comes up again very soon, the system will skip the local staff and report the matter directly to higher authorities or the owner.
3. **Prevention:** I would build an "Issue Tracker" module to catch these patterns. Once a problem is flagged as recurring, it forces a maintenance check-up to be scheduled so that the issue is fixed properly before a fourth complaint can happen.