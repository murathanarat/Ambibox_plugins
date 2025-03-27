import lightpack, time, random

# User-specific LED configurations
top_leds = list(range(1, 31))  # Top LEDs (1-30)
bottom_leds = list(range(31, 61))  # Bottom LEDs (31-60)
left_leds = list(range(61, 81))  # Left LEDs (61-80)
right_leds = list(range(81, 112))  # Right LEDs (81-111)

all_leds = top_leds + bottom_leds + left_leds + right_leds  # All LEDs combined

lpack = lightpack.lightpack('127.0.0.1', 3636, all_leds)  # 111 LEDs in total
lpack.connect()
lpack.lock()

print ('***pyLightpack animation examples (read script header first)***')
print ('    1 -- Basic flash 4 times')
print ('    2 -- "Snake"')
print ('    3 -- Cylon effect')
print ('    4 -- Basic random color fluid')
print ('    5 -- Lightning Effect')

choice = 6 

while True:    
    if int(choice) == 1:
        lpack.setSmooth(100)  # 4 basic flashes
        lpack.setColorToAll(0, 0, 0)
        time.sleep(0.3)
        for k in range(0, 5):  
            lpack.setColorToAll(0, 255, 0)  # Green flash
            time.sleep(1)
            lpack.setColorToAll(0, 0, 0)  # Turn off all LEDs
            time.sleep(1)
        lpack.setColorToAll(0, 0, 0)
        print('Next')
        time.sleep(4)
        
    elif int(choice) == 2:
        lpack.setSmooth(10)  # Snake effect
        i = 1
        while i < 80:
            i = i + 1
            for k in range(0, len(all_leds)):  # Iterate through all LEDs
                idx = (i + k) % len(all_leds)
                if k < len(all_leds) // 3:
                    lpack.setColor(all_leds[idx], 255, 0, 0)  # Red color
                else:
                    lpack.setColor(all_leds[idx], 0, 0, 125)  # Blue color                                                 
            time.sleep(0.05)
            print('Next')
    
    elif int(choice) == 3:
        lpack.setSmooth(10)  # Tiny Cylon effect
        lpack.setColorToAll(0, 0, 0)    
        time.sleep(1)    
        on = [255, 0, 0]  # Red color
        off = [0, 0, 0]  # Turn off (black)
        lpack.setSmooth(45)    
        
        # Turn on the top and bottom LEDs
        for i in all_leds:
            lpack.setColor(i, on[0], on[1], on[2])
        
        l = 0
        while l < 15:    
            for i in range(1, 4):        
                for idx in all_leds:
                    lpack.setColor(idx, on[0], on[1], on[2])  # Keep LEDs on
                time.sleep(0.2)
            l += 1
        lpack.setColorToAll(0, 0, 0)
        time.sleep(5)
    
    elif int(choice) == 4:
        lpack.setSmooth(250)  # Random color fluid effect
        lpack.setGamma(2.00)
        lpack.setColorToAll(255, 255, 255)  # Start with white
        ark = []
        for i in range(0, 101):
            n = i % 2
            if n == 0:
                ark.append(0)
            else:
                ark.append(random.randint(200, 255))  # Random value between 200 and 255
        random.shuffle(ark)
        while True:            
            num = random.randint(1, len(all_leds))  # Randomly pick a LED
            r = random.choice(ark)
            g = random.choice(ark)
            b = random.choice(ark)
            if num != 1 and num != len(all_leds):
                lpack.setColor(all_leds[num], r, g, b)
                time.sleep(random.uniform(0, 1))  # Wait randomly
                lpack.setColor(all_leds[num - 1], r, g, b)            
                lpack.setColor(all_leds[num + 1], r, g, b)
            elif num == 1:
                lpack.setColor(all_leds[num + 1], r, g, b)
                time.sleep(random.uniform(0, 1))
                lpack.setColor(all_leds[num], r, g, b)            
                lpack.setColor(all_leds[num + 2], r, g, b)
            elif num == len(all_leds):
                lpack.setColor(all_leds[num - 1], r, g, b)
                time.sleep(random.uniform(0, 1))
                lpack.setColor(all_leds[num], r, g, b)            
                lpack.setColor(all_leds[num - 2], r, g, b)
            time.sleep(random.uniform(1, 3))

    elif int(choice) == 5:
        lpack.setSmooth(10)  # Lightning Effect
        
        while True:
            # Lightning effect: multiple random lightning strikes
            for _ in range(5):  # Number of lightning strikes per cycle
                flash_intensity = random.randint(180, 255)  # Random intensity for the lightning (brightness)
                
                # Select a random subset of LEDs for the lightning strike
                lightning_leds = random.sample(all_leds, random.randint(30, 60))  # Random number of LEDs
                
                # Flash all selected LEDs in white (lightning)
                for led in lightning_leds:
                    lpack.setColor(led, flash_intensity, flash_intensity, flash_intensity)  # White flash
                time.sleep(random.uniform(0.05, 0.2))  # Flash duration (varies randomly)
                
                # Turn off all LEDs
                for led in lightning_leds:
                    lpack.setColor(led, 0, 0, 0)  # Turn off
                time.sleep(random.uniform(0.1, 0.3))  # Off duration (varies randomly)
                
            # Pause between lightning cycles
            time.sleep(random.uniform(2, 5))  # Random pause before the next cycle

    elif int(choice) == 6:
        lpack.setSmooth(30)  # Smooth transitions for the fireplace effect
        
        while True:
            # Simulate the flickering of flames
            for led in all_leds:
                # Randomly generate the color of the flame (between red, orange, yellow)
                red = random.randint(180, 255)  # Flickering red intensity
                green = random.randint(40, 150)  # Flickering green intensity
                blue = random.randint(0, 50)  # No blue for realistic fire colors
                
                # Randomly adjust the brightness to simulate flickering
                brightness = random.randint(50, 255)  # Varying brightness for each LED
                
                # Apply the color with the flickering brightness
                lpack.setColor(led, red, green, blue)
                time.sleep(random.uniform(0.05, 0.15))  # Flicker effect speed
                
            # After a few flickers, simulate ember glow (dim red/yellow)
            for led in all_leds:
                if random.random() < 0.2:  # 20% chance to simulate an ember
                    ember_brightness = random.randint(50, 100)
                    lpack.setColor(led, ember_brightness, ember_brightness // 2, 0)  # Dimmer red/orange
                else:
                    lpack.setColor(led, 0, 0, 0)  # Turn off some LEDs for randomness
            
            # Pause briefly before the next round of flickers
            time.sleep(random.uniform(1, 2))  # Pause between rounds of flickers
