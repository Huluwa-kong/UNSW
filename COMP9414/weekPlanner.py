# activities with name and duration
activity hnamei hdurationi
# binary constraints
constraint hA1i before hA2i # A1 ends when or before A2 starts
constraint hA1i after hA2i # A1 starts after or when A2 ends
constraint hA1i starts hA2i # A1 and A2 start at the same day and time
constraint hA1i ends hA2i # A1 and A2 end at the same day and time
constraint hA1i overlaps hA2i # A2 starts after A1 starts and not after A1 ends,
# and ends after A1 ends
constraint hA1i during hA2i # A1 starts after A2 starts and ends before A2 ends
constraint hA1i equals hA2i # A1 and A2 start and end at the same day and time
constraint hA1i same-day hA2i # A1 and A2 start and end on the same day

# hard domain constraints
domain hAi on hdi # A starts (and ends) on day d
domain hAi before hdi # A starts (and ends) before day d
domain hAi after hdi # A starts (and ends) after day d
domain hAi starts-before hti # A starts at or before time t on any day
domain hAi starts-after hti # A starts at or after time t on any day
domain hAi ends-before hti # A ends at or before time t on any day
domain hAi ends-after hti # A ends on or after time t on any day
