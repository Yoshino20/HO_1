from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=100)
    _balance = models.FloatField(default=0)

    def _format_balance(self):
        return f"{self._balance:g}"

    def _save_balance(self):
        if self.pk:
            self.save(update_fields=["_balance"])

    def display_info(self):
        return f"Account of {self.name} has balance {self._format_balance()}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._save_balance()
            return True
        return False

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._save_balance()
            return True
        return False

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self._save_balance()
            return True
        return False
