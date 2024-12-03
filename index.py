class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = True
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            print("User not a member")

        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount<=self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        return self

user_1 = User("Armando", "Sadiku", "mandi@hotmil.com", 29)
user_2 = User("Arlind", "Bytyqi", "abyty@hotmail.com", 31)
user_3 = User("Ylli", "Emini", "mrlee@gmail.com", 33)

user_1.spend_points(50).display_info()
user_2.enroll().spend_points(80).display_info()
user_3.display_info()
