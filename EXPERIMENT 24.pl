% Disease - Diet facts
diet(diabetes, [vegetables, whole_grains, legumes, fish]).
diet(hypertension, [fruits, low_salt_food, green_leafy_veg]).
diet(obesity, [salads, soups, lean_meat, oats]).
diet(anemia, [spinach, beetroot, red_meat, beans]).

% Rule: suggest diet
suggest_diet(Disease, Diet) :- diet(Disease, Diet).
