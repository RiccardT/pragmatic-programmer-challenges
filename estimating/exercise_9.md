# Exercise 9

You are asked "Which has a higher bandwidth: a 1Gbps net connection or a person walking between two computers with a full 1TB of storage device in their pocket?"

What constraints will you put on your answer to ensure that the scope of your response is correct? (For example, you might say that the time taken to access the 
storage device is ignored)

## Answer:


Let's make a few assumptions:

1. The two computers are 1 mile apart
2. The human is walking at a speed of 4 miles per hour (the average walk speed for a person as per Google Search)
3. We are ignoring the time it takes for the person to plug in the storage device and boot up the computer.

# Exercise 10

## Answer:


Given the assumptions/constraints made in the answer to question 9, we can do some calculations to compare apples to apples:

The human has a transfer rate of about 1TB every quarter hour, or 1TB every 15 minutes, or .067TB/min.

Let's convert this to Gb per second:

.067TB/min -> 533Gb/min -> 8Gb/sec

Therefore, the person walking 1TB of data 1 mile at a speed of 4mph is actually faster than the net connection of 1 Gbps!

The net connection would win once we pass 8 miles of distance. 
