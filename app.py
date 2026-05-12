from flask import Flask, request, jsonify
import uuid
import anthropic
import json, uuid,os, dotenv,re


dotenv.load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))


def query_classifier(message_text):
    text = message_text.lower()
    if "available" in text or "dates" in text:
        return "pre_sales_availability"
    elif "rate" in text or "price" in text or "cost" in text:
        return "pre_sales_pricing"
    elif "check in" in text or "wifi" in text:
        return "post_sales_checkin"
    elif "ac is not working" in text or "complaint" in text or "not happy" in text:
        return "complaint"
    return "general_enquiry"

def api_call(user_query) -> json:
    context = '''Property: Villa B1, Assagao, North Goa
                Bedrooms: 3 | Max guests: 6 | Private pool: Yes
                Check-in: 2pm | Check-out: 11am
                Base rate: INR 18,000 per night (up to 4 guests)
                Extra guest: INR 2,000 per night per person
                WiFi password: Nistula@2024
                Caretaker: Available 8am to 8pm
                Chef on call: Yes, pre-booking required
                Availability April 20-24: Available
                Cancellation: Free up to 7 days before check-in'''

    response = client.messages.create(
    model='claude-sonnet-4-20250514',
    max_tokens=1024,
    system=(
        "You are a guest-relations manager at Nistula Villas. "
        f"Use this context: {context}. "
        "Your goal is to answer queries or handle complaints. "
        "You MUST return ONLY a JSON object with these keys: "
        "message_id, query_type, drafted_reply, confidence_score, action. "
        "Action logic: auto_send (>0.85), agent_review (0.60-0.85), escalate (<0.60 or complaint)."
        "Output Format : message_id:,query_type: ,drafted_reply:,confidence_score: ,action: "
    ),
    messages=[{"role": "user", "content": user_query}])
    raw_text = response.content[0].text
    json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)

    if json_match:
        json_string = json_match.group(0)
        data_dict = json.loads(json_string)
        print(data_dict["drafted_reply"])
        print(f"Action: {data_dict['action']}")
        return data_dict

app = Flask(__name__)
@app.route('/webhook/message', methods = ['POST'])
def get_message():
    data = request.get_json()
    print("Recieved Message")
    return api_call(user_query= str(
        {"message_id": str(uuid.uuid4()),
        "source": data.get('source'),
        "guest_name": data.get('guest_name'),
        "message_text": data.get('message'),
        "timestamp": data.get('timestamp'),
        "booking_ref": data.get('booking_ref'),
        "property_id": data.get('property_id'),
        "query_type": query_classifier(message_text=data.get('message'))}))


if __name__ == '__main__':
    app.run(debug=True)

   