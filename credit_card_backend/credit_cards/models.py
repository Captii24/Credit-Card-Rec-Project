from django.db import models


class CreditCard(models.Model):
    name = models.CharField(max_length=100)
    annual_fee = models.DecimalField(max_digits=6, decimal_places=2)
    rewards_rate = models.DecimalField(max_digits=4, decimal_places=2)  # E.g., "3% cashback on groceries"
    introductory_offer = models.CharField(max_length=255, null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    reward_type = models.CharField(max_length=50)  # E.g., "cashback", "travel points"

    def __str__(self):
        return self.name

class UserPreferences(models.Model):
    spending_habits = models.CharField(max_length=255)
    credit_score_range = models.CharField(max_length=50)
    desired_rewards = models.CharField(max_length=50)
    monthly_budget = models.DecimalField(max_digits=8, decimal_places=2)

