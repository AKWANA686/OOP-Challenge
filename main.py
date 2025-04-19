from pet import Pet

if __name__ == "__main__":
    # Create pet and demo actions
    my_pet = Pet("Lidiamba")
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    
    # Teaching max tricks
    my_pet.train("Roll over")
    my_pet.train("Sit Down")
    my_pet.train("play dead")
    
    # Show final status
    my_pet.get_status()
    
    # Demonstrate edge case
    print("\nTesting edge case:")
    tired_pet = Pet("Lidiamba", energy=1)
    tired_pet.play()
    tired_pet.play()
    
    