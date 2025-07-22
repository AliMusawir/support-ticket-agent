mocked_kb = {
    "Billing": [
        "Please check your billing history under Account > Payments.",
        "Refunds are processed after 7 business days."
    ],
    "Technical": [
        "Try restarting the app and ensure your internet connection is stable.",
        "Check for app updates in your store."
    ],
    "Security": [
        "Reset your password and enable two-factor authentication.",
        "Contact us immediately if you suspect unauthorized access."
    ],
    "General": [
        "We appreciate your query. Our team will respond shortly.",
        "Please describe your issue in detail so we can help."
    ]
}

def get_mocked_context(category):
    return mocked_kb.get(category, [])
