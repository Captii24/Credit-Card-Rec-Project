from django.shortcuts import render
from .models import CreditCard, UserPreferences

def recommend_cards(request):
    if request.method == 'POST':
        spending_habits = request.POST.get('spending_habits')
        credit_score_range = request.POST.get('credit_score_range')
        desired_rewards = request.POST.get('desired_rewards')
        monthly_budget = request.POST.get('monthly_budget')

        # Save user preferences
        user_preferences = UserPreferences(
            spending_habits=spending_habits,
            credit_score_range=credit_score_range,
            desired_rewards=desired_rewards,
            monthly_budget=monthly_budget
        )
        user_preferences.save()

        # Filter cards based on user input
        recommended_cards = CreditCard.objects.filter(
            reward_type=desired_rewards
        )
        return render(request, 'recommendations.html', {'recommended_cards': recommended_cards})

    return render(request, 'user_input.html')  # Render form if not a POST request
