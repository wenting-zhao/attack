steps=4
for (( start_idx=12; start_idx<=100; start_idx+=$steps))
do 
    echo $start_idx
    python3 real_attack.py --dataset corbyrosset/researchy_questions --start_idx $start_idx --steps $steps
done