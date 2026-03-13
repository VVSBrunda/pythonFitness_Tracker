import datetime

class Workout:
    def __init__(self, name, duration, calories_burned):
        self.name = name
        self.duration = duration
        self.calories_burned = calories_burned

class FitnessTracker:
    def __init__(self):
        self.workouts = []

    def log_workout(self):
        Name = input("Enter workout name: ")
        Duration = float(input("Enter workout duration (minutes): "))
        Calories_burned = float(input("Enter calories burned: "))
        workout = Workout(Name, Duration, Calories_burned)
        self.workouts.append(workout)
        print("Workout logged successfully!")

    def track_progress(self):
        total_duration = sum(workout.duration for workout in self.workouts)
        total_calories_burned = sum(workout.calories_burned for workout in self.workouts)
        print(f"Total workout duration: {total_duration} minutes")
        print(f"Total calories burned: {total_calories_burned}")

    def suggest_exercise_plan(self):
        print("Suggested exercise plan:")
        print("1.Monday: Cardio (30 minutes)")
        print("2.Tuesday: Strength training (45 minutes)")
        print("3.Wednesday: Rest day")
        print("4.Thursday: Cardio (30 minutes)")
        print("5.Friday: Strength training (45 minutes)")
        print("6.Saturday: Rest day")
        print("7.Sunday: Long run (60 minutes)")

def main():
    tracker = FitnessTracker()
    while True:
        print("1.Log workout")
        print("2.Track progress")
        print("3.Suggest exercise plan")
        print("4.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tracker.log_workout()
        elif choice == "2":
            tracker.track_progress()
        elif choice == "3":
            tracker.suggest_exercise_plan()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
