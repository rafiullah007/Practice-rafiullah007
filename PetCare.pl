%-------------------------------
% PET TYPES
%-------------------------------
pet_type(dog).
pet_type(cat).
pet_type(bird).

%-------------------------------
% AGE GROUPS
%-------------------------------
age_group(puppy).
age_group(adult).
age_group(senior).
age_group(kitten).
age_group(young).

%-------------------------------
% HEALTH CONDITIONS
%-------------------------------
health_condition(healthy).
health_condition(arthritis).
health_condition(kidney_issues).
health_condition(feather_plucking).

%-------------------------------
% PET CARE RECOMMENDATIONS
% Format: food_for/4, toy_for/4, accessory_for/4, tip_for/4
%-------------------------------

% Dog - Puppy - Healthy
food_for(dog, puppy, healthy, puppy_food).
food_for(dog, puppy, healthy, high_protein_diet).
toy_for(dog, puppy, healthy, chew_toys).
toy_for(dog, puppy, healthy, squeaky_toys).
accessory_for(dog, puppy, healthy, collar).
accessory_for(dog, puppy, healthy, leash).
tip_for(dog, puppy, healthy, regular_exercise).
tip_for(dog, puppy, healthy, socialization).

% Dog - Senior - Arthritis
food_for(dog, senior, arthritis, senior_dog_food).
food_for(dog, senior, arthritis, joint_supplements).
toy_for(dog, senior, arthritis, soft_chew_toys).
toy_for(dog, senior, arthritis, comfort_toys).
accessory_for(dog, senior, arthritis, orthopedic_bed).
accessory_for(dog, senior, arthritis, ramp).
tip_for(dog, senior, arthritis, low_impact_exercise).
tip_for(dog, senior, arthritis, comfortable_resting_area).

% Cat - Kitten - Healthy
food_for(cat, kitten, healthy, kitten_food).
food_for(cat, kitten, healthy, high_calorie_diet).
toy_for(cat, kitten, healthy, feather_wands).
toy_for(cat, kitten, healthy, small_balls).
accessory_for(cat, kitten, healthy, litter_box).
accessory_for(cat, kitten, healthy, scratching_post).
tip_for(cat, kitten, healthy, playtime).
tip_for(cat, kitten, healthy, safe_exploration).

% Bird - Young - Healthy
food_for(bird, young, healthy, seed_mix).
food_for(bird, young, healthy, fresh_fruits).
toy_for(bird, young, healthy, mirror_toys).
toy_for(bird, young, healthy, swing_perches).
accessory_for(bird, young, healthy, cage).
accessory_for(bird, young, healthy, perches).
tip_for(bird, young, healthy, social_interaction).
tip_for(bird, young, healthy, flying_time).

%-------------------------------
% EVOLUTION OF PET FOOD TYPES (Recursive Rule)
%-------------------------------
evolved_food(senior_dog_food, adult_dog_food).
evolved_food(adult_dog_food, puppy_food).
evolved_food(senior_cat_food, adult_cat_food).
evolved_food(adult_cat_food, kitten_food).

food_ancestor(Food, Ancestor) :-
    evolved_food(Food, Ancestor).
food_ancestor(Food, Ancestor) :-
    evolved_food(Food, Mid),
    food_ancestor(Mid, Ancestor).
